# Estratégia de Integração — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | ITP-AASP-GOV-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |

---

## 1. Componentes a integrar

| Componente | Descrição |
|---|---|
| SensrJiraSync (serviço) | Processo .NET 8 que orquestra a leitura no Sensr, a transformação e a gravação no Jira |
| API Sensr | Fonte dos dados — fornece atividades, detalhes, sub-atividades e histórico |
| API Jira v3 | Destino — recebe criação de Epics, Tasks, Subtasks, transições e comentários |
| Azure Scheduler | Agendamento e execução periódica do serviço |

## 2. Interfaces

| Interface | Entre | Tipo / contrato |
|---|---|---|
| Autenticação e leitura Sensr | SensrJiraSync ↔ API Sensr | REST; autenticação JWT por desenvolvedor (endpoint de login) |
| Gravação e sincronização Jira | SensrJiraSync ↔ API Jira v3 | REST; Basic Auth (e-mail + API Token); texto rico em ADF |
| Agendamento | Azure Scheduler ↔ Executável SensrJiraSync | Processo isolado; código de saída 0 (sucesso) / 1 (falha) |

## 3. Integração com a API Sensr

Autenticação via token JWT obtido no endpoint de login, por sessão de desenvolvedor. Endpoints consumidos: `login`, `getactivitiesbyprojectstatus`, `getsingleactivity` e `subactivity`. Campos de texto retornados em HTML, tratados pelo HtmlHelper antes do envio ao Jira.

## 4. Integração com a API Jira

REST API v3 com Basic Auth (e-mail + API Token). Operações: criação de Epic, busca de issues por Epic (com paginação via `nextPageToken`), criação de Task e Subtask, consulta e aplicação de transições, adição de comentários. Todo conteúdo textual é formatado em ADF via `BuildAdfDocument`. As issues são identificadas pelo prefixo `#ID` no summary.

## 5. Integração com o Azure Scheduler

Executável .NET 8 auto-contido, agendado no Azure Scheduler. Retorna código de saída 0 em sucesso e 1 em falha. **Stateless:** cada execução consulta o estado atual das duas plataformas, sem persistência entre execuções (decisão D07).

## 6. Estratégia e ordem de integração

A integração seguiu a ordem das fases do projeto:

1. **Mapeamento e autenticação (Fase 2):** mapeamento dos endpoints das APIs Sensr e Jira e implementação dos fluxos de autenticação (JWT no Sensr; Basic Auth no Jira).
2. **Desenvolvimento dos serviços (Fase 3):** SensrService e JiraService, com StatusMapper e HtmlHelper na camada de transformação; orquestração no SyncService (criação e atualização incremental).
3. **Agendamento e execução (Fase 3):** configuração do Azure Scheduled Job.

## 7. Critérios de prontidão para integração

- Camada de transformação (StatusMapper, HtmlHelper) implementada e validada.
- Tratamento de exceção por desenvolvedor implementado no SyncService (RNF02).
- Verificação de existência por `#ID` antes de qualquer criação (RNF01).

## 8. Testes do produto integrado

O fluxo integrado (autenticação Sensr → leitura → transformação → criação/atualização no Jira) foi validado por testes de integração end-to-end executados diretamente contra os ambientes reais do Sensr e do Jira em modo de homologação, incluindo migração inicial, idempotência, atualização de status e tratamento de HTML inválido. Detalhes em VV-AASP-GOV-001 e REL-VV-AASP-GOV-001.

## 9. Entrega e implantação

O executável publicado foi implantado no Azure de forma manual após validação em homologação, com substituição do artefato anterior e verificação do agendamento (ver GCO-AASP-GOV-001).

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Estratégia de integração consolidada a partir do Registro de Projeto AASP_Automacao-Governanca v2.0 (08/06/2026). |
