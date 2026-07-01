# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Relatório de Acompanhamento
**Código:** RAC-AASP01-001
**Versão auditada:** 1.2
**Data do documento:** 15/06/2026
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 0 | 0 |
| Conteúdo (CNT) | 1 | 2 | 0 | 0 |
| Datas (DT) | 1 | 0 | 0 | 0 |
| Papéis (PAP) | 0 | 0 | 0 | 0 |
| Coerência (CON) | 0 | 1 | 0 | 0 |
| MPS.BR (MPS) | 1 | 0 | 0 | 0 |
| **TOTAL** | **3** | **3** | **0** | **0** |

**Veredicto:** NÃO-CONFORME CRÍTICO

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-RAC-01 — Ausência de relatório pós-Sprint 2 (o RAC não foi atualizado após 15/06/2026)
**Severidade:** 🔴 Grave
**RAP impactado:** GPR RAP 4 — progresso monitorado e documentado
**Localização:** Documento inteiro — data do documento é 15/06/2026
**Problema:** O RAC está na versão 1.2, datado de 15/06/2026 (meio da Sprint 2). A seção 6 promete "próximo relatório em 20/06/2026". Na data de auditoria (30/06/2026), não há versão 1.3 ou posterior — o RAC não foi atualizado após o encerramento da Sprint 2 e no início da Sprint 3. O processo GPR exige monitoramento contínuo documentado. A ausência de atualização do RAC por 15 dias consecutivos constitui falha no processo de monitoramento de projeto.
**Evidência:** > "O próximo relatório de acompanhamento está previsto para 20/06/2026, ao encerramento da Sprint 2..."
**Referência normativa:** GPR RAP 4 — progresso do projeto monitorado periodicamente com registro.
**Ação corretiva:** Criar urgentemente a versão 1.3 do RAC com: (a) resultados da Sprint 2 (histórias entregues, SP realizados, qualidade); (b) resultado do aceite formal da Sprint 2; (c) status da Sprint 3 (em andamento desde 23/06); (d) atualização dos riscos; (e) métricas M1-M8 atualizadas.

---

### NC-RAC-02 — Sprint 2 registra AG-23 e AG-24 como "Não iniciado" em 15/06 — desvio de cronograma crítico não documentado
**Severidade:** 🔴 Grave
**RAP impactado:** GPR RAP 4 — desvios registrados e ações corretivas documentadas
**Localização:** Seção 3.1 — Status Atual das Histórias da Sprint 2
**Problema:** O RAC de 15/06/2026 registra que AG-23 e AG-24 "ainda não foram iniciados no código" — isso é o 7º dia útil da Sprint 2 (de 10 dias úteis totais). Com 70% da sprint decorrida e 0% de implementação registrada, o risco de não-entrega da Sprint 2 é alto. O documento menciona os riscos R-04 e R-01 como "em monitoramento" mas não registra ação corretiva para o atraso de implementação. A seção "Projeção de Encerramento" apenas repete o planejamento original sem análise de risco real.
**Evidência:** > "AG-23 — Auditoria de Grupos | RF-07 | Não iniciado | Planejado para a Sprint 2; auditoria ainda não implementada no código" em 15/06/2026 (70% da sprint consumida).
**Referência normativa:** GPR RAP 4 — desvios identificados devem ter ação corretiva documentada.
**Ação corretiva:** O RAC deve documentar: (a) análise de risco real dado o atraso de 7 dias; (b) ação corretiva proposta (ex.: escopo reduzido na Sprint 2, Sprint 3 absorve AG-23); (c) comunicação do risco ao PO (Marcos Turnes).

---

### NC-RAC-03 — Métrica M3 calculada incorretamente: 5 achados / 34 SP ≠ 0,088
**Severidade:** 🟡 Moderada
**RAP impactado:** MED — métricas calculadas corretamente
**Localização:** Seção 5 — Métricas Consolidadas, M3
**Problema:** A métrica M3 registra "0,088 (3 achados P2/P3 em 34 SP)". Porém o REV-AASP01-001 registra 5 achados (P2: 3, P3: 2) — não 3. 5/34 = 0,147 (não 0,088). O cálculo usa 3 achados (apenas os P2) em vez de 5 (todos os achados), o que subestima o índice de defeitos e pode distorcer a análise de qualidade.
**Evidência:** > "M3 | Índice de defeitos por SP | 0,088 (3 achados P2/P3 em 34 SP)"
**Referência normativa:** MED — métricas devem ser calculadas corretamente com a base definida.
**Ação corretiva:** Corrigir M3 para 0,147 (5 achados / 34 SP) ou redefinir a base de cálculo: se M3 conta apenas achados P2 (3/34 = 0,088), documentar explicitamente "M3 = achados P2 por SP" (excluindo P3). A meta de ≤ 0,20 é atingida em ambos os casos, mas a base deve ser consistente.

---

### NC-RAC-04 — Riscos R-02, R-03 e R-05 não mencionados no acompanhamento da Sprint 2
**Severidade:** 🟡 Moderada
**RAP impactado:** GRE RAP 5 — todos os riscos monitorados
**Localização:** Seção 3.2 — Riscos Ativos Sprint 2
**Problema:** A tabela de riscos ativos da Sprint 2 menciona apenas R-04 e R-01. Os riscos R-02 (schema do banco auxo3 com inconsistências), R-03 (mudança de escopo) e R-05 (indisponibilidade de desenvolvedor) não são mencionados — nem como "encerrados" nem como "monitorados". O processo GRE exige que todos os riscos identificados sejam monitorados até sua mitigação ou encerramento formal.
**Evidência:** > "R-04 | Falha ou instabilidade na integração [...] | Em monitoramento | R-01 | Atraso na disponibilização do ambiente [...] | Em monitoramento" — R-02, R-03, R-05 ausentes.
**Referência normativa:** GRE RAP 5 — todos os riscos identificados devem ser monitorados.
**Ação corretiva:** Registrar o status de R-02, R-03 e R-05 na tabela de riscos da Sprint 2: "Encerrado (não materializado)" ou "Monitoramento contínuo". Justificar o encerramento de cada risco com evidência.

---

### NC-RAC-05 — "Time de Melhoria Contínua" como autor — problema sistêmico
**Severidade:** 🟡 Moderada
**RAP impactado:** GCO RAP 2
**Localização:** Histórico de Revisões — versão 1.3
**Problema:** O histórico registra versão 1.3 com "Time de Melhoria Contínua". Mas há problema adicional: o RAC tem versão 1.2 datada de 15/06/2026 com autor "Abraão" e versão 1.3 com "Time de Melhoria Contínua" — mas a versão 1.3 não está visivelmente distinta da 1.2 no conteúdo auditado. Há contradição: a data do documento é 15/06/2026 mas a versão 1.3 deveria ser de 24/06/2026.
**Evidência:** > "Data do relatório | 15/06/2026 | Versão | 1.2" no cabeçalho, mas histórico indica v1.2 e v1.3.
**Referência normativa:** GCO RAP 2.
**Ação corretiva:** Corrigir o cabeçalho para refletir a versão e data atuais. Identificar o responsável nominal da v1.3.
