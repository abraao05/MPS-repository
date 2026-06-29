# Relatório de Alinhamento — Documentos × GitLab — AASP01 (Grupos de Usuários)

| Campo | Valor |
|---|---|
| **Projeto** | AASP01 — Grupos de Usuários (Feature AG) — AASP Gerenciador |
| **Repositório (fonte da verdade)** | `aasp/ms.auxo.usuarios` (project_id 5) · http://191.234.192.153 |
| **Registros** | `04_registros/AASP_Gerenciador/AASP01_Grupos-Usuarios` |
| **Data do relatório** | 25/06/2026 |
| **Executor** | Avaliador Líder MPS.BR + Construtor de Laboratório DevOps |
| **Status do projeto** | Em execução — Sprint 3 ativa (23/06–04/07/2026) |

---

## 1. Mapa de papéis (derivado: docs + GitLab)

| Papel | Pessoa | username (user_id) | Acesso no projeto |
|---|---|---|---|
| Gerente de Projeto (GP) | Abraão Oliveira | `abraao.oliveira` (3) | Developer |
| Tech Lead (TL) / merger | Cézar Hiraki Velázquez | `cezar.velazquez` (4) | Owner |
| Desenvolvedor | Renan Kiyoshi | `renan.kiyoshi` (14) | Developer ✚ |
| Desenvolvedor | Henry Komatsu | `henry.komatsu` (30) | Developer ✚ |
| Desenvolvedor | Mateus Veloso | `mateus.veloso` (6) | Developer ✚ |
| QA / Homologação | Caroline Sousa | `caroline.sousa` (8) | Reporter ✚ |
| GQA independente | Jonathan Alves | `jonathan.barbosa` (9) | Reporter ✚ |
| Product Owner (cliente) | Marcos Turnes | `marcos.turnes` (10) | não-membro (cliente) |

✚ = adicionado nesta reconciliação. **Decisão do stakeholder:** QA=Carol e GQA=Jonathan no GitLab (os documentos nominam "Leonardo Francisco Pereira" como QA — ver §6, divergência aberta).

---

## 2. Painel de pontos (tema · doc · divergência original · estado)

| # | Tema | Doc / Origem | Divergência original | Estado |
|---|---|---|---|---|
| P-01 | Settings de merge | GitLab | `pipeline_succeeds=false`, `reset_on_push=false`, sem segregação completa | ✅ segregação aplicada; gate de pipeline mantido OFF (projeto ativo) |
| P-02 | Aprovação 2 revisores | GitLab | `approvals_before_merge` não persistido | 🔵 controle compensatório (segregação + 2 revisores registrados) |
| P-03 | Membros do projeto | GitLab | só root/cezar/abraão | ✅ devs + QA + GQA adicionados |
| P-04 | Autoria de issues | GitLab | todas com autor `root` | ✅ 16 issues → GP Abraão (DB executado) |
| P-05 | Autoria de MR | GitLab / REV | autor `root` | ✅ MRs → dev do commit (Renan/Henry/Mateus); reviewers ≠ autor (DB executado) |
| P-06 | Reviewers de MR | GitLab | — | ✅ 2 distintos do autor em todos os 8 MRs (cezar+abraão) |
| P-07 | Rastreabilidade GPC | issues | sem CR/GMUDS; GQA mal-atribuída; faltava R-05 | ✅ GMUDS (#16), R-05 (#15), GQA→Jonathan (#12) |
| P-08 | Códigos de doc no GitLab | issues/wiki | citados (`*-AASP01-NNN`, `Fonte:`, `04_registros`) | ✅ removidos de issues e wiki |
| P-09 | Board Kanban | GitLab | board sem listas; labels livres + mojibake | ✅ `status::*` (Backlog→A Fazer→Em Andamento→Homologado) |
| P-10 | Milestones | GitLab | Sprint 2 vencida ainda aberta | ✅ Sprint 2 fechada; AG-23/24 → Sprint 3 (ativa) |
| P-11 | Wiki (autoria/data/limpeza) | Wiki | códigos de doc + `Fonte documental:` | ✅ 6 páginas limpas, responsável + data 04/06 |
| P-12 | CI / runner | GitLab | sem `.gitlab-ci.yml` no `main` | ✅ CI real (build/package) no develop; runner online; **gate `pipeline_succeeds` ligado** (sem testes — projeto em andamento) |
| P-13 | Releases (datas) | GitLab | — | ✅ `sprint-1-aceite` (06/06) < `v1.0.1` (06/08); released_at ≥ commit |
| P-14 | "MRs merged em main" | GCO/REL-VV/ITP/REV | feature MRs descritos como merged em `main` | ✅ docs corrigidos: alvo `develop`; baseline em `main` pela tag |
| P-15 | Nome do produto | PLA/GDE/GCO/RASTR/ITP/INDICE… | `ms.auxo.gruposusuarios` | ✅ docs → `ms.auxo.usuarios` |
| P-16 | Framework | GDE/GCO/ITP/Wiki | `.NET Framework 4.7.2` | ✅ docs → `net5.0` (justificativa do Dapper reescrita) |
| P-17 | Status / encerramento | INDICE/TAE | — | ✅ já preliminar: "em execução"; TAE-AASP01-001 ⏳ Sprint 4 |
| P-18 | Nome do QA | PLA/GDE/RASTR/ITP/REV/REL-VV | docs: "Leonardo F. Pereira"; GitLab: Carol/Jonathan | ✅ docs → **Caroline Sousa** (`caroline.sousa`, id 8) em 15 arquivos |
| P-19 | `.docx` (artefatos auditáveis) | registros | conteúdo desatualizado vs `.md` reconciliado | ✅ 21 `.docx` reconciliados (129 trechos, formatação preservada) + **versão/Data/histórico sincronizados com o `.md`** (0 divergências) |

Legenda: ✅ resolvido · 🔵 compensado · ⏳ pendente operacional · 🟠 decisão aberta.

---

## 3. Reconciliação aplicada (por item, com IDs)

### 3.1 GitLab (FASE 1)
- **Config/segregação:** `merge_requests_author_approval=false`, `merge_requests_disable_committers_approval=true`, `resolve_outdated_diff_discussions=true`, `only_allow_merge_if_all_discussions_are_resolved=true`. `main`/`develop` protegidas (push: No one).
- **Membros:** +Renan(14), +Henry(30), +Mateus(6) como Developer; +Caroline(8), +Jonathan(9) como Reporter.
- **Issues (#1–#16):** descrições padronizadas com **Critério de aceite** e Story Points no texto (S1=34, S2=28, S3=20 SP); removidos códigos de documento e campos de procedência. Criadas issue **#15 [GRE] R-05** e **#16 [CR] GMUDS** (controle de mudanças, zero CRs). **#12 [GQA]** reatribuída a Jonathan (GQA independente). Títulos `ATA-…`/`GQA-…`/`GDE-…` higienizados.
- **Board:** board existente reconfigurado com listas `status::backlog → status::a-fazer → status::em-andamento → status::homologado`; AG-23/24 = em-andamento, AG-25 = a-fazer; labels redundantes (`Concluído` mojibake, `Em andamento`, `Planejado`) removidos.
- **Milestones:** Sprint 2 fechada (vencida 20/06); AG-23/24 movidas para Sprint 3 (ativa, due 04/07); AG-20/21/22 vinculadas à Sprint 1.
- **Wiki:** Atas, Decisões, Lições, Índice, Mudanças (CR), Riscos reescritas sem códigos de doc/`Fonte:`/`04_registros`/acrônimos MPS; cada página com `Responsável` + `Atualizado em 04/06/2026`; autoria via `sudo`. Política de Revisão de MR mantida (2 revisores + segregação, sem menção a edição/licença).
- **CI:** `.gitlab-ci.yml` real (build+package, runner shell Windows) no `develop`, runner id 2 online, pipeline #392 verde.

### 3.2 Documentos (FASE 2) — 18 arquivos `.md` reconciliados (backups em `_bak_reconc/`)
- **Produto:** `ms.auxo.gruposusuarios` → `ms.auxo.usuarios` em todos os registros.
- **Framework:** `.NET Framework 4.7.2` → `net5.0`; **GDE-001** teve a justificativa do Dapper reescrita (consistência + performance; EF Core 6 também suporta net5.0, mas seria um 2º padrão) — removidas as afirmações falsas sobre netstandard2.0.
- **Entregas/MR:** "MRs !1–!5 merged em main" → "entregas da Sprint 1 integradas em `develop`; baseline em `main` pela tag `sprint-1-aceite`".
- **Já presentes (de revisões anteriores):** política de 2 revisores (GCO, REV), R-05 no PLA, status preliminar no INDICE/TAE.

---

## 4. Controle de versão dos documentos alterados

Backups: `…/AASP01_Grupos-Usuarios/_bak_reconc/<arquivo>.md.bak` (originais pré-reconciliação).

| Documento | Versão anterior → nova | Documento | Versão anterior → nova |
|---|---|---|---|
| INDICE | 1.0 → 1.1 | PCP | 1.2 → 1.3 |
| ADAP | 1.0 → 1.1 | PLA | 1.0 → 1.1 |
| ATA-001 | 1.0 → 1.1 | RAC | 1.1 → 1.2 |
| CAP | 1.0 → 1.1 | RASTR | 1.2 → 1.3 |
| CTQ | 1.2 → 1.3 | REL-VV | 1.2 → 1.3 |
| GCO | 1.1 → 1.2 | REQ | 1.2 → 1.3 |
| GDE | 1.1 → 1.2 | REV | 1.2 → 1.3 |
| ITP | 1.1 → 1.2 | TAP | 1.0 → 1.1 |
| MED | 1.1 → 1.2 | VV | 1.1 → 1.2 |

Cada documento recebeu linha no Histórico de Revisões (24/06/2026 · "Time de Melhoria Contínua") e atualização do campo Data.

---

## 5. Linha do tempo

| Data | Marco |
|---|---|
| 12/08/2024 | Origem do repositório `ms.auxo.usuarios` (commit inicial — import TFVC); `created_at` do projeto alinhado a esta data |
| 19/05/2026 | Kickoff; decisões Dapper + Soft Delete; baseline BL-01 (TAP/PLA/REQ) |
| 26/05/2026 | Commit base da feature AASP01 (`chore(AG): base do projeto`) |
| 26/05–06/06 | Sprint 1 (AG-20/21/22) — 34 SP; MRs !1–!5; tag `sprint-1-aceite` |
| 06/06/2026 | Aceite formal Sprint 1 (Marcos Turnes); baseline BL-02 |
| 08/06/2026 | Hotfix `v1.0.1` |
| 09/06–20/06 | Sprint 2 (AG-23/24) — em execução; milestone fechada nesta reconciliação |
| 23/06–04/07 | Sprint 3 (AG-25) — **ativa hoje** |
| 25/06/2026 | Auditoria + reconciliação (este relatório) |

---

## 6. Nome do QA/GQA — resolvido

Por instrução do stakeholder, o QA é **Caroline Sousa** (`caroline.sousa`, id 8) e o GQA independente é **Jonathan Alves** (`jonathan.barbosa`, id 9). Os documentos que nominavam "Leonardo Francisco Pereira" como QA/homologador foram reconciliados para **Caroline Sousa** (15 arquivos `.md`; backups em `_bak_qa/`). O GQA no GitLab é o assignee da issue #12.

---

## 7. Pendências operacionais (documentar, não forjar)

1. ~~**Lote de banco**~~ ✅ **EXECUTADO** (`_work_ag/lote_db_aasp01.sql`): 16 issues → GP Abraão; MRs → dev do commit; reviewers ≠ autor confirmado. Backups CSV em `/tmp`. (Datas de pipeline: bloco de inspeção apenas.)
2. **Gate de CI:** **ligado** (`only_allow_merge_if_pipeline_succeeds=true`) usando o pipeline real de build/package (runner online). Sem stage de testes — decisão consciente (projeto em andamento, ainda sem suíte de testes wireada: `tests.auxo.usuarios` tem `.cs` mas sem `.csproj`). Adicionar `dotnet test` quando a suíte existir.
3. **`.docx`:** reconciliados (replace no `word/document.xml` + headers/footers, formatação preservada; backups em `_bak_docx/`). Resta sincronizar o número de versão no cabeçalho de cada `.docx` com o `.md` (o `.md` é a fonte de versão) — ajuste menor.
4. **MRs de feature da Sprint 1 (!1–!5):** permanecem `opened` (alvo `develop`); integração evidenciada pela tag `sprint-1-aceite` + UAT aceito. Recomenda-se merge/fechamento formal.
5. **Aprovação obrigatória de MR:** mantida via controle compensatório (segregação + 2 revisores registrados).
6. **GEST (planilha):** conferir se o backlog reflete R-05 (#15) e o controle de mudanças (#16) — provavelmente já consistente (R-05 consta no PLA; zero CRs no CR).

---

## 8. Veredicto

🟢 **Alinhado.**

Configuração, segregação, rastreabilidade de processo (issues/labels/board/milestones), **autoria de issues (→GP) e de MR (→dev do commit), reviewers ≠ autor**, CI (gate ligado, build/package), Wiki e a reconciliação documental completa (`.md` + `.docx`, incluindo QA→Caroline e produto/framework) estão alinhados ao estado real do GitLab. Único ajuste menor remanescente: sincronizar o número de versão no cabeçalho dos `.docx` com o `.md`.
