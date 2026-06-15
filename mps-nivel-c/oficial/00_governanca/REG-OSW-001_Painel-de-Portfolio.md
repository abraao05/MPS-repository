# Painel de Portfólio de Projetos — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | REG-OSW-001 — Painel de Portfólio de Projetos |
| **Versão** | 1.0 |
| **Data** | 13/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Responsável** | COO (Operações) — escritório de portfólio de projetos |
| **Processo MPS-SW** | OSW (evidência organizacional — OSW 8, OSW 9, OSW 10) |
| **Classificação** | Registro organizacional de governança |

---

## 1. Objetivo

Registrar, de forma consolidada e auditável, a situação do **portfólio de projetos** da Timeware no período de referência: os projetos em andamento e concluídos, sua priorização, a alocação dos recursos compartilhados e o acompanhamento dos compromissos assumidos.

Este painel materializa, para fins de avaliação, a gestão de portfólio definida em **PRO-OSW-002**. A operação corrente (quadro de capacity e situação dos projetos) é mantida no Jira e no Confluence, conforme PRO-OSW-002 §4.1; este documento é o recorte consolidado (snapshot) dessa operação.

---

## 2. Período e fonte de dados

| Item | Descrição |
|---|---|
| Período de referência | Abr/2025 – Jun/2026 (ciclo de implantação MPS-SW Nível C) |
| Data do snapshot | 13/06/2026 |
| Fontes | Jira (situação dos projetos e quadro de capacity), Confluence (atas de priorização e de análise crítica), registros de projeto (04_registros) |
| Responsável pela consolidação | COO (Operações), com apoio do Time de Melhoria Contínua |

---

## 3. Portfólio — situação consolidada (snapshot)

| Projeto | Cliente | Natureza | Período | Situação | Registros de origem |
|---|---|---|---|---|---|
| Cadastro de Clientes | Profarma S.A. / Rede D1000 | Desenvolvimento de software (modernização de cadastro) | Abr/2025 – Jan/2026 | ✅ Concluído (aceite final) | 04_registros/PROFARMA_Cadastro-de-Clientes |
| SuperApp Força de Vendas — Pacote 1 (Metas e RV) | Fruki | Desenvolvimento mobile (React Native) | Jun/2025 – Set/2025 | ✅ Concluído (piloto + aceite) | 04_registros/FTFRUKI_SuperApp-Forca-de-Vendas |
| SuperApp Força de Vendas — Pacote Final 24 | Fruki | Desenvolvimento mobile (React Native) | Out/2025 – Jan/2026 | ✅ Concluído (aceite 15/01/2026) | 04_registros/FTFRUKI_SuperApp-Forca-de-Vendas |
| Fundação Tecnológica — Governança de APIs (OS-001 e OS-002) | GASMIG | Configuração cloud (Azure API Management) | Abr/2026 – Jun/2026 | ✅ Concluído (OS-002 encerrada 09/06/2026) | 04_registros/FTGASMIG_Governanca-APIs |
| WorkerAndamentos — Captura de Andamentos Processuais | AASP | Desenvolvimento back-end / worker | ~9 meses (em curso) | 🟡 Em execução (encerramento previsto 30/06/2026) | 04_registros/AASP_CNJ |

> Os projetos acima compõem o portfólio do ciclo. Demais oportunidades em prospecção são qualificadas pela área comercial e só entram no portfólio após aprovação da priorização (§4).

---

## 4. Priorização aplicada (OSW 8)

A priorização das oportunidades e dos projetos é conduzida pelo **COO (Operações)**, conforme os critérios de PRO-OSW-002 §3:

- **alinhamento com os objetivos de negócio** (crescer com qualidade e previsibilidade);
- **compromissos contratuais e prazos** com clientes;
- **disponibilidade de recursos**, especialmente os compartilhados (Tech Lead, Arquiteto, Product Owner);
- **retorno e relevância estratégica.**

No período de referência, os projetos foram assumidos de forma escalonada, respeitando a capacidade real da organização: a entrada da Fundação Tecnológica GASMIG (abr/2026) ocorreu após a conclusão dos pacotes do SuperApp Fruki (jan/2026), evitando sobreposição dos recursos técnicos compartilhados. A decisão de assumir cada projeto e sua ordem de prioridade é registrada nas atas do escritório de portfólio (Confluence).

---

## 5. Recursos, capacidade e autoridade (OSW 9)

### 5.1. Quadro de capacity

A alocação dos recursos compartilhados (Tech Lead, Arquiteto, Product Owner) entre os projetos é registrada no **quadro de capacity** mantido no Jira, conforme a estrutura e a cadência definidas em PRO-OSW-002 §4.1 (campos: colaborador, projeto, alocação %, período, status; revisão antes de cada sprint).

No período de referência, os projetos ativos operaram com **equipes dedicadas por projeto**, com acúmulo de papéis registrado em cada adaptação (ADAP-*). Não houve acionamento do critério de escalada de PRO-OSW-002 §4.1 (recurso compartilhado acima de 100% de alocação por duas sprints consecutivas); portanto, não foi necessária reunião de repriorização por conflito de recursos no período.

### 5.2. Autoridade

A autoridade para priorizar o portfólio e decidir a alocação de recursos compartilhados é do **COO (Operações)**, responsável pelo escritório de portfólio de projetos (PRO-OSW-002 §4.2). Decisões de natureza estratégica são reportadas ao CEO.

---

## 6. Riscos organizacionais de portfólio

Os riscos de natureza organizacional associados ao portfólio — concorrência de recursos entre projetos e dependência de pessoas-chave — são geridos conforme a **Estratégia de Gerência de Riscos e Oportunidades (EST-GPC-002)** e acompanhados pela direção e pelo Time de Melhoria Contínua (PRO-OSW-001 §5). Riscos de maior exposição são levados à análise crítica pela direção.

---

## 7. Acompanhamento do portfólio e tratamento de desvios (OSW 10)

Os projetos do portfólio são acompanhados de forma consolidada quanto ao cumprimento dos compromissos (prazo, escopo, recursos), apoiados pela situação no Jira e pelo quadro de capacity (PRO-OSW-002 §5).

| Projeto | Compromissos | Situação no acompanhamento |
|---|---|---|
| Cadastro de Clientes (Rede D1000) | Prazo/escopo do contrato | Concluído com aceite formal; desvios de prazo originados por dependências externas do cliente (ambiente AKS, GMUD) foram registrados e tratados no projeto |
| SuperApp Fruki (Pacote 1 e Final) | Entregas incrementais por módulo | Concluído; entregas validadas por piloto e aceite final |
| Fundação Tecnológica GASMIG | Entrega por marco (OS-001 e OS-002) | Concluído; OS-002 encerrada em 09/06/2026 |
| WorkerAndamentos (AASP) | Entrega por fase/onda | Em execução; acompanhamento por horas e fases; encerramento previsto 30/06/2026 |

Desvios identificados no acompanhamento são tratados por realocação de recursos, repriorização ou ações específicas no projeto, conforme PRO-OSW-002 §5.

---

## 8. Análise crítica pela direção

A situação do portfólio é insumo da **análise crítica trimestral dos processos**, conduzida pelo COO e reportada ao CEO (PRO-OSW-001 §7). As decisões e os encaminhamentos da análise crítica são registrados em ata mantida no Confluence e acompanhados pelo Time de Melhoria Contínua.

---

## 9. Rastreabilidade com o modelo MR-MPS-SW:2024

| Resultado | Como este documento atende |
|---|---|
| OSW 8 — oportunidades de negócio/investimentos priorizados (portfólio) | §3 (portfólio consolidado) e §4 (priorização aplicada) |
| OSW 9 — recursos, orçamento e autoridade do portfólio estabelecidos | §5 (capacity, recursos compartilhados e autoridade) |
| OSW 10 — projetos do portfólio mantidos e tratados conforme os acordos | §7 (acompanhamento e tratamento de desvios) |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 13/06/2026 | Time de Melhoria Contínua | Versão inicial — consolidação (snapshot) do portfólio do ciclo MPS-SW Nível C, materializando a evidência de OSW 8, 9 e 10 mantida no Jira/Confluence |
