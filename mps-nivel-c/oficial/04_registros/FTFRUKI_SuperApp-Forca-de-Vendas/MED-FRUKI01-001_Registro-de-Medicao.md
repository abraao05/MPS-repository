# Registro de Medição — SuperApp Fruki · Força de Vendas

| Campo | Valor |
|---|---|
| **Documento** | MED-FRUKI01-001 — Registro de Medição |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | SuperApp Fruki — Força de Vendas (Pacote 1 + Pacote Final 24) |
| **Responsável por Medição** | Abraão Oliveira |
| **Referência** | PLA-MED-001 — Plano de Medição Organizacional |

---

## 1. Objetivo

Registrar as medidas coletadas ao longo do projeto SuperApp Fruki conforme o PLA-MED-001, apoiando a análise de aderência ao prazo, capacidade de entrega e qualidade das entregas.

---

## 2. Pacote 1 — Módulo Metas e Remuneração Variável

**Período:** Jun/2025 – Set/2025

### M1 — Aderência ao prazo

| Marco | Data planejada | Data realizada | Variação |
|---|---|---|---|
| Kickoff / proposta | 05/06/2025 | 05/06/2025 | 0 dias |
| Levantamento de requisitos | 25/06/2025 | 25/06/2025 | 0 dias |
| Acesso ao repositório e APIs | 26/06/2025 | 26/06/2025 | 0 dias |
| Piloto com vendedores | 05/08/2025 | 05/08/2025 | 0 dias |
| Aceite e encerramento | Ago/Set 2025 | Set/2025 | Dentro do período |

**Resultado M1:** Sem desvios de prazo relevantes. O piloto revelou defeitos que exigiram uma semana adicional de ajustes, absorvida dentro do período planejado.

### M2 — Esforço estimado × realizado

| Item | Estimado (SP) | Realizado (SP) | Desvio |
|---|---|---|---|
| RF-01 — Metas por família | 13 | 13 | 0% |
| RF-02 — Cobertura, drop size, positivação | 13 | 13 | 0% |
| RF-03 — Composição de RV por perfil | 13 | 15 | +15% (ajustes de cálculo pós-piloto) |
| RF-04 — Adaptação por perfil de vendedor | 8 | 8 | 0% |
| Integração com APIs + tratamento performance | 8 | 10 | +25% (deduplicação e normalização adicionais) |
| Builds, PR, ajustes de piloto | 5 | 6 | +20% |
| **Total** | **~60 SP** | **~65 SP** | **+8%** |

**Resultado M2:** Desvio de +8% no esforço — dentro da margem aceitável. Os desvios concentraram-se em itens de integração com API e ajustes pós-piloto.

### M3 — Velocity

| Sprint / período | SP concluídos | Duração |
|---|---|---|
| Sprint 1 (Jun–Jul/2025) | ~35 SP | 5 semanas |
| Sprint 2 / Ajustes (Ago/2025) | ~30 SP | 4 semanas |
| **Velocity média** | **~32 SP/sprint (2 semanas)** | — |

**Base de referência atualizada:** Velocity de ~32 SP/sprint para equipe de 2 devs React Native + 1 UX. Utilizada como base para estimativa do Pacote Final 24.

### M5 — Densidade de defeitos

| Ciclo | Defeitos identificados | Defeitos em produção |
|---|---|---|
| Desenvolvimento Sprint 1 | 2 (duplicação de famílias; latência API) | 0 |
| Piloto (05/08/2025) | 2 (duplicação visível residual; cálculo positivação) | 0 |
| Pós-correção e PR | 0 | 0 |

**Resultado M5:** 4 defeitos identificados em homologação, 0 em produção.

### M6 — Defeitos em homologação × produção

**Taxa de contenção:** 100% — nenhum defeito chegou à produção.

---

## 3. Pacote Final 24 — Pedidos Não Alocados · Regra de Ouro · PDV

**Período:** Out/2025 – Jan/2026

### M1 — Aderência ao prazo

| Marco | Data planejada | Data realizada | Variação |
|---|---|---|---|
| Kickoff / aprovação proposta | 09/10/2025 | 09/10/2025 | 0 dias |
| Entrega PR #57 — Pedidos Não Alocados | 25/10/2025 | 25/10/2025 | 0 dias |
| Entrega Regra de Ouro | Nov/2025 | Nov/2025 | Dentro do mês |
| Alinhamento PDV | 04/12/2025 | 04/12/2025 | 0 dias |
| Recebimento API Rota PDV | Dez/2025 (previsto) | 08/01/2026 | +~3 semanas (risco R-01) |
| Aceite final via Teams | 15/01/2026 | 15/01/2026 | 0 dias |

**Resultado M1:** Um desvio de prazo no recebimento da API Rota PDV (+3 semanas), gerenciado com desenvolvimento paralelo da interface (mock). O prazo final de aceite não foi afetado.

### M2 — Esforço estimado × realizado

| Módulo | Estimado (SP) | Realizado (SP) | Desvio |
|---|---|---|---|
| Pedidos Não Alocados (RF-05 a RF-08) | 21 | 22 | +5% (normalização front-end adicional) |
| Regra de Ouro (RF-09 a RF-11) | 21 | 20 | -5% |
| PDV / Rota PDV (RF-12 a RF-14) | 21 | 23 | +10% (integração API atrasada; trabalho paralelo com mock) |
| Ajustes Metas/RV | 5 | 5 | 0% |
| Builds AAB, versionamento 2.0, PRs | 5 | 5 | 0% |
| Documentação e aceite | 2 | 2 | 0% |
| **Total** | **~75 SP** | **~77 SP** | **+3%** |

**Resultado M2:** Desvio de +3% — dentro da margem aceitável.

### M3 — Velocity

| Sprint | Módulo | SP concluídos | Duração |
|---|---|---|---|
| Sprint 1 (Out/2025) | Pedidos Não Alocados | 22 SP | ~4 semanas |
| Sprint 2 (Nov/2025) | Regra de Ouro | 20 SP | ~4 semanas |
| Sprint 3 (Dez/2025–Jan/2026) | PDV / Rota PDV + builds | 35 SP | ~6 semanas |
| **Velocity média sprints 1-2** | | **~21 SP/sprint (4 semanas)** | — |

**Nota:** A Sprint 3 foi estendida devido ao atraso da API Rota PDV; não reflete a velocity de desenvolvimento puro.

### M5 — Densidade de defeitos

| Ciclo | Módulo | Defeitos identificados | Defeitos em produção |
|---|---|---|---|
| Sprint 1 | Pedidos Não Alocados | 1 (formato não padronizado da API) | 0 |
| Sprint 2 | Regra de Ouro | 0 | 0 |
| Sprint 3 | PDV / Rota PDV | 1 (integração API com atraso — gerenciada como risco, não defeito) | 0 |
| Aceite final | Todos | 0 | 0 |

**Resultado M5:** 1 defeito real identificado em homologação, 0 em produção.

### M6 — Defeitos em homologação × produção

**Taxa de contenção:** 100% — nenhum defeito chegou à produção.

---

## 4. Consolidado do projeto

| Medida | Pacote 1 | Pacote Final 24 | Referência organizacional |
|---|---|---|---|
| Aderência ao prazo | 100% dos marcos no prazo | 5 de 6 marcos no prazo (1 desvio gerenciado) | Meta: ≤10% de desvio |
| Desvio de esforço | +8% | +3% | Meta: ≤15% de desvio |
| Velocity (2 semanas) | ~32 SP/sprint | ~21 SP/sprint (módulos de 4 semanas) | Base: ~25 SP/sprint (PLA-FRUKI01-002) |
| Taxa de contenção de defeitos | 100% | 100% | Meta: >95% |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — registro de medição consolidado dos dois pacotes |
