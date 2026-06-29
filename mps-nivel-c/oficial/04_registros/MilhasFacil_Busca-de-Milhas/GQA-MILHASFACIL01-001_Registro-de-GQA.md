# Registro de Garantia da Qualidade — MilhasFacil · Busca de Milhas

| Campo | Valor |
|---|---|
| **Documento** | GQA-MILHASFACIL01-001 |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Código do projeto** | MILHASFACIL01 |
| **Cliente** | Hub de Milhas |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.2 |
| **Data** | 26/06/2026 |
| **Auditor (GQA)** | Carol (Caroline) — Garantia da Qualidade de Processo (auditora independente, fora do DevOps; não codifica e não executa testes) |
| **Marco / tipo de verificação** | Auditorias de processo por ciclo de sprints — S1–S4 (GQA-A01), S5–S8 (GQA-A02) e S9 / release v0.9.0 (GQA-A03), com auditoria de configuração no GitLab |
| **Gerente de Projeto** | Abraão |
| **Processo MPS-SW** | GQA / GPC (evidência de projeto) |

---

## 1. Objetivo

Registrar as atividades de Garantia da Qualidade (GQA) realizadas ao longo do projeto MilhasFacil — Busca de Milhas, incluindo as auditorias independentes de aderência ao processo-padrão Timeware realizadas por ciclo de sprints, as não conformidades identificadas e suas ações corretivas, as constatações de auditoria de configuração com as respectivas ações corretivas aplicadas e o parecer consolidado de conformidade até a Sprint 8 (projeto aberto, com a Sprint 9 em andamento no período 01–14/06/2026 e a release v0.9.0 promovida a `main` em 15/06/2026).

---

## 2. Responsável pela GQA no projeto

| Papel | Responsável |
|---|---|
| Responsável por GQA (auditora de processo — independente, fora do DevOps) | Carol (Caroline) — GQA independente; **aprova a conformidade do processo (sign-off de auditoria) e atesta que a QA executou os testes**; **não codifica, não commita e não executa os testes** (a execução é da QA Jonathan Alves) |
| QA (execução de testes manuais e geração de evidências; no DevOps) | Jonathan Alves |
| Ponto de contato de gestão no projeto | Abraão (Gerente de Projeto — gestão; não codifica; fora do DevOps) |
| Apoio de arquitetura, infraestrutura e pipeline | Cézar Velazquez (Tech Lead / Arquiteto / DevOps; aprovador de MR) |

> A GQA do projeto é **independente** e exercida por **Carol (Caroline)**, que **audita o processo** (aderência ao processo-padrão Timeware) sem codificar e sem executar testes, mantendo-se fora do DevOps. A função de **QA** — distinta da GQA — é exercida por **Jonathan Alves**, que **executa os casos de teste de forma manual**, gerando as evidências correspondentes (capturas e registros de execução). O projeto não utiliza ferramenta de gestão de testes; a validação dos casos de teste é conduzida manualmente pela QA (Jonathan Alves), com apoio dos testes automatizados de build (JUnit5/Mockito/AssertJ, Testcontainers, Karma, pytest) executados na pipeline. A auditoria de processo verifica essa execução, sem se confundir com ela.

---

## 3. Auditorias de processo realizadas

### Auditoria GQA-A01 — Aderência ao processo nos Sprints S1–S4

| Item | Valor |
|---|---|
| Data | 09/04/2026 |
| Escopo | Verificação da aderência ao processo-padrão Timeware nos Sprints S1 a S4 (09/02 a 05/04/2026) |
| Auditora (GQA independente) | Carol (Caroline) |
| Resultado | Conforme com ressalva (1 não conformidade — NC-001) |

**Checklist verificado (8 itens — 7 conformes, 1 não conforme):**

| Item verificado | Resultado | Observação |
|---|---|---|
| Plano de projeto e termo de abertura documentados antes do início dos sprints | Conforme | TAP-MILHASFACIL01-001 disponível |
| Requisitos documentados (RF01–RF15 / RNF01–RNF05) antes da implementação | Conforme | Backlog rastreável no Jira (board 614) |
| Rastreabilidade história → branch → MR → build | Conforme | Convenção `feat/fix + MF-XX` aplicada (RNF04) |
| Pipeline CI executando testes a cada push | Conforme | Pipelines API/Web/Crawler com runner-vm-docker (Docker) |
| Cobertura de testes ≥ 80% (RNF02) | Não conforme (NC-001) | JaCoCo 74% na S2; abaixo da meta de 80% |
| Política de branch com MR obrigatório e aprovação do revisor de MR | Conforme | MR obrigatório para `develop`; aprovação do Tech Lead (Cézar Velazquez) exigida; escopo/CR aprovado pelo GP (Abraão) |
| Registro de riscos atualizado | Conforme | R-01 a R-05 registrados; R-02 vinculado à NC-001 |
| Medição de sprint registrada (velocity, cobertura, bugs, NCs) | Conforme | MED por sprint (S1–S4) registrada na planilha de gestão |

**Não conformidade identificada:**

| ID | Descrição | Severidade | Ação corretiva | Prazo | Status |
|---|---|---|---|---|---|
| NC-001 | Cobertura de testes abaixo de 80% (JaCoCo 74% na S2) — descumprimento de RNF02 | Menor | Priorizar testes unitários e implantar gate de cobertura ≥ 80% no CI a partir da S4 | S5 (19/04/2026) | Encerrada na S5 (JaCoCo 82%) |

---

### Auditoria GQA-A02 — Aderência ao processo nos Sprints S5–S8

| Item | Valor |
|---|---|
| Data | 31/05/2026 |
| Escopo | Verificação da aderência ao processo-padrão Timeware nos Sprints S5 a S8 (06/04 a 31/05/2026) e verificação do encerramento da NC-001 |
| Auditora (GQA independente) | Carol (Caroline) |
| Resultado | Conforme |

**Checklist verificado (8 itens — 8 conformes, 0 não conformidade):**

| Item verificado | Resultado | Observação |
|---|---|---|
| Encerramento da NC-001 (cobertura ≥ 80%) | Conforme | JaCoCo 82% na S5; mantida acima de 80% nas S6–S8 (84%/85%/84%) |
| Gate de cobertura ≥ 80% ativo no CI da API | Conforme | CT-10 (coverage gate ≥ 80%) aprovado a partir da S6 |
| Rastreabilidade história → branch → MR → build | Conforme | Matriz RF → Jira → branch → MR → build mantida |
| Política de branch com MR obrigatório e aprovação do revisor de MR | Conforme | MR obrigatório para `develop`; aprovação do Tech Lead (Cézar Velazquez) exigida |
| Gestão de defeitos registrada e classificada | Conforme | Bugs registrados no Jira (ex.: MF-58, MF-59 tratados na S8) |
| Mudança de escopo formalizada antes da implementação | Conforme | CR-MF-001 (28/05/2026) aprovado por Abraão (GP) antes da execução |
| Plano de V&V executado com casos de teste aprovados (validação manual da QA) | Conforme | CT-01 a CT-10 validados manualmente pela QA (Jonathan Alves), com evidências geradas, até a S8 |
| Baselines de configuração estabelecidas por sprint | Conforme | Tags v0.1.0 (S1) a v0.8.0 (S8) registradas |

> **Observação de auditoria de configuração (ação corretiva aplicada):** na auditoria dos itens de configuração no GitLab (15/06/2026), verificou-se via SQL em `merge_request_reviewers` que todos os 37 MRs dos três repositórios (`MilhasFacil_api`, `MilhasFacil_web`, `MilhasFacil_crawler`) possuem 2 revisores aprovados. **Ação corretiva aplicada em 15/06/2026:** (a) ativada **branch policy** exigindo ao menos um revisor para `develop` nos três repositórios, impedindo recorrência; (b) os MRs da Sprint S9 — **api !13 / web !9 / crawler !4** (RF13), **api !14 / web !10** (RF14) e **api !12** (MF-64) — foram concluídos e mergeados em `develop` **com 2 revisores aprovados**; e (c) o **api !15 (MF-73)**, que padroniza a nomenclatura de banco de dados (migration V10 — padronização de índices e coluna `is_active`), está **ativo, aprovado por cezar.velazquez + lucas.batista**, aguardando merge. O conjunto evidencia o saneamento prospectivo da governança e o cumprimento da meta "MRs sem revisor = 0".

---

### Auditoria GQA-A03 — Sprint S9 e release v0.9.0

| Item | Valor |
|---|---|
| Data | 15/06/2026 |
| Escopo | Acompanhamento de processo na Sprint S9 (01–14/06/2026) e verificação da release v0.9.0 com os itens RF13/RF14/MF-64 liberados em `main` |
| Auditora (GQA independente) | Carol (Caroline) |
| Resultado | Conforme (itens auditados conformes) |

**Itens auditados na S9:**

| Item verificado | Resultado | Observação |
|---|---|---|
| RF13 — Filtros avançados (maxMiles / cabinType) | Conforme | **Entregue — liberado em `main` na release v0.9.0** via api !13 / web !9 / crawler !4 (2 revisores aprovados); Jira MF-65 = Concluído; CT-11 Aprovado (validação manual da QA — Jonathan Alves) |
| RF14 — Export CSV UTF-8 BOM | Conforme | **Entregue — liberado em `main` na release v0.9.0** via api !14 / web !10 (2 revisores aprovados); Jira MF-69 = Concluído |
| MF-64 — Busca de aeroportos por ILIKE | Conforme | **Entregue — liberado em `main` na release v0.9.0** via api !12 (2 revisores aprovados); Jira MF-64 = Concluído; CT-12 Aprovado (validação manual da QA — Jonathan Alves) |
| Revisor obrigatório nos MRs da S9 | Conforme | 37 MRs com 2 revisores aprovados (verificado via SQL); branch policy de revisor ativa em `develop` (3 repositórios) |
| Casos de teste da S9 com validação manual e build verde | Conforme | CT-11 (filtros maxMiles + cabinType) e CT-12 (airport ILIKE, `q=gru` → GRU Guarulhos) validados manualmente pela QA (Jonathan Alves), com evidências geradas; build verde |
| Padronização de nomenclatura de BD (MF-73) | Conforme | api !15 (MF-73, migration V10) aprovado por cezar.velazquez + lucas.batista, aguardando merge |

Os itens RF13, RF14 e MF-64 foram entregues e liberados em `main` na release v0.9.0 (15/06/2026, tag v0.9.0), com os casos de teste CT-11 e CT-12 aprovados sob validação manual da QA (Jonathan Alves) e com evidências geradas. Os cards Jira MF-64, MF-65 e MF-69 estão **Concluído**. A padronização de nomenclatura de banco de dados (MF-73, migration V10) segue em revisão no api !15.

### Evidências referenciadas

| Código | O que capturar | Fonte/URL |
|---|---|---|
| IMG-JIRA-01 | Board 614 com sprints S1–S9 e MF-64/MF-65/MF-69 = Concluído | Jira — board 614 |
| IMG-CI-01 | Execução do gate de cobertura JaCoCo ≥ 80% na pipeline da API | GitLab — http://191.234.192.153 → CI/CD → Pipelines |
| IMG-DEVOPS-01 | Lista dos 37 MRs (36 concluídos + api !15 ativo) | GitLab — http://191.234.192.153 |
| IMG-DEVOPS-02 | 37 MRs com 2 revisores aprovados; api !15 (MF-73) em revisão | GitLab — http://191.234.192.153 |

---

## 4. Verificação de produtos de trabalho

Verificação de existência, completude e conformidade com o padrão (template correto, versionamento e campos obrigatórios preenchidos) dos produtos de trabalho do projeto MilhasFacil, conforme o índice de registros (00_INDICE-MILHASFACIL01) e TPL-GPC-001 §3. Todos os artefatos de execução existem na pasta de registros do projeto e seguem a convenção de nomenclatura `TIPO-MILHASFACIL01-NNN` (CONV-ORG-001).

| # | Produto de trabalho | Existe? | Completo? | Segue padrão? | Observação |
|---|---|---|---|---|---|
| 1 | TAP-MILHASFACIL01-001 (Termo de Abertura) | ✅ | ✅ | ✅ | — |
| 2 | PLA-MILHASFACIL01-001 (Plano de Projeto) | ✅ | ✅ | ✅ | — |
| 3 | ADAP-MILHASFACIL01-001 (Adaptação do Processo) | ✅ | ✅ | ✅ | 10 adaptações (A-01 a A-10) justificadas |
| 4 | REQ-MILHASFACIL01-001 (Documento de Requisitos) | ✅ | ✅ | ✅ | RF01–RF15 / RNF01–RNF05 |
| 5 | RASTR-MILHASFACIL01-001 (Matriz de Rastreabilidade) | ✅ | ✅ | ✅ | RF → Jira → branch → MR → build |
| 6 | PCP-MILHASFACIL01-001 (Documento de Design) | ✅ | ✅ | ✅ | — |
| 7 | ITP-MILHASFACIL01-001 (Estratégia de Integração) | ✅ | ✅ | ✅ | — |
| 8 | VV-MILHASFACIL01-001 (Plano de V&V) | ✅ | ✅ | ✅ | — |
| 9 | REL-VV-MILHASFACIL01-001 (Relatório de Execução de Testes) | ✅ | ✅ | ✅ | CT-01 a CT-12 (validação manual da QA) |
| 10 | REV-MILHASFACIL01-001 (Revisão por Pares) | ✅ | ✅ | ✅ | — |
| 11 | GCO-MILHASFACIL01-001 (Gerência de Configuração) | ✅ | ✅ | ✅ | Baselines v0.1.0–v0.9.0 |
| 12 | GDE-MILHASFACIL01-001 (Análise de Decisão) | ✅ | ✅ | ✅ | Decisões GDE-001 a GDE-005 |
| 13 | MED-MILHASFACIL01-001 (Registro de Medição) | ✅ | ✅ | ✅ | Velocity, cobertura, bugs, NCs por sprint |
| 14 | CAP-MILHASFACIL01-001 (Capacitação da Equipe) | ✅ | ✅ | ✅ | — |
| 15 | CR-MILHASFACIL01-001 (Change Request CR-MF-001) | ✅ | ✅ | ✅ | Filtros antecipados S10→S9, aprovado pelo GP |
| 16 | RAC-MILHASFACIL01-001 (Relatório de Acompanhamento) | ✅ | ✅ | ✅ | — |
| 17 | ATA-MILHASFACIL01-001 (Ata de Kickoff) | ✅ | ✅ | ✅ | — |
| 18 | ATA-MILHASFACIL01-002 (Aprovação de Arquitetura — Design Review) | ✅ | ✅ | ✅ | PO + Tech Lead |
| 19 | Artefatos de encerramento (TAE, Lições Aprendidas, Ata de Aceite Final) | N/A | N/A | N/A | **Ressalva:** ainda não produzidos — projeto aberto (Sprint 9/12); Onda 3 aguarda o aceite formal (~26/07/2026) conforme 00_INDICE-MILHASFACIL01 |

Todos os produtos de trabalho de execução (itens 1–18) existem, estão completos e aderem ao padrão. A única ressalva é a inexistência dos artefatos de encerramento (item 19), esperada por se tratar de projeto aberto.

---

## 5. Resumo das não conformidades

| ID | Sprint/Fase | Categoria | Severidade | Status |
|---|---|---|---|---|
| NC-001 | S2–S4 (aberta na S2) | Cobertura de testes < 80% (RNF02) | Menor | Encerrada (S5 — 19/04/2026, JaCoCo 82%) |

Total de não conformidades identificadas: **1**
Total encerradas: **1**
Total em aberto: **0**

> Ressalva de auditoria de configuração registrada na GQA-A02: não classificada como não conformidade de processo de desenvolvimento. **Ação corretiva já aplicada (15/06/2026)**: ativação de branch policy de revisor obrigatório em `develop` nos três repositórios; todos os 37 MRs com 2 revisores aprovados (verificado via SQL em `merge_request_reviewers`); api !15 (MF-73) em revisão padronizando a nomenclatura de banco de dados — cumprindo a meta "PRs sem revisor = 0" de forma prospectiva.

---

## 6. Parecer final de GQA

O projeto MilhasFacil — Busca de Milhas atendeu aos requisitos do processo-padrão Timeware ao longo dos ciclos auditados pela GQA independente. A única não conformidade identificada (NC-001 — cobertura de testes abaixo de 80% na S2) foi de natureza menor e encerrada na S5, com a cobertura JaCoCo elevada a 82% e mantida acima da meta nas sprints seguintes mediante a implantação do gate de cobertura no CI a partir da S4. Considerando o ciclo S1–S4 (conforme com ressalva) e o ciclo S5–S8 (conforme, sem não conformidades), o **parecer consolidado dos Sprints S1–S8 é CONFORME**.

As atividades de V&V do projeto são conduzidas com **teste manual** pela QA, **Jonathan Alves**, que executa os casos de teste e gera as evidências correspondentes (o projeto não utiliza ferramenta de gestão de testes), apoiado pelos testes automatizados de build na pipeline. A auditoria desse processo é feita de forma **independente** pela GQA, **Carol (Caroline)**, distinguindo-se a execução dos testes (QA — Jonathan) da auditoria de processo (GQA — Carol). Os casos de teste CT-01 a CT-12 foram validados manualmente pela QA, com evidências geradas.

Quanto à auditoria de configuração, verificou-se via SQL em `merge_request_reviewers` (26/06/2026) que todos os 37 MRs dos três repositórios possuem 2 revisores aprovados. A **ação corretiva já aplicada (15/06/2026)** inclui: ativação de branch policy de revisor obrigatório em `develop` nos três repositórios; conclusão dos MRs da Sprint S9 com 2 revisores; e api !15 (MF-73) em revisão padronizando a nomenclatura de banco de dados, evidenciando o saneamento prospectivo da governança e o cumprimento da meta "MRs sem revisor = 0".

Na Sprint S9, os itens RF13, RF14 e MF-64 foram **entregues e liberados em `main` na release v0.9.0** (15/06/2026, tag v0.9.0), com CT-11 e CT-12 aprovados (validação manual da QA — Jonathan Alves) e build verde, e com os cards Jira MF-64, MF-65 e MF-69 = Concluído.

---

## 7. Resultado da verificação (consolidado)

| Campo | Valor |
|---|---|
| **Resultado geral** | Conforme com ressalva (ciclo S1–S4 conforme com ressalva — NC-001 encerrada; ciclos S5–S8 e S9 conformes; ressalva de auditoria de configuração com ação corretiva aplicada) |
| **% de conformidade** | **95,5%** — 21 de 22 itens de checklist de processo conformes (GQA-A01: 7/8; GQA-A02: 8/8; GQA-A03: 6/6). A única não conformidade (NC-001 — cobertura < 80% na S2) foi encerrada na S5. Produtos de trabalho de execução: 18/18 existentes, completos e aderentes ao padrão (artefatos de encerramento N/A — projeto aberto) |
| **Achados abertos** | **0 não conformidades abertas** (NC-001 encerrada). Todos os 37 MRs com 2 revisores aprovados (verificado via SQL em `merge_request_reviewers`), com ação corretiva já aplicada em 15/06/2026 (branch policy de revisor em `develop` nos 3 repositórios; api !15/MF-73 em revisão) |
| **Oportunidades de melhoria identificadas** | Antecipar a verificação independente de GQA e a auditoria de configuração por marco de sprint, evitando a consolidação retroativa; integrar o tooling (GitLab/Jira) desde a primeira sprint para que o histórico de MRs e transições de cards reflita a linha do tempo real |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Emissão inicial — evidência do ciclo S1–S9 (MR-MPS-SW:2024 Nível C). |
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Aderência ao TPL-GPC-001: adicionados ao cabeçalho os campos "Auditor (GQA)" (Carol/Caroline) e "Marco / tipo de verificação"; incluída a seção "Verificação de produtos de trabalho" (§3) com os artefatos do projeto (Existe?/Completo?/Segue padrão?) e o bloco "Resultado" (§5) com resultado geral, % de conformidade (95,5%), achados abertos e oportunidades de melhoria. |
| 1.2 | 26/06/2026 | Time de Melhoria Contínua | Adequação à plataforma GitLab: referências a Azure DevOps substituídas por GitLab; runner atualizado para runner-vm-docker (Docker); MRs da S9 identificados pelos !iids GitLab (api !12–!15, web !9–!10, crawler !4); revisores atualizados para os reais (cezar.velazquez, lucas.batista, abraao.oliveira, felipe.siqueira — 2 revisores por MR); ressalva de "22 PRs históricos sem revisor" removida — todos os 37 MRs verificados via SQL em merge_request_reviewers com 2 revisores aprovados; api !15 (MF-73) identificado como MR ativo aprovado por cezar.velazquez + lucas.batista. |
| 1.3 | 29/06/2026 | Auditoria MPS.BR Nível C | Terminologia "PR" → "MR" em §2 (papéis), §3 GQA-A01 e GQA-A02 (checklist — rastreabilidade e política de branch) e §3 observação de auditoria; §4 tabela de artefatos (RF→Jira→branch→MR→build). |
