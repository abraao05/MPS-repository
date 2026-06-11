# Repositório Organizacional de Medidas — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | REG-MED-001 — Repositório Organizacional de Medidas |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Responsável** | Time de Melhoria Contínua |
| **Processo MPS-SW** | MED (evidência organizacional — MED 3, MED 4, MED 5, MED 6) |

---

## 1. Objetivo

Consolidar as medidas coletadas nos projetos do ciclo MPS-SW Nível C, permitindo análise comparativa do desempenho organizacional, identificação de desvios e tendências, e tomada de decisão pela direção. Este documento é o **repositório organizacional de medidas** previsto em PLA-MED-001 §4.1.

---

## 2. Escopo

Projetos incluídos nesta consolidação:

| Projeto | Período | Sprints / OSs |
|---|---|---|
| PROFARMA — Cadastro de Clientes · Rede D1000 | Abr/2025 – Jan/2026 | 19 sprints |
| GASMIG — Fundação Tecnológica · Governança de APIs (OS-001) | Abr/2026 – Mai/2026 | 1 OS (15 dias) |
| GASMIG — Fundação Tecnológica · Governança de APIs (OS-002) | Mai/2026 – Jun/2026 | 1 OS (14 dias) |

---

## 3. Consolidação das medidas por projeto

### 3.1 M1 — Aderência ao prazo

| Projeto / OS | Resultado | Meta Org. | Status | Observação |
|---|---|---|---|---|
| PROFARMA (projeto completo) | SPI 0,91 (desvio acumulado de 4 meses vs. plano original) | ≥ 0,90 | ⚠ Atenção | Desvio totalmente explicado por 12 CRs formais aprovados e bloqueios de infraestrutura externos; prazo revisado cumprido |
| GASMIG OS-001 | 100% — entregue em 15 dias conforme planejado | ≥ 90% | ✅ |  |
| GASMIG OS-002 | 100% — entregue em 14 dias (1 dia antes do planejado) | ≥ 90% | ✅ |  |

### 3.2 M2 — Desvio de esforço estimado × realizado

| Projeto / OS | Resultado | Meta Org. | Status | Observação |
|---|---|---|---|---|
| PROFARMA | Desvio de esforço absorvido pelos CRs; escopo expandido de 5 para 7 integrações | ≤ 10% | ⚠ Atenção | Desvio de prazo, não de produtividade — SP entregues dentro do SPI |
| GASMIG OS-001 | 0% — 84 SP planejados = 84 SP entregues | ≤ 10% | ✅ |  |
| GASMIG OS-002 | 0% — 78 SP planejados = 78 SP entregues | ≤ 10% | ✅ |  |

### 3.3 M3 — Velocity

| Projeto / OS | Resultado | Meta Org. | Status |
|---|---|---|---|
| PROFARMA | ~30 SP/sprint (pico: 42 SP no Sprint 16) | Referência interna | ✅ |
| GASMIG OS-001 | ≈ 5,6 SP/dia (equipe de 2 engenheiros) | Referência interna | ✅ |
| GASMIG OS-002 | ≈ 5,6 SP/dia (equipe de 2 engenheiros) | Referência interna | ✅ |

### 3.4 M4 — Itens entregues × planejados

| Projeto / OS | Resultado | Meta Org. | Status |
|---|---|---|---|
| PROFARMA | 564/573 SP = 98,4% (−9 SP, −1,6%) | ≥ 90% | ✅ |
| GASMIG OS-001 | 84/84 = 100% | ≥ 90% | ✅ |
| GASMIG OS-002 | 78/78 = 100% | ≥ 90% | ✅ |

### 3.5 M5 — Densidade de defeitos

| Projeto / OS | Resultado | Meta Org. | Status | Observação |
|---|---|---|---|---|
| PROFARMA | 14 defeitos em homologação (0 S1, 2 S2, 7 S3 + outros); 0 defeitos S1 em produção | ≤ 5% dos itens | ✅ | 100% dos defeitos resolvidos antes do aceite |
| GASMIG OS-001 | 0 não conformidades na verificação técnica | ≤ 5% | ✅ |  |
| GASMIG OS-002 | 0 não conformidades na verificação técnica | ≤ 5% | ✅ |  |

### 3.6 M6 — Defeitos escapados para produção

| Projeto / OS | Resultado | Meta Org. | Status |
|---|---|---|---|
| PROFARMA | 0 incidentes S1 no piloto loja 9 | 0 | ✅ |
| GASMIG OS-001 | 0 incidentes pós-aceite | 0 | ✅ |
| GASMIG OS-002 | 0 incidentes pós-aceite | 0 | ✅ |

### 3.7 M7 — Retrabalho

| Projeto / OS | Resultado | Meta Org. | Status | Observação |
|---|---|---|---|---|
| PROFARMA | NC-01 e NC-02 (Sprints 1–3): documentação retroativa; resolvidas em 30/06/2025 | ≤ 10% itens reabertos | ✅ | Retrabalho de formalização, não de desenvolvimento |
| GASMIG OS-001 | 0 | ≤ 10% | ✅ |  |
| GASMIG OS-002 | 0 | ≤ 10% | ✅ |  |

---

## 4. Análise organizacional consolidada

### 4.1 Tendências e aprendizados

| Dimensão | Análise |
|---|---|
| **Previsibilidade de prazo** | O desvio de SPI do PROFARMA (0,91) é atípico e explicado por fatores externos (CRs e bloqueios de infraestrutura). Os projetos GASMIG demonstram que, sob escopo estável, a Timeware executa com SPI = 1,0. Tendência organizacional: boa previsibilidade em projetos de escopo estável; fragilidade em projetos com integrações a sistemas legados externos. |
| **Qualidade do produto** | 0 defeitos escapados para produção em todos os projetos do ciclo. Alta densidade de detecção em homologação (PROFARMA: 14 defeitos detectados antes da produção). Padrão de qualidade consistente. |
| **Velocity** | GASMIG OS-001 e OS-002 produziram velocity idêntica (5,6 SP/dia), confirmando estabilidade do processo. Dado referencial estabelecido para projetos Azure de configuração. PROFARMA: ~30 SP/sprint — referência para projetos de desenvolvimento backend. |
| **Gerência de configuração** | Zero inconsistências de GCO em todos os projetos do ciclo. Modelo de controle via Git Flow + Azure DevOps mostrou-se eficaz. |

### 4.2 Desvios tratados e ações corretivas

| Projeto | Desvio | Ação | Resultado |
|---|---|---|---|
| PROFARMA | SPI 0,91 — desvio de 4 meses vs. plano original | Revisão formal do cronograma com absorção dos 12 CRs; novo prazo comunicado e aceito pela Profarma S.A. | Projeto encerrado dentro do prazo revisado |
| PROFARMA | Fase 5 bloqueada por AKS indisponível (+2,5 meses) | Escalação formal à infraestrutura da Rede D1000 | AKS disponibilizado; homologação concluída |
| GASMIG | Esforço de alertas Azure subestimado ~20% (OS-001) | Adoção de thresholds de mercado na OS-002; OM-07 registrada para evolução da base de estimativas | OS-002 sem desvio de esforço |

---

## 5. Comunicação dos resultados

| Data | Canal | Destinatários | Conteúdo |
|---|---|---|---|
| Quinzenal (Sprints 1–19 PROFARMA) | RAC publicado no Confluence | COO, Gerente de Projeto, cliente | Indicadores de sprint (velocity, defeitos, aderência ao prazo) |
| 07/05/2026 | TAE-GASMIG02-001 + LI | COO, Time de Melhoria Contínua | Encerramento OS-001: todos os indicadores M1–M9 atingidos |
| 09/06/2026 | TAE-GASMIG02-002 + LI | COO, Time de Melhoria Contínua | Encerramento OS-002: todos os indicadores M1–M9 atingidos |
| 11/06/2026 | Este documento (REG-MED-001) — Confluence | COO, Time de Melhoria Contínua, Founder e CEO | Consolidação organizacional do ciclo MPS-SW Nível C |

---

## 6. Rastreabilidade com o modelo MR-MPS-SW:2024

Este documento evidencia:

| Resultado | Como este documento atende |
|---|---|
| MED 3 — procedimentos de coleta e armazenamento executados | §3: dados coletados de MED-PROFARMA01-001 e MED-GASMIG02-001, conforme PLA-MED-001 §4.1 |
| MED 4 — análise das medidas realizada e resultados usados | §4: análise de tendências, desvios e aprendizados organizacionais |
| MED 5 — coleta e análise realizadas; ações corretivas | §4.2: desvios tratados e ações tomadas com evidências |
| MED 6 — resultados comunicados aos interessados | §5: tabela de comunicações com datas, canais e destinatários |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Versão inicial — consolidação organizacional das medidas do ciclo MPS-SW Nível C (PROFARMA + GASMIG) |
