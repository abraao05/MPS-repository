# Documento de Design — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | PCP-AASP-GOV-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Responsáveis** | Cezar Hiraki Velazquez (GP / Tech Lead) · Raony Chagas (Desenvolvedor Sênior) |

---

## 1. Visão geral da solução

O **SensrJiraSync** é um serviço de sincronização unidirecional (Sensr → Jira) desenvolvido em .NET 8, executado como processo agendado no Azure Scheduler. A cada execução, realiza a migração e a sincronização de atividades de todos os desenvolvedores configurados. O design atende aos requisitos de idempotência (RNF01), confiabilidade por desenvolvedor (RNF02), manutenibilidade por camadas (RNF04) e segurança de credenciais (RNF05).

## 2. Design técnico (arquitetura)

### 2.1. Estrutura da solução em camadas

| Projeto | Responsabilidade | Componentes principais |
|---|---|---|
| `SensrJiraSync.Core` | Contratos, modelos de domínio e mapeadores. Sem dependências externas | AppSettings, DeveloperConfig, ProjectConfig, SensrModels, JiraModels, StatusMapper |
| `SensrJiraSync.Infrastructure` | Implementação dos serviços de integração e helpers de transformação | SensrService, JiraService, SyncService, HtmlHelper |
| `SensrJiraSync.App` | Ponto de entrada, configuração e composição de dependências via DI | Program.cs, appsettings.json |

Dependências unidirecionais: `App → Infrastructure → Core` (decisão D01).

### 2.2. Fluxo de sincronização

1. O `SyncService` percorre os desenvolvedores configurados e, para cada um, autentica-se no Sensr.
2. Para cada projeto: busca as atividades do desenvolvedor via API Sensr.
3. Resolve ou cria o Epic correspondente no Jira pelo nome do projeto.
4. Busca as Tasks existentes sob o Epic, indexadas pelo prefixo `#ID` no summary.
5. Para cada atividade:
   - Se o `#ID` **não existe** → cria Task completa com descrição, labels, status, histórico como comentários e subtarefas.
   - Se **já existe** → verifica divergência de status e aplica a transição se necessário.

### 2.3. Mapeamento de entidades

| Entidade Sensr | Entidade Jira | Observações |
|---|---|---|
| Projeto (`name_project`) | Epic | Um Epic por projeto, reutilizado em execuções subsequentes via busca por nome |
| Atividade (`activity`) | Task | Summary `#ID Nome`; descrição com texto, progresso, tempo gasto e responsáveis |
| Sub-atividade | Subtask | Vinculada à Task pai; summary `#ID Nome`; descrição convertida de HTML |
| `description_history` | Comentários | Cada entrada do histórico HTML convertida e adicionada como comentário individual |
| Tags | Labels | Sanitizadas: espaços e barras substituídos por underscore |
| Status Sensr → Jira | Transição de status | TODO→To Do, DOING→In Progress, VALIDATION→To Test, STOPPED→Blocked, DONE→Done |

### 2.4. Decisões de design

| Decisão | Escolha e justificativa | RAD |
|---|---|---|
| Estrutura da solução | Três camadas (Core, Infrastructure, App) — substituição de serviços sem impacto na lógica de domínio | GDE-AASP-GOV-001 (D01) |
| Autenticação Sensr | Por desenvolvedor (token JWT individual) — a API retorna atividades filtradas por usuário | GDE-AASP-GOV-001 (D02) |
| Identificação de cards migrados | Prefixo `#ID` no summary — lookup eficiente sem persistir estado | GDE-AASP-GOV-001 (D03) |
| Texto rico no Jira | ADF (Atlassian Document Format) — exigido pela API Jira v3 | GDE-AASP-GOV-001 (D04) |
| Conversão de HTML | HtmlHelper converte HTML do Sensr para texto plano antes do envio | GDE-AASP-GOV-001 (D05) |
| Sincronização incremental | Limitada a status — evita sobrescrever edições manuais no Jira | GDE-AASP-GOV-001 (D06) |
| Execução | Azure Scheduled Job stateless — idempotência por `#ID` dispensa rastrear estado | GDE-AASP-GOV-001 (D07) |

## 3. Design de produto (UX/UI) — não aplicável

Serviço de retaguarda (Azure Scheduled Job), sem interface de usuário. Conforme ADAP-AASP-GOV-001, o design de UX/UI não se aplica.

## 4. Rastreabilidade requisito → design

| Requisito (ID) | Elemento de design |
|---|---|
| RF01 | SensrService — login JWT por desenvolvedor |
| RF02, RF03, RF04 | JiraService — criação de Epic, Task e Subtask |
| RF05 | SyncService — `UpdateIssueIfNeededAsync` (transição de status) |
| RF06 | JiraService — comentários a partir de `description_history` |
| RF07 | HtmlHelper + `BuildAdfDocument` (HTML → texto plano → ADF) |
| RF08 | StatusMapper (mapeamento Sensr → Jira) |
| RF09 | `SanitizeLabel` |
| RF10 | AppSettings / DeveloperConfig / ProjectConfig |
| RF11 | Program.cs — bootstrap via DI; código de saída em falha |
| RNF01 | Verificação por `#ID` em `GetIssuesByEpicAsync` antes de criar |
| RNF04 | Separação Core / Infrastructure / App |

Matriz completa em RASTR-AASP-GOV-001.

## 5. Avaliação do design

| Item avaliado | Problema encontrado | Tratamento |
|---|---|---|
| Envio de campos de texto rico ao Jira | HTML do Sensr enviado diretamente causava formatação inválida | HtmlHelper com `ToPlainText` e `ParseDescriptionHistory` (BUG-01) |
| Transições de status | Transições falhando silenciosamente quando o status alvo estava indisponível | Consulta prévia via `GetTransitionsAsync` e log de aviso (BUG-02) |
| Busca de issues por Epic | Ausência de paginação em projetos com muitos cards | Paginação via `nextPageToken` no `GetIssuesByEpicAsync` (BUG-05) |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Documento de design consolidado a partir do Registro de Projeto AASP_Automacao-Governanca v2.0 (08/06/2026) — seção 7 (rotulada "OSW" na fonte) reclassificada como PCP. |
