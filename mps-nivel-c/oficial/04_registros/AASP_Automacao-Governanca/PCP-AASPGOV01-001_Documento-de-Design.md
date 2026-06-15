# Documento de Design — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | PCP-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Responsáveis** | Cezar Hiraki Velazquez (Tech Lead / Arquiteto) · Raony Chagas (Desenvolvedor Sênior) |
| **Design avaliado em** | 16/04/2026 — Cezar Hiraki Velazquez |

---

## 1. Visão geral da solução

O **SensrJiraSync** é um serviço de sincronização unidirecional (Sensr → Jira) em .NET 8 LTS, executado como **Azure Scheduled Job**. A cada execução, migra e sincroniza as atividades de todos os desenvolvedores configurados. O design atende aos requisitos de idempotência (RNF02), disponibilidade (RNF03), rastreabilidade (RNF04), manutenibilidade (RNF05) e segurança de credenciais (RNF06).

## 2. Arquitetura (clean architecture em camadas) — decisão D01

| Projeto | Responsabilidade | Componentes principais |
|---|---|---|
| `SensrJiraSync.Core` | Contratos, modelos de domínio e mapeadores; sem dependências externas | AppSettings, DeveloperConfig, ProjectConfig, SensrModels, JiraModels, StatusMapper |
| `SensrJiraSync.Infrastructure` | Serviços de integração e helpers de transformação | SensrService, JiraService, SyncService, HtmlHelper |
| `SensrJiraSync.App` | Ponto de entrada, configuração (Azure Key Vault) e composição via DI | Program.cs, appsettings.json |

Dependências unidirecionais: `App → Infrastructure → Core`. Separação de responsabilidades, testabilidade e manutenibilidade (D01).

## 3. Fluxo de sincronização

1. Para cada desenvolvedor configurado: autenticação no Sensr via JWT individual (D05).
2. Para cada projeto: busca das atividades do desenvolvedor via API Sensr.
3. Resolve ou cria o Epic correspondente no Jira pelo nome do projeto.
4. Indexa as Tasks existentes sob o Epic pelo prefixo `#ID` no summary (D03), com paginação via `nextPageToken` (D06).
5. Para cada atividade:
   - Se o `#ID` **não existe** → cria Task completa (descrição em ADF, labels, status, histórico como comentários, subtasks).
   - Se **já existe** → verifica divergência de status e aplica a transição se necessário (sincronização incremental).

## 4. Mapeamento de entidades

| Entidade Sensr | Entidade Jira | Observações |
|---|---|---|
| Projeto | Epic | Um Epic por projeto, reutilizado em execuções subsequentes via busca por nome |
| Atividade | Task | Summary `#ID Nome`; descrição convertida de HTML para ADF |
| Sub-atividade | Subtask | Vinculada à Task pai (RF05) |
| `description_history` | Comentários | Cada entrada do histórico convertida e adicionada como comentário individual (RF09) |
| Tags | Labels | Normalizadas/sanitizadas para o formato aceito pelo Jira (CT-08, CT-12) |
| Status Sensr → Jira | Transição de status | TODO→To Do, DOING→In Progress, VALIDATION→To Test, STOPPED→Blocked, DONE→Done (StatusMapper, D07) |

## 5. Decisões de design (resumo)

| Decisão | Escolha | RAD |
|---|---|---|
| Arquitetura da solução | Clean architecture em 3 camadas | GDE-AASPGOV01-001 (D01) |
| Texto rico no Jira | ADF (Atlassian Document Format) | GDE-AASPGOV01-001 (D02) |
| Idempotência | Prefixo `#ID` no summary | GDE-AASPGOV01-001 (D03) |
| Runtime | Azure Scheduled Job | GDE-AASPGOV01-001 (D04) |
| Autenticação Sensr | JWT por desenvolvedor | GDE-AASPGOV01-001 (D05) |
| Paginação Jira | Cursor via `nextPageToken` | GDE-AASPGOV01-001 (D06) |
| StatusMapper | Classe isolada | GDE-AASPGOV01-001 (D07) |

## 6. Design de produto (UX/UI) — não aplicável

Serviço de retaguarda (Azure Scheduled Job), sem interface de usuário.

## 7. Rastreabilidade requisito → design

| Requisito | Elemento de design |
|---|---|
| RF01 | SensrService — login JWT por desenvolvedor |
| RF02, RF03, RF04, RF05 | JiraService — Epic, Task, Subtask |
| RF06 | SyncService — atualização incremental de status |
| RF07 | HtmlHelper + ADF |
| RF08 | StatusMapper |
| RF09 | JiraService — comentários a partir do `description_history` |
| RF10 | Indexação por `#ID` antes de criar |
| RF11 | Paginação `nextPageToken` em `GetIssuesByEpicAsync` |
| RNF04 | Camadas Core / Infrastructure / App |
| RNF06 | Azure Key Vault na camada App |

Matriz completa em RASTR-AASPGOV01-001.

## 8. Avaliação do design (PCP 2)

Design em camadas avaliado formalmente por **Cezar Hiraki Velazquez** em **16/04/2026** (fim da Fase 1), antes do início da construção. A separação Core/Infrastructure/App e a estratégia de idempotência por `#ID` foram aprovadas como base para o desenvolvimento. Problemas de integração identificados posteriormente (HTML/ADF, status, labels, paginação) foram tratados como defeitos na homologação (BUG-01 a BUG-05, ver REL-VV-AASPGOV01-001).

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Documento de design consolidado a partir do INTAKE-AASPGOV01 (14/06/2026), Blocos 6 e 7. |
