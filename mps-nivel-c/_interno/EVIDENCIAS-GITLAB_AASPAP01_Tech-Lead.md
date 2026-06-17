# Evidências Técnicas — Projeto AASP AndamentosProcessuais (AASPAP01)
# Fonte: GitLab (self-hosted)

| Campo | Valor |
|---|---|
| **Para** | Raony Chagas (Desenvolvedor Sênior / Principal) |
| **De** | Abraão Oliveira (GP / Responsável MPS-SW) |
| **Data** | 17/06/2026 |
| **Projeto** | AASPAP01 — Refatoração da Solução de Captura de Andamentos Processuais (DataJud/CNJ via WorkerAndamentos) |
| **Fonte das evidências** | **GitLab self-hosted** — `http://191.234.192.153/aasp/andamentosprocessuais` (Project ID 1) |

---

## Contexto

A fonte das evidências técnicas do AASPAP01 passa a ser o **GitLab self-hosted** da Timeware (antes: Azure DevOps). As capturas visuais antigas (`devops_andamentos_*.png`) eram do **Azure DevOps** e devem ser substituídas pelas telas equivalentes do GitLab. Este documento é o índice de evidências, com **links reais** por item MPS.

**Projeto no GitLab:** `http://191.234.192.153/aasp/andamentosprocessuais` (branch padrão `main`).

Estado conferido (17/06/2026): **33 branches** (GitFlow: `main`, `develop`, `homolog`, `feature/*`, `fix/*`), **27 merge requests** (todos merged, **revisor = Cézar** nos 27), **40 pipelines** (39 verdes; 1 falha conhecida na `feature/46500` por `NuGet.config` local), **7 tags + 7 releases** (`v1.0.0`–`v1.5.1`), **43 work items** (27 de PR fechados + governança + 11 CARDs da Iteração 7) e **7 milestones/iterações** (5 concluídas + 2 em andamento).

---

## 1. PCP — Design / Arquitetura

### 1.1 Estrutura da solução (módulos .NET)
**Evidência:** árvore do repositório com os módulos `Andamentos.Captura`, `Andamentos.CapturaApi`, `Andamentos.CapturaServer`, `Andamentos.Models`, `Andamentos.Repositorio`, etc.
`http://191.234.192.153/aasp/andamentosprocessuais/-/tree/main`

### 1.2 Pipeline CI/CD no repositório
**Evidência:** `.gitlab-ci.yml` (estágios build/test/deploy .NET).
`http://191.234.192.153/aasp/andamentosprocessuais/-/blob/main/.gitlab-ci.yml`

---

## 2. ITP — Integração

### 2.1 Pipelines CI/CD
**Evidência:** 40 pipelines por ref (branches + tags), com jobs `build`/`test`. 39 verdes.
`http://191.234.192.153/aasp/andamentosprocessuais/-/pipelines`
*(Obs.: a `feature/46500-criacao-endipoints-novos-distribuidos` falha no restore por `NuGet.config` apontando fonte local — config da branch, não defeito de CI.)*

### 2.2 Integrações (CNJ/EPROC/ESAJ/parceiras) por branch de feature
**Evidência:** branches `feature/*` por frente de integração.
`http://191.234.192.153/aasp/andamentosprocessuais/-/branches`

---

## 3. GCO — Gerência de Configuração

### 3.1 Branches e GitFlow
`http://191.234.192.153/aasp/andamentosprocessuais/-/branches` (33 branches; `main`/`develop`/`homolog` protegidas)

### 3.2 Baselines (tags + releases)
**Evidência:** 7 tags + 7 releases. Numeração `v1.x` do AndamentosProcessuais:
`http://191.234.192.153/aasp/andamentosprocessuais/-/tags` · `…/-/releases`

| Tag | Data | Marco |
|---|---|---|
| `v1.0.0` | 26/09/2025 | Baseline inicial |
| `v1.1.0` | 06/01/2026 | DiscoveryFull + Solucionare |
| `v1.2.0` | 20/02/2026 | Captura EPROC |
| `v1.3.0` | 18/03/2026 | ESAJ/TJSP webhook |
| `v1.4.0` | 26/02/2026 | Worker por instância + RabbitMQ |
| `v1.5.0` | 05/06/2026 | Integração CNJ |
| `v1.5.1` | 09/06/2026 | Hotfix chave de API |

### 3.3 Pull/Merge Requests revisados (code review)
**Evidência:** 27 MRs merged, **revisor vinculado = Cézar** em todos.
`http://191.234.192.153/aasp/andamentosprocessuais/-/merge_requests?state=merged`

---

## 4. VV — Verificação e Validação

### 4.1 Code review (VV2)
27 MRs com revisor/aprovação do Cézar — `…/-/merge_requests?state=merged`.

### 4.2 Pipeline (build/test) — PCP3/VV
Jobs `build`/`test` verdes nos pipelines — `…/-/pipelines`.

### 4.3 Bugs / correções
Work items e MRs de correção (ex.: PR 1725 — chave de API hardcoded; correções de captura/nullabilidade) — `…/-/issues`.

---

## 5. RASTR / REQ — Rastreabilidade

**Evidência:** convenção de branch por feature + MRs que fecham o work item correspondente.
`…/-/branches` + `…/-/merge_requests?state=merged`

---

## 6. GPR — Gestão do Projeto

### 6.1 Iterações (milestones)
7 milestones (5 concluídas + 2 em andamento — Iteração 6 governança e Iteração 7 robustez CNJ).
`http://191.234.192.153/aasp/andamentosprocessuais/-/milestones`

### 6.2 Work items (backlog)
43 work items (27 de PR fechados + governança + 11 CARDs em aberto da Iteração 7).
`http://191.234.192.153/aasp/andamentosprocessuais/-/issues`

---

## 7. Prioridade máxima (fonte GitLab)

| # | Item | Onde buscar no GitLab |
|---|---|---|
| 1 | PRs aprovados (code review) — VV2 | `…/-/merge_requests?state=merged` (27, revisor Cézar) |
| 2 | Baselines (tags/releases) — GCO3 | `…/-/tags` (`v1.0.0`–`v1.5.1`) + `…/-/releases` |
| 3 | Pipelines verdes (build/test) — PCP3 | `…/-/pipelines` |
| 4 | Branches/GitFlow + rastreabilidade — GCO/RASTR | `…/-/branches` + MRs |
| 5 | Iterações + work items — GPR | `…/-/milestones` + `…/-/issues` |

---

## 8. Mapa de equivalência — Azure DevOps → GitLab

| Print antigo (Azure DevOps) | Substituir por (GitLab) |
|---|---|
| `devops_andamentos_estrutura.png` | `/-/tree/main` |
| `devops_andamentos_branches.png` | `/-/branches` |
| `devops_andamentos_commits.png` | `/-/commits/main` |
| `devops_andamentos_prs.png` · `pr_detail_1/2.png` | `/-/merge_requests` (+ detalhe com revisor Cézar) |
| `devops_andamentos_pipeline_ci.png` · `pipeline_cicd.png` | `/-/pipelines` (+ jobs) |
| `devops_andamentos_tags.png` | `/-/tags` + `/-/releases` |

> Os diagramas/fotos neutros (`andamentos_arquitetura.svg`, `ApisParceiras`, `historicoPreservado*`, `retry_webhook`) permanecem válidos. Os prints `devops_*` devem ser recapturados do GitLab e os embutidos em `GCO-AASPAP01` substituídos.

---

*Documento gerado a partir do estado real do GitLab self-hosted (`aasp/andamentosprocessuais`, id 1) em 17/06/2026. Nenhum dado foi inventado.*
