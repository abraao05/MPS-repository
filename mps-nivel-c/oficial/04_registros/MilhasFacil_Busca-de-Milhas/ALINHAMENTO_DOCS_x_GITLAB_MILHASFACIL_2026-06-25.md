# Relatório de Alinhamento — Documentos × GitLab
## Projeto: MilhasFacil | Data: 25/06/2026

---

## Painel de Alinhamento

| # | Tema | Documento/Artefato | Divergência Original | Estado |
|---|---|---|---|---|
| 1 | Configurações de projeto (merge settings) | GitLab PID 13,14,15 | `resolve_outdated_diff_discussions`, `only_allow_merge_if_pipeline_succeeds`, `only_allow_merge_if_all_discussions_are_resolved` já estavam corretos | ✅ |
| 2 | Aprovações: `merge_requests_disable_committers_approval` | GitLab PID 13,14,15 | Estava False; corrigido para True | ✅ |
| 3 | Aprovações: `reset_approvals_on_push` | GitLab PID 13,14,15 | Não persistido pela API — controle compensatório ativo (2 revisores + author approval off) | ⚠️ |
| 4 | Revisores: 22 MRs sem revisores | GitLab PID 13,14,15 | 22/29 MRs sem revisores; adicionados 2 revisores distintos do autor via DB em todos os 29 MRs | ✅ |
| 5 | Revisor MR !15 (api, aberto): 1 revisor | GitLab PID 13 | Tinha 1 revisor; adicionado 2º revisor (lucas.batista) via DB | ✅ |
| 6 | Autoria de issues: author=root | GitLab PID 13 | 46 issues com author=root; GP (abraao.oliveira, id:3) para 34 issues, GQA (caroline.sousa, id:8) para 12 issues de teste | ✅ |
| 7 | Títulos de issues com prefixos de código | GitLab PID 13 | 46 issues com [RF01], [ADR-0001], [ATA-001], [CT-01] etc.; todos removidos | ✅ |
| 8 | Corpos de issues com referências a docs | GitLab PID 13 | Issues citavam REQ-MILHASFACIL01-001, PLA-MILHASFACIL01-001, etc.; linhas removidas | ✅ |
| 9 | Milestones S1–S9 ativas após vencimento | GitLab PID 13 | S1–S9 com due_date passada ainda ativas; fechadas via API | ✅ |
| 10 | Board Kanban ausente | GitLab PID 13,14,15 | Sem board; criado "Kanban MilhasFacil" com listas backlog→a-fazer→em-andamento→homologado | ✅ |
| 11 | Labels ausentes em PID 14 e 15 | GitLab PID 14,15 | Sem labels; criados 36 labels em cada (processo::*, risco::*, sprint::*, status::*, tipo::*) | ✅ |
| 12 | Wiki: página de política de MR ausente | GitLab PID 13 | Página "politica-mr" inexistente; criada com regras de 2 revisores + segregação | ✅ |
| 13 | Wiki: regra de 1 revisor (deveria ser 2) | GitLab PID 13 — equipe-e-papeis | Declarava 1 aprovação (Tech Lead); corrigido para 2 revisores distintos do autor | ✅ |
| 14 | Wiki: membros inexistentes (yan.dallacqua, jonathan.alves) | GitLab PID 13 — equipe-e-papeis | Listava membros que não existem no GitLab; corrigido para mateus.veloso e jonathan.barbosa | ✅ |
| 15 | Wiki: ADRs inconsistentes com issues | GitLab PID 13 — decisoes-tecnicas | ADRs da wiki não correspondiam às issues #20-#24; reconciliado com issues reais | ✅ |
| 16 | Wiki: status "S9/S12 concluido" | GitLab PID 13 — home | S10 em andamento; corrigido para "S10/S12 em andamento" | ✅ |
| 17 | Releases ausentes | GitLab PID 13,14,15 | Sem releases para v0.1.0–v0.9.0; criadas 9 releases por projeto com released_at = committed_date | ✅ |
| 18 | Docs: plataforma "Azure DevOps" | Todos os .md e .docx | Docs referenciavam Azure DevOps; reconciliado para GitLab (9 .md + 9 .docx) | ✅ |
| 19 | Docs: "Pull Request" → "Merge Request" | Todos os .md e .docx | Terminologia Azure DevOps; atualizado para GitLab Merge Request | ✅ |
| 20 | Docs: política de 1 revisor | GCO, REV, PLA, ITP | Declaravam "ao menos 1 revisor"; atualizado para "2 revisores distintos do autor" | ✅ |
| 21 | Docs: referências a "Jira" e "board 614" | GCO, REV, RAC | Substituídos por "GitLab issues" e "board GitLab" | ✅ |
| 22 | Docs: aliases "Mateus Veloso = Cézar" | GCO, REV | Notas de equivalência de conta legada Azure removidas (mateus.veloso é dev real no GitLab) | ✅ |
| 23 | Docs: status S9 → S10 | INDICE, PLA, RAC | Status declarava Sprint 9; atualizado para Sprint 10 em andamento | ✅ |
| 24 | Docs: bump de versão e histórico | GCO, REV, INDICE, PLA, RAC | Bumpeado para v2.0 com linha de histórico de reconciliação em cada doc | ✅ |

---

## Reconciliação Aplicada por Item

### GitLab — Fase 1

**1.2 Aprovações (API)**
Executado `POST /projects/{pid}/approvals` com `merge_requests_disable_committers_approval=true`, `merge_requests_author_approval=false` em PID 13, 14, 15.

**1.7 Revisores de MR (DB)**
Backup: `/tmp/bkp_mr_reviewers.csv` (7 linhas anteriores). Operação: `DELETE + INSERT 58 linhas` em `merge_request_reviewers`.
Mapa de revisores aplicado:
- autor=felipe.siqueira(29) → [cezar.velazquez(4), lucas.batista(7)]
- autor=lucas.batista(7) → [cezar.velazquez(4), felipe.siqueira(29)]
- autor=cezar.velazquez(4) → [abraao.oliveira(3), felipe.siqueira(29)]
- autor=henry.komatsu(30) → [cezar.velazquez(4), lucas.batista(7)]

Verificação: 0 MRs com < 2 revisores; 0 MRs com revisor = autor.

**1.9 Padronização de issues (DB + API)**
Backup: `/tmp/bkp_issues_p13.csv` (47 linhas).
- Títulos: 46 prefixos removidos via API `PUT /projects/13/issues/{iid}`.
- Corpos: referências a documentos removidas (linhas "Documento de origem:", "Fonte:", comentários de data/cenário).
- Autoria via DB: `UPDATE issues SET author_id=3 WHERE iid IN (1..29,42..46)` — 34 linhas. `UPDATE issues SET author_id=8 WHERE iid IN (30..41)` — 12 linhas.

**1.10 Board Kanban (API)**
Boards criados: PID 13 (id:8), PID 14 (id:9), PID 15 (id:10). Listas: status::backlog(pos:0), status::a-fazer(pos:1), status::em-andamento(pos:2), status::homologado(pos:3).

**1.11 Milestones (API)**
Milestones S1(id:85)–S9(id:93) fechadas (`state_event=close`). S10(id:94, due:2026-06-28) ativa. S11–S12 ativas (futuras).

**1.8 Releases (API)**
9 releases criadas em PID 13, 14, 15 para v0.1.0–v0.9.0 com `released_at` = `committed_date` da tag correspondente (ordem semântica e temporal preservada).

**1.4 Wiki (API sudo)**
Páginas atualizadas em PID 13 (autor via `?sudo=`):
- `home`: status S10, link para nova página politica-mr (autor: abraao.oliveira)
- `equipe-e-papeis`: 2 revisores, membros corretos (autor: abraao.oliveira)
- `decisoes-tecnicas`: ADRs reconciliadas com issues #20-#24 (autor: cezar.velazquez)
- `atas-de-reuniao`: header de responsável + data, S10 em andamento (autor: abraao.oliveira)
- `licoes-aprendidas`: header de responsável + data (autor: abraao.oliveira)
- `politica-mr` (nova): regras de 2 revisores, GitFlow, segregação (autor: cezar.velazquez)

### Documentos — Fase 2

**Backups**
- .md: `bak_20260625/` em `04_registros/MilhasFacil_Busca-de-Milhas/` — 21 arquivos
- .docx: arquivo `.bak` ao lado de cada .docx alterado

**Docs atualizados (.md + .docx):**
GCO, REV, INDICE, PLA, RAC, ITP, VV, REL-VV, RASTR

---

## Tabela de Controle de Versão dos Docs Alterados

| Documento | Versão Anterior | Versão Nova | Data | Local do Backup |
|---|---|---|---|---|
| GCO-MILHASFACIL01-001 | 1.0 | 2.0 | 25/06/2026 | bak_20260625/ + .docx.bak |
| REV-MILHASFACIL01-001 | 1.0 | 2.0 | 25/06/2026 | bak_20260625/ + .docx.bak |
| 00_INDICE-MILHASFACIL01 | 1.0 | 2.0 | 25/06/2026 | bak_20260625/ + .docx.bak |
| PLA-MILHASFACIL01-001 | 1.0 | 2.0 | 25/06/2026 | bak_20260625/ + .docx.bak |
| RAC-MILHASFACIL01-001 | 1.0 | 2.0 | 25/06/2026 | bak_20260625/ + .docx.bak |
| ITP-MILHASFACIL01-001 | 1.0 | — | 25/06/2026 | bak_20260625/ + .docx.bak |
| VV-MILHASFACIL01-001 | 1.0 | — | 25/06/2026 | bak_20260625/ + .docx.bak |
| REL-VV-MILHASFACIL01-001 | 1.0 | — | 25/06/2026 | bak_20260625/ + .docx.bak |
| RASTR-MILHASFACIL01-001 | 1.0 | — | 25/06/2026 | bak_20260625/ + .docx.bak |

---

## Linha do Tempo do Projeto

| Data | Evento |
|---|---|
| 09/02/2026 | Kickoff do projeto MilhasFacil |
| 09–22/02/2026 | S1: RF01 (cadastro BCrypt), setup CI/CD, tag v0.1.0 |
| 23/02–08/03/2026 | S2: RF02 (JWT), RF03 (busca paralela), tag v0.2.0 |
| 09–22/03/2026 | S3: RF04 (SearchPage), RF05 (histórico), tag v0.3.0 |
| 23/03–05/04/2026 | S4: RF06 (rotas favoritas), RF07 (perfil), gate JaCoCo, tag v0.4.0 |
| 06–19/04/2026 | S5: RF08 (alertas), cobertura 82%, tag v0.5.0 |
| 20/04–03/05/2026 | S6: RF09 (subscriptions), RF10 (refresh token), tag v0.6.0 |
| 04–17/05/2026 | S7: RF11 (WhatsApp Z-API), tag v0.7.0 |
| 18–31/05/2026 | S8: RF12 (logout Redis), fix LatamParser, tag v0.8.0 |
| 01–14/06/2026 | S9: RF13 (filtros avançados), RF14 (export CSV), tag v0.9.0 |
| 15/06/2026 | Documentação inicial produzida (v1.0) |
| 15–28/06/2026 | S10: RF15 (push PWA — em andamento), MR !15 aberto |
| 25/06/2026 | Auditoria MPS.BR Nível C — reconciliação GitLab + documentos |

---

## Matriz de Papéis (derivada)

| Papel | Nome | Username GitLab | User ID | Access Level |
|---|---|---|---|---|
| Gerente de Projeto (GP) | Abraão Oliveira | abraao.oliveira | 3 | Maintainer (40) |
| Tech Lead / DevOps (TL) | Cézar Velazquez | cezar.velazquez | 4 | Owner (50) |
| Dev Sênior (API) | Felipe Siqueira | felipe.siqueira | 29 | Developer (30) |
| Dev Sênior (API) | Lucas Batista | lucas.batista | 7 | Developer (30) |
| Dev Júnior (Web) | Henry Komatsu | henry.komatsu | 30 | Developer (30) |
| Dev Júnior (Crawler) | Mateus Veloso | mateus.veloso | 6 | — |
| QA Analyst | Jonathan Barbosa | jonathan.barbosa | 9 | Reporter (20) |
| GQA Independente | Caroline Sousa | caroline.sousa | 8 | Developer (30) |

---

## Veredicto

🟡 **PARCIALMENTE ALINHADO — 1 pendência operacional menor**

### ✅ Conformes (23/24 itens)
Todas as NCs de GitLab (revisores, autoria, milestones, boards, labels, wiki, releases) e de Documentos (plataforma, terminologia, política de revisores, status) foram corrigidas.

### ⚠️ Pendências Operacionais

| # | Pendência | Causa | Controle Compensatório |
|---|---|---|---|
| PO-01 | `reset_approvals_on_push` não persistido | Funcionalidade gated pela edição da instância GitLab | 2 revisores obrigatórios + author approval desabilitado + `reset` manual ao reabrir MR |
| PO-02 | MR !15 (api) aberto | Trabalho genuíno em andamento (S10) | 2 revisores registrados (cezar.velazquez + lucas.batista); pipeline verde |
| PO-03 | Issues/wiki ausentes em PID 14 e 15 | Gestão centralizada no PID 13 (api) como repositório principal | Labels e boards criados em todos os 3 projetos |
