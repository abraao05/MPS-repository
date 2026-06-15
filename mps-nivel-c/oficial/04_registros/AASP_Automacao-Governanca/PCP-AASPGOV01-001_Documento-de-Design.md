# Documento de Design — AASP_GOV · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | PCP-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync (AASPGOV01) |
| **Versão** | 1.0 |
| **Data** | 02/06/2026 |
| **Responsáveis** | Cezar Hiraki (Arquiteto / Tech Lead) |

---

## 1. Visão geral da solução

O SensrJiraSync é um serviço de sincronização **unidirecional** (Sensr → Jira) desenvolvido em .NET 8, executado como processo agendado no Azure Scheduler. A cada execução, o serviço realiza a migração e sincronização de atividades de todos os desenvolvedores configurados, sem necessidade de intervenção manual. A solução atende aos requisitos de migração automatizada com fidelidade (RF01–RF09), sincronização incremental de status (RF05) e idempotência por identificação via prefixo `#ID` no campo summary do Jira (RNF01), garantindo que execuções repetidas não gerem duplicatas. A resiliência por desenvolvedor (RNF02) assegura que uma falha de autenticação ou processamento de um desenvolvedor não interrompa a execução dos demais. A separação em três camadas (RNF04) sustenta a manutenibilidade e a evolução futura do serviço, enquanto as credenciais gerenciadas externamente via `appsettings.json` (RNF05) atendem aos requisitos de segurança. A compatibilidade com .NET 8 e Azure Scheduler (RNF06) garante a operação no ambiente de nuvem do cliente.

---

## 2. Design técnico (arquitetura)

### 2.1. Arquitetura

A solução é estruturada em três projetos .NET com separação clara de responsabilidades:

| Projeto | Responsabilidade | Componentes Principais | Dependências |
|---|---|---|---|
| SensrJiraSync.Core | Contratos, modelos de domínio e mapeadores. Sem dependências externas. | AppSettings, DeveloperConfig, ProjectConfig, SensrModels, JiraModels, StatusMapper | Nenhuma |
| SensrJiraSync.Infrastructure | Implementação dos serviços de integração e helpers de transformação. | SensrService, JiraService, SyncService, HtmlHelper | Core, HtmlAgilityPack, Newtonsoft.Json |
| SensrJiraSync.App | Ponto de entrada, configuração e composição de dependências via injeção de dependências. | Program.cs, appsettings.json | Core, Infrastructure, Microsoft.Extensions.* |

**Fluxo de sincronização (por execução do Azure Scheduler):**

1. `SyncService` percorre os desenvolvedores configurados e, para cada um, autentica-se no Sensr via `SensrService.LoginAsync`, obtendo token JWT individual.
2. Para cada projeto do desenvolvedor, busca a lista de atividades via API Sensr (`getactivitiesbyprojectstatus`).
3. Resolve ou cria o Epic correspondente no Jira pelo nome do projeto via `JiraService.GetOrCreateEpicAsync`.
4. Busca as Tasks existentes sob o Epic, indexadas pelo prefixo `#ID` no summary via `JiraService.GetIssuesByEpicAsync`.
5. Para cada atividade: se o `#ID` não existe na listagem do Jira → cria Task completa com descrição, labels sanitizadas, status, histórico convertido como comentários e subtarefas. Se já existe → verifica divergência de status e aplica transição via `JiraService.TransitionAsync` somente se necessário.

### 2.2. Modelo de dados

Mapeamento de entidades entre as plataformas Sensr e Jira:

| Entidade Sensr | Entidade Jira | Observações |
|---|---|---|
| Projeto (`name_project`) | Epic | Um Epic por projeto, reutilizado em execuções subsequentes via busca por nome. |
| Atividade (`activity`) | Task | Summary: `#ID Nome`. Descrição composta por texto, progresso, tempo gasto e responsáveis. |
| Sub-atividade | Subtask | Vinculada à Task pai. Summary: `#ID Nome`. Descrição convertida de HTML para texto plano via HtmlHelper. |
| `description_history` | Comentários | Cada entrada do histórico HTML convertida individualmente e adicionada como comentário no Jira. |
| Tags | Labels | Sanitizadas: espaços e barras substituídos por underscore via `JiraService.SanitizeLabel`. |
| Status Sensr → Jira | Transição de status | TODO → To Do · DOING → In Progress · VALIDATION → To Test · STOPPED → Blocked · DONE → Done |

### 2.3. Integrações

| Componente / Serviço | Tipo | Papel na Solução |
|---|---|---|
| API Sensr | API REST externa | Fonte dos dados. Fornece atividades, detalhes, sub-atividades e histórico de descrição. |
| API Jira v3 | API REST externa | Destino. Recebe criação de Epics, Tasks, Subtasks, transições de status e comentários. |
| Azure Scheduler | Serviço de nuvem | Agendamento e execução periódica do serviço conforme configuração do cliente. |
| HtmlAgilityPack | Pacote NuGet | Parsing e transformação de HTML dos campos de descrição e histórico do Sensr. |
| Newtonsoft.Json | Pacote NuGet | Serialização e desserialização JSON nas requisições e respostas das APIs. |
| Microsoft.Extensions.* | Framework .NET | Injeção de dependências, configuração via IConfiguration e logging estruturado. |
| Azure DevOps | Controle de versão / CI/CD | Repositório do código-fonte e pipeline de publicação no Azure Scheduler. |

Detalhamento de contratos e endpoints em ITP-AASPGOV01-001.

### 2.4. Decisões de design

| ID | Decisão | Alternativas consideradas | Escolha e justificativa | RAD |
|---|---|---|---|---|
| D01 | Estruturar a solução em três camadas: Core, Infrastructure e App | (a) Monolito em projeto único; (b) 3 camadas separadas | 3 camadas — separar contratos e modelos da implementação permite substituir serviços sem impactar a lógica de domínio e facilita evolução futura | — |
| D02 | Autenticação por desenvolvedor no Sensr (token JWT individual) | (a) Service account única; (b) Token por desenvolvedor | Por desenvolvedor — a API do Sensr retorna atividades filtradas por usuário; autenticação compartilhada retornaria dados sem filtragem adequada | — |
| D03 | Identificar cards migrados pelo prefixo `#ID` no summary do Jira | (a) Campo customizado; (b) Banco de mapeamento externo; (c) Prefixo no summary | Prefixo no summary — simples, sem dependência de campos personalizados; permite lookup eficiente sem persistir estado entre execuções | — |
| D04 | Utilizar ADF (Atlassian Document Format) para campos de texto no Jira | (a) Texto plano; (b) HTML; (c) ADF | ADF — a API Jira v3 exige ADF; envio de texto plano ou HTML resulta em erro. ADF é JSON estruturado representando documentos como árvore de nós tipados | GDE-AASPGOV01-001 |
| D05 | Converter HTML do Sensr para texto plano antes de enviar ao Jira | (a) Enviar HTML direto; (b) Conversão para texto plano via HtmlHelper | Conversão — enviar HTML diretamente resultaria em tags visíveis para o usuário; conversão preserva o conteúdo sem poluição de marcação | — |
| D06 | Sincronização incremental limitada a status | (a) Atualização completa de todos os campos; (b) Apenas status | Apenas status — atualizar descrição e subtarefas a cada execução criaria risco de sobrescrever edições manuais feitas no Jira durante a transição | — |
| D07 | Executar o serviço como Azure Scheduled Job stateless | (a) Worker persistente; (b) Stateless agendado | Stateless — persistir estado adicionaria complexidade desnecessária; a idempotência por `#ID` elimina a necessidade de rastrear o que já foi migrado entre execuções | — |

---

## 3. Design de produto (UX/UI) — não aplicável

Projeto de back-end/serviço, sem interface de usuário. Conforme ADAP-AASPGOV01-001, o design de UX/UI não se aplica a este projeto. O único ponto de configuração exposto ao operador é o arquivo `appsettings.json`, cuja estrutura está descrita em RF10 e na seção §2.1 deste documento.

---

## 4. Rastreabilidade requisito → design

| Requisito (ID) | Elemento de design |
|---|---|
| RF01 — Autenticação Sensr por desenvolvedor | `SensrService.LoginAsync` — JWT individual por `DeveloperConfig` |
| RF02 — Criar ou reutilizar Epic por nome de projeto | `JiraService.GetOrCreateEpicAsync` |
| RF03 — Criar Task com prefixo `#ID` no summary | `JiraService.CreateTaskAsync` + `SyncService.ExtractSensrId` |
| RF04 — Criar Subtask vinculada à Task pai | `JiraService.CreateSubtaskAsync` |
| RF05 — Sincronizar status incrementalmente | `SyncService.UpdateIssueIfNeededAsync` + `JiraService.TransitionAsync` |
| RF06 — Migrar histórico de descrição como comentários individuais | `HtmlHelper.ParseDescriptionHistory` + `JiraService.AddCommentAsync` |
| RF07 — Converter HTML do Sensr para ADF no Jira | `HtmlHelper.ToPlainText` + `JiraService.BuildAdfDocument` |
| RF08 — Mapear status entre as plataformas | `StatusMapper.MapSensrToJira` |
| RF09 — Sanitizar labels antes de enviar ao Jira | `JiraService.SanitizeLabel` |
| RF10 — Configuração de desenvolvedores e projetos via appsettings.json | `AppSettings` + `DeveloperConfig` + `ProjectConfig` |
| RF11 — Executável compatível com Azure Scheduler (exit code 0/1) | `Program.cs` — bootstrap com saída determinística |
| RNF01 — Idempotência (sem duplicatas em execuções repetidas) | `SyncService` — verificação por prefixo `#ID` antes de criar |
| RNF02 — Confiabilidade por desenvolvedor (falha isolada) | `SyncService` — bloco `try/catch` por `DeveloperConfig` |
| RNF03 — Log estruturado em todos os serviços | `Microsoft.Extensions.Logging` em `SensrService`, `JiraService`, `SyncService` |
| RNF04 — Separação em camadas (manutenibilidade) | Estrutura de projetos Core / Infrastructure / App |
| RNF05 — Credenciais fora do código-fonte | `appsettings.json` gerenciado externamente; tokens não registrados em log |
| RNF06 — Compatibilidade .NET 8 e Azure Scheduler | `TargetFramework net8.0` em todos os projetos; publicação como executável auto-contido |

Matriz completa de rastreabilidade em RASTR-AASPGOV01-001.

---

## 5. Avaliação do design (PCP 2)

| Item avaliado | Avaliador | Problema encontrado | Tratamento |
|---|---|---|---|
| Estrutura em 3 camadas (Core / Infrastructure / App) | Cezar Hiraki (Tech Lead / Arquiteto) | Nenhum problema identificado | Aprovado em 16/04/2026 |
| Fluxo de sincronização — lógica criar vs. atualizar | Cezar Hiraki + Raony Chagas | Risco de sobrescrever edições manuais realizadas no Jira durante a transição | Mitigado pela D06 — sincronização incremental limitada a status |
| Estratégia de identificação por prefixo `#ID` no summary | Cezar Hiraki | Necessidade de extração robusta do identificador Sensr no summary do Jira | Implementação de `SyncService.ExtractSensrId` com cobertura de testes |
| Conversão HTML → ADF para campos de texto | Cezar Hiraki + Raony Chagas | API Jira v3 rejeita texto plano e HTML direto; risco de conteúdo ilegível para o usuário | Decisão D04 — uso de ADF via `JiraService.BuildAdfDocument`; formalizada em GDE-AASPGOV01-001 |
| Gestão de credenciais por desenvolvedor | Cezar Hiraki | Risco de exposição de tokens em logs de execução | Mitigado por RNF05 — credenciais fora do código, sem registro de tokens nos logs |

O design da solução foi avaliado e formalmente aprovado pelo Tech Lead / Arquiteto **Cezar Hiraki** em **16/04/2026**, ao final da Fase 1 (Arquitetura), antes do início do desenvolvimento. A aprovação constitui evidência do atendimento ao critério PCP2 do processo de Desenvolvimento e Manutenção de Software (DES) do MR-MPS-SW:2024 Nível C.

---

## Controle de atualizações

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 02/06/2026 | Time de Melhoria Contínua | Documento de design consolidado a partir do Registro de Projeto AASP_GOV v2.0. |
