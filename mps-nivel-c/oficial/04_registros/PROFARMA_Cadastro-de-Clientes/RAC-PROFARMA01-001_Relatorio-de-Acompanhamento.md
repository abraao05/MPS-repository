# Relatório de Acompanhamento — Rede D1000 · Cadastro de Clientes

| Campo | Valor |
|---|---|
| **Documento** | RAC-PROFARMA01-001 |
| **Projeto** | Cadastro de Clientes — Rede D1000 |
| **Cliente** | Profarma S.A. / Rede D1000 |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR |

---

## 1. Objetivo

Monitorar o progresso do projeto Cadastro de Clientes — Rede D1000 em relação ao plano estabelecido, identificar desvios de prazo, escopo e qualidade em cada fase, e registrar as ações corretivas acionadas. Este relatório consolida os snapshots de acompanhamento de todas as fases do projeto e serve como evidência do processo GPR (Gerência de Projeto).

---

## 2. Fases do projeto

### Fase 1 — Fundação (Sprints 1–3, Abril–Junho/2025)

**Snapshot de progresso — 20/06/2025**

| Item | Detalhe |
|---|---|
| Status geral | Dentro do prazo para a fase |
| Sprints cobertos | 1, 2 e 3 |
| Período | Abril a Junho/2025 |

**Itens concluídos vs. planejados**

| Requisito | Entrega | Status |
|---|---|---|
| RF-01 a RF-05 | CRUD básico de clientes | Concluído |
| RF-11 | Integração outbox ITEC | Concluído |
| RF-18 | Health check da API | Concluído |
| — | Pipeline de CI | Concluído |

Todos os itens planejados para a fase foram entregues dentro do período previsto.

**Desvios identificados**

| ID | Descrição | Referência |
|---|---|---|
| NC-01 (GQA) | Requisitos documentados retroativamente — Sprints 1–3 sem documento formal de requisitos no início | GQA-PROFARMA01-001 |
| NC-02 (GQA) | Rastreabilidade no Jira inexistente nos Sprints 1–3 | GQA-PROFARMA01-001 |

**Riscos materializados**

| Risco | Impacto observado |
|---|---|
| R-05 — Documentação ITEC inexistente | Necessidade de engenharia reversa da integração outbox, consumindo esforço adicional nos Sprints 2 e 3 |

**Ações corretivas tomadas**

- Elaboração retroativa do REQ-PROFARMA01-001, cobrindo todos os requisitos identificados nos Sprints 1–3.
- Adoção do Jira como ferramenta oficial de rastreabilidade a partir do Sprint 4, com registro retroativo das histórias dos Sprints anteriores.

---

### Fase 2 — Integrações Principais (Sprints 4–7, Julho–Agosto/2025)

**Snapshot de progresso — 22/08/2025**

| Item | Detalhe |
|---|---|
| Status geral | Replanejamento necessário para Sprints 8–10 |
| Sprints cobertos | 4, 5, 6 e 7 |
| Período | Julho a Agosto/2025 |

**Itens concluídos vs. planejados**

| Requisito | Entrega | Status |
|---|---|---|
| RF-09 | Verificação de existência de cliente (HEAD) | Concluído |
| RF-10 | Reativação de cadastro inativo | Concluído |
| RF-06 | Busca paginada de clientes | Concluído |
| RF-12 | Integração VTEX (canal Omni) | Concluído |
| RF-13 | Integração Call Center | Concluído |
| RF-14 | Integração Propz CRM | Iniciado (continuação nas fases seguintes) |

**Desvios identificados**

| Descrição | Impacto |
|---|---|
| Contratos de API do VTEX e Call Center entregues pela D1000 com 3 semanas de atraso em relação ao previsto | Início das integrações RF-12 e RF-13 postergado; absorção de BlueSoft e CloseUp deslocada para Sprints 8–10 |

**Change Requests absorvidos na fase**

| CR | Descrição |
|---|---|
| CR-01 a CR-04 | Integrações BlueSoft e CloseUp (realocadas para os Sprints 8–10) |
| CR-05 | Worker de anonimização LGPD |
| CR-07 | Aceleração do prazo da integração Propz |

**Riscos materializados**

| Risco | Impacto observado |
|---|---|
| R-02 — Atraso na entrega de contratos de API por terceiros | Contratos de API do VTEX e Call Center recebidos 3 semanas após a data prevista; necessidade de replanejamento dos Sprints seguintes |

**Ações corretivas tomadas**

- Replanejamento dos Sprints 8–10 para acomodar as integrações BlueSoft e CloseUp, originalmente previstas para esta fase.
- Estabelecimento de deadline fixo em 04/12/2025 para a entrega da integração Propz CRM.

---

### Fase 3 — Integrações Satélites (Sprints 8–10, Agosto–Setembro/2025)

**Snapshot de progresso — 03/10/2025**

| Item | Detalhe |
|---|---|
| Status geral | Testes formais de homologação com início postergado |
| Sprints cobertos | 8, 9 e 10 |
| Período | Agosto a Setembro/2025 |

**Itens concluídos vs. planejados**

| Requisito | Entrega | Status |
|---|---|---|
| RF-15 | Integração BlueSoft (score de crédito) | Concluído |
| RF-16 | Integração CloseUp (dados de consumo) | Concluído |
| RF-17 | Worker de anonimização LGPD | Concluído |
| RF-08 | Carga batch de estrutura organizacional | Concluído |

**Desvios identificados**

| Descrição | Impacto |
|---|---|
| Ambiente de homologação AKS indisponível durante a fase | Desenvolvimento continuou localmente com Docker Compose; início dos testes formais de homologação postergado para Setembro/2025 |

**Riscos materializados**

| Risco | Impacto observado |
|---|---|
| R-01 — Ambiente de homologação AKS indisponível | Testes de integração em ambiente próximo à produção não puderam ser executados no período previsto; impacto no início da fase de Qualidade |

**Ações corretivas tomadas**

- Abertura de chamado junto à equipe de Operações D1000 (responsável: Fagner Pereira) para provisionamento do ambiente AKS.
- Continuidade do desenvolvimento e testes locais com Docker Compose para não bloquear o progresso das entregas.
- Ambiente AKS disponibilizado em Setembro/2025, viabilizando o início da fase de Qualidade e Carga no prazo.

---

### Fase 4 — Qualidade e Carga (Sprints 11–13, Setembro–Outubro/2025)

**Snapshot de progresso — 31/10/2025**

| Item | Detalhe |
|---|---|
| Status geral | Carga inicial concluída com atraso; demais entregas dentro do planejado |
| Sprints cobertos | 11, 12 e 13 |
| Período | Setembro a Outubro/2025 |

**Itens concluídos vs. planejados**

| Entrega | Resultado | Status |
|---|---|---|
| Suíte de testes unitários | 273 cenários, cobertura de 84% (Domain + Application) | Concluído |
| Testes de performance | p95 = 142 ms a 500 req/s | Concluído |
| Carga inicial — base de CPFs | 7 milhões de CPFs carregados após múltiplos ciclos de validação | Concluído com atraso |

**Desvios identificados**

| Descrição | Impacto |
|---|---|
| Carga inicial da base legada levou 3 semanas além do estimado | Inconsistências na base legada (CPFs inválidos, máscaras divergentes, registros duplicados) exigiram múltiplos ciclos de extração, validação e correção |

**Change Requests absorvidos na fase**

| CR | Descrição |
|---|---|
| CR-06 | Backup PITR explicitado nos requisitos de infraestrutura |
| CR-08 | Adição de métricas Prometheus ao serviço |
| CR-09 | Ajuste no contrato de API VTEX (campo de endereço) |
| CR-10 | Campo `score_credito` na integração BlueSoft |

**Riscos materializados**

| Risco | Impacto observado |
|---|---|
| R-06 — Inconsistências na base legada de CPFs | Necessidade de múltiplas rodadas de extração, validação e correção, atrasando em 3 semanas a conclusão da carga inicial |

**Ações corretivas tomadas**

- Múltiplas rodadas de extração → validação → correção realizadas em parceria com o DBA Marcus Ribeiro (D1000).
- Carga final concluída e validada dentro do Sprint 13.

---

### Fase 5 — Homologação (Sprints 14–17, Outubro/2025–Janeiro/2026)

**Snapshot de progresso — 22/01/2026**

| Item | Detalhe |
|---|---|
| Status geral | Homologação concluída; ambiente final liberado em 22/01/2026 |
| Sprints cobertos | 14, 15, 16 e 17 |
| Período | Outubro/2025 a Janeiro/2026 |

**Evolução da cobertura de homologação por canal**

| Canal | Snapshot 08/10/2025 | Snapshot 17/10/2025 | Snapshot 22/01/2026 |
|---|---|---|---|
| Balcão | 76% (16/21 cenários) | 74% (23/31 — escopo expandido) | 100% (31/31) |
| PDV | 67% (4/6) | 67% (4/6) | 100% (6/6) |
| Call Center | 0% (bloqueado) | 12% (1/8 — desbloqueado em 16/10) | 100% (8/8) |
| Omni (VTEX) | 0% (webhook URL pendente) | 50% (1/2) | 100% (2/2) |
| Conveniados | 100% (4/4) | 100% (4/4) | 100% (4/4) |
| Propz CRM | — | — | 100% (13/13) — validado em 10/12/2025 |

**Defeitos identificados na homologação**

| Total identificados | S1 | S2 | S3 |
|---|---|---|---|
| 14 | 2 | 5 | 7 |

**Desvios identificados**

| Descrição | Impacto |
|---|---|
| Lead time de GMUD (Gerenciamento de Mudanças) adicionou 2 a 5 dias úteis por ciclo de release | Compressão do tempo disponível para correção de defeitos antes das janelas de aceite, exigindo sessões intensivas de correção |

**Riscos materializados**

| Risco | Impacto observado |
|---|---|
| R-03 — Lead time de janelas de mudança (GMUD) | Cada ciclo de correção e redeploy adicionou 2 a 5 dias úteis, comprimindo o tempo disponível para resolução dos defeitos S1 e S2 |

**Change Requests absorvidos na fase**

| CR | Descrição |
|---|---|
| CR-11 | Ajuste no fluxo de opt-out (redefinição do comportamento junto ao Propz) |
| CR-12 | Suporte a campo adicional de conveniado no canal Call Center |

**Eventos relevantes**

- "Sala de guerra" realizada em 02/10/2025: resolução concentrada dos defeitos S1 (BAL-B03 e PDV-B01) e dos defeitos S2 prioritários.
- Integração Propz CRM validada em 10/12/2025, dentro do deadline fixado em 04/12/2025 (validação concluída antes do marco).
- Ambiente de homologação final liberado em 22/01/2026.

**Ações corretivas tomadas**

- Antecipação das solicitações de janela de GMUD para reduzir o tempo de espera nos ciclos subsequentes.
- Sessões intensivas de correção realizadas entre 27 e 29/01/2026 para resolução dos defeitos S2 remanescentes.

---

### Fase 6 — Piloto e Encerramento (Sprints 18–19, Janeiro/2026)

**Snapshot de progresso — 29/01/2026**

| Item | Detalhe |
|---|---|
| Status geral | Piloto concluído com sucesso; aceite formal emitido |
| Sprints cobertos | 18 e 19 |
| Período | Janeiro/2026 |

**Itens concluídos vs. planejados**

| Entrega | Resultado | Status |
|---|---|---|
| Piloto — Loja 9 (canais PDV, Balcão e OMNI) | Operacional desde 15/01/2026 | Concluído |
| Monitoramento de incidentes no período de piloto | 0 incidentes S1 registrados | Conforme |
| SLAs de performance em todos os canais | Todos os canais dentro dos limites contratados | Conforme |
| Aceite formal | Emitido por Humberto Erler em 29/01/2026 | Concluído |

**Desvios identificados**

Nenhum desvio identificado nesta fase.

**Riscos materializados**

Nenhum risco materializado nesta fase.

**Ações corretivas tomadas**

Não aplicável — fase concluída sem desvios.

O projeto foi encerrado em 29/01/2026 sem pendências de escopo contratado.

---

## 3. Resumo de indicadores consolidados

| Indicador | Meta | Resultado | Status |
|---|---|---|---|
| Prazo de entrega | Janeiro/2026 | Aceite formal em 29/01/2026 | Dentro do prazo |
| Escopo contratado | 100% dos requisitos RF-01 a RF-18 entregues | 100% entregues; 12 CRs aprovados e absorvidos | Completo |
| Cobertura de testes unitários | ≥ 80% (Domain + Application) | 84% | Atendido |
| Performance (p95) | ≤ 200 ms a 500 req/s | 142 ms a 500 req/s | Atendido |
| Defeitos S1 abertos no aceite | 0 | 0 | Atendido |
| Defeitos S2 abertos no aceite | 0 | 0 | Atendido |
| Incidentes S1 no piloto | 0 | 0 | Atendido |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Time de Melhoria Contínua | Versão inicial — consolidação dos snapshots de acompanhamento de todas as 6 fases do projeto |
