# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Plano de Verificação e Validação
**Código:** VV-AASP01-001
**Versão auditada:** 1.2
**Data do documento:** 24/06/2026
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 0 | 0 |
| Conteúdo (CNT) | 0 | 2 | 1 | 1 |
| Datas (DT) | 0 | 1 | 0 | 0 |
| Papéis (PAP) | 0 | 1 | 0 | 0 |
| Coerência (CON) | 0 | 1 | 0 | 0 |
| MPS.BR (MPS) | 0 | 1 | 0 | 0 |
| **TOTAL** | **0** | **6** | **1** | **1** |

**Veredicto:** NÃO-CONFORME

---

## OBSERVAÇÕES POSITIVAS

O VV-AASP01-001 é um dos documentos mais completos do projeto, com 7 seções bem estruturadas cobrindo níveis de teste, critérios de qualidade, atividades por sprint, critérios de entrada/saída, gestão de defeitos e ferramentas. O histórico de defeitos (seção 6.3) cross-referencia o REV com IDs de defeitos e MRs, criando rastreabilidade adequada.

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-VV-01 — Sprint 2 permanece "Em andamento" no documento de 24/06/2026
**Severidade:** 🟡 Moderada
**RAP impactado:** VV — estado das atividades de V&V atualizado
**Localização:** Seção 4 — Atividades de V&V por Sprint, Sprint 2
**Problema:** Na data do documento (24/06/2026), a Sprint 2 estava em seus últimos dias (encerramento previsto 20/06/2026). Na data de auditoria (30/06/2026), a Sprint 2 já encerrou. O status permanece "Em andamento" sem resultado. Este é o segundo documento (após ITP) que não reflete o resultado da Sprint 2.
**Evidência:** > "Sprint 2 (09/06–20/06) | AG-23: auditoria; AG-24: integração | [...] | Em andamento"
**Referência normativa:** VV — atividades concluídas devem ser registradas com resultado.
**Ação corretiva:** Atualizar status da Sprint 2 com resultado das atividades de V&V (testes unitários, UAT, aceite formal ou desvio registrado).

---

### NC-VV-02 — Responsável por testes unitários (Nível 1) inclui "Cezar Hiraki" mas REV mostra que cada dev testa seu próprio código
**Severidade:** 🟡 Moderada
**RAP impactado:** VV — responsabilidades corretas
**Localização:** Seção 3.1 — Níveis de Teste, Nível 1
**Problema:** O Nível 1 (Testes Unitários) atribui responsabilidade a "Cezar Hiraki + Renan Kiyoshi". Porém o REV-AASP01-001 mostra que MR !3 foi desenvolvido por Henry Komatsu e MRs !4/!5 por Mateus Veloso. O PLA também atribui testes unitários apenas a Renan Kiyoshi. Há inconsistência sobre quem escreve os testes unitários para o código de Henry e Mateus.
**Evidência:** > "1 | Testes Unitarios | Cezar Hiraki + Renan Kiyoshi (Timeware) | xUnit (.NET FW 5.0) + Moq"
**Referência normativa:** VV — responsabilidades de teste devem refletir a prática real.
**Ação corretiva:** Corrigir para "Renan Kiyoshi, Henry Komatsu e Mateus Veloso (cada desenvolvedor responsável pelos testes unitários do próprio código); Cezar Hiraki como revisor e orientador de cobertura".

---

### NC-VV-03 — Critério "≥ 95% dos cenários críticos aprovados" vs "100% dos P1" cria ambiguidade
**Severidade:** 🟡 Moderada
**RAP impactado:** VV — critérios de aceite claros e não contraditórios
**Localização:** Seção 3.1 Nível 5 e Seção 3.2 Critérios de Qualidade
**Problema:** O documento define dois critérios diferentes para homologação: (a) Nível 5 (UAT): "≥ 95% dos cenários críticos aprovados; todos os cenários P1 (críticos) aprovados sem ressalvas"; (b) Seção 3.2: "Cenários de homologação aprovados (críticos): 100% dos cenários P1 aprovados; ≥ 95% do total". A terminologia "cenários críticos" vs "P1 (críticos)" vs "total" cria ambiguidade sobre o que é P1 e o que é o total. Na prática, todos os 10 cenários da Sprint 1 foram aprovados (100%), mas o critério formal é ambíguo.
**Evidência:** > "Testes de Homologação (UAT) | [...] | >= 95% dos cenários criticos aprovados; todos os cenários P1 (criticos) aprovados sem ressalvas"
**Referência normativa:** VV — critérios de aceite devem ser não-ambíguos e consistentes.
**Ação corretiva:** Padronizar em uma única definição: "100% dos cenários classificados como Crítico (P1) aprovados; ≥ 95% do total de cenários aprovados". Aplicar consistentemente em todas as seções do VV.

---

### NC-VV-04 — "Testes de sistema" sem protocolo formal documentado
**Severidade:** 🟡 Moderada
**RAP impactado:** VV — atividades de V&V documentadas
**Localização:** Seção 3.1 — Nível 4; Seção 7 — Ferramentas
**Problema:** Os testes de sistema (Nível 4) são atribuídos a "Cezar Hiraki via Swagger UI / Postman" mas não há protocolo documentado: quais cenários serão testados neste nível, quais a diferença entre os testes de Nível 4 e os cenários UAT do Nível 5, e como os resultados são registrados. O _DOSSIE-EVIDENCIAS classifica "Swagger execução" como lacuna de evidência.
**Evidência:** > "4 | Testes de Sistema | Cezar Hiraki via Swagger UI / Postman | Swagger UI + Postman | [...] | Todos os endpoints respondem com status HTTP correto"
**Referência normativa:** VV — atividades de teste devem ter protocolo rastreável.
**Ação corretiva:** Definir explicitamente quais cenários são cobertos pelo Nível 4 (testes de sistema pelo desenvolvedor) versus Nível 5 (UAT pelo QA). Arquivar evidências dos testes de sistema (capturas de Swagger ou relatório Postman).

---

### NC-VV-05 — "Desvio de SP por sprint: ≤ 10%" como critério de qualidade mistura métricas de prazo com V&V
**Severidade:** 🟢 Leve
**RAP impactado:** VV — critérios de qualidade pertinentes ao processo de V&V
**Localização:** Seção 3.2 — Critérios de Qualidade do Projeto
**Problema:** O critério "Desvio de SP por sprint: ≤ 10%" é uma métrica de gestão de projeto (GPR/MED), não um critério de qualidade de produto ou processo de V&V. Sua inclusão na tabela de critérios de qualidade do VV é inadequada e pode criar confusão sobre o que o processo V&V é responsável por monitorar.
**Evidência:** > "Desvio de SP por sprint | <= 10% | PLA-AASP01-001"
**Referência normativa:** VV — o plano de V&V deve focar em critérios de qualidade de produto e processo, não em prazo.
**Ação corretiva:** Remover o critério de desvio de SP do VV e mantê-lo apenas no PLA e no RAC (onde pertence).

---

### NC-VV-06 — Plano cobre Sprint 3 apenas genericamente
**Severidade:** 🔵 Obs
**RAP impactado:** VV — planejamento de V&V para todas as sprints
**Localização:** Seção 4 — Sprint 3
**Problema:** A Sprint 3 está em andamento (desde 23/06/2026) e o VV descreve apenas "Testes unitários AG-25; testes de sistema; UAT (regressão AG-20 a AG-25); preparação para aceite final" sem critérios específicos. Dada a criticidade da Sprint 3 (sprint final com testes de regressão completos e aceite final), o plano de V&V deveria ser mais detalhado.
**Evidência:** > "Sprint 3 (23/06–04/07) | AG-25 | Testes unitarios AG-25; testes de sistema (Swagger + Postman); UAT (Leonardo Francisco Pereira) com regressão de AG-20 a AG-25; preparação para aceite final"
**Referência normativa:** VV — plano deve ser suficientemente detalhado para orientar a execução.
**Ação corretiva:** Expandir o plano da Sprint 3 com: (a) quantos cenários de regressão serão executados (AG-20 a AG-25 = pelo menos 15 cenários); (b) critério de aprovação para regressão; (c) prazo para execução do UAT antes da Sprint Review.
