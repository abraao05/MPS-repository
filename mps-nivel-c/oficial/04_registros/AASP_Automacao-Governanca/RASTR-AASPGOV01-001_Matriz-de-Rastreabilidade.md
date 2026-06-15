# Matriz de Rastreabilidade — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | RASTR-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.1 |
| **Data** | 02/06/2026 |

---

## Matriz

A rastreabilidade bidirecional é mantida nesta matriz e refletida no Jira via épico → história → tarefa → caso de teste. Cada linha permite navegar da **necessidade do cliente** até o **caso de teste** que valida o atendimento.

### Requisitos funcionais

| Necessidade do cliente | Requisito (ID) | Item de design (PCP) | Item no backlog/Jira | Sprint | Caso de teste (CT) | Critério de aceite | Situação |
|---|---|---|---|---|---|---|---|
| Autenticar no Sensr por desenvolvedor para obter atividades filtradas | RF-01 | SensrService.LoginAsync — JWT individual por DeveloperConfig | EPIC-001 / STORY-AASPGOV-001 | Sprint 0 | CT-06 | CA07 (Resiliência por desenvolvedor) | ✅ Verificado |
| Preservar a hierarquia de projetos na migração | RF-02 | JiraService.GetOrCreateEpicAsync | EPIC-002 / STORY-AASPGOV-002 | Sprint 1 | CT-01 | CA02 (Fidelidade da hierarquia) | ✅ Verificado |
| Migrar atividades preservando todos os campos | RF-03 | JiraService.CreateTaskAsync + SyncService.ExtractSensrId | EPIC-002 / STORY-AASPGOV-003 | Sprint 1 | CT-01, CT-09 | CA02, CA03 (Hierarquia e conteúdo) | ✅ Verificado |
| Preservar relação atividade → sub-atividade | RF-04 | JiraService.CreateSubtaskAsync | EPIC-002 / STORY-AASPGOV-004 | Sprint 1 | CT-09 | CA02 (Fidelidade da hierarquia) | ✅ Verificado |
| Refletir mudanças de status do Sensr no Jira | RF-05 | SyncService.UpdateIssueIfNeededAsync + JiraService.TransitionAsync | EPIC-003 / STORY-AASPGOV-005 | Sprint 2 | CT-03, CT-04 | CA05 (Sincronização incremental) | ✅ Verificado |
| Preservar histórico de alterações | RF-06 | HtmlHelper.ParseDescriptionHistory + JiraService.AddCommentAsync | EPIC-002 / STORY-AASPGOV-006 | Sprint 2 | CT-11 | CA06 (Migração do histórico) | ✅ Verificado |
| Conteúdo legível no Jira (sem tags HTML) | RF-07 | HtmlHelper.ToPlainText + JiraService.BuildAdfDocument | EPIC-002 / STORY-AASPGOV-007 | Sprint 1 | CT-05 | CA03 (Fidelidade do conteúdo) | ✅ Verificado |
| Status equivalente entre as plataformas | RF-08 | StatusMapper.MapSensrToJira | EPIC-003 / STORY-AASPGOV-008 | Sprint 1 | CT-07, CT-08 | CA04 (Fidelidade do status) | ✅ Verificado |
| Labels válidos no Jira sem erro de criação | RF-09 | JiraService.SanitizeLabel | EPIC-002 / STORY-AASPGOV-009 | Sprint 1 | CT-10 | CA03 (Fidelidade do conteúdo) | ✅ Verificado |
| Configuração multi-desenvolvedor sem alteração de código | RF-10 | AppSettings + DeveloperConfig + ProjectConfig | EPIC-001 / STORY-AASPGOV-010 | Sprint 0 | CT-06 | CA07 (Resiliência por desenvolvedor) | ✅ Verificado |
| Execução agendada não supervisionada no Azure | RF-11 | Program.cs — bootstrap com DI + exit code 0/1 | EPIC-004 / STORY-AASPGOV-011 | Sprint 2 | (validado na entrega — execução no Azure Scheduler) | Entrega ao cliente | ✅ Verificado |

### Requisitos não funcionais

| Necessidade do cliente | Requisito (ID) | Item de design (PCP) | Item no backlog/Jira | Sprint | Caso de teste (CT) | Critério de aceite | Situação |
|---|---|---|---|---|---|---|---|
| Sem duplicatas em execuções repetidas | RNF-01 | SyncService — verificação por `#ID` antes de criar | STORY-AASPGOV-012 | Sprint 2 | CT-02 | CA01 (Sem duplicatas) | ✅ Verificado |
| Continuidade do processamento em falha de 1 desenvolvedor | RNF-02 | SyncService — try/catch por DeveloperConfig | STORY-AASPGOV-013 | Sprint 2 | CT-06, CT-12 | CA07 (Resiliência por desenvolvedor) | ✅ Verificado |
| Auditoria de cada execução | RNF-03 | Microsoft.Extensions.Logging em todos os serviços | STORY-AASPGOV-014 | Sprint 2 | (validado por inspeção de log na Fase 4) | Auditoria de execução | ✅ Verificado |
| Evolução do serviço sem reescrita massiva | RNF-04 | Estrutura Core / Infrastructure / App (Decisão D01) | STORY-AASPGOV-015 | Sprint 0 | (validado por inspeção arquitetural) | Decisão D01 (GDE-AASPGOV01-001) | ✅ Verificado |
| Sem exposição de credenciais | RNF-05 | `appsettings.json` gerenciado externamente | STORY-AASPGOV-016 | Sprint 0 | (validado por auditoria de configuração — GCO §6) | Auditoria de configuração (GCO-AASPGOV01-001 §6) | ✅ Verificado |
| Compatibilidade .NET 8 / Azure | RNF-06 | TargetFramework `net8.0` em todos os projetos | STORY-AASPGOV-017 | Sprint 0 | (validado por publicação no Azure) | Entrega ao cliente | ✅ Verificado |

---

## Cobertura

**Requisitos sem cobertura de teste:** nenhum. Todos os 11 RF + 6 RNF possuem caso de teste associado (CT-01 a CT-12) ou validação por inspeção/auditoria documentada (RNF-03, RNF-04, RNF-05, RF-11, RNF-06).

**Itens desenvolvidos sem requisito associado:** nenhum. Todos os componentes implementados (SensrService, JiraService, SyncService, StatusMapper, HtmlHelper, AppSettings/DeveloperConfig/ProjectConfig) estão vinculados a um ou mais requisitos.

**Resumo da cobertura:**

| Categoria | Total | Com caso de teste direto | Com validação por inspeção | Sem cobertura |
|---|---|---|---|---|
| Requisitos funcionais (RF) | 11 | 10 | 1 (RF-11) | 0 |
| Requisitos não funcionais (RNF) | 6 | 2 | 4 | 0 |
| **Total** | **17** | **12** | **5** | **0** |

**Cobertura por critério de aceite:**

| CA | Descrição | Atendido por (RF/RNF) | Validado em (CT) | Situação |
|---|---|---|---|---|
| CA01 | Migração sem duplicatas | RNF-01 | CT-02 | ✅ Verificado |
| CA02 | Fidelidade da hierarquia | RF-02, RF-03, RF-04 | CT-01, CT-09 | ✅ Verificado |
| CA03 | Fidelidade do conteúdo | RF-03, RF-07, RF-09 | CT-01, CT-05, CT-10 | ✅ Verificado |
| CA04 | Fidelidade do status | RF-08 | CT-07, CT-08 | ✅ Verificado |
| CA05 | Sincronização incremental | RF-05 | CT-03, CT-04 | ✅ Verificado |
| CA06 | Migração do histórico | RF-06 | CT-11 | ✅ Verificado |
| CA07 | Resiliência por desenvolvedor | RF-01, RF-10, RNF-02 | CT-06, CT-12 | ✅ Verificado |

Todos os 7 critérios de aceite foram cobertos por casos de teste executados e aprovados — ver REL-VV-AASPGOV01-001 §4.

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 02/06/2026 | Time de Melhoria Contínua | Matriz de rastreabilidade consolidada a partir do Registro de Projeto AASP_Automacao-Governanca v2.0 (08/06/2026). Vínculos a items de backlog (Jira) refletem a modelagem retroativa em 17 stories + sprints conforme GEST-AASPGOV01. |
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Correção de consistência: critério de RNF-05 referenciado à auditoria de configuração (GCO §6) em vez da Decisão D02 (autenticação); padronização do nome. |
