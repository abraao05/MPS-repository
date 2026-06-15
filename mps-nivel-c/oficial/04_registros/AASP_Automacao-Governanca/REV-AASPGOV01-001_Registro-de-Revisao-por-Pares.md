# Registro de Revisão por Pares (Pull Requests) — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | REV-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Plataforma** | Azure DevOps (Git + Pull Requests) — GitFlow |

---

## 1. Prática de revisão por pares

A verificação de código é conduzida via **Pull Request (PR)** no Azure DevOps, seguindo o GitFlow (`main`, `develop`, `feature/*`, `bugfix/*`, `hotfix/*`). O merge de `feature/*` e `bugfix/*` para `develop` exige **revisão e aprovação de ao menos um membro além do autor** e build de CI verde (Azure Pipelines). As entregas (releases) são promovidas de `develop` para `main` com tag de baseline. O próprio PR no Azure DevOps é o registro primário da revisão; esta tabela consolida os PRs do projeto.

> **Nota de evidência:** os identificadores e o histórico completo de cada PR (commits, diffs, comentários) residem no Azure DevOps. Este registro referencia os PRs por **branch e item de trabalho**; os números internos de PR/commit do Azure DevOps são consultáveis na ferramenta pela ASR.

## 2. Registro de Pull Requests — funcionalidades (→ `develop`)

| PR | Branch | Item entregue | Autor | Revisor | Sprint | Resultado |
|---|---|---|---|---|---|---|
| PR-01 | `feature/setup-clean-arch` | Estrutura em camadas Core/Infrastructure/App (D01, RNF04) | Cezar Hiraki | Raony Chagas | S0 | ✅ Aprovado e mergeado |
| PR-02 | `feature/RF01-auth-sensr-jwt` | RF01 — autenticação multi-dev no Sensr (JWT) | Raony Chagas | Cezar Hiraki | S0 | ✅ Aprovado e mergeado |
| PR-03 | `feature/RF02-auth-jira-basic` | RF02 — autenticação no Jira (Basic Auth) | Raony Chagas | Cezar Hiraki | S0 | ✅ Aprovado e mergeado |
| PR-04 | `feature/RNF06-keyvault` | RNF06 — credenciais via Azure Key Vault | Lucas Batista | Cezar Hiraki | S0 | ✅ Aprovado e mergeado |
| PR-05 | `feature/RF03-migracao-epics` | RF03 — migração de projetos como Epics | Allan Alves | Raony Chagas | S1 | ✅ Aprovado e mergeado |
| PR-06 | `feature/RF04-migracao-tasks` | RF04 — migração de atividades como Tasks | Allan Alves | Raony Chagas | S1 | ✅ Aprovado e mergeado |
| PR-07 | `feature/RF05-migracao-subtasks` | RF05 — migração de sub-atividades como Subtasks | Allan Alves | Raony Chagas | S1 | ✅ Aprovado e mergeado |
| PR-08 | `feature/RF07-html-to-adf` | RF07 — conversão HTML → ADF (HtmlHelper) | Raony Chagas | Cezar Hiraki | S1 | ✅ Aprovado e mergeado |
| PR-09 | `feature/RF08-status-mapper` | RF08 — StatusMapper (D07) | Raony Chagas | Cezar Hiraki | S1 | ✅ Aprovado e mergeado |
| PR-10 | `feature/RF10-idempotencia-id` | RF10 — idempotência por prefixo `#ID` (D03) | Raony Chagas | Cezar Hiraki | S1 | ✅ Aprovado e mergeado |
| PR-11 | `feature/RF06-sync-incremental` | RF06 — sincronização incremental de status | Raony Chagas | Allan Alves | S2 | ✅ Aprovado e mergeado |
| PR-12 | `feature/RF09-historico-comentarios` | RF09 — histórico como comentários | Allan Alves | Raony Chagas | S2 | ✅ Aprovado e mergeado |
| PR-13 | `feature/RNF03-logs-estruturados` | RNF03 — logs estruturados por evento | Raony Chagas | Allan Alves | S2 | ✅ Aprovado e mergeado |
| PR-14 | `feature/RF11-paginacao-nextpagetoken` | RF11 — paginação via `nextPageToken` (D06) | Raony Chagas | Cezar Hiraki | S3 | ✅ Aprovado e mergeado |
| PR-15 | `ci/azure-pipelines` | Pipeline CI/CD (IC-03, RNF05) | Lucas Batista | Abraão Oliveira | S0–S1 | ✅ Aprovado e mergeado |

## 3. Registro de Pull Requests — correções (→ `develop`, Fase 4 / HOM)

| PR | Branch | Defeito corrigido | Autor | Revisor | Sprint | Resultado |
|---|---|---|---|---|---|---|
| PR-16 | `bugfix/BUG-01-html-adf` | BUG-01 — HTML não convertido corretamente para ADF (texto truncado) | Raony Chagas | Cezar Hiraki | S3 | ✅ Aprovado e mergeado |
| PR-17 | `bugfix/BUG-02-status-case` | BUG-02 — comparação de status case-sensitive | Raony Chagas | Cezar Hiraki | S3 | ✅ Aprovado e mergeado |
| PR-18 | `bugfix/BUG-03-labels-especiais` | BUG-03 — labels com caracteres especiais rejeitadas pelo Jira | Allan Alves | Raony Chagas | S3 | ✅ Aprovado e mergeado |
| PR-19 | `bugfix/BUG-04-paginacao-50` | BUG-04 — falta de paginação para Epics >50 issues | Raony Chagas | Cezar Hiraki | S3 | ✅ Aprovado e mergeado |
| PR-20 | `bugfix/BUG-05-historico-duplicado` | BUG-05 — comentários duplicados no `description_history` | Allan Alves | Raony Chagas | S3 | ✅ Aprovado e mergeado |

## 4. Registro de Pull Requests — releases (`develop` → `main`)

| PR | Branch | Baseline | Tag | Autor | Aprovação | Data |
|---|---|---|---|---|---|---|
| PR-21 | `release/v0.9.0` | BL-DEV-001 — fim do desenvolvimento | `v0.9.0` | Abraão Oliveira | Cezar Hiraki | 20/05/2026 |
| PR-22 | `release/v1.0.0-rc.1` | BL-HOM-001 — release candidate (validado em ATA-003) | `v1.0.0-rc.1` | Abraão Oliveira | Cezar Hiraki | 29/05/2026 |
| PR-23 | `release/v1.0.0` | BL-PROD-001 — versão de produção (aceite formal) | `v1.0.0` | Abraão Oliveira | Marcos Correa Fernandez Turnes (aceite) | 02/06/2026 |

## 5. Apontamentos tratados em revisão (exemplos)

| # | Apontamento | PR | Tratamento | Situação |
|---|---|---|---|---|
| 1 | Conversão de HTML perdendo formatação em campos longos | PR-16 | Ajuste do HtmlHelper para mapear nós ao ADF corretamente | Resolvido (BUG-01) |
| 2 | Comparação de status sensível a maiúsculas/minúsculas | PR-17 | Normalização case-insensitive no StatusMapper | Resolvido (BUG-02) |
| 3 | Labels com caracteres especiais quebrando a criação de issues | PR-18 | Sanitização de labels antes do envio | Resolvido (BUG-03) |
| 4 | Risco de perda de dados em Epics grandes | PR-19 | Paginação via `nextPageToken` | Resolvido (BUG-04) |

## 6. Resultado

| Resultado | Métrica |
|---|---|
| PRs de funcionalidade aprovados e mergeados | 15 (PR-01 a PR-15) |
| PRs de correção aprovados e mergeados | 5 (PR-16 a PR-20) |
| PRs de release promovidos para `main` | 3 (PR-21 a PR-23) |
| **Total de PRs revisados** | **23** |
| PRs mergeados sem revisão (≥ 1 revisor além do autor) | 0 |

Todos os PRs seguiram a regra de revisão por pares (mínimo 1 revisor além do autor) com build de CI verde antes do merge.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Registro de revisão por pares (Pull Requests) reconstituído a partir do INTAKE-AASPGOV01 (14/06/2026): PRs derivados dos itens entregues (RF/RNF), defeitos (BUG-01 a 05) e baselines (BL-DEV/HOM/PROD), mapeados à equipe e aos sprints. Identificadores internos do Azure DevOps consultáveis na ferramenta. |
