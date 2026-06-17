# Registro de Garantia da Qualidade — SuperApp Fruki · Força de Vendas

| Campo | Valor |
|---|---|
| **Documento** | GQA-FRUKI01-001 — Registro de Garantia da Qualidade |
| **Versão** | 1.3 |
| **Data** | 17/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | SuperApp Fruki — Força de Vendas (Pacote 1 + Pacote Final 24) |
| **Auditor** | COO (Operações) |

---

## 1. Objetivo

Registrar as auditorias de qualidade realizadas ao longo do projeto SuperApp Fruki, verificando a aderência ao processo definido e a conformidade dos artefatos produzidos com os padrões estabelecidos pelo MPS-SW Nível C.

---

## 2. Auditoria de aderência ao processo

### 2.1 Pacote 1 — Módulo Metas e Remuneração Variável

**Data da auditoria:** 05/06/2026
**Auditado por:** COO (Operações)
**Período auditado:** 05/06/2025 – Set/2025

| Item verificado | Conforme? | Observação |
|---|---|---|
| Termo de abertura elaborado antes do início das atividades | ✅ Sim | TAP-FRUKI01-001 v1.1 — abertura em 05/06/2025; ata de kickoff registrada em ATA-FRUKI01-001 |
| Requisitos documentados e rastreáveis antes do desenvolvimento | ✅ Sim | REQ-FRUKI01-001 v1.1 — levantamento em 25/06/2025; ata ATA-FRUKI01-002 |
| Registro de adaptação do processo formalizado | ✅ Sim | ADAP-FRUKI01-001 v1.1 — adaptações justificadas; ITP e GDE referenciados |
| Plano de projeto documentado e aprovado pelo cliente | ✅ Sim | PLA-FRUKI01-001 v1.1 — aprovado em 05/06/2025; ref. ATA-FRUKI01-001 |
| Design técnico e de UX documentado antes da construção | ✅ Sim | PCP-FRUKI01-001 v1.0 — protótipos validados por Cecília antes das sprints |
| Estratégia de integração documentada | ✅ Sim | ITP-FRUKI01-001 v1.0 — 4 APIs REST Fruki; estratégia incremental |
| Plano de V&V definido e executado | ✅ Sim | VV-FRUKI01-001 v1.0 — cenários Gherkin executados; piloto 05/08/2025 (ATA-FRUKI01-007) |
| Rastreabilidade mantida entre requisitos, design e verificação | ✅ Sim | RASTR-FRUKI01-001 v1.0 — cobertura total RF-01 a RF-04 |
| Revisão por pares realizada antes do merge | ✅ Sim | PR revisada e aprovada por Jardel Dargas Silva (Fruki) antes do merge na branch `main` |
| Análise de decisão registrada para decisões arquiteturais relevantes | ✅ Sim | GDE-FRUKI01-001 v1.0 — Decisão 1: normalização de dados no front-end (impacta Pacote 1) |
| Acompanhamento do projeto registrado | ✅ Sim | RAC-FRUKI01-002 v1.0 — relatório de encerramento do Pacote 1 (Set/2025) |
| Papéis e responsabilidades seguidos conforme planejado | ✅ Sim | GP: Abraão Oliveira; UX/analista: Brenda Chrystie; devs: Luca Watson e Thiago Gomes; GQA: COO (Operações) |
| Encerramento formal realizado com aceite do cliente | ✅ Sim | TAE-FRUKI01-001 v1.0 + aceite de Leandro Lottermann (Set/2025) |

**Resultado Pacote 1:** Sem não conformidades.

---

### 2.2 Pacote Final 24 — Pedidos Não Alocados · Regra de Ouro · PDV

**Data da auditoria:** 05/06/2026
**Auditado por:** COO (Operações)
**Período auditado:** 09/10/2025 – 15/01/2026

| Item verificado | Conforme? | Observação |
|---|---|---|
| Termo de abertura elaborado antes do início das atividades | ✅ Sim | TAP-FRUKI01-002 v1.1 — abertura em 09/10/2025; ata de kickoff registrada em ATA-FRUKI01-008 |
| Ata de kickoff registrada | ✅ Sim | ATA-FRUKI01-008 v1.0 — kickoff e aprovação do plano em 09/10/2025 |
| Requisitos documentados e rastreáveis antes do desenvolvimento | ✅ Sim | REQ-FRUKI01-002 v1.0 — 10 RF e 5 RNF levantados antes de cada sprint |
| Registro de adaptação do processo formalizado | ✅ Sim | ADAP-FRUKI01-002 v1.1 — ITP-002 e GDE-001 referenciados |
| Plano de projeto documentado e aprovado pelo cliente | ✅ Sim | PLA-FRUKI01-002 v1.0 — aprovado em 09/10/2025; ref. ATA-FRUKI01-008 |
| Design técnico e de UX documentado antes da construção | ✅ Sim | PCP-FRUKI01-002 v1.0 — protótipos por módulo validados antes de cada sprint |
| Estratégia de integração documentada | ✅ Sim | ITP-FRUKI01-002 v1.0 — 3 módulos × APIs; estratégia de mock para API atrasada |
| Plano de V&V definido e executado | ✅ Sim | VV-FRUKI01-002 v1.0 — cenários Gherkin por sprint; aceite final 15/01/2026 |
| Rastreabilidade mantida entre requisitos, design e verificação | ✅ Sim | RASTR-FRUKI01-002 v1.0 — cobertura total RF-05 a RF-14 |
| Revisão por pares realizada antes do merge | ✅ Sim | PRs revisadas e aprovadas por Jardel: PR #57 (25/10/2025), PR Regra de Ouro (Nov/2025), PR PDV (Jan/2026) |
| Análise de decisão registrada para decisões arquiteturais relevantes | ✅ Sim | GDE-FRUKI01-001 — Decisão 2: renomeação "Caixa Preta" → "Regra de Ouro" |
| Mudança de escopo formalizada via change request | ✅ Sim | CR-FRUKI01-001 v1.0 — inclusão do Módulo Regra de Ouro aprovada em 09/10/2025 |
| Gerência de configuração aplicada (ICs, baselines, mudanças) | ✅ Sim | GCO-FRUKI01-001 v1.3 — 5 branches, 5 baselines (BL-01 a BL-05), 3 mudanças (CM-01 a CM-03) |
| Acompanhamento do projeto registrado | ✅ Sim | RAC-FRUKI01-001 v1.0 — relatório parcial de 27/12/2025 (Sprints 1 e 2 concluídas; Sprint 3 em andamento) |
| Ata de aceite final elaborada | ✅ Sim | ATA-FRUKI01-003 v1.0 — reunião Teams 15/01/2026 |
| Encerramento formal realizado com aceite do cliente | ✅ Sim | TAE-FRUKI01-002 v1.1 — aceite de Leandro Lottermann e Cecília Ribeiro (15/01/2026) |

**Resultado Pacote Final 24:** Sem não conformidades.

---

## 3. Revisão dos artefatos produzidos

### 3.1 Pacote 1

| Artefato | Versão | Padrão esperado | Conforme? | Observação |
|---|---|---|---|---|
| TAP-FRUKI01-001 | v1.1 | Cabeçalho completo, escopo, stakeholders, cronograma, ref. de abertura | ✅ Sim | |
| ATA-FRUKI01-001 | v1.0 | Participantes, pauta, decisões, ações de follow-up | ✅ Sim | Kickoff do Pacote 1 — 05/06/2025 |
| ATA-FRUKI01-002 | v1.0 | Participantes, pauta, decisões, ações de follow-up | ✅ Sim | Levantamento de requisitos — 25/06/2025 |
| ATA-FRUKI01-007 | v1.0 | Registro do piloto, defeitos identificados e resoluções | ✅ Sim | Piloto com vendedores — 05/08/2025 |
| PLA-FRUKI01-001 | v1.3 | Planejamento detalhado, estimativas, orçamento de horas, riscos, recursos, marcos, aprovação | ✅ Sim | Aprovação via ATA-FRUKI01-001 |
| REQ-FRUKI01-001 | v1.1 | Requisitos numerados, rastreáveis, com critério de aceite, validação documentada | ✅ Sim | |
| ADAP-FRUKI01-001 | v1.1 | Adaptações justificadas, pontos de controle marcados, ITP e GDE referenciados | ✅ Sim | |
| PCP-FRUKI01-001 | v1.0 | Arquitetura documentada, design UX validado, decisões técnicas | ✅ Sim | |
| ITP-FRUKI01-001 | v1.0 | Componentes, interfaces, estratégia, ambientes, critérios de prontidão | ✅ Sim | |
| VV-FRUKI01-001 | v1.0 | Plano de V&V com cenários Gherkin e resultados de execução | ✅ Sim | |
| RASTR-FRUKI01-001 | v1.0 | Cobertura total dos RFs em artefatos e verificações | ✅ Sim | |
| GDE-FRUKI01-001 | v1.0 | Decisão registrada com alternativas, critérios e justificativa | ✅ Sim | Decisão 1 impacta o Pacote 1 |
| RAC-FRUKI01-002 | v1.0 | Status, realizado, esforço, riscos, ações corretivas, melhorias | ✅ Sim | Relatório de encerramento — Set/2025 |
| LI-FRUKI01-001 | v1.0 | Lições positivas, negativas e oportunidades de melhoria | ✅ Sim | Abrange Pacote 1 e Pacote Final 24 |
| MED-FRUKI01-001 | v1.0 | Indicadores medidos por pacote; estimado vs. realizado | ✅ Sim | M1–M6 por pacote |
| TAE-FRUKI01-001 | v1.0 | Entregas, escopo realizado, aceite do cliente, lições aprendidas | ✅ Sim | |

### 3.2 Pacote Final 24

| Artefato | Versão | Padrão esperado | Conforme? | Observação |
|---|---|---|---|---|
| TAP-FRUKI01-002 | v1.1 | Cabeçalho completo, escopo, stakeholders, cronograma, ref. de abertura | ✅ Sim | |
| ATA-FRUKI01-008 | v1.0 | Participantes, pauta, decisões (kickoff + aprovação do plano + CR-001) | ✅ Sim | Kickoff Pacote Final 24 — 09/10/2025 |
| ATA-FRUKI01-004 | v1.0 | Validação de sprint, cenários, resultado | ✅ Sim | Sprint 1 — Pedidos Não Alocados — 24/10/2025 |
| ATA-FRUKI01-005 | v1.0 | Validação de sprint, cenários, resultado | ✅ Sim | Sprint 2 — Regra de Ouro — 28/11/2025 |
| ATA-FRUKI01-006 | v1.0 | Validação de sprint, cenários, resultado, AAB v2.0 | ✅ Sim | Sprint 3 — PDV — 14/01/2026 |
| ATA-FRUKI01-003 | v1.0 | Ata de aceite com decisões e ressalvas | ✅ Sim | Aceite final — 15/01/2026 |
| PLA-FRUKI01-002 | v1.2 | Planejamento detalhado, estimativas, orçamento de horas, riscos, recursos, marcos, aprovação | ✅ Sim | Aprovação via ATA-FRUKI01-008 |
| REQ-FRUKI01-002 | v1.0 | Requisitos numerados, rastreáveis, com critério de aceite, validação documentada | ✅ Sim | |
| ADAP-FRUKI01-002 | v1.1 | Adaptações justificadas, pontos de controle marcados, ITP e GDE referenciados | ✅ Sim | |
| PCP-FRUKI01-002 | v1.0 | Arquitetura documentada, design UX validado por módulo, decisões técnicas | ✅ Sim | |
| ITP-FRUKI01-002 | v1.0 | Componentes, interfaces, estratégia, mock strategy, ambientes | ✅ Sim | |
| VV-FRUKI01-002 | v1.0 | Plano de V&V por módulo com cenários Gherkin e resultados | ✅ Sim | |
| RASTR-FRUKI01-002 | v1.0 | Cobertura total dos RFs em artefatos e verificações | ✅ Sim | |
| GDE-FRUKI01-001 | v1.0 | Decisão registrada com alternativas, critérios e justificativa | ✅ Sim | Decisão 2 impacta o Pacote Final 24 |
| CR-FRUKI01-001 | v1.0 | Descrição da mudança, análise de impacto, aprovação, rastreabilidade | ✅ Sim | Inclusão do Módulo Regra de Ouro |
| GCO-FRUKI01-001 | v1.3 | ICs, branches, baselines, controle de mudanças, auditoria de configuração | ✅ Sim | |
| RAC-FRUKI01-001 | v1.0 | Status parcial, esforço, riscos, ações corretivas | ✅ Sim | Snapshot de 27/12/2025 |
| TAE-FRUKI01-002 | v1.1 | Entregas, escopo realizado (com ref. ao CR-001), aceite do cliente, lições aprendidas | ✅ Sim | |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 01/09/2025 | COO (Operações) | Auditoria de encerramento do Pacote 1 |
| 1.1 | 05/06/2026 | COO (Operações) | Inclusão da auditoria de encerramento do Pacote Final 24 |
| 1.2 | 05/06/2026 | COO (Operações) | Novos itens de auditoria: ITP, GCO, CR, RAC, ata de kickoff do Pacote Final 24; versões corrigidas (ADAP-001/002 v1.1, TAP-002 v1.1, TAE-002 v1.1); novos artefatos adicionados às tabelas §3.1 e §3.2 (ITP-001/002, GCO-001, CR-001, RAC-001/002, ATA-004 a 008, LI-001, MED-001) |
| 1.3 | 17/06/2026 | COO (Operações) | Versões dos PLAs atualizadas nas tabelas §3.1 e §3.2: PLA-001 v1.3 e PLA-002 v1.2 (adição do orçamento de horas em cada plano) |
