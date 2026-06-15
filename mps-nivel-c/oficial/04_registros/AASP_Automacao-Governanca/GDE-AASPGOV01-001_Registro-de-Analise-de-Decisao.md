# Registro de Análise de Decisão (RAD) — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | GDE-AASPGOV01-001 |
| **Projeto / contexto** | AASP_Automacao-Governanca — SensrJiraSync |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Responsável pelas decisões** | Cezar Hiraki Velazquez (Tech Lead / Arquiteto), com o time |
| **Processo MPS-SW** | GDE (evidência de projeto) · PRO-GDE-001 |

---

## 1. Objetivo

Registrar as decisões arquiteturais e de design relevantes do projeto, com alternativas consideradas, escolha e justificativa, conforme PRO-GDE-001. As decisões foram tomadas na Fase 1 e início da Fase 3, e o design foi avaliado formalmente por Cezar Hiraki em 16/04/2026 (ver PCP-AASPGOV01-001).

## 2. Decisões registradas (D01–D07)

| ID | Decisão / Alternativas | Escolha | Justificativa |
|---|---|---|---|
| D01 | Arquitetura: monolito flat vs. clean architecture em 3 camadas | Clean architecture (Core, Infrastructure, App) | Separação de responsabilidades, testabilidade e manutenibilidade |
| D02 | Texto rico no Jira: HTML bruto vs. texto plano vs. ADF | ADF (Atlassian Document Format) | Requisito mandatório da API Jira v3; HTML bruto é rejeitado pela API |
| D03 | Idempotência: busca por ID externo vs. prefixo de texto no summary | Prefixo `#ID` no summary | A API Jira v3 não oferece busca por referência externa; o prefixo é confiável e inspecionável |
| D04 | Runtime: AWS Lambda vs. Azure Functions vs. App Service vs. Azure Scheduler | Azure Scheduled Job | Alinhamento com a infraestrutura existente da AASP; menor overhead operacional |
| D05 | Autenticação Sensr: API key única vs. token compartilhado vs. JWT por desenvolvedor | JWT por desenvolvedor | Rastreabilidade de atividades por responsável; isolamento de falha de credencial (CT-09) |
| D06 | Paginação Jira: offset paginado vs. cursor (`nextPageToken`) | Cursor via `nextPageToken` | Compatibilidade com a API Jira v3; única opção suportada para `GetIssuesByEpicAsync` |
| D07 | StatusMapper: switch inline vs. dicionário vs. classe isolada | Classe `StatusMapper` isolada | Extensibilidade para novos mapeamentos sem alterar o fluxo principal; testável de forma independente |

## 3. Análise detalhada — Runtime de execução (D04)

| Item | Conteúdo |
|---|---|
| **Problema** | Definir a plataforma de execução do serviço agendado de sincronização |
| **Gatilho (PRO-GDE-001)** | Escolha de tecnologia/infraestrutura de alto impacto operacional |
| **Alternativas** | (A) AWS Lambda; (B) Azure Functions; (C) Azure App Service; (D) Azure Scheduled Job |
| **Critérios** | Alinhamento com a infraestrutura da AASP, overhead operacional, adequação a execução agendada/não supervisionada |
| **Escolha** | (D) Azure Scheduled Job |
| **Justificativa** | Alinha-se à infraestrutura Azure já adotada pela AASP, com menor overhead operacional e modelo natural de execução agendada stateless (idempotência por `#ID` dispensa estado entre execuções) |
| **Riscos / premissa** | Disponibilidade do Azure Scheduler (premissa do projeto); execução stateless mitiga reprocessamento |

## 4. Decisão de design avaliada

O conjunto de decisões D01–D07 foi consolidado no design avaliado formalmente por Cezar Hiraki Velazquez em **16/04/2026** e ratificado nas atas de alinhamento (D01 em ATA-AASPGOV01-001; D02, D03, D04 em ATA-AASPGOV01-002).

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Registro de decisões (D01–D07) consolidado a partir do INTAKE-AASPGOV01 (14/06/2026), Bloco 7. |
