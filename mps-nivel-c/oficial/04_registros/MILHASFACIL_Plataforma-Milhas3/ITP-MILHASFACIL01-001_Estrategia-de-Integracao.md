# Estratégia de Integração — Milhas3 · Motor de Rastreamento e Programas de Fidelidade

| Campo | Valor |
|---|---|
| **Documento** | ITP-MILHASFACIL01-001 — Estratégia de Integração |
| **Versão** | 1.0 |
| **Data** | 02/06/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Milhas3 — Plataforma de Busca e Monitoramento de Milhas |
| **Cliente** | Hub de Milhas (Felipe) |
| **Tech Lead** | Henry Komatsu |
| **Processo MPS-SW** | ITP — Integração do Produto |

---

## 1. Itens a integrar (ITP 1)

| ID | Integração | Tipo | Sprint prevista |
|---|---|---|---|
| INT-01 | Motor de rastreamento ↔ LATAM Pass | Scraping via Selenium (headless Chrome) | Sprint 2 |
| INT-02 | Motor de rastreamento ↔ Smiles (GOL) | Scraping via Selenium (headless Chrome) | Sprint 3 |
| INT-03 | Motor de rastreamento ↔ TudoAzul (Azul) | Scraping via Selenium (headless Chrome) | Sprint 3 |
| INT-04 | Motor de rastreamento ↔ TAP Miles&Go | Scraping via Selenium (headless Chrome) | Sprint 4 |
| INT-05 | Motor de rastreamento ↔ Iberia Plus | Scraping via Selenium (headless Chrome) | Sprint 4 |
| INT-06 | Servidor Central ↔ Motor de Rastreamento | Invocação interna (Spring Scheduler) | Sprint 2 |
| INT-07 | Frontend Angular ↔ Servidor Central | HTTP REST (JSON) | Sprint 1 |
| INT-08 | Servidor Central ↔ PostgreSQL | JDBC / Spring Data JPA | Sprint 0 |
| INT-09 | Servidor Central ↔ SMTP (e-mail) | Spring Mail | Sprint 8 |

## 2. Estratégia de integração com programas de fidelidade

Todos os portais-alvo são protegidos pelo **Akamai Bot Manager**, que bloqueia requisições HTTP automatizadas comuns. A estratégia adotada — Selenium WebDriver com headless Chrome e configurações anti-detecção — está documentada em GDE-MILHASFACIL01-001. As configurações críticas de bypass aplicadas a todos os programas são:

- Flag `--headless=new` (nova API headless, menor pegada de detecção)
- `--disable-blink-features=AutomationControlled` (remove `navigator.webdriver = true`)
- User-agent de browser desktop real (não headless)
- Viewport 1920×1080
- Delays variáveis de 300–1500ms entre ações
- Reutilização de cookies de sessão entre requisições do mesmo programa

### 2.1 LATAM Pass — INT-01

| Atributo | Detalhe |
|---|---|
| Portal | latam.com |
| Proteção anti-bot | Akamai Bot Manager |
| Dados coletados | Voos disponíveis, custo em milhas, número de escalas, horários de partida e chegada |
| Padrão de implementação | Define o padrão para as demais integrações; implementado no Sprint 2 como referência arquitetural |
| Tratamento de falha | Retry com backoff exponencial (3 tentativas, intervalos: 2s, 5s, 10s); após 3 falhas: status `falha` em `sessoes_scraping`, log de erro |

### 2.2 Smiles — GOL — INT-02

| Atributo | Detalhe |
|---|---|
| Portal | smiles.com.br |
| Proteção anti-bot | Akamai Bot Manager |
| Dados coletados | Voos disponíveis, custo em milhas Smiles, escalas, categoria (econômica / executiva), clube de benefícios quando disponível |
| Observação | User-agent rotacionado entre sessões; comportamento de scroll simulado na listagem de resultados |
| Tratamento de falha | Idem INT-01 |

### 2.3 TudoAzul — Azul — INT-03

| Atributo | Detalhe |
|---|---|
| Portal | voeazul.com.br/milhas |
| Proteção anti-bot | Akamai Bot Manager |
| Dados coletados | Voos disponíveis, custo em pontos TudoAzul, escalas, categoria do assento |
| Tratamento de falha | Idem INT-01 |

### 2.4 TAP Miles&Go — INT-04

| Atributo | Detalhe |
|---|---|
| Portal | flytap.com |
| Proteção anti-bot | Akamai Bot Manager / Imperva (verificado durante Sprint 4) |
| Dados coletados | Voos disponíveis, custo em milhas TAP, validade da oferta |
| Observação | Fingerprint de browser gerenciado via ChromeDriver capabilities; portal com carregamento mais lento — timeout configurado em 45s |
| Tratamento de falha | Idem INT-01 |

### 2.5 Iberia Plus — INT-05

| Atributo | Detalhe |
|---|---|
| Portal | iberia.com |
| Proteção anti-bot | Akamai Bot Manager |
| Dados coletados | Voos disponíveis, custo em Avios (moeda do programa Iberia Plus), parceiros oneworld |
| Observação | Resultados incluem voos operados por parceiros da aliança oneworld (British Airways, American Airlines, etc.) quando disponíveis em Avios |
| Tratamento de falha | Idem INT-01 |

## 3. Sequência de integração

Ordem definida por prioridade de negócio (programas com maior base brasileira primeiro) e por similaridade técnica (clusters de portais com mesma proteção Akamai):

| Ordem | Integração | Justificativa |
|---|---|---|
| 1 | LATAM Pass (Sprint 2) | Maior programa de milhas do Brasil; define o padrão de implementação Selenium para as demais |
| 2 | Smiles + TudoAzul (Sprint 3) | Portais de comportamento similar ao LATAM Pass; implementados em paralelo |
| 3 | TAP + Iberia (Sprint 4) | Portais internacionais; podem ter variações de comportamento Akamai; implementados em paralelo |
| 4 | Frontend ↔ Backend (Sprint 5) | Integração ponta a ponta após motor de rastreamento completo |

## 4. Critérios de aceite de integração

| ID | Critério de aceite |
|---|---|
| INT-01 a INT-05 | Coleta retorna dados válidos (voos com custo em milhas, horários, escalas) para ao menos 3 rotas de teste por programa; mecanismo de retry funcional em caso de bloqueio temporário; taxa de falha ≤ 10% por sessão de teste |
| INT-06 | Spring Scheduler dispara motor nos intervalos configurados; resultados persistidos no PostgreSQL com timestamp correto; sem memory leak de instâncias ChromeDriver |
| INT-07 | Frontend consome todos os endpoints do servidor central sem erros CORS; payload JSON validado no front-end; autenticação JWT funcional em toda navegação autenticada |
| INT-08 | Transações CRUD persistidas corretamente; rollback funcional em caso de erro; Flyway migrations aplicadas automaticamente no boot |
| INT-09 | E-mail de alerta enviado e recebido em ≤ 5 minutos após disparo; template com informações corretas; falha de SMTP logada sem quebrar o fluxo principal |

## 5. Evidências de integração

Resultados dos testes de integração por programa registrados conforme VV-MILHASFACIL01-001 (itens VV-02 a VV-06); evidências mantidas no Azure DevOps Test Plans.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 02/06/2025 | Time de Melhoria Contínua | Documento inicial |
