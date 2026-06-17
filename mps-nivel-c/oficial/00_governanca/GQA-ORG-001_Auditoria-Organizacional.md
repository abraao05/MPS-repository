# Auditoria de Garantia da Qualidade Organizacional — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | GQA-ORG-001 — Auditoria de GQA Organizacional |
| **Versão** | 1.2 |
| **Data** | 13/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Auditor** | COO (Operações) |
| **Aprovação** | Time de Melhoria Contínua |
| **Responsável** | Caroline Jenifer |
| **Processo MPS-SW** | GPC (evidência organizacional — GPC 3, GPC 6, GPC 7); cobre também a verificação organizacional de AQU e OSW |

---

## 1. Objetivo

Registrar a auditoria organizacional de garantia da qualidade realizada ao final do ciclo de implantação MPS-SW Nível C, verificando a aderência dos processos organizacionais (ativos de processo, medição, gerência de processos, capacitação, gerência de configuração) em relação às definições estabelecidas.

Esta auditoria corresponde ao `CHK-Auditoria Organizacional` previsto em EST-GPC-001 §9 e verifica os processos de apoio organizacional — complementar às auditorias de projeto (GQA-PROFARMA01-001, GQA-GASMIG02-001).

---

## 2. Escopo e período

| Item | Descrição |
|---|---|
| Período auditado | Jan/2026 – Jun/2026 |
| Processos auditados | GPC (Gerência de Processos), MED (Medição), GCO organizacional, CAP (Capacitação), GDE (Gerência de Decisões), AQU (Aquisição), OSW (Gerência Organizacional de Software) |
| Data da auditoria | 11/06/2026 |
| Auditor | COO (Operações) — independente das equipes que produziram os ativos |

---

## 3. Verificação por área de processo

### 3.1 Gerência de Processos (GPC)

| # | Item verificado | Resultado | Referência | Observação |
|---|---|---|---|---|
| 1 | Inventário de ativos de processo definido e atualizado | ✅ Conforme | PLA-GPC-001 §2 v1.6 | Inventário completo com todos os processos, planos, guias e templates |
| 2 | Processo-padrão organizacional documentado (PRO-GPC-001) | ✅ Conforme | PRO-GPC-001 v2.3 | Inclui entradas/saídas (§3) e rastreabilidade GPC 1–12 (§11) |
| 3 | Estratégia de GQA documentada | ✅ Conforme | EST-GPC-001 v1.3 | Cobre verificação por marcos e por amostragem; escalonamento definido |
| 4 | Registro de oportunidades de melhoria mantido | ✅ Conforme | REG-GPC-001 v1.0 | 11 OMs registradas com origem, prioridade, status e responsável |
| 5 | Melhorias priorizadas e planejadas | ✅ Conforme | REG-GPC-001 §4 | OM-06 implementada; 7 planejadas; 2 em análise |
| 6 | Ambientes-padrão de trabalho estabelecidos | ✅ Conforme | PLA-GPC-001 §3 | Jira, Azure DevOps, Pipelines, Test Plans, Confluence |
| 7 | Processos implantados nas equipes e acompanhados | ✅ Conforme | GQA-PROFARMA01-001; GQA-GASMIG02-001 | Verificação nos 3 projetos do ciclo |
| 8 | Efetividade de melhoria avaliada | ✅ Conforme | REG-GPC-001 §6; LI-GASMIG02-001 §5 | OM-06 (checklist pré-engajamento) avaliada e confirmada efetiva na OS-002 |

**Resultado GPC:** Conforme — 8/8 itens.

### 3.2 Medição (MED)

| # | Item verificado | Resultado | Referência | Observação |
|---|---|---|---|---|
| 1 | Objetivos de medição derivados dos objetivos de negócio | ✅ Conforme | PLA-MED-001 §2 | OM1–OM4 rastreados ao objetivo de crescimento com qualidade |
| 2 | Catálogo de medidas com definições operacionais | ✅ Conforme | PLA-MED-001 §3 | M1–M7 com fórmula, fonte e frequência definidos |
| 3 | Procedimentos de coleta e armazenamento executados | ✅ Conforme | MED-PROFARMA01-001; MED-GASMIG02-001 | Medidas coletadas em todos os projetos do ciclo |
| 4 | Análise organizacional das medidas realizada | ✅ Conforme | REG-MED-001 §4 | Análise comparativa PROFARMA + GASMIG com identificação de tendências |
| 5 | Ações corretivas para desvios registradas | ✅ Conforme | MED-PROFARMA01-001 §6; MED-GASMIG02-001 §6 | Ações documentadas para SPI e desvio de estimativa de alertas |
| 6 | Resultados comunicados aos interessados | ✅ Conforme | MED-PROFARMA01-001 §7; MED-GASMIG02-001 §7; REG-MED-001 §5 | Comunicação quinzenal (RAC), por encerramento e consolidação organizacional |
| 7 | Repositório de medidas avaliado (qualidade das medidas) | ✅ Conforme | REG-MED-001; PLA-MED-001 §8 | Verificação de integridade e consistência documentada |

**Resultado MED:** Conforme — 7/7 itens.

### 3.3 Gerência de Configuração — camada organizacional (GCO)

| # | Item verificado | Resultado | Referência | Observação |
|---|---|---|---|---|
| 1 | Plano de GCO organizacional documentado | ✅ Conforme | PLA-GCO-001 | Define estratégia de controle, ICs, baselines e auditoria |
| 2 | GCO verificada nos projetos do ciclo | ✅ Conforme | GQA-PROFARMA01-001 §3; GQA-GASMIG02-001 §2 | Itens GCO-1 a GCO-3 auditados em todos os projetos |
| 3 | Template de GQA atualizado com itens de GCO | ✅ Conforme | TPL-GPC-001 v1.1 | GCO-1 a GCO-3 adicionados como itens padrão |

**Resultado GCO (org):** Conforme — 3/3 itens.

### 3.4 Capacitação (CAP)

| # | Item verificado | Resultado | Referência | Observação |
|---|---|---|---|---|
| 1 | Plano de capacitação documentado | ✅ Conforme | PLA-CAP-001 | Define necessidades, ações e cronograma |
| 2 | Registro de capacitação mantido | ✅ Conforme | REG-CAP-001 (Confluence) | Competências mapeadas por colaborador |
| 3 | Mapa de capacidade dos processos disponível | ✅ Conforme | MAPA-CAP-001 | Relaciona papéis a competências exigidas e adquiridas |

**Resultado CAP:** Conforme — 3/3 itens.

### 3.5 Gerência de Decisões (GDE)

| # | Item verificado | Resultado | Referência | Observação |
|---|---|---|---|---|
| 1 | Processo de gerência de decisões documentado | ✅ Conforme | PRO-GDE-001 | Define critérios de ativação e registro de análise de decisão |
| 2 | Registros de análise de decisão produzidos quando aplicável | ✅ Conforme | GDE-PROFARMA01-001 | Decisões arquiteturais do projeto PROFARMA registradas |

**Resultado GDE:** Conforme — 2/2 itens.

### 3.6 Aquisição (AQU)

| # | Item verificado | Resultado | Referência | Observação |
|---|---|---|---|---|
| 1 | Processo de aquisição documentado (critérios de seleção, acordo, monitoramento e revisão técnica) | ✅ Conforme | PRO-AQU-001 (§3–6); rastreabilidade AQU 1–4 (§9) | Processo definido e disponível na biblioteca organizacional |
| 2 | Aplicabilidade da aquisição avaliada e registrada nos projetos do ciclo | ✅ Conforme | ADAP-PROFARMA01-001 §5; ADAP-GASMIG02-001/002 §2; ADAP-FRUKI01-001/002 §2; ADAP-AASPCNJ01-001 §2 | Nenhum projeto do ciclo subcontratou terceiro responsável por entrega; AQU registrado como **não aplicável**, com justificativa, em todas as adaptações |

**Resultado AQU:** Conforme — 2/2 itens. Não houve aquisição no ciclo; a não aplicabilidade está documentada e justificada em todos os projetos (PRO-AQU-001 §2).

### 3.7 Gerência Organizacional de Software (OSW)

| # | Item verificado | Resultado | Referência | Observação |
|---|---|---|---|---|
| 1 | Diretrizes organizacionais de processos definidas e patrocinadas pela alta direção | ✅ Conforme | POL-ORG-001; PRO-OSW-001 §1–2 | Diretrizes alinhadas ao objetivo de crescer com qualidade e previsibilidade |
| 2 | Governança organizacional documentada (recursos, autoridade/competências, riscos, medidas) | ✅ Conforme | PRO-OSW-001 §3–6; MAPA-ORG-001; EST-GPC-002; REG-MED-001 | Recursos garantidos, RACI definido e medidas organizacionais em uso |
| 3 | Análise crítica dos processos pela direção conduzida | ✅ Conforme | PRO-OSW-001 §7 (ata no Confluence) | Cadência trimestral, conduzida pelo COO com reporte ao CEO |
| 4 | Gestão de portfólio documentada e operada | ✅ Conforme | PRO-OSW-002; REG-OSW-001 | Portfólio do ciclo priorizado, com capacity acompanhado e sem conflito de recurso compartilhado no período |

**Resultado OSW:** Conforme — 4/4 itens.

---

## 4. Resumo por área de processo

| Área | Itens auditados | Conformes | % Aderência | Resultado |
|---|---|---|---|---|
| GPC | 8 | 8 | 100% | Conforme |
| MED | 7 | 7 | 100% | Conforme |
| GCO (org) | 3 | 3 | 100% | Conforme |
| CAP | 3 | 3 | 100% | Conforme |
| GDE | 2 | 2 | 100% | Conforme |
| AQU | 2 | 2 | 100% | Conforme |
| OSW | 4 | 4 | 100% | Conforme |
| **Total** | **29** | **29** | **100%** | **Conforme** |

---

## 5. Achados e oportunidades de melhoria

Nenhuma não conformidade identificada nesta auditoria organizacional.

Oportunidades de melhoria observadas (encaminhadas ao ciclo de GPC):
- REG-MED-001 deve ser atualizado trimestralmente; periodicidade formal a ser incluída no PLA-MED-001 na próxima revisão (OM candidata).
- Publicação dos ativos de processo no Confluence (CP-vii) pendente de ação manual pela equipe.

---

## 6. Parecer final

A organização Timeware demonstra aderência plena aos processos organizacionais auditados neste ciclo (GPC, MED, GCO, CAP, GDE, AQU e OSW). Os ativos de processo estão documentados, os indicadores foram coletados e analisados, as melhorias foram identificadas e registradas, e as capacitações estão mapeadas. O processo de Aquisição (AQU) está definido e teve sua não aplicabilidade justificada e registrada nos projetos do ciclo; a governança organizacional e a gestão de portfólio (OSW) estão documentadas e operantes, com evidência consolidada no Painel de Portfólio (REG-OSW-001). O ciclo de melhoria contínua está operante, com pelo menos uma melhoria implementada (OM-06) e efetividade verificada.

---

## Rastreabilidade com o modelo MR-MPS-SW:2024

| Resultado | Como este documento atende |
|---|---|
| GPC 3 — estratégia de GQA executada por função independente | §2: auditor = COO (independente das equipes de processo); §3: verificação realizada |
| GPC 6 — aderência dos processos verificada | §3.1–3.7: aderência verificada em GPC, MED, GCO, CAP, GDE, AQU e OSW |
| GPC 7 — produtos de trabalho organizacionais verificados | §3.1–3.7: produtos de trabalho auditados em todas as áreas |

Esta auditoria fornece também a **verificação objetiva (GQA) dos processos organizacionais AQU e OSW** — atendendo aos critérios iv e v do atributo de processo no nível organizacional (CP_Organizacional) para esses dois processos, antes cobertos apenas pelas definições de processo.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.2 | 15/06/2026 | Time de Melhoria Contínua | Campo "Responsável" adicionado ao cabeçalho: Caroline Jenifer |
| 1.0 | 11/06/2026 | COO (Operações) | Versão inicial — auditoria organizacional ao final do ciclo MPS-SW Nível C |
| 1.1 | 13/06/2026 | COO (Operações) | Escopo ampliado com a verificação organizacional de AQU (§3.6) e OSW (§3.7); resumo (§4), parecer (§6) e rastreabilidade atualizados; total de 23 para 29 itens auditados |
