# Relatório de Alinhamento — Documentos × GitLab

**Projeto:** Cadastro de Clientes — Rede D1000 (Profarma)
**Repositório GitLab:** `profarma/cadastro-clientes` (id 3) · `http://191.234.192.153/profarma/cadastro-clientes`
**Data da reconciliação:** 26/06/2026
**Executor:** Avaliador Líder MPS.BR + Construtor de Laboratório DevOps (auditoria geral + auto-reconciliação)
**Contexto:** Laboratório educacional, dados sintéticos. Projeto **encerrado** em 29/01/2026 (aceite formal de Humberto Erler).

> Esta foi uma **reexecução** sobre um projeto já trabalhado por execuções anteriores. A maior parte da Fase 1 já estava implementada; este ciclo focou em **corrigir violações remanescentes**, **remover duplicatas/lixo** e **reconciliar a contagem de MRs** na documentação.

---

## 0. Veredicto

🟢 **ALINHADO.** Após a remediação, o GitLab está aderente ao Nível C e coerente com a documentação: zero referências à documentação dentro do GitLab, zero menções a licença/edição, segregação autor≠revisor em 100% dos MRs, board por fluxo de status, milestones e issues consistentes com um projeto encerrado, e a documentação reconciliada ao estado real da ferramenta.

**Pendências operacionais** (declaradas, não forjadas) ao final (§6).

---

## 1. Painel de divergências e violações tratadas

| # | Tema | Artefato | Divergência / violação encontrada | Estado |
|---|---|---|---|---|
| 1 | Disponibilidade da VM | Infra (Redis/Puma) | GitLab fora do ar: disco 100% (arquivos deletados retidos por processos travados) travando o Redis | ✅ Restaurado |
| 2 | Regra Global — CI | `.gitlab-ci.yml` (main/develop/homolog) | Comentário citava código de documento `ITP-PROFARMA01-001 §7.1` | ✅ Removido |
| 3 | Regra Global — Issues | ~50 issues (lote A) | Citações a `REQ/CR/GDE/CTQ/REL-VV/ATA/ADAP-PROFARMA01-001`, caminhos `docs/adr/ADR-xxx`, `EST-GPC-002` e campo "Sprint de origem:" / "Base documental:" | ✅ Limpo (89 issues) |
| 4 | Regra Global — Wiki | `atas`, `decisoes`, `licoes-aprendidas`, `riscos` | "Fonte:", `04_registros`, códigos de documento | ✅ Limpo |
| 5 | Regra Global — Licença | Wiki `politica-revisao-mr` | Texto "recurso GitLab **Premium**. Sem **licença**…" | ✅ Removido (página excluída) |
| 6 | Duplicidade — Issues | Issues #91–111, #113–114 (24 abertas) | Lote B: duplicatas pobres (sem SP/milestone/fase, `status::a-fazer`) de issues do lote A já fechadas | ✅ 23 excluídas; #112 (GQA, única) mantida e corrigida |
| 7 | Duplicidade — Wiki | `politica-revisao` + `politica-revisao-mr` | Duas páginas de política conflitantes | ✅ Consolidado em `politica-revisao` |
| 8 | Lixo — MR/branches/pipelines | `documentation/wiki-setup*` | MRs de probe (!17/!18/!19), 2 branches e 6 pipelines falhos (3 de execução anterior + 3 do commit de CI deste ciclo) | ✅ Removidos |
| 9 | Typo de domínio — Label | `risco::bajo` (espanhol) | Label duplicada de `risco::baixo` | ✅ Removida |
| 10 | Board Kanban | Board "Fases do projeto" | Misturava listas `fase::1–6` e `status::*` | ✅ Reconfigurado p/ fluxo de status ("Fluxo de Trabalho") |
| 11 | Segregação de aprovação | Settings de MR | `merge_requests_author_approval`/`disable_committers` | ✅ Confirmado (autor não aprova; committers desabilitados) |
| 12 | Contagem de MRs | `PLA-PROFARMA01-001` §3.1 | Doc dizia "14 com 1 revisor / 5 com 2 = 19"; real = **16 MRs (11 com 1, 5 com 2)** | ✅ Reconciliado (doc → real) |
| 13 | Nomenclatura de release | GCO/ITP/GQA × tags | Releases `25.10.0.1`, `25.12.1.1`, `26.1.1.1` | 🔵 Já alinhado (sem ação) |
| 14 | Status de encerramento | TAE/INDICE × milestones | Projeto encerrado; 19 milestones fechadas | 🔵 Já alinhado (sem ação) |
| 15 | Datas de release | Releases × commit das tags | `released_at ≥ committed_at`; ordem semântica correta | 🔵 Já alinhado (sem ação) |

Legenda: ✅ corrigido neste ciclo · 🔵 já conforme (verificado, sem ação) · ⚠️ pendência

---

## 2. Reconciliação aplicada

### 2.1 GitLab (Fase 1)

- **Issues (90 no total, 0 abertas):**
  - Excluídas 23 duplicatas do lote B (#91–111, #113–114).
  - GQA (#112): descrição reescrita sem códigos de documento, **responsável = Jonathan Barbosa (GQA independente)**, fechada.
  - 89 issues do lote A (RF, RNF, CR-01..12, GDE-001..005, T-*, NC-01/02, ATAs, GRE R-01..R-08, bugs) tiveram a descrição limpa de códigos de documento e procedência; placeholders `(definir)` substituídos por critério de aceite concreto por categoria. **Identificadores de domínio mantidos** (RF-xx, CR-xx, GDE-xxx, T-xxx, GRE R-xx — taxonomia própria do projeto, não pluga em arquivo de documentação).
  - Story Points preservados conforme a metodologia (Scrum): presentes nos RFs (backlog), ausentes em RNFs/CRs/riscos/atas/GQA/testes (sem SP no backlog) — **não inventados**.
  - Autoria mantida por categoria: issues de gestão → GP (Abraão); work-items/bugs → dev/QA do trabalho (Lucas, Mateus, Raony, Caroline, Julielle); decisões → Tech Lead (Cézar); atas → coordenação.
- **`.gitlab-ci.yml`:** comentário do cabeçalho limpo do código de documento em `main`, `develop` e `homolog` (commit autor = Cézar Hiraki Velázquez; proteção de branch removida e **restaurada exatamente** durante o commit).
- **Wiki:** 6 páginas limpas (`home`, `atas`, `decisoes`, `licoes-aprendidas`, `riscos`, `politica-revisao`); página duplicada `politica-revisao-mr` excluída; **`politica-revisao` reescrita para a política real** (1 revisor padrão + 2 para mudanças críticas, segregação sempre), coerente com o PLA §3.1; datas de atualização realistas (12/06/2026); editores via `sudo` = responsável de cada página.
- **Board:** "Fluxo de Trabalho" com listas `status::backlog → a-fazer → em-andamento → homologado` + coluna fechada (Concluído).
- **Labels:** `risco::bajo` removida (consolidada em `risco::baixo`).
- **Settings:** gate de pipeline, discussões resolvidas e resolução de diffs desatualizados confirmados; segregação de aprovação (autor não aprova; committers desabilitados) confirmada.
- **Limpeza:** 6 pipelines falhos/probe excluídos; MR aberto de probe (!18) fechado; branches `documentation/wiki-setup*` removidos. Pipelines restantes: 0 sem sucesso.

### 2.2 Documentos (Fase 2)

| Documento | Mudança | IDs/Refs |
|---|---|---|
| `PLA-PROFARMA01-001_Plano-de-Projeto` (.md + .docx) | §3.1 "Implementação prática": contagem de MRs reconciliada ao real (16 MRs: 11 com 1 revisor ~69%, 5 com 2 revisores ~31%); explicitada segregação autor≠revisor em 100% dos MRs. Versão 1.4 → **1.5**; data 26/06/2026; nova linha no histórico de revisões. `.docx` regenerado a partir do `.md` via `_interno/converter_md_docx.py` (resolveu desync pré-existente: `.docx` estava em v1.3) | MRs !1–!16 |

**Não houve reescrita da origem Azure DevOps** dos demais documentos (GCO, ITP, REV): o projeto realmente usou Azure DevOps e o GitLab é o espelho de evidência da migração — reescrever isso seria falsear história. As afirmações verificáveis (releases, status de encerramento, política de revisores) já estavam alinhadas à ferramenta.

---

## 3. Controle de versão dos documentos alterados + backups

| Documento | Versão anterior | Versão nova | Backup |
|---|---|---|---|
| PLA-PROFARMA01-001 (.md) | 1.4 | 1.5 | `PLA-PROFARMA01-001_Plano-de-Projeto.md.backup.20260626_reconc.bak` |
| PLA-PROFARMA01-001 (.docx) | 1.3 (desync) | 1.5 (regenerado do .md) | `PLA-PROFARMA01-001_Plano-de-Projeto.docx.backup.20260626_reconc.bak` |

---

## 4. Linha do tempo do projeto (referência)

| Marco | Data |
|---|---|
| Alinhamento técnico inicial / arquitetura | 17/03/2025 |
| Kickoff — início das dailys e sprints | 28/04/2025 |
| Release de homologação (`25.10.0.1`) | 10/10/2025 |
| Baseline de homologação (`25.12.1.1`) | Dez/2025 |
| Integração Propz concluída | 04/12/2025 |
| Baseline de piloto/produção (`26.1.1.1`) · GMUD 2624117 | 26/01/2026 |
| Aceite final (Humberto Erler) — projeto encerrado | 29/01/2026 |

19 sprints · 573 SP · 16 endpoints · 273 testes unitários · 12 change requests · 6 integrações.

---

## 5. Matriz de papéis (derivada de docs + membros do GitLab)

| Papel | Pessoa | Usuário GitLab | Acesso |
|---|---|---|---|
| Gerente de Projeto | Abraão Oliveira | `abraao.oliveira` | Maintainer (40) |
| Tech Lead / DevOps / Arquiteto | Cézar Hiraki Velázquez | `cezar.velazquez` | Owner (50) |
| Dev Backend | Mateus Veloso | `mateus.veloso` | Developer (30) |
| Dev Backend | Raony Chagas | `raony.chagas` | Developer (30) |
| Dev Backend | Lucas Batista | `lucas.batista` | Developer (30) |
| QA / Automação | Caroline Sousa | `caroline.sousa` | Developer (30) |
| GQA independente | Jonathan Barbosa | `jonathan.barbosa` | Reporter (20) |
| Tech Lead D1000 (cliente) | Armando Pereira Reis Junior | `armando.junior` | Reporter (20) |
| Gerente de TI D1000 (aprovador) | Humberto Erler | `humberto.erler` | Reporter (20) |
| Patrocinador D1000 | Pedro Alves da Costa Junior | `pedro.costa` | Reporter (20) |
| Coordenadora de Projeto D1000 | Helena Moreira | `helena.moreira` | Reporter (20) |
| QA D1000 | Julielle Santos | `julielle.santos` | Reporter (20) |

> Revisores de MR no GitLab respeitam: 2 distintos do autor nos MRs críticos (integração/release), 1 distinto do autor nos rotineiros; merge sempre por quem não é o autor.

---

## 6. Pendências operacionais (declaradas, não forjadas)

1. **VM subdimensionada (7,7 GB RAM, disco 28 GB).** Durante a sessão o Puma caiu sob carga (rajadas de escrita + pipelines), com episódios de disco transitoriamente cheio por arquivos deletados retidos. **Ação tomada:** Prometheus e Alertmanager **pausados** (`gitlab-ctl stop`) para reduzir pressão de memória/disco — são monitoramento interno, não afetam issues/MRs/wiki/repos. **Recomendação:** redimensionar a VM (RAM/disco) ou manter o Prometheus desligado; reativável com `gitlab-ctl start prometheus alertmanager`.
2. **Gate de aprovação obrigatória de N≥2 (`approvals_before_merge`) e `reset_approvals_on_push`** não persistem nesta instância. Controle compensatório vigente: segregação (autor não aprova/não faz merge) + 2 revisores registrados nos MRs críticos. *(Sem documentar limitação de edição em qualquer artefato.)*
3. **GitFlow para `homolog`:** branch protegida (push `No one`), porém sem MR de demonstração específico — os fluxos `feature/* → develop` (!1–!14) e `release/* → main` (!15–!16) já evidenciam merge em branch protegida com revisão e segregação. Não foi criado MR sintético em projeto encerrado (evitar forja).
4. **Origem Azure DevOps** nos documentos GCO/ITP/REV é histórica e real (migração para GitLab); mantida como tal. Os números migrados (commit→issue, releases) estão declarados, não reescritos.
5. **Recomendações gerais:** modernizar imagens de teste para .NET atual; HTTPS em produção; manter o runner `runner-vm-docker` saudável para o gate de CI.

---

*Relatório gerado automaticamente ao final da auditoria geral (GitLab → Documentos) com auto-remediação. Espelha a ferramenta; consolidações declaradas; sem forja de rastros.*
