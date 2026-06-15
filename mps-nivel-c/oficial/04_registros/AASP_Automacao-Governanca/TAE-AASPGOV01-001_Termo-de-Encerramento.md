# Termo de Aceite e Encerramento — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | TAE-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.0 |
| **Data de emissão** | 02/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Patrocinador / Cliente** | Marcos Correa Fernandez Turnes — AASP |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Declaração de encerramento

O projeto AASP_Automacao-Governanca foi formalmente encerrado em **02/06/2026**. O serviço **SensrJiraSync** foi desenvolvido, homologado e entregue conforme os critérios de aceite definidos no TAP-AASPGOV01-001. A entrega (versão de produção v1.0.0, BL-PROD-001) foi validada pelo Patrocinador, e o aceite formal foi concedido na reunião de encerramento (ATA-AASPGOV01-004).

## 2. Escopo entregue

- Serviço SensrJiraSync — .NET 8 LTS, executável como Azure Scheduled Job.
- Autenticação multi-desenvolvedor (Sensr/Jira) e credenciais via Azure Key Vault.
- Migração automatizada de projetos (Epics), atividades (Tasks) e sub-atividades (Subtasks), com conversão HTML→ADF e histórico como comentários.
- Sincronização incremental de status com idempotência por `#ID`.
- Paginação para Epics grandes e execução agendada via Azure Scheduler.

## 3. Resultados dos indicadores (M1–M7)

| Indicador | Meta | Resultado |
|---|---|---|
| M1 — Prazo | ≤ 5% desvio | 0% (entregue em 02/06/2026) — ✅ |
| M2 — Esforço | ≤ 10% desvio | +9,3% (216 h → 236 h) — ✅ |
| M3 — Velocity | ≥ 12 SP/sprint | 15 SP/sprint — ✅ |
| M4 — Itens entregues | ≥ 95%/sprint | 100% (17/17) — ✅ |
| M5 — Defeitos | ≤ 1 def/4 SP | 0,085 def/SP — ✅ |
| M6 — Contenção | 100% em HOM | 5/5 em HOM; 0 em produção — ✅ |
| M7 — Retrabalho | ≤ 5% reabertos | 0% — ✅ |

Detalhamento em MED-AASPGOV01-001.

## 4. Situação dos critérios de aceite e defeitos

- Critérios de aceite CA01–CA07: **todos aprovados** pelo Patrocinador em 29/05/2026 (ATA-AASPGOV01-003).
- Defeitos: 5 identificados na homologação (BUG-01 a BUG-05), **todos corrigidos** antes da entrega; **0 em produção**.

## 5. Lições aprendidas

7 lições registradas em LI-AASPGOV01-001 (com as ações de melhoria AC-01 e AC-02 incorporadas aos ativos organizacionais).

## 6. Situação dos produtos de trabalho

| Item | Situação |
|---|---|
| 23 produtos de trabalho (TAP, ADAP, PLA, RAC, REQ, RASTR, PCP, ITP, VV, REL-VV, REV, GCO, GDE, MED, CAP, GQA, 4 ATAs, GEST, LI, TAE) | Produzidos, completos e aderentes ao padrão |
| Auditoria GQA ao encerramento | ✅ Conforme — 16/16 itens, 0 NCs (GQA-AASPGOV01-001, 02/06/2026) |
| Pendências de escopo | Nenhuma |

## 7. Aprovação do encerramento

| Papel | Responsável | Data |
|---|---|---|
| Patrocinador / Cliente | Marcos Correa Fernandez Turnes — AASP | 02/06/2026 |
| Gerente de Projeto | Abraão Oliveira — Timeware Brasil | 02/06/2026 |
| Auditor GQA | Jonathan Alves | 02/06/2026 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Termo de aceite e encerramento consolidado a partir do INTAKE-AASPGOV01 (14/06/2026), Bloco 13. |
