# Plano de Projeto — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | PLA-AASP-GOV-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Gerente de Projeto** | Cezar Hiraki Velazquez |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Identificação e objetivo do projeto

Desenvolver o serviço **SensrJiraSync** — solução .NET 8 executada como Azure Scheduled Job que migra cards do Sensr para o Jira e mantém a sincronização incremental de status durante o período de transição entre as duas ferramentas. A AASP migra sua gestão de projetos do Sensr para o Jira de forma gradual, com operação em paralelo durante a transição. Ver REQ-AASP-GOV-001 para os requisitos detalhados.

## 2. Escopo (GPR 1)

- **Incluído:** autenticação nas APIs Sensr (por desenvolvedor) e Jira; migração de projetos (Epics), atividades (Tasks) e sub-atividades (Subtasks) com preservação de hierarquia, descrição, status, responsáveis, labels e histórico; sincronização incremental de status; execução agendada e não supervisionada via Azure Scheduler.
- **Não incluído:** sincronização bidirecional (apenas Sensr → Jira); atualização de campos de cards já migrados além do status.

Detalhamento em REQ-AASP-GOV-001.

## 3. Adaptação do processo (GPR 2)

O processo-padrão (PRO-GPR-001) foi adaptado a este projeto. Registro completo em ADAP-AASP-GOV-001. Principais decisões:

| Item de adaptação | Decisão | Justificativa |
|---|---|---|
| Planejamento e acompanhamento | Consolidados em documento único, sem plano separado | Projeto de curta duração com escopo fixo |
| Cronograma | Por atividade, sem sprints formais | Equipe pequena com comunicação direta |
| Origem dos requisitos | Timeware especifica; AASP valida e homologa | Escopo definido na reunião de abertura |
| Medição | Indicadores apurados ao encerramento | Projeto sem sprints formais; ciclo único |

## 4. Estrutura de fases e entregas (GPR 5)

| Fase | Descrição | Período | Status |
|---|---|---|---|
| Fase 1 — Arquitetura | Definição da arquitetura em camadas, estrutura de projetos, contratos de interface e modelo de configuração | 14/04 – 16/04/2026 | ✅ Concluída |
| Fase 2 — Mapeamento e Autenticação | Mapeamento dos endpoints das APIs Sensr e Jira; implementação dos fluxos de autenticação JWT (Sensr) e Basic Auth (Jira) | 17/04 – 23/04/2026 | ✅ Concluída |
| Fase 3 — Desenvolvimento dos Serviços | Implementação do SensrService, JiraService, SyncService, StatusMapper, HtmlHelper, modelos de dados e fluxo completo | 24/04 – 20/05/2026 | ✅ Concluída |
| Fase 4 — Homologação e Correções | Execução em ambiente real, comparação de cards migrados, identificação e correção de defeitos | 21/05 – 02/06/2026 | ✅ Concluída |

## 5. Cronograma executado (GPR 5)

| Atividade principal | Início | Fim |
|---|---|---|
| Definição da arquitetura em camadas (Core, Infrastructure, App) | 14/04/2026 | 16/04/2026 |
| Definição do modelo de configuração (AppSettings, DeveloperConfig, ProjectConfig) | 14/04/2026 | 16/04/2026 |
| Mapeamento dos endpoints da API Sensr (login, atividades, detalhe, sub-atividades) | 17/04/2026 | 21/04/2026 |
| Mapeamento dos endpoints da API Jira v3 (search, create, transitions, comments) | 17/04/2026 | 23/04/2026 |
| Implementação do fluxo de autenticação Sensr (JWT por desenvolvedor) | 17/04/2026 | 19/04/2026 |
| Implementação do fluxo de autenticação Jira (Basic Auth com API Token) | 20/04/2026 | 22/04/2026 |
| Implementação dos modelos de dados Sensr (SensrModels.cs) | 24/04/2026 | 26/04/2026 |
| Implementação dos modelos de dados Jira (JiraModels.cs, ADF) | 24/04/2026 | 27/04/2026 |
| Desenvolvimento do SensrService (login, atividades, detalhe, sub-atividades) | 27/04/2026 | 30/04/2026 |
| Desenvolvimento do JiraService (epic, task, subtask, transitions, comments) | 28/04/2026 | 07/05/2026 |
| Desenvolvimento do StatusMapper (mapeamento de status Sensr → Jira) | 05/05/2026 | 06/05/2026 |
| Desenvolvimento do HtmlHelper (ToPlainText, ParseDescriptionHistory) | 05/05/2026 | 07/05/2026 |
| Desenvolvimento do SyncService — fluxo de criação de issues | 07/05/2026 | 13/05/2026 |
| Desenvolvimento do SyncService — fluxo de atualização (sincronização incremental) | 11/05/2026 | 15/05/2026 |
| Implementação do Program.cs e bootstrap via DI | 15/05/2026 | 17/05/2026 |
| Configuração do Azure Scheduled Job | 17/05/2026 | 20/05/2026 |
| Execução inicial em homologação e comparação com dados do Sensr | 21/05/2026 | 23/05/2026 |
| Identificação e correção de defeitos na atualização de cards existentes | 23/05/2026 | 29/05/2026 |
| Reteste e validação final dos critérios de aceite | 29/05/2026 | 02/06/2026 |

## 6. Estimativas de esforço (GPR 3, 4)

| Fase | Esforço estimado (h) | Esforço realizado (h) |
|---|---|---|
| Fase 1 — Arquitetura | 16 | 16 |
| Fase 2 — Mapeamento e Autenticação | 40 | 44 |
| Fase 3 — Desenvolvimento dos Serviços | 120 | 128 |
| Fase 4 — Homologação e Correções | 40 | 48 |
| **Total** | **216** | **236** |

Desvio de esforço: **+9% (+20 h)**, dentro da meta de ≤ 10% (ver MED-AASP-GOV-001).

## 7. Recursos (GPR 6, 7)

| Papel | Membro | Período | Fases |
|---|---|---|---|
| Gerente de Projeto / Tech Lead | Cezar Hiraki Velazquez | 14/04 – 02/06/2026 | Todas |
| Desenvolvedor Sênior | Raony Chagas | 14/04 – 02/06/2026 | 1, 2, 3 e 4 |
| Desenvolvedor | Allan Barbosa Patrocínio Alves | 17/04 – 02/06/2026 | 2, 3 e 4 |

**Ambiente e ferramentas:** Azure DevOps (controle de versão e pipeline CI/CD), Azure Scheduler (execução agendada), .NET 8. Ver GCO-AASP-GOV-001.

## 8. Partes interessadas e comunicação (GPR 9)

| Parte interessada | Interesse | Comunicação |
|---|---|---|
| Marcos Correa Fernandez Turnes (Patrocinador / Cliente — AASP) | Validação do comportamento e aceite formal | Reunião de abertura e homologação |
| Time de desenvolvimento | Execução e decisões técnicas | Alinhamento direto e revisão de código |
| Jonathan Barbosa (Auditor GQA) | Aderência ao processo MPS-SW | Auditoria ao encerramento |

## 9. Riscos identificados e tratamentos (GPR 10)

Exposição = Probabilidade × Impacto (escala 1 = Baixo · 2 = Médio · 3 = Alto).

| ID | Risco | Prob. | Imp. | Exp. | Resposta / Tratamento | Status |
|---|---|---|---|---|---|---|
| R-01 | Criação de cards duplicados no Jira por execuções repetidas | 3 | 3 | 9 | Mitigar: verificação de existência pelo prefixo `#ID` no summary antes de qualquer criação | ✅ Controlado |
| R-02 | Diferenças de formato entre modelos de dados das plataformas | 3 | 2 | 6 | Mitigar: camada de transformação dedicada — StatusMapper e HtmlHelper | ✅ Controlado |
| R-03 | Falha de autenticação de um desenvolvedor interrompendo toda a execução | 2 | 3 | 6 | Mitigar: tratamento de exceção por desenvolvedor no SyncService com continuidade | ✅ Controlado |
| R-04 | Comportamento inconsistente da API Jira para transições de status | 2 | 3 | 6 | Mitigar: consulta prévia das transições disponíveis antes de aplicar; log de aviso | ⚠️ Ocorreu — corrigido |
| R-05 | Volume elevado de issues no Epic exigindo paginação | 2 | 2 | 4 | Mitigar: paginação via `nextPageToken` no `GetIssuesByEpicAsync` | ✅ Controlado |
| R-06 | Campos de texto rico do Sensr em HTML incompatível com Jira | 3 | 2 | 6 | Mitigar: HtmlHelper para conversão de HTML para texto plano e serialização para ADF | ⚠️ Ocorreu — corrigido |

## 10. Aprovação do plano (GPR 13)

| Envolvido | Papel | Aceite | Data |
|---|---|---|---|
| Marcos Correa Fernandez Turnes | Patrocinador / Cliente (AASP) | Autorização do projeto | 14/04/2026 (TAP-AASP-GOV-001) |
| Cezar Hiraki Velazquez | Gerente de Projeto | Baseline do plano | 14/04/2026 |

> A baseline de aprovação foi estabelecida na abertura (TAP-AASP-GOV-001) e o aceite final foi registrado no encerramento (TAE-AASP-GOV-001, 02/06/2026).

---

## Controle de atualizações do plano

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Plano consolidado a partir do Registro de Projeto AASP_Automacao-Governanca v2.0 (08/06/2026). |
