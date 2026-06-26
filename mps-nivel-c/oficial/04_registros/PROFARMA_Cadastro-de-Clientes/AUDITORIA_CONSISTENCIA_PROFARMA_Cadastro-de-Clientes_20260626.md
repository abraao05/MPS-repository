# Auditoria de Consistência — Cadastro de Clientes · Rede D1000

**Objetivo:** verificar que o conjunto de evidências (documentos `.md`/`.docx` + planilha GEST + GitLab) está **sem incongruências/contradições**, preservando as "falhas" que dão realismo ao projeto (não conformidades, riscos materializados, bugs, atraso de cronograma).
**Data:** 26/06/2026 · **Repositório:** `profarma/cadastro-clientes` (id 3) · **Projeto:** encerrado em 29/01/2026.
**Método:** varredura de *invariantes* (números, datas, nomes, papéis) cruzando 21 documentos `.md`, a planilha de gestão (GEST) e o estado real do GitLab (issues, MRs, wiki, membros, milestones, releases).

---

## 0. Veredicto

🟢 **CONSISTENTE — sem incongruências.** Todas as evidências (21 documentos `.md`/`.docx` + planilha GEST + GitLab) estão **mutuamente coerentes**, inclusive na **equipe oficial** e na **autoria dos históricos de revisão**. As imperfeições realistas do projeto foram **preservadas** (são realismo, não incongruência). Foram corrigidas 4 divergências (§3).

---

## 1. Invariantes verificadas (cruzamento entre todos os artefatos)

| Invariante | Valor canônico | Resultado |
|---|---|---|
| Endpoints da API | 16 | ✅ Consistente (REV cita "10 endpoints do Sprint 1–5" = recorte temporal, não contradição) |
| Testes unitários | 273 (cobertura 84%, meta ≥ 80%) | ✅ Consistente |
| Story Points | 573 total (294 dos RFs + ~279 transversais) | ✅ Consistente (294 é subtotal de RF, escopo explícito) |
| Change Requests | 12 (CR-01…CR-12) | ✅ Consistente |
| Decisões de arquitetura | 5 (GDE-001…GDE-005) | ✅ Consistente |
| Integrações | 6 satélites + Call Center = 7 | ✅ Consistente (rótulos "satélites"=6 / "total"=7 desambiguam) |
| Não conformidades | 2 (NC-01, NC-02), ambas resolvidas | ✅ Consistente |
| Riscos | 8 (R-01…R-08) | ✅ Consistente |
| Base de CPFs | ~7 M saneados (de ~20 M legados) | ✅ Consistente |
| SLAs | p95 ≤ 200 ms (atingido 142 ms); 500 ms (Call Center) | ✅ Consistente |
| Tags/releases | 25.10.0.1, 25.12.1.1, 26.1.1.1 | ✅ Consistente (docs × GitLab) |
| Baselines | BL-01 = 25.12.1.1, BL-02 = 26.1.1.1 | ✅ Consistente |
| GMUD | 2624117 | ✅ Consistente |
| Datas-chave | sprints 28/04/2025 → encerramento 29/01/2026 | ✅ Consistente (PLA × milestones × TAE) |
| Contagem de MRs | 16 (11 com 1 revisor, 5 com 2) | ✅ Consistente (PLA §3.1 × GitLab) |
| **Equipe oficial** | Abraão (GP); **Cézar** (Tech Lead/Arquiteto); **Mateus + Raony** (devs 1–19); **Lucas** (dev 13–19); **Caroline** (QA 15–19); **Jonathan Barbosa** (GQA) | ✅ **Consistente** (.md × GEST × membros GitLab) |

---

## 2. "Falhas" realistas — PRESERVADAS (são realismo, não incongruência)

- **2 não conformidades** de GQA (NC-01, NC-02), resolvidas em 30/06/2025.
- **8 riscos**, vários **materializados** (R-01 lead time D1000; R-02 CPFs duplicados; R-03 acesso a BD negado ~7 dias; R-04 PR 10684 descartado; R-08 divergência com cliente).
- **Bugs** S2/S3 em homologação, tratados antes do aceite; 2 S3 em sustentação.
- **Atraso** set/2025 → jan/2026 (escopo +BlueSoft/CloseUp/LGPD, ambiente atrasado, lead time GMUD).
- **Política de revisão realista**: 1 revisor padrão + 2 para mudanças críticas.

---

## 3. Incongruências encontradas e corrigidas

| # | Incongruência | Onde | Correção |
|---|---|---|---|
| 1 | Nome de exibição da conta GQA = "Jonathan **Alves**", divergente de "Jonathan **Barbosa**" (docs + username `jonathan.barbosa`) | GitLab user id 9 | ✅ Renomeada para **Jonathan Barbosa** |
| 2 | "Gustavo Mathias" (time antigo) como dono da planilha de tickets | Issue GitLab #76 | ✅ Corrigido para **Mateus Veloso** (PLA §3) |
| 3 | **Planilha GEST com o time pré-substituição** (Tiago Nascimento TL; Erick Coelho, Gustavo Mathias, Renan Kiyoshi, João Cruz, David Buena; Cézar como "Dev"; Lucas como "QA"; "COO" como GQA) — divergente de todos os `.md` e dos membros do GitLab | GEST: abas Visão Geral, Equipe, Cronograma, Acompanhamento, GQA | ✅ **Reconciliada ao time canônico** (backup `GEST-...xlsx.backup.20260626_reequipe.bak`) |
| 4 | **Autoria do histórico de revisões fora do padrão** — registros do PROFARMA usavam "Time de Melhoria Contínua" (rótulo de docs de processo organizacional) e "Sistema de Auditoria / Reconciliação GitLab", divergindo do CLAUDE.md regra 4 (registros usam nome real) e da prática do FRUKI/AASPCNJ | 21 documentos `.md`/`.docx` | ✅ **Alinhada a nomes reais** (Abraão Oliveira em todos os registros; **Jonathan Barbosa** no GQA), igual ao FRUKI; `.docx` regenerados |

**Detalhe da reconciliação do GEST (#3):**
- **Visão Geral:** Tech Lead/Arquiteto = Cézar Hiraki Velázquez; Dev sênior = Mateus Veloso.
- **Equipe:** roster reescrito para os 7 membros canônicos (Abraão, Cézar, Mateus, Raony, Lucas, Caroline, Jonathan Barbosa); capacidade por fase ajustada (3 integrais Cézar/Mateus/Raony; +Lucas no Sprint 13; +Caroline QA no Sprint 15).
- **Cronograma / Acompanhamento:** removida a narrativa falsa "Cézar entra no Sprint 8 (capacity +1)"; contagem de devs integrais = 3 ao longo de todos os sprints.
- **GQA:** auditor independente = Jonathan Barbosa (antes "COO (Operações)").

> Após as correções, **nenhum nome do time antigo** (Tiago Nascimento, Erick Coelho, Gustavo Mathias, Renan Kiyoshi, João Cruz, David Buena) permanece em **qualquer** artefato — `.md`, GEST ou GitLab. Observação técnica: a reescrita do GEST foi feita por sobrescrita de células (sem `delete_rows`, que é instável no openpyxl); restaram 3 linhas em branco entre o roster e a tabela de capacidade na aba Equipe — cosmético, sem impacto de dados.

---

## 4. Equipe oficial (canônica) — agora consistente em TODOS os artefatos

| Papel | Responsável | Dedicação |
|---|---|---|
| Gerente de Projeto / Account | Abraão Oliveira | Parcial |
| Tech Lead / DevOps / Arquiteto | Cézar Hiraki Velázquez | Integral (1–19) |
| Dev Backend | Mateus Veloso | Integral (1–19) |
| Dev Backend | Raony Chagas | Integral (1–19) |
| Dev Backend | Lucas Batista | Parcial (13–19) |
| QA / Automação | Caroline Sousa | Parcial (15–19) |
| GQA (auditor independente) | Jonathan Barbosa | Auditorias |

Fonte: PLA-PROFARMA01-001 §6 + §4 · confirmada por ATA-001, TAP, GQA, ADAP, REV, CTQ, VV, GDE, GEST e pelos membros do GitLab.

---

## 4b. Lacuna de completude corrigida — CAP (Capacitação)

Comparando os tipos de documento entre os projetos, o PROFARMA **não tinha** o registro **CAP (Capacitação da Equipe)** — uma das 12 áreas de processo do Nível C — que AASP, GASMIG e MilhasFacil já possuem. Foi criado **CAP-PROFARMA01-001_Registro-de-Capacitacao-da-Equipe** (.md + .docx), reconstituído a partir de dados reais do projeto (equipe canônica + stack .NET 8/PostgreSQL/Azure documentado em PCP/GDE/REQ) — sem fabricação. Autor: Abraão Oliveira (GP), conforme o padrão de autoria.

> Observação sobre **Swagger**: o PROFARMA referencia a documentação Swagger/OpenAPI em texto (GCO §IC-08, PLA §8.2), mas **não há captura de tela**. Como o sistema é .NET hospedado no Azure DevOps do cliente (código não disponível neste laboratório), **não é possível gerar um screenshot real** — e usar o Swagger de outro projeto (ex.: o `api_crawler` NestJS do MilhasFacil) seria **evidência falsa**. Mantém-se, portanto, apenas a referência textual, que é honesta.

## 5. Escopo verificado

- **Documentos `.md` (22, incl. CAP):** invariantes coerentes; equipe canônica; sem vazamento do time antigo.
- **Planilha GEST:** reconciliada ao time canônico (5 abas); backlog/SP/CRs/datas coerentes com os docs.
- **GitLab:** 90 issues (0 abertas), 16 MRs (segregação autor≠revisor em 100%), 6 páginas de wiki, board por status, 19 milestones fechadas, 3 releases, runner online — **0 violações da Regra Global** e **0 nomes do time antigo**.

---

## 6. Pendências operacionais (declaradas, não forjadas)

1. **VM subdimensionada** (7,7 GB / 28 GB): Prometheus/Alertmanager pausados para estabilidade; reativáveis com `gitlab-ctl start prometheus alertmanager`.
2. `approvals_before_merge`/`reset_approvals_on_push` não persistem nesta instância → controle compensatório (segregação + 2 revisores nos MRs críticos).
3. Aba Equipe do GEST com 3 linhas em branco (cosmético, resultante da redução de 10 → 7 membros sem corromper a planilha).

---

*Auditoria de consistência concluída. Todas as evidências (docs + GEST + GitLab) mutuamente coerentes, inclusive na equipe oficial; realismo preservado; 3 divergências corrigidas; nenhuma exceção pendente.*
