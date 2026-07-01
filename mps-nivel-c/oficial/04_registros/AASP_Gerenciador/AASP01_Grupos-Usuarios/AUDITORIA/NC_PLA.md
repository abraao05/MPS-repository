# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Plano de Projeto
**Código:** PLA-AASP01-001
**Versão auditada:** 1.1
**Data do documento:** 24/06/2026
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 1 | 0 |
| Conteúdo (CNT) | 1 | 2 | 1 | 0 |
| Datas (DT) | 0 | 1 | 0 | 0 |
| Papéis (PAP) | 0 | 1 | 0 | 0 |
| Coerência (CON) | 0 | 1 | 0 | 0 |
| MPS.BR (MPS) | 1 | 0 | 0 | 0 |
| **TOTAL** | **2** | **5** | **2** | **0** |

**Veredicto:** NÃO-CONFORME CRÍTICO

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-PLA-01 — Plano de risco sem monitoramento documentado (RAP ausente)
**Severidade:** 🔴 Grave
**RAP impactado:** GRE RAP 5 — riscos monitorados ao longo do projeto
**Localização:** Seção 6.2 — Registro de Riscos
**Problema:** O plano registra 5 riscos (R-01 a R-05) com probabilidade, impacto e ação de mitigação, mas não há coluna de "Status do monitoramento" nem seção de acompanhamento de riscos. O RAC-AASP01-001 menciona R-01 e R-04 como "em monitoramento" na Sprint 2, mas o próprio PLA não é atualizado com o status dos riscos. O processo GRE exige que os riscos sejam monitorados e que o status de cada risco seja documentado periodicamente. A ausência de coluna de monitoramento no PLA e a falta de atualização das colunas de risco tornam impossível evidenciar o RAP de monitoramento sem consultar o RAC.
**Evidência:** > "| R-01 | Indisponibilidade do ambiente de homologação AASP | P2 | I2 | 4 | Agendamento prévio... |" — sem coluna de status/monitoramento.
**Referência normativa:** GRE RAP 5 — as ações de gestão de risco devem ser implementadas e monitoradas. Evidência: registro atualizado com status e resultado do monitoramento.
**Ação corretiva:** Adicionar colunas "Status atual" e "Última atualização" à tabela de riscos. Preencher com o estado de cada risco na data do documento (24/06/2026): R-04 materializado parcialmente (integração ms.temis ainda não concluída), R-01 mitigado (ambiente disponível desde Sprint 2). Atualizar o PLA a cada sprint.

---

### NC-PLA-02 — Plano sem seção de encerramento ou critérios de done do projeto
**Severidade:** 🔴 Grave
**RAP impactado:** GPR RAP 7 — encerramento formal do projeto planejado
**Localização:** Ausência — nenhuma seção de encerramento
**Problema:** O PLA não contém seção de planejamento de encerramento do projeto — critérios de encerramento, responsável pelo TAE, lições aprendidas, checklist de encerramento. O índice prevê o TAE e o LI para a Sprint 3, mas o PLA não os planeja formalmente. O MPS.BR GPR exige que o encerramento do projeto seja planejado, incluindo confirmação dos critérios de conclusão e responsabilidades.
**Evidência:** As 10 seções do PLA cobrem: objetivo, escopo, cronograma, papéis, comunicação, riscos, V&V, métricas e process de CR — encerramento ausente.
**Referência normativa:** GPR RAP 7 — o plano deve incluir o planejamento para o encerramento do projeto.
**Ação corretiva:** Adicionar seção "11. Plano de Encerramento" contendo: critérios de aceite final (100% RFs entregues, cobertura ≥ 60%, zero defeitos P1), responsável pelo TAE (Marcos Turnes), prazo (~04/07/2026), artefatos de encerramento a produzir (TAE, LI), e responsável pelas Lições Aprendidas (Abraão).

---

### NC-PLA-03 — Responsável por testes unitários é Renan Kiyoshi, mas MRs mostram Henry Komatsu e Mateus Veloso como autores
**Severidade:** 🟡 Moderada
**RAP impactado:** GPR RAP 2 — responsabilidades claramente atribuídas
**Localização:** Seção 7 — Plano de V&V, linha "Testes unitários"
**Problema:** A tabela de V&V do PLA atribui "Testes unitários" exclusivamente a Renan Kiyoshi. Porém o REV-AASP01-001 mostra que MR !3 (AG-21) foi desenvolvido por Henry Komatsu e MR !4/!5 (AG-22) por Mateus Veloso. O VV-AASP01-001 (Nível 1) também atribui testes unitários a "Cezar Hiraki + Renan Kiyoshi". As responsabilidades de teste unitário não refletem a divisão real de trabalho entre os três desenvolvedores.
**Evidência:** > "Testes unitários | A cada sprint | Renan Kiyoshi | Cobertura ≥ 60%..."
**Referência normativa:** GPR RAP 2 — responsabilidades devem refletir a realidade de execução.
**Ação corretiva:** Atualizar para "Renan Kiyoshi, Henry Komatsu e Mateus Veloso" como responsáveis pelos testes unitários (cada desenvolvedor responsável pelos testes de seu próprio código).

---

### NC-PLA-04 — M7 ("Sem change requests não planejados aprovados") é métrica impossível de medir
**Severidade:** 🟡 Moderada
**RAP impactado:** MED — métricas mensuráveis
**Localização:** Seção 8 — Métricas de Sucesso, M7
**Problema:** A métrica M7 "Sem change requests não planejados aprovados durante o projeto" é tautológica: qualquer CR aprovado é automaticamente "planejado" após aprovação. Além disso, esta métrica não tem valor de linha base nem critério quantitativo — é uma restrição de escopo, não uma métrica. Métricas de processo MPS.BR devem ser quantitativas e mensuráveis.
**Evidência:** > "M7 | Sem change requests não planejados aprovados durante o projeto"
**Referência normativa:** MED — métricas devem ser mensuráveis com valor numérico ou faixa aceitável.
**Ação corretiva:** Reformular M7 como "Número de Change Requests aprovados: 0 (escopo estável) — qualquer CR aprovado deve ser documentado com impacto em prazo e custo" ou eliminar como métrica e manter como restrição de escopo na seção 2.

---

### NC-PLA-05 — Data da versão 1.1 idêntica à v1.0 (ambas poderiam indicar criação e revisão no mesmo dia)
**Severidade:** 🟢 Leve
**RAP impactado:** GCO — controle de versão
**Localização:** Histórico de Revisões
**Problema:** O histórico registra v1.0 em 19/05/2026 (Abraão) e v1.1 em 24/06/2026 (Time de Melhoria Contínua). A diferença de mais de 1 mês entre versões, combinada com a ausência de versão intermediária refletindo o aceite da Sprint 1, sugere que o PLA não foi atualizado após a conclusão da Sprint 1 (06/06/2026), contrariando GPR RAP 4.
**Evidência:** > "1.0 | 19/05/2026 | Abraão | Criação do documento" — sem versão entre 19/05 e 24/06.
**Referência normativa:** GPR RAP 4 — o plano deve ser atualizado quando há progresso significativo (conclusão de sprint é evento suficiente).
**Ação corretiva:** Adicionar versão 1.1 em 06/06/2026 (pós-aceite Sprint 1) com os ajustes de status. A versão 1.2 seria a reconciliação de 24/06/2026.

---

### NC-PLA-06 — Plano de comunicação não menciona Silvio Baroni (GQA) como destinatário
**Severidade:** 🟡 Moderada
**RAP impactado:** GQA RAP 1 — independência do auditor assegurada no planejamento
**Localização:** Seção 5 — Plano de Comunicação
**Problema:** O plano de comunicação não inclui o auditor GQA (Silvio Baroni — SEPG) como participante ou destinatário de qualquer comunicação, incluindo o relatório de status semanal ou as sprint reviews. A independência do GQA requer que ele receba informações do projeto por canal formal, não apenas via consulta de documentos a posteriori.
**Evidência:** > "Relatório de Status | Semanal | E-mail | Marcos Turnes, Leonardo Francisco Pereira | Abraão" — Silvio Baroni ausente.
**Referência normativa:** GQA RAP 1 — auditoria independente requer acesso a informações de progresso do projeto.
**Ação corretiva:** Adicionar linha ao plano de comunicação: "Relatório GQA | Mensal | E-mail | Silvio Baroni (SEPG) | Abraão".

---

### NC-PLA-07 — "Time de Melhoria Contínua" sem identificação nominal
**Severidade:** 🟢 Leve
**RAP impactado:** GCO RAP 2
**Localização:** Histórico de Revisões — versão 1.1
**Problema:** Mesmo problema sistêmico dos demais documentos.
**Evidência:** > "1.1 | 24/06/2026 | Time de Melhoria Contínua | Reconciliação..."
**Referência normativa:** GCO RAP 2.
**Ação corretiva:** Identificar o responsável nominal.
