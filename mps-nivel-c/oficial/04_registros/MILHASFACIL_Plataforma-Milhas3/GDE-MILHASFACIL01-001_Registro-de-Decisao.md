# Registro de Análise de Decisão — Milhas3 · Tecnologia do Motor de Rastreamento

| Campo | Valor |
|---|---|
| **Documento** | GDE-MILHASFACIL01-001 — Registro de Análise de Decisão |
| **Versão** | 1.0 |
| **Data** | 16/05/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Milhas3 — Plataforma de Busca e Monitoramento de Milhas |
| **Cliente** | Hub de Milhas (Felipe) |
| **Responsável pela Decisão** | Henry Komatsu (Tech Lead) |
| **Processo MPS-SW** | GDE — Gerência de Decisões |

---

## 1. Contexto e problema

O motor de rastreamento da plataforma Milhas3 precisa coletar dados de disponibilidade de voos em milhas dos portais de cinco programas de fidelidade: LATAM Pass, Smiles (GOL), TudoAzul (Azul), TAP Miles&Go e Iberia Plus.

Todos esses portais são protegidos pelo **Akamai Bot Manager**, um sistema de proteção anti-bot de mercado que detecta e bloqueia automaticamente requisições HTTP não humanas por meio de:

- Fingerprinting de TLS (perfil de handshake do cliente Java identifica automação)
- Análise de headers HTTP (ausência de headers típicos de browser real)
- Detecção de `navigator.webdriver = true` em JavaScript (flag inserida por drivers de automação)
- Ausência de comportamento humano (sem eventos de mouse, sem delays naturais, sem scroll)
- Detecção de browsers headless convencionais por perfil de canvas e WebGL

A questão é: **qual tecnologia de rastreamento automatizado supera o Akamai Bot Manager com confiabilidade suficiente para uso em produção no contexto deste projeto?**

## 2. Critérios de avaliação

| ID | Critério | Peso |
|---|---|---|
| C-01 | Capacidade de contornar o Akamai Bot Manager nos 5 portais-alvo | Alto |
| C-02 | Compatibilidade nativa com Java (linguagem do projeto) | Médio |
| C-03 | Maturidade, suporte e documentação da ferramenta | Médio |
| C-04 | Complexidade de configuração, manutenção e deploy | Médio |
| C-05 | Custo de licenciamento | Baixo |

## 3. Alternativas avaliadas

### Alternativa 1 — HTTP Direto + Jsoup (Java)

| Atributo | Avaliação |
|---|---|
| Descrição | Requisições HTTP nativas com manipulação de headers + biblioteca Jsoup para parsing HTML |
| Contorna Akamai? | Não — fingerprint TLS do cliente Java é identificado e bloqueado na maioria dos portais; não há execução de JavaScript |
| Compatibilidade Java | Alta (nativo) |
| Complexidade | Baixa |
| Custo | Gratuito |
| **Resultado** | **Descartada** — falha crítica no critério C-01; confirmado em testes contra portais LATAM e Smiles durante Sprint 0 |

### Alternativa 2 — Puppeteer / Playwright (Node.js)

| Atributo | Avaliação |
|---|---|
| Descrição | Browser headless Chromium controlado via DevTools Protocol; madura e amplamente usada para scraping |
| Contorna Akamai? | Parcialmente — versões headless com plugins stealth (puppeteer-extra-plugin-stealth) passam na maioria dos casos; requer configurações específicas análogas às do Selenium |
| Compatibilidade Java | Nenhuma — requer serviço Node.js separado, introduzindo heterogeneidade tecnológica no projeto |
| Complexidade | Alta — novo stack tecnológico, deploy de serviço adicional, IPC entre Java e Node.js |
| Custo | Gratuito |
| **Resultado** | **Descartada** — introduz segundo stack tecnológico incompatível com projeto Java; overhead de deploy e manutenção não justificado |

### Alternativa 3 — Selenium WebDriver com Chrome headless (Java)

| Atributo | Avaliação |
|---|---|
| Descrição | Controla um Chrome real via WebDriver; API Java nativa; Chrome headless emula browser completo incluindo execução de JavaScript |
| Contorna Akamai? | Sim — com configurações adequadas (detalhadas abaixo), Chrome headless contorna o Akamai de forma consistente; validado nos 5 portais-alvo em testes realizados durante Sprint 0 |
| Compatibilidade Java | Alta — Selenium Java API matura, amplamente documentada |
| Complexidade | Média — configuração inicial de ChromeDriver e pool; WebDriverManager simplifica gestão de versões |
| Custo | Gratuito (Apache License 2.0) |
| **Resultado** | **Selecionada** |

## 4. Decisão

**Selenium WebDriver 4.x com Chrome headless** é adotado como tecnologia do motor de rastreamento da plataforma Milhas3.

### 4.1 Configurações críticas para bypass do Akamai

| Configuração | Valor / Estratégia |
|---|---|
| Modo headless | `--headless=new` — nova API headless do Chrome (menos detectável que o modo `--headless` legado) |
| Flag de automação | `--disable-blink-features=AutomationControlled` — remove `navigator.webdriver = true` detectado pelo Akamai |
| User-agent | User-agent de browser desktop real (ex.: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ...`) — nunca o user-agent padrão do ChromeDriver |
| Viewport | `--window-size=1920,1080` — dimensão real de monitor desktop |
| Delays | Delays variáveis (300–1500ms) entre ações simulando comportamento humano (cliques, scrolls, inputs) |
| Cookies | Reutilização de cookies de sessão entre requisições do mesmo portal para evitar re-validação Akamai |
| Exclusão de flags de automação | Remoção de `enable-automation` dos switches do ChromeOptions |
| WebDriverManager | Gerenciamento automático de versão do ChromeDriver compatível com o Chrome instalado na VM |

### 4.2 Decisão arquitetural complementar — Monolito modular

O Motor de Rastreamento (Selenium) é implementado como um componente Spring Scheduler dentro do mesmo JAR do Servidor Central, e não como microserviço separado. Justificativa:

- Infraestrutura de VM única não justifica overhead de múltiplos serviços
- Elimina necessidade de IPC / fila de mensagens entre componentes
- Simplifica o pipeline CI/CD (único build, único deploy)
- Pode ser extraído para microserviço independente em versão futura sem mudança de interface

## 5. Consequências e riscos

| Item | Detalhe |
|---|---|
| Risco principal | Akamai evolui suas técnicas de detecção; atualizações futuras podem exigir ajustes nas configurações do ChromeDriver |
| Mitigação | Monitorar taxa de falhas de scraping por programa (métrica em MED-MILHASFACIL01-001); reajustar configurações quando taxa ultrapassar 10% em qualquer programa |
| Dependência | Chrome e ChromeDriver instalados na VM Linux; manter versão atualizada e compatível (WebDriverManager gerencia automaticamente) |
| Performance | Pool limitado a máximo 5 instâncias ChromeDriver simultâneas para não sobrecarregar a VM; tamanho configurável via propriedade de aplicação |
| Manutenção | Seletores CSS / XPath dos portais podem mudar; smoke tests diários em CI/CD detectam quebras antes de impactar usuários |

## 6. Aprovação

Decisão revisada e aprovada por Abraão Oliveira (Gerente de Projeto) e Henry Komatsu (Tech Lead) em 16/05/2025, conforme ATA-MILHASFACIL01-001.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 16/05/2025 | Time de Melhoria Contínua | Documento inicial — decisão arquitetural do motor de rastreamento |
