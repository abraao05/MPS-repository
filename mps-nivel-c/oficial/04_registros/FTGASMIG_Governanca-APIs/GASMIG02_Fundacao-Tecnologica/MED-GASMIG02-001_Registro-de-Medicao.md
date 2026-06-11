# Registro de Medição — Fundação Tecnológica GASMIG

| Campo | Valor |
|---|---|
| **Documento** | MED-GASMIG02-001 |
| **Projeto** | Fundação Tecnológica GASMIG — Governança de APIs GASMIG |
| **Cliente** | GASMIG — Companhia de Gás de Minas Gerais |
| **Versão** | 1.2 |
| **Data** | 11/06/2026 |
| **Responsável pela medição** | Abraão Oliveira |
| **Processo MPS-SW** | MED (evidência de projeto) |

---

## 1. Objetivo

Registrar os resultados medidos ao longo do projeto para avaliar o desempenho da execução e alimentar a base histórica organizacional conforme PLA-MED-001.

---

## 2. Indicadores OS-PARCELA-001 — resultados finais

| Código | Indicador | Resultado | Meta Org. | Status |
|---|---|---|---|---|
| M1 | % Entregas no prazo | 100% — escopo completo entregue dentro dos 15 dias corridos; aceite formal com 4 dias de defasagem em relação à data-alvo, sem impacto contratual | ≥ 90% | ✅ |
| M2 | Desvio de esforço (%) | 0% — 84 SP planejados = 84 SP entregues | ≤ 10% | ✅ |
| M3 | SP entregues vs. planejados | 84/84 = 100% | ≥ 90% | ✅ |
| M4 | Velocity média | 84 SP em 15 dias (≈ 5,6 SP/dia · equipe de 2 engenheiros integrais) | Referência interna | ✅ |
| M5 | Taxa de defeitos na verificação técnica | 0 — checklist executado por Cézar Hiraki sem itens não conformes | ≤ 5% dos itens verificados | ✅ |
| M6 | Defeitos escapados para produção (pós-aceite) | 0 — nenhum incidente registrado após o aceite de 26/05/2026 | 0 | ✅ |
| M7 | % Requisitos com rastreabilidade completa | 100% — RF-01 a RF-10 e RNF-01 a RNF-05 rastreados em RASTR-GASMIG02-001 | ≥ 95% | ✅ |
| M8 | % Conformidade GQA | 100% — auditoria de encerramento sem não conformidades (GQA-GASMIG02-001) | ≥ 90% | ✅ |
| M9 | Satisfação do cliente | Positivo — aceite formal concedido via e-mail 26/05/2026; cliente iniciou imediatamente a OS-002 | Satisfatório | ✅ |

---

## 3. Indicadores OS-PARCELA-002 — resultados finais

| Código | Indicador | Resultado | Meta Org. | Status |
|---|---|---|---|---|
| M1 | % Entregas no prazo | 100% — todos os marcos de configuração entregues dentro dos 15 dias corridos (entregue em 14 dias) | ≥ 90% | ✅ |
| M2 | Desvio de esforço (%) | 0% — 78 SP planejados = 78 SP entregues | ≤ 10% | ✅ |
| M3 | SP entregues vs. planejados | 78/78 = 100% | ≥ 90% | ✅ |
| M4 | Velocity média | 78 SP em 14 dias (≈ 5,6 SP/dia · equipe de 2 engenheiros integrais) | Referência interna | ✅ |
| M5 | Taxa de defeitos na verificação técnica | 0 — checklist executado por Cézar Hiraki em 09/06/2026 sem itens não conformes | ≤ 5% | ✅ |
| M6 | Defeitos escapados (pós-aceite) | 0 — nenhum incidente registrado após aceite de 09/06/2026 | 0 | ✅ |
| M7 | % Requisitos com rastreabilidade completa | 100% — RF-11 a RF-19 e RNF-06 a RNF-09 rastreados em RASTR-GASMIG02-002 | ≥ 95% | ✅ |
| M8 | % Conformidade GQA | 100% — auditorias de processo sem não conformidades (GQA-GASMIG02-001) | ≥ 90% | ✅ |
| M9 | Satisfação do cliente | Positivo — aceite formal concedido via e-mail 09/06/2026; NF emitida em 09/06/2026 | Satisfatório | ✅ |

---

## 4. Consolidado do projeto (OS-001 + OS-002)

| Dimensão | Resultado consolidado | Meta Org. |
|---|---|---|
| SP total entregues | 162/162 = 100% (84 + 78) | ≥ 90% |
| Change Requests | 0 | Referência |
| Defeitos totais identificados (OS-001 + OS-002) | 0 | ≤ 5% |
| % Requisitos rastreados | 100% (RF-01 a RF-19 + RNF-01 a RNF-09) | ≥ 95% |
| Duração total | OS-001: 15 dias corridos · OS-002: 14 dias corridos | Dentro do planejado |

---

## 5. Contribuição à base histórica organizacional

Estes dados alimentam a base histórica de projetos de configuração Azure da Timeware:

- **Velocity de referência — projetos Azure API Management:** ≈ 5,6 SP/dia por engenheiro integral em projetos de configuração e governança de APIs
- **Consistência entre OS:** a velocity da OS-002 (5,6 SP/dia) reproduziu exatamente a da OS-001, confirmando a transferência de conhecimento e a estabilidade do processo
- **Padrão de qualidade:** 0 defeitos em dois ciclos consecutivos de configuração Azure, validados por checklist técnico

---

## 6. Ações corretivas registradas

Conforme PLA-MED-001 §6, desvios identificados pela análise de medição geram ações corretivas com responsável e prazo.

| Variância | Ação corretiva | Responsável | Data | Resultado |
|---|---|---|---|---|
| M8 (OS-001): esforço de alertas subestimado em ~20% (LE-06 / OM-07) | Inclusão de métricas de referência para alertas Azure Monitor na base de estimativas organizacional (OM-07 no REG-GPC-001); adoção de thresholds de mercado na OS-002 para evitar ciclos adicionais de alinhamento | Time de Melhoria Contínua | Jun/2026 | OM-07 registrada como Planejada no REG-GPC-001; OS-002 executada sem desvio de esforço |

Nas demais medidas (M1–M7, M9), nenhum desvio foi identificado em OS-001 ou OS-002 — não foram necessárias ações corretivas adicionais.

---

## 7. Comunicação dos resultados

Conforme PLA-MED-001 §7, os resultados de medição foram comunicados:

| Periodicidade | Canal | Destinatários | Período coberto |
|---|---|---|---|
| Por marco (semanal) | Ata de reunião + e-mail de status | Sérgio Villaça (GASMIG), COO | OS-001: abr–mai/2026; OS-002: mai–jun/2026 |
| Encerramento OS-001 | TAE-GASMIG02-001 + LI-GASMIG02-001 | COO, Time de Melhoria Contínua | 07/05/2026 |
| Encerramento OS-002 | TAE-GASMIG02-002 + LI-GASMIG02-001 v1.1 | COO, Time de Melhoria Contínua | 09/06/2026 |
| Consolidação organizacional | REG-MED-001 (repositório organizacional) | COO, Time de Melhoria Contínua | Jun/2026 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 09/06/2026 | Abraão Oliveira | Versão inicial — indicadores finais OS-001 e parciais OS-002 (aceite pendente) |
| 1.1 | 10/06/2026 | Time de Melhoria Contínua | Finalização dos indicadores OS-002: M6 e M9 confirmados após aceite formal de 09/06/2026 |
| 1.2 | 11/06/2026 | Time de Melhoria Contínua | Adição de §6 Ações Corretivas e §7 Comunicação dos Resultados (evidência de MED 5 e MED 6) |
