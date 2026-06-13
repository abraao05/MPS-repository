# Relatório de Acompanhamento — SuperApp Fruki · Pacote Final 24

## 0. Identificação do ciclo

| Campo | Valor |
|---|---|
| **Documento** | RAC-FRUKI01-001 |
| **Projeto** | SuperApp Fruki — Pacote Final 24 |
| **Plano de referência** | PLA-FRUKI01-002 v1.0 |
| **Período / ciclo** | Out/2025 – 27/12/2025 (Sprints 1 e 2 concluídas; Sprint 3 em andamento) |
| **Data do relatório** | 27/12/2025 |
| **Responsável** | Abraão Oliveira |

---

## 1. Monitoramento do planejado vs. realizado

### 1.1 Progresso de escopo e tarefas

| Módulo / Sprint | Planejado | Realizado | Desvio | Comentário |
|---|---|---|---|---|
| Sprint 1 — Pedidos Não Alocados (RF-05 a RF-08) | Out/2025 — entregue até 25/10/2025 | Concluída — PR #57 mergeada em 25/10/2025 | 0 | Normalização front-end da API implementada sem impacto no prazo |
| Sprint 2 — Regra de Ouro (RF-09 a RF-11) | Nov/2025 | Concluída — PR mergeada Nov/2025 | 0 | Nomenclatura "Regra de Ouro" adotada (era "Caixa Preta") — ver GDE-FRUKI01-001 |
| Sprint 3 — PDV / Rota PDV (RF-12 a RF-14) | Dez/2025 — início | Em andamento — interface desenvolvida; integração com API Rota PDV pendente | +3 semanas (atraso API) | API de Rota PDV ainda não recebida de Jardel; previsão de recebimento: início de Jan/2026 |

**Módulos concluídos:** 2 de 3 (67%)
**Aceite final:** previsto para 15/01/2026 — dentro do prazo; atraso da API absorvível.

### 1.2 Estimado vs. realizado (esforço)

| Sprint | SP estimados | SP entregues | Comentário |
|---|---|---|---|
| Sprint 1 — Pedidos Não Alocados | 21 SP | 22 SP | +1 SP — normalização adicional de formato não padronizado da API |
| Sprint 2 — Regra de Ouro | 21 SP | 20 SP | -1 SP — módulo mais simples que o estimado após validação com Cecília |
| Sprint 3 — PDV (parcial) | 21 SP | ~10 SP | Interface desenvolvida; integração real pendente após API |

- **Velocity Sprint 1:** ~22 SP / 4 semanas
- **Velocity Sprint 2:** ~20 SP / 4 semanas
- **Velocity média observada:** ~21 SP/sprint (compatível com estimativa de 25 SP do PLA-FRUKI01-002)

### 1.3 Cronograma

| Marco | Planejado | Realizado / Previsto | Desvio |
|---|---|---|---|
| Kickoff | 09/10/2025 | 09/10/2025 | 0 |
| PR #57 — Pedidos Não Alocados | 25/10/2025 | 25/10/2025 | 0 |
| Entrega Regra de Ouro | Nov/2025 | Nov/2025 | 0 |
| Recebimento API Rota PDV | Dez/2025 | Previsto para início Jan/2026 | ~3 semanas |
| Aceite final via Teams | 15/01/2026 | Previsto 15/01/2026 | 0 (absorvido) |

### 1.4 Recursos

| Dimensão | Planejado | Realizado | Desvio |
|---|---|---|---|
| Equipe Timeware | Abraão (GP/PO), Brenda (UX), Luca + Thiago (devs) | Conforme planejado — equipe integral | 0 |
| APIs Fruki | Disponíveis antes de cada sprint | Pedidos Não Alocados ✅ Out; Regra de Ouro ✅ Nov; Rota PDV ⚠️ atrasada | Rota PDV com atraso de ~3 semanas |

---

## 2. Envolvimento das partes interessadas

- **Cecília Ribeiro:** participou das validações de protótipos antes das Sprints 1 e 2; validou e aprovou os APKs de homologação de ambos os módulos. Disponível para Sprint 3.
- **Leandro Lottermann:** informado via e-mail sobre o atraso da API Rota PDV; confirmou que o prazo de 15/01/2026 permanece viável e que a responsabilidade pelo atraso é do time técnico Fruki.
- **Jardel Dargas Silva:** aprovou as PRs de Pedidos Não Alocados e Regra de Ouro; informado sobre urgência no envio da API Rota PDV; comprometeu envio para início de Janeiro/2026.
- **Alexsandro de Vargas Braga:** forneceu a lista completa de perguntas do formulário PDV em 04/12/2025 — interface do formulário em desenvolvimento.

---

## 3. Transição para operação e suporte

Ainda não iniciada. A transição ocorre via merge das PRs e entrega do AAB para a Play Store pelo time Fruki após o aceite final (previsto 15/01/2026).

---

## 4. Riscos e oportunidades

| ID | Risco | Situação atual | Mudança desde kickoff | Comunicado a |
|---|---|---|---|---|
| R-01 | API Rota PDV não disponibilizada no prazo | **Ativo** — API não recebida até 27/12/2025 | Materializado parcialmente: atraso de ~3 semanas | Leandro Lottermann (e-mail); Jardel informado diretamente |
| R-02 | Atraso na validação de protótipos por Cecília | Encerrado | Não ocorreu; validações dentro do prazo | — |
| R-03 | Mudança de escopo durante a sprint | Encerrado (fase) | Renomeação "Caixa Preta" → "Regra de Ouro" tratada via GDE-FRUKI01-001, sem impacto de prazo | Cecília, Leandro |
| R-04 | Problema de agenda para aceite final | Monitorando | Aceite agendado para 15/01/2026 via Teams — aguardar confirmação de Leandro | Leandro Lottermann |

---

## 5. Ações corretivas e questões

| ID | Questão / desvio | Ação tomada | Tratada com | Responsável | Situação |
|---|---|---|---|---|---|
| AC-01 | API Rota PDV não recebida de Jardel até Dez/2025 | Interface da tela de PDV e formulário desenvolvidos com mock de dados; integração real será feita após recebimento da API em Jan/2026 | Jardel (WhatsApp/e-mail); Leandro (e-mail de status) | Abraão Oliveira | Aberta — aguardando API |
| AC-02 | Aceite final de 15/01/2026 não pode escorregar | Reunião agendada via Teams com Leandro e Cecília; integração do PDV priorizada para primeira semana de Jan/2026 | Leandro Lottermann | Abraão Oliveira | Aberta — em acompanhamento |

---

## 6. Análise de resultados significativos

| Resultado | Análise de causa | Encaminhamento |
|---|---|---|
| Sprints 1 e 2 concluídas no prazo sem defeitos em produção | Protótipos validados por Cecília antes de cada sprint eliminou retrabalho; revisão de PR por Jardel garantiu qualidade técnica | Manter modelo de validação de protótipo antes de cada sprint |
| API Rota PDV atrasada (~3 semanas) | Jardel priorizou outras demandas internas Fruki no Q4/2025; ausência de data formal de comprometimento no contrato | Incluir cláusula de pré-requisito com data de comprometimento em próximos projetos — ver LI-FRUKI01-001 OM-01 |

---

## 7. Melhorias de processo propostas

| O que funcionou | Por que propor como melhoria | Encaminhado para |
|---|---|---|
| Desenvolvimento de interface com mock antes da API real (Sprint 3) | Eliminou bloqueio de desenvolvimento por dependência externa; reduz impacto de atraso de API de cliente | LI-FRUKI01-001 — OM-05 / processo organizacional GPR |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 27/12/2025 | Abraão Oliveira | Status report parcial — Sprints 1 e 2 concluídas; Sprint 3 em andamento |
