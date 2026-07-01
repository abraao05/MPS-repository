# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Relatório de Execução de Testes (V&V)
**Código:** REL-VV-AASP01-001
**Versão auditada:** 1.3
**Data do documento:** 24/06/2026
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 0 | 0 |
| Conteúdo (CNT) | 1 | 2 | 1 | 1 |
| Datas (DT) | 0 | 1 | 0 | 0 |
| Papéis (PAP) | 0 | 0 | 0 | 0 |
| Coerência (CON) | 0 | 1 | 0 | 0 |
| MPS.BR (MPS) | 0 | 0 | 0 | 0 |
| **TOTAL** | **1** | **4** | **1** | **1** |

**Veredicto:** NÃO-CONFORME CRÍTICO

---

## OBSERVAÇÕES POSITIVAS

A seção 3 (Sprint 1) é detalhada e rastreável: testes unitários com métricas de cobertura (Coverlet), testes de integração com descrição dos cenários, UAT com resultado por cenário, code review com MRs e achados identificados. O nível de detalhe da Sprint 1 é o esperado para um artefato de processo MPS.BR.

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-RELVV-01 — Sprint 2 sem qualquer resultado documentado no relatório v1.3 (24/06/2026)
**Severidade:** 🔴 Grave
**RAP impactado:** VV RAP — resultados de V&V documentados para todas as sprints concluídas
**Localização:** Seção 4 — Sprint 2
**Problema:** O relatório v1.3, datado de 24/06/2026, registra a Sprint 2 como "Em andamento — implementação ainda não iniciada no código na data de referência (15/06/2026)". A data de referência interna (15/06/2026) é da versão anterior — a v1.3 foi gerada em 24/06/2026, 4 dias antes do encerramento previsto da Sprint 2 (20/06/2026). Mas na data de auditoria (30/06/2026), a Sprint 2 deveria ter encerrado há 10 dias. O relatório não tem nenhum resultado de teste da Sprint 2 — nem unitários, nem UAT, nem code review, nem aceite. Esta ausência é grave: sem resultados de V&V documentados, não há evidência de que a Sprint 2 foi verificada e validada.
**Evidência:** > "Status Geral — Sprint 2: Em andamento — implementação ainda não iniciada no código na data de referência (15/06/2026)"
**Referência normativa:** VV RAP — resultados de V&V devem ser documentados para cada sprint/fase concluída.
**Ação corretiva:** Atualizar urgentemente a seção 4 com os resultados reais da Sprint 2: (a) testes unitários — quantidade, cobertura; (b) code review dos MRs !6 e !7; (c) UAT — AUD-01, AUD-02, INT-01; (d) aceite formal de Marcos Turnes (ou registro de desvio se o aceite não ocorreu).

---

### NC-RELVV-02 — Métricas consolidadas desatualizadas (seção 6) — Sprint 2 sem dados
**Severidade:** 🟡 Moderada
**RAP impactado:** MED — medições atualizadas e completas
**Localização:** Seção 6 — Métricas Consolidadas de V&V
**Problema:** A tabela de métricas consolidadas tem coluna "Sprint 2 (15/06/2026)" com "— (não iniciado)" para todas as métricas. Esta coluna não foi atualizada na v1.3 (24/06/2026). As métricas M3 (defeitos por SP), M4 (cobertura), M5 (aceite) e M6 (performance) da Sprint 2 estão em branco no relatório oficial.
**Evidência:** > "Testes unitários — total passando | 22/22 (100%) | — (não iniciado) | 100%"
**Referência normativa:** MED — métricas devem ser atualizadas ao encerramento de cada sprint.
**Ação corretiva:** Preencher a coluna Sprint 2 com os dados reais após atualização da seção 4.

---

### NC-RELVV-03 — Cobertura medida por Coverlet em ambiente local — sem validação em CI
**Severidade:** 🟡 Moderada
**RAP impactado:** VV RAP 2 — verificação com ferramentas documentadas e rastreáveis
**Localização:** Seção 3.2 — Testes Unitários Sprint 1
**Problema:** A cobertura de 68.4% de linhas / 61.9% de branches é medida pelo "Coverlet 3.1.2 na execução xUnit", mas não há evidência de que esta medição foi realizada pelo pipeline CI (que poderia ser auditada pelo log do GitLab) ou localmente (onde os resultados não são rastreáveis). O _DOSSIE-EVIDENCIAS classifica o pipeline como lacuna de evidência. Uma medição de cobertura feita localmente por um desenvolvedor não constitui evidência auditável independente.
**Evidência:** > "Nota: Cobertura medida pelo Coverlet 3.1.2 na execução xUnit da Sprint 1 — 68.4% de linhas e 61.9% de branches cobertas."
**Referência normativa:** VV — evidências de teste devem ser rastreáveis e independentemente verificáveis.
**Ação corretiva:** Arquivar o relatório de cobertura gerado pelo Coverlet (arquivo XML ou HTML) como evidência no pacote documental. Ou exportar o log do pipeline CI com o resultado da execução dos testes.

---

### NC-RELVV-04 — SP "34" listado para Sprint 1 mas a soma dos SPs por história é 13+11+10=34
**Severidade:** 🟢 Leve
**RAP impactado:** —
**Localização:** Seção 3.1 — Status Geral Sprint 1
**Problema:** O total de 34 SP está correto (13+11+10=34), mas o PLA lista os SPs como: RF-01=5, RF-02=4, RF-03=2, RF-04=2 (AG-20=13 total), RF-05=11 (AG-21), RF-06=10 (AG-22). No entanto o PLA lista na tabela de cronograma Sprint 1 com 34 SP total — consistente. Observação: nenhuma inconsistência real; apenas verificação confirmatória.
**Evidência:** > "Total Story Points entregue | 34 SP (100% do planejado — 0% de desvio)"
**Referência normativa:** —
**Ação corretiva:** Nenhuma — consistente.

---

### NC-RELVV-05 — Testes de integração Sprint 1 com apenas 3 cenários — cobertura limitada
**Severidade:** 🔵 Obs
**RAP impactado:** VV — cobertura de testes de integração
**Localização:** Seção 3.3 — Testes de Integração Sprint 1
**Problema:** Apenas 3 testes de integração foram executados na Sprint 1. O VV-AASP01-001 menciona "endpoints integrados validados em ambiente de desenvolvimento" como critério de saída, mas 3 testes de integração para 8 endpoints e 3 tabelas de banco é cobertura mínima.
**Evidência:** > "3 testes de integração | 3/3 (100%) — Meta atingida"
**Referência normativa:** VV — cobertura adequada.
**Ação corretiva:** Para a Sprint 3 (regressão), ampliar os testes de integração para cobrir cenários de fronteira não cobertos pelos testes unitários.
