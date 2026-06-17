# Checklist de Capturas — Evidências PROFARMA01 (Cezar)

> Documento de apoio interno. Acompanhamento das 13 tarefas de `TAREFAS-CEZAR_Evidencias-PROFARMA.md`.
> Atualizado em 12/06/2026.

## Status geral

| Tarefa | Descrição | Arquivo esperado | Pasta | Status |
|---|---|---|---|---|
| G1 | Export do cronograma GanttPro (4 fases) | `ganttPro-cronograma-fases-profarma.pdf` | `ganttPro/` | ⬜ Captura manual |
| AD1 | Estrutura de pastas Clean Architecture | `azuredevops-repo-estrutura-clean-arch.png` | `azure-devops/` | ⬜ Captura manual |
| AD2 | Pipeline com 273 testes e 84% cobertura | `azuredevops-pipeline-cobertura-273-testes.png` | `azure-devops/` | ⬜ Captura manual |
| AD3 | Tags de baseline 25.12.1.1 e 26.1.1.1 | `azuredevops-tags-baselines-2512-e-2611.png` | `azure-devops/` | ⬜ Captura manual |
| AD4 | 2–3 PRs aprovados (1 com Armando Junior) | `azuredevops-pr-aprovado-01/02.png` | `azure-devops/` | ⬜ Captura manual |
| AD5 | Branches com rastreabilidade ao Jira | `azuredevops-branches-nomenclatura-jira.png` | `azure-devops/` | ⬜ Captura manual |
| AD6 | AKS homologação com pods Running | `azure-aks-homologacao-pods-running.png` | `azure-devops/` | ⬜ Captura manual |
| AD7 | Pipeline com stage deploy-homologação | `azuredevops-pipeline-stages-deploy-hom.png` | `azure-devops/` | ⬜ Captura manual |
| J1 | Backlog com sprints e story points | `jira-backlog-sprints-story-points.csv` | `jira/` | ✅ Exportado em 12/06/2026 |
| J2 | 3–5 histórias com critérios de aceite | `jira-historia-criterios-aceite-01..03.png` | `jira/` | ⬜ Captura manual |
| J3 | Bugs da homologação (BAL-B03, PDV-B01...) | `jira-bugs-homologacao.csv` | `jira/` | ⚠️ Ver nota abaixo |
| DD1 | Datadog APM pós go-live (`clientes-api`) | `datadog-apm-clientes-api-pos-golive.png` | `datadog/` | ⬜ Captura manual |
| SW1 | Swagger/OpenAPI da API | `api-swagger-ui-screenshot.png` ou `api-documentation-openapi.json` | `swagger/` | ⬜ Captura manual |

## J1 — O que foi exportado

Export via API do Jira (chirakivelazquez.atlassian.net, projeto SCRUM), 66 issues:
7 épicos (SCRUM-5..11), 16 histórias, 41 subtasks, distribuídas em SCRUM Sprint 1 (31 issues) e Sprint 2 (24 issues), com story points em 62/66 issues.

## J3 — Nota

A busca por issues do tipo Bug no projeto SCRUM retornou **0 resultados**. Os bugs citados nas tarefas (BAL-B03, PDV-B01, CC-B01, PBI-26, API-B01, BAL-B01, BAL-B02) não existem nesse Jira — eles devem estar no Jira do cliente (projeto PROFARMA em `profarma.visualstudio.com`/Jira Profarma). A captura J3 precisa ser feita no ambiente onde os bugs foram registrados.

## Prioridade máxima (§7 das tarefas)

1. AD3 — Tags de baseline (GCO3)
2. AD4 — PRs aprovados (VV2)
3. AD2 — Pipeline 273 testes (PCP3, VV4/5)
4. AD6 — AKS homologação (ITP2/4/5, VV3)
5. J3 — Bugs no Jira do cliente (VV1, ITP3)
6. DD1 — Datadog pós go-live (GPR16)
