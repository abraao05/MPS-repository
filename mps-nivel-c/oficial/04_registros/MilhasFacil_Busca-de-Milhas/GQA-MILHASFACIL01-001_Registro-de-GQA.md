# Registro de Garantia da Qualidade — MilhasFacil · Busca de Milhas

| Campo | Valor |
|---|---|
| **Documento** | GQA-MILHASFACIL01-001 |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Código do projeto** | MILHASFACIL01 |
| **Cliente** | Hub de Milhas |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
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
| Apoio de arquitetura, infraestrutura e pipeline | Cézar Velazquez (Tech Lead / Arquiteto / DevOps; aprovador de PR) |

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
| Rastreabilidade história → branch → PR → build | Conforme | Convenção `feat/fix + MF-XX` aplicada (RNF04) |
| Pipeline CI executando testes a cada push | Conforme | Pipelines API/Web/Crawler com PowerShell@2, agente Windows |
| Cobertura de testes ≥ 80% (RNF02) | Não conforme (NC-001) | JaCoCo 74% na S2; abaixo da meta de 80% |
| Política de branch com PR obrigatório e aprovação do revisor de PR | Conforme | PR obrigatório para `develop`; aprovação do Tech Lead (Cézar Velazquez) exigida; escopo/CR aprovado pelo GP (Abraão) |
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
| Rastreabilidade história → branch → PR → build | Conforme | Matriz RF → Jira → branch → PR → build mantida |
| Política de branch com PR obrigatório e aprovação do revisor de PR | Conforme | PR obrigatório para `develop`; aprovação do Tech Lead (Cézar Velazquez) exigida |
| Gestão de defeitos registrada e classificada | Conforme | Bugs registrados no Jira (ex.: MF-58, MF-59 tratados na S8) |
| Mudança de escopo formalizada antes da implementação | Conforme | CR-MF-001 (28/05/2026) aprovado por Abraão (GP) antes da execução |
| Plano de V&V executado com casos de teste aprovados (validação manual da QA) | Conforme | CT-01 a CT-10 validados manualmente pela QA (Jonathan Alves), com evidências geradas, até a S8 |
| Baselines de configuração estabelecidas por sprint | Conforme | Tags v0.1.0 (S1) a v0.8.0 (S8) registradas |

> **Observação de auditoria de configuração (ressalva com ação corretiva aplicada):** na auditoria dos itens de configuração no Azure DevOps (15/06/2026), constatou-se que, dos 29 PRs existentes nos três repositórios (`MilhasFacil_api`, `MilhasFacil_web`, `MilhasFacil_crawler`), **os 22 PRs históricos dos Sprints S1–S8** (API #1–#10, Web #13–#20, Crawler #23–#26) **estão sem revisor registrado na API** do Azure DevOps. A ausência decorre da inicialização retroativa do histórico (datas de PR/build concentradas em 13–15/06/2026); por se tratar de PRs já concluídos, o registro é imutável e **permanece como ressalva** com causa-raiz identificada. **Ação corretiva aplicada em 15/06/2026:** (a) ativada **branch policy** exigindo ao menos um revisor para `develop` nos três repositórios, impedindo recorrência; (b) os **6 PRs da Sprint S9** (API #11/#12/#28, Web #21/#22, Crawler #27) foram concluídos e mergeados em `develop` **com revisor Mateus Veloso — Approved (vote 10)**; e (c) o **PR #29 (MF-73)**, que padroniza a nomenclatura de banco de dados (migration V10 — padronização de índices e coluna `is_active`), está **ativo, aprovado pelo Tech Lead Cézar Velazquez na conta própria dele no Azure DevOps (vote 10)**, aguardando merge. O conjunto evidencia o saneamento prospectivo da governança e o cumprimento da meta "PRs sem revisor = 0". A constatação não constitui afirmação de revisão onde a evidência não existe. (Equivalência de identidade: a aprovação de PR sob a conta `Mateus Veloso` no Azure DevOps corresponde ao Tech Lead / aprovador de PR **Cézar Velazquez** no time atual.)

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
| RF13 — Filtros avançados (maxMiles / cabinType) | Conforme | **Entregue — liberado em `main` na release v0.9.0** via PRs #11 / #21 / #27 (revisor Mateus Veloso = Cézar Velazquez — Approved); Jira MF-65 = Concluído; CT-11 Aprovado (validação manual da QA — Jonathan Alves) |
| RF14 — Export CSV UTF-8 BOM | Conforme | **Entregue — liberado em `main` na release v0.9.0** via PRs #12 / #22 (revisor Mateus Veloso = Cézar Velazquez — Approved); Jira MF-69 = Concluído |
| MF-64 — Busca de aeroportos por ILIKE | Conforme | **Entregue — liberado em `main` na release v0.9.0** via PR #28 (revisor Mateus Veloso = Cézar Velazquez — Approved); Jira MF-64 = Concluído; CT-12 Aprovado (validação manual da QA — Jonathan Alves) |
| Revisor obrigatório nos PRs da S9 | Conforme | 6 PRs da S9 mergeados em `develop` com revisor Mateus Veloso (= Cézar Velazquez, Tech Lead) — Approved (vote 10); branch policy de revisor ativa em `develop` (3 repositórios) |
| Casos de teste da S9 com validação manual e build verde | Conforme | CT-11 (filtros maxMiles + cabinType) e CT-12 (airport ILIKE, `q=gru` → GRU Guarulhos) validados manualmente pela QA (Jonathan Alves), com evidências geradas; build verde |
| Padronização de nomenclatura de BD (MF-73) | Conforme | PR #29 (MF-73, migration V10) aprovado pelo Cézar Velazquez (conta própria, vote 10), aguardando merge |

Os itens RF13, RF14 e MF-64 foram entregues e liberados em `main` na release v0.9.0 (15/06/2026, tag v0.9.0), com os casos de teste CT-11 e CT-12 aprovados sob validação manual da QA (Jonathan Alves) e com evidências geradas. Os cards Jira MF-64, MF-65 e MF-69 estão **Concluído**. A padronização de nomenclatura de banco de dados (MF-73, migration V10) segue em revisão no PR #29.

### Evidências referenciadas

| Código | O que capturar | Fonte/URL |
|---|---|---|
| IMG-JIRA-01 | Board 614 com sprints S1–S9 e MF-64/MF-65/MF-69 = Concluído | Jira — board 614 |
| IMG-CI-01 | Execução do gate de cobertura JaCoCo ≥ 80% na pipeline da API | Azure DevOps — Pipeline "MilhasFacil API - Pipeline" |
| IMG-DEVOPS-01 | Lista de PRs (29) dos três repositórios com situação de revisor (28 concluídos + 1 ativo) | Azure DevOps — Repos MilhasFacil_api/web/crawler |
| IMG-DEVOPS-02 | 6 PRs da S9 concluídos com Mateus Veloso — Approved (vote 10), branch policy de revisor ativa em `develop` e PR #29 (MF-73) em revisão | Azure DevOps — Repos MilhasFacil_api/web/crawler |

---

## 4. Resumo das não conformidades

| ID | Sprint/Fase | Categoria | Severidade | Status |
|---|---|---|---|---|
| NC-001 | S2–S4 (aberta na S2) | Cobertura de testes < 80% (RNF02) | Menor | Encerrada (S5 — 19/04/2026, JaCoCo 82%) |

Total de não conformidades identificadas: **1**
Total encerradas: **1**
Total em aberto: **0**

> Ressalva de auditoria de configuração registrada na GQA-A02 (22 PRs históricos S1–S8 concluídos sem revisor na API): não classificada como não conformidade de processo de desenvolvimento. A ressalva **permanece** (PRs concluídos são imutáveis), porém com **ação corretiva aplicada em 15/06/2026**: ativação de branch policy de revisor obrigatório em `develop` nos três repositórios, conclusão dos 6 PRs da S9 com revisor Mateus Veloso (= Cézar Velazquez — Approved) e PR #29 (MF-73) em revisão padronizando a nomenclatura de banco de dados — cumprindo a meta "PRs sem revisor = 0" de forma prospectiva.

---

## 5. Parecer final de GQA

O projeto MilhasFacil — Busca de Milhas atendeu aos requisitos do processo-padrão Timeware ao longo dos ciclos auditados pela GQA independente. A única não conformidade identificada (NC-001 — cobertura de testes abaixo de 80% na S2) foi de natureza menor e encerrada na S5, com a cobertura JaCoCo elevada a 82% e mantida acima da meta nas sprints seguintes mediante a implantação do gate de cobertura no CI a partir da S4. Considerando o ciclo S1–S4 (conforme com ressalva) e o ciclo S5–S8 (conforme, sem não conformidades), o **parecer consolidado dos Sprints S1–S8 é CONFORME**.

As atividades de V&V do projeto são conduzidas com **teste manual** pela QA, **Jonathan Alves**, que executa os casos de teste e gera as evidências correspondentes (o projeto não utiliza ferramenta de gestão de testes), apoiado pelos testes automatizados de build na pipeline. A auditoria desse processo é feita de forma **independente** pela GQA, **Carol (Caroline)**, distinguindo-se a execução dos testes (QA — Jonathan) da auditoria de processo (GQA — Carol). Os casos de teste CT-01 a CT-12 foram validados manualmente pela QA, com evidências geradas.

Quanto à auditoria de configuração, permanece registrada a ressalva de que os 22 PRs históricos dos Sprints S1–S8 estão sem revisor registrado na API do Azure DevOps, decorrente da inicialização retroativa do histórico — registros imutáveis por já estarem concluídos. A ressalva foi tratada com **ação corretiva já aplicada (15/06/2026)**: ativação de branch policy de revisor obrigatório em `develop` nos três repositórios, conclusão dos 6 PRs da Sprint S9 com revisor Mateus Veloso (= Cézar Velazquez, Tech Lead — Approved, vote 10) e PR #29 (MF-73) em revisão padronizando a nomenclatura de banco de dados, evidenciando o saneamento prospectivo da governança e o cumprimento da meta "PRs sem revisor = 0".

Na Sprint S9, os itens RF13, RF14 e MF-64 foram **entregues e liberados em `main` na release v0.9.0** (15/06/2026, tag v0.9.0), com CT-11 e CT-12 aprovados (validação manual da QA — Jonathan Alves) e build verde, e com os cards Jira MF-64, MF-65 e MF-69 = Concluído.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Emissão inicial — evidência do ciclo S1–S9 (MR-MPS-SW:2024 Nível C). |
