# 📦 DOCS ANTIGOS — versões PRÉ-GitLab (AASP_CNJ / Andamentos Processuais / WorkerAndamentos)

> **Esta pasta guarda as versões ANTIGAS dos documentos** — as que apontavam para **Azure DevOps / Jira / ClickUp** e que tinham os dados **antes da reconciliação com o GitLab**.
> São mantidas **apenas como histórico / fallback**. As versões **válidas e atuais** (fonte = GitLab) estão nas pastas originais (`oficial/04_registros/AASP_CNJ/` e `_interno/`).

## O que tem aqui

| Subpasta | Conteúdo |
|---|---|
| `registros-AASP_CNJ/` | Versões **originais** (pré-GitLab) dos registros oficiais do projeto AASP_CNJ — ainda com referências a Azure DevOps/Jira/ClickUp e com o catálogo antigo (9 bugs / 2 baselines). |
| `coleta-e-backlog/` | Guia de coleta de evidências original (`COLETA-EVIDENCIAS_AASPCNJ`) e o arquivo de importação do Jira (`JIRA-AASPCNJ01_Backlog-Import.csv`). |

## De → Para (versão antiga → versão GitLab atual)

| Antigo (aqui) | Atual (fonte GitLab) |
|---|---|
| `coleta-e-backlog/COLETA-EVIDENCIAS_AASPCNJ_Tech-Lead.*` | `_interno/EVIDENCIAS-GITLAB_AASPCNJ_Tech-Lead.*` |
| `coleta-e-backlog/JIRA-AASPCNJ01_Backlog-Import.csv` | `_interno/GITLAB-AASPCNJ01_Backlog-Export.csv` |
| `registros-AASP_CNJ/*` | `oficial/04_registros/AASP_CNJ/*` (versões alinhadas ao GitLab) |

## Principais diferenças do conteúdo antigo

- Fonte de evidência: **Azure DevOps / Jira / ClickUp** (antigo) → **GitLab self-hosted `aasp/cnj`** (atual).
- Bugs: **9** (BUG-01..09) no antigo → **10** (BUG-01..10) alinhado ao GitLab.
- Baselines: **2** (BL-EPROC, BL-CNJ) no antigo → **5** (`v0.9.0`..`v2.0.2`) alinhado ao GitLab.

Data do arquivamento: 17/06/2026.
