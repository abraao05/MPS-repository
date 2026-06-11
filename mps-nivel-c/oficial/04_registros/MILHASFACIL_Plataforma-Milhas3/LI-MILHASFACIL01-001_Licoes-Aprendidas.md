# Lições Aprendidas — Milhas3

| Campo | Valor |
|---|---|
| **Documento** | LI-MILHASFACIL01-001 — Lições Aprendidas |
| **Versão** | 1.0 |
| **Data** | 16/11/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Milhas3 — Plataforma de Busca e Monitoramento de Milhas |
| **Cliente** | Hub de Milhas (Felipe) |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR — Gerência de Projeto |

---

## 1. Objetivo

Registrar os aprendizados positivos e negativos do projeto Milhas3 para alimentar a base de conhecimento da Timeware e melhorar a execução de projetos futuros com características similares.

## 2. Lições aprendidas

### L-01 — Selenium com headless Chrome é eficaz contra Akamai quando bem configurado

| Atributo | Detalhe |
|---|---|
| Tipo | Positivo — técnico |
| O que aconteceu | A escolha do Selenium WebDriver com Chrome headless (`--headless=new`, `--disable-blink-features=AutomationControlled`, user-agent real, delays variáveis) provou-se eficaz para contornar o Akamai Bot Manager em todos os cinco portais-alvo ao longo de toda a execução do projeto |
| Impacto | Taxa de sucesso do motor acima de 90% em todos os programas; zero incidentes de bloqueio permanente em produção |
| Recomendação para projetos futuros | Em qualquer projeto de scraping com portais protegidos por Akamai, adotar esta configuração como padrão de partida. Documentar a configuração no GDE desde o kickoff. Versionar as configurações do ChromeOptions para facilitar ajustes futuros |

### L-02 — Instabilidade de seletores CSS é o principal risco de manutenção de scrapers

| Atributo | Detalhe |
|---|---|
| Tipo | Negativo — risco materializado |
| O que aconteceu | O portal Smiles (GOL) alterou sua estrutura HTML durante a Sprint 7, quebrando os seletores CSS do motor de rastreamento para aquele programa |
| Impacto | 1 dia de retrabalho para reajuste dos seletores; sem impacto no prazo geral, mas interrupção no rastreamento Smiles durante esse período |
| Recomendação para projetos futuros | Implementar smoke tests automatizados para os seletores de cada portal (execução diária em CI/CD); configurar alerta imediato quando qualquer seletor falha — isso detecta mudanças nos portais antes de impactar os usuários finais. Separar seletores em arquivo de configuração externo ao código para facilitar ajustes sem re-deploy |

### L-03 — Sprint Reviews quinzenais com cliente reduzem retrabalho na homologação

| Atributo | Detalhe |
|---|---|
| Tipo | Positivo — processo |
| O que aconteceu | A cadência de Sprint Reviews quinzenais com Felipe (Hub de Milhas) permitiu ajustes de UI/UX e de regras de negócio durante o desenvolvimento, de forma que a fase de homologação formal (Sprints 11 e 12) teve volume de retrabalho significativamente menor do que o estimado inicialmente |
| Impacto | Homologação concluída em 2 sprints (menor do que as 3 estimadas); cliente engajado e com expectativas alinhadas ao longo de todo o projeto |
| Recomendação para projetos futuros | Manter Sprint Reviews obrigatórias com cliente em todos os projetos de produto web; incluir demonstração ao vivo do motor de rastreamento a partir da sprint em que o primeiro programa é integrado — cliente consegue validar dados reais desde cedo |

### L-04 — Pool de ChromeDriver protege a VM Linux de degradação de recursos

| Atributo | Detalhe |
|---|---|
| Tipo | Positivo — técnico |
| O que aconteceu | A decisão de limitar o pool de instâncias ChromeDriver a 5 simultâneas e de gerenciá-las explicitamente com enfileiramento de solicitações evitou degradação de CPU e memória da VM Linux durante os picos de demanda de rastreamento |
| Impacto | VM operando dentro dos limites de recursos durante todo o projeto; sem incidentes de OOM (Out of Memory) ou degradação de performance do servidor central |
| Recomendação para projetos futuros | Definir o tamanho máximo do pool como parâmetro de configuração externalizado (variável de ambiente ou arquivo de propriedades), não como constante no código — facilita ajuste conforme capacidade do servidor sem necessidade de re-deploy |

### L-05 — Monolito modular é a escolha certa para MVP em VM única

| Atributo | Detalhe |
|---|---|
| Tipo | Positivo — arquitetural |
| O que aconteceu | A decisão de implementar o Motor de Rastreamento como um componente Spring Scheduler dentro do mesmo JAR do Servidor Central (monolito modular) simplificou o pipeline CI/CD, o deploy e a operação na VM Linux única do cliente |
| Impacto | Pipeline de CI/CD com um único artefato de build; deploy com um único SSH command; sem latência de IPC entre componentes |
| Recomendação para projetos futuros | Para MVPs e projetos com infraestrutura de VM única, preferir monolito modular (Spring Scheduler ou módulos bem separados) sobre microserviços. Planejar a extração para microserviço apenas quando volume justificar a complexidade operacional |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 16/11/2025 | Time de Melhoria Contínua | Documento final — projeto encerrado |
