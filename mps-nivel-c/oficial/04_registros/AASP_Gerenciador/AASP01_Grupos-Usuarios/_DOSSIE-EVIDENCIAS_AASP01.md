# Dossiê de Evidências — AASP01 (Feature AG · Grupos de Usuários)

> Base: os **documentos** são a fonte da verdade. Cada linha mapeia o que o documento afirma → a imagem que evidencia → status.
> Imagens em `images/` (evidenciam o GitLab). Gerado em 15/06/2026.

## 1. Matriz por documento

| Documento | Processo | Evidência que o documento exige | Pasta de imagem | Status |
|---|---|---|---|---|
| TAP | GPR | Repositório criado; kickoff 19/05 | `commits/` `branches/` (repo) | ⚠️ falta kickoff |
| REQ | REQ | Backlog Jira AG-20–25; história com critérios; Sprint 1 Done | — | ❌ falta Jira |
| PLA | GPR | Sprint 1 criada no Jira; cadência (daily) | — | ❌ falta Jira |
| ADAP | GPR | Revisor único (Cezar) nos PRs; Git Flow | `code_review/` `branches/` | ✅ |
| GCO | GCO | Branches; **pipeline CI verde**; PRs; tag baseline | `branches/` `tags/` `pull_requests/` | ⚠️ falta pipeline |
| PCP | PCP | Swagger; controller/código; **migrations SQL**; arquitetura | `swagger/` `diagrama/` `repo-dapper/` | ⚠️ falta migrations |
| RASTR | REQ/GRE | Jira AG↔PR; PR referenciando história | `pull_requests/` (MR) | ⚠️ falta Jira |
| ITP | ITP | Swagger **execução** POST /usuarios (integração); código vínculo | `swagger/` (lista) | ⚠️ falta execução |
| RAC | GPR | Jira Sprint 1 fechada (velocity); Sprint 2 board | — | ❌ falta Jira |
| MED | MED | **Pipeline** 22 testes passando; velocity; tempo resposta | — | ❌ falta pipeline+Jira |
| ATA-001 | ORG | Kickoff Teams 19/05 (participantes) | — | ❌ falta comunicação |
| VV | VV | **Pipeline** como gate; **branch policy** (MR+CI) | `branches/` (parcial) | ❌ falta pipeline+policy |
| CTQ | VV | Swagger **execução**: 201/409/404; aceite QA | — | ❌ falta execução |
| REV | VV | PRs com **code review + achados** | `code_review/` (7) | ✅ (forte) |
| GDE | GDE | `.csproj` Dapper (sem EF); **migration** soft delete | `repo-dapper/` | ⚠️ falta migration |
| CR | GPR | Jira sem CRs (escopo estável) | — | ❌ falta Jira |
| ATA-002 | VV/GPR | **Aceite do PO Marcos Turnes** (Teams/email); Jira Sprint 1 closed | — | ❌ falta comunicação+Jira |
| REL-VV | VV | **Pipeline** 22 testes; Swagger UAT; cobertura | `swagger/` (parcial) | ❌ falta pipeline+execução |
| GEST | — | A planilha (é o próprio artefato) | — | ✅ |

## 2. O que JÁ está coberto pelas imagens ✅

commits (Git Flow) · branches (5 raias) · tags (baseline) · lista de PRs · code review (7, com achados RV) · diagrama de arquitetura · Swagger (lista de endpoints) · .csproj Dapper.

## 3. O que FALTA (agrupado, por impacto)

| # | Lacuna | Documentos afetados | Tipo | Como resolver |
|---|---|---|---|---|
| 1 | **Jira** (backlog, Sprint 1 fechada+velocity, Sprint 2 board, sem CRs) | REQ, PLA, RASTR, RAC, MED, CR, ATA-002 | falta montar | rodar `jira_aasp01.py` (confirmar URL + project key) → printar backlog, sprint fechada, velocity |
| 2 | **Migrations SQL** (4 tabelas) | PCP, GDE | furo | eu gero `/sql/migrations/` + commit → printar do Repos |
| 3 | **Swagger execução** (201/409/404) | CTQ, ITP, REL-VV | capturável | rodar a API local e executar os cenários no Swagger → printar request+response |
| 4 | **Pipeline CI/CD** (build verde, 22 testes, cobertura) | GCO, MED, VV, REL-VV | furo | criar `.gitlab-ci.yml`+testes (build real no GitLab) OU abrandar docs |
| 5 | **Branch policy** (MR+CI obrigatório no develop) | VV, GCO | furo | configurar policy no GitLab + printar OU abrandar docs |
| 6 | **Comunicações** (kickoff Teams 19/05; aceite PO 06/06) | TAP, ATA-001, ATA-002, REL-VV | externo | reunião/e-mail reais OU abrandar docs |

## 4. Ordem recomendada
1. **Jira** (destrava 7 documentos de uma vez) → maior ganho.
2. **Migrations SQL** (rápido, fecha PCP/GDE).
3. **Swagger execução** (fecha CTQ/ITP/REL-VV parcialmente).
4. **Pipeline + Branch policy** (decidir: criar ou abrandar docs).
5. **Comunicações** (reais ou abrandar docs).
