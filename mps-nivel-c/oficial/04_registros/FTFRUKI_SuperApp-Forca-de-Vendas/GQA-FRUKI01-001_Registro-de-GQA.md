# Registro de Garantia da Qualidade — SuperApp Fruki · Força de Vendas

| Campo | Valor |
|---|---|
| **Documento** | GQA-FRUKI01-001 — Registro de Garantia da Qualidade |
| **Versão** | 1.1 |
| **Data** | 05/06/2026 |
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
| Termo de abertura elaborado antes do início das atividades | ✅ Sim | TAP-FRUKI01-001 v1.1 — abertura em 05/06/2025 |
| Requisitos documentados e rastreáveis antes do desenvolvimento | ✅ Sim | REQ-FRUKI01-001 v1.1 — levantamento em 25/06/2025 |
| Registro de adaptação do processo formalizado | ✅ Sim | ADAP-FRUKI01-001 v1.0 |
| Plano de projeto documentado e aprovado | ✅ Sim | PLA-FRUKI01-001 v1.1 — aprovado em 26/06/2025 |
| Design técnico e de UX documentado antes da construção | ✅ Sim | PCP-FRUKI01-001 v1.0 — protótipos validados por Cecília antes das sprints |
| Plano de V&V definido e executado | ✅ Sim | VV-FRUKI01-001 v1.0 — cenários executados; piloto 05/08/2025 |
| Rastreabilidade mantida entre requisitos, design e verificação | ✅ Sim | RASTR-FRUKI01-001 v1.0 — cobertura total RF-01 a RF-04 |
| Papéis e responsabilidades seguidos conforme planejado | ✅ Sim | GP: Abraão Oliveira; UX/analista: Brenda Chrystie; devs: Luca Watson e Thiago Gomes |
| Revisão técnica de código realizada antes do merge | ✅ Sim | PR revisada e aprovada por Jardel Dargas Silva (Fruki) |
| Encerramento formal realizado com aceite do cliente | ✅ Sim | TAE-FRUKI01-001 + aceite de Leandro Lottermann (Set/2025) |

**Resultado Pacote 1:** Sem não conformidades.

---

### 2.2 Pacote Final 24 — Pedidos Não Alocados · Regra de Ouro · PDV

**Data da auditoria:** 05/06/2026
**Auditado por:** COO (Operações)
**Período auditado:** 09/10/2025 – 15/01/2026

| Item verificado | Conforme? | Observação |
|---|---|---|
| Termo de abertura elaborado antes do início das atividades | ✅ Sim | TAP-FRUKI01-002 v1.0 — abertura em 09/10/2025 |
| Requisitos documentados e rastreáveis antes do desenvolvimento | ✅ Sim | REQ-FRUKI01-002 v1.0 — 10 RF e 5 RNF levantados antes de cada sprint |
| Registro de adaptação do processo formalizado | ✅ Sim | ADAP-FRUKI01-002 v1.0 |
| Plano de projeto documentado e aprovado | ✅ Sim | PLA-FRUKI01-002 v1.0 — aprovado em 09/10/2025 |
| Design técnico e de UX documentado antes da construção | ✅ Sim | PCP-FRUKI01-002 v1.0 — protótipos por módulo validados antes de cada sprint |
| Plano de V&V definido e executado | ✅ Sim | VV-FRUKI01-002 v1.0 — cenários executados por sprint; aceite final 15/01/2026 |
| Rastreabilidade mantida entre requisitos, design e verificação | ✅ Sim | RASTR-FRUKI01-002 v1.0 — cobertura total RF-05 a RF-14 |
| Papéis e responsabilidades seguidos conforme planejado | ✅ Sim | Mesma equipe do Pacote 1; Alexsandro de Vargas Braga incluído para PDV |
| Revisão técnica de código realizada antes do merge | ✅ Sim | PRs revisadas e aprovadas por Jardel (PR #57 em 25/10/2025; demais em Nov/2025 e Jan/2026) |
| Registro de análise de decisão para decisões arquiteturais relevantes | ✅ Sim | GDE-FRUKI01-001 — normalização front-end e renomeação Regra de Ouro |
| Ata de aceite final elaborada | ✅ Sim | ATA-FRUKI01-003 — reunião Teams 15/01/2026 |
| Encerramento formal realizado com aceite do cliente | ✅ Sim | TAE-FRUKI01-002 + aceite de Leandro Lottermann e Cecília Ribeiro (15/01/2026) |

**Resultado Pacote Final 24:** Sem não conformidades.

---

## 3. Revisão dos artefatos produzidos

### 3.1 Pacote 1

| Artefato | Padrão esperado | Conforme? | Observação |
|---|---|---|---|
| TAP-FRUKI01-001 | Cabeçalho completo, escopo, stakeholders, cronograma, ref. de abertura | ✅ Sim | v1.1 |
| PLA-FRUKI01-001 | Planejamento detalhado, estimativas, riscos, recursos, marcos, aprovação | ✅ Sim | v1.1 |
| REQ-FRUKI01-001 | Requisitos numerados, rastreáveis, com critério de aceite, validação documentada | ✅ Sim | v1.1 |
| ADAP-FRUKI01-001 | Adaptações justificadas e pontos de controle marcados | ✅ Sim | v1.0 |
| ATA-FRUKI01-001 | Participantes, pauta, decisões, ações de follow-up | ✅ Sim | v1.0 (kickoff) |
| ATA-FRUKI01-002 | Participantes, pauta, decisões, ações de follow-up | ✅ Sim | v1.0 (levantamento metas) |
| PCP-FRUKI01-001 | Arquitetura documentada, design UX validado, decisões técnicas | ✅ Sim | v1.0 |
| VV-FRUKI01-001 | Plano de V&V com cenários Gherkin e resultados de execução | ✅ Sim | v1.0 |
| RASTR-FRUKI01-001 | Cobertura total dos RFs em artefatos e verificações | ✅ Sim | v1.0 |
| TAE-FRUKI01-001 | Entregas, escopo realizado, aceite do cliente, lições aprendidas | ✅ Sim | v1.0 |

### 3.2 Pacote Final 24

| Artefato | Padrão esperado | Conforme? | Observação |
|---|---|---|---|
| TAP-FRUKI01-002 | Cabeçalho completo, escopo, stakeholders, cronograma, ref. de abertura | ✅ Sim | v1.0 |
| PLA-FRUKI01-002 | Planejamento detalhado, estimativas, riscos, recursos, marcos, aprovação | ✅ Sim | v1.0 |
| REQ-FRUKI01-002 | Requisitos numerados, rastreáveis, com critério de aceite, validação documentada | ✅ Sim | v1.0 |
| ADAP-FRUKI01-002 | Adaptações justificadas e pontos de controle marcados | ✅ Sim | v1.0 |
| PCP-FRUKI01-002 | Arquitetura documentada, design UX validado por módulo, decisões técnicas | ✅ Sim | v1.0 |
| VV-FRUKI01-002 | Plano de V&V por módulo com cenários Gherkin e resultados | ✅ Sim | v1.0 |
| RASTR-FRUKI01-002 | Cobertura total dos RFs em artefatos e verificações | ✅ Sim | v1.0 |
| GDE-FRUKI01-001 | Decisão registrada com alternativas, critérios e justificativa | ✅ Sim | v1.0 |
| ATA-FRUKI01-003 | Ata de aceite com decisões e ressalvas | ✅ Sim | v1.0 |
| TAE-FRUKI01-002 | Entregas, escopo realizado, aceite do cliente, lições aprendidas | ✅ Sim | v1.0 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | COO (Operações) | Auditoria de encerramento do Pacote 1 |
| 1.1 | 05/06/2026 | COO (Operações) | Inclusão da auditoria de encerramento do Pacote Final 24 |
