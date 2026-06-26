# Registro de Capacitação da Equipe — Cadastro de Clientes · Rede D1000

| Campo | Valor |
|---|---|
| **Documento** | CAP-PROFARMA01-001 — Registro de Capacitação da Equipe |
| **Projeto** | Cadastro de Clientes — Rede D1000 |
| **Código do projeto** | PROFARMA01 |
| **Cliente** | Profarma S.A. / Rede D1000 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Aprovação** | Abraão Oliveira |
| **Processo MPS-SW** | CAP (evidência de projeto) |

---

## 1. Objetivo

Registrar a composição da equipe alocada ao projeto Cadastro de Clientes — Rede D1000, as competências exigidas por papel, as trilhas de capacitação conduzidas e as evidências de competência demonstradas ao longo do desenvolvimento (Sprints 1–19), em aderência ao processo de Capacitação (CAP) do MR-MPS-SW:2024 Nível C.

## 2. Equipe alocada

| Membro (papel) | Dedicação | Sprints |
|---|---|---|
| Abraão Oliveira — Gerente de Projeto (gestão; não codifica) | Parcial | 1–19 |
| Cézar Hiraki Velázquez — Tech Lead / DevOps / Arquiteto (revisor de PR) | Integral | 1–19 |
| Mateus Veloso — Dev Backend | Integral | 1–19 |
| Raony Chagas — Dev Backend | Integral | 1–19 |
| Lucas Batista — Dev Backend | Parcial (50%) | 13–19 |
| Caroline Sousa — QA / Automação | Parcial (40%) | 15–19 |
| Jonathan Barbosa — GQA independente (auditoria de processo; não codifica) | Pontual | Auditorias |

> A função de **QA** (Caroline — execução de testes e automação) é distinta da função de **GQA** (Jonathan Barbosa — auditoria independente de processo). O GP (Abraão) e a GQA (Jonathan) atuam fora do fluxo de codificação.

## 3. Competências exigidas por papel

| Papel | Competências técnicas exigidas |
|---|---|
| Gerente de Projeto (Abraão Oliveira) | Gestão de projeto e MPS-SW Nível C (GPR, REQ, PCP, ITP, VV, GCO, MED, GDE, CAP, GQA/GPC); gestão de escopo e aprovação de change requests (CR); planejamento e medição por sprint; comunicação formal com o cliente |
| Tech Lead / DevOps / Arquiteto (Cézar Hiraki Velázquez) | Clean Architecture em .NET 8 (Domain/Application/Infrastructure/API); PostgreSQL no Azure (Flexible Server); Azure Kubernetes Service (AKS) e Docker; pipelines Azure DevOps (build, testes, análise estática); observabilidade (Datadog APM, Prometheus/Grafana); Azure Key Vault; e **aprovação de PR** como revisor (Tech Lead) |
| Dev Backend (Mateus Veloso, Raony Chagas) | .NET 8 / C#; EF Core (escrita) e Dapper (leitura) — padrão CQRS light; Outbox pattern com worker de polling (integração ITEC); Azure Service Bus com worker dedicado (Propz CRM); integrações REST (VTEX, Call Center, PBM, BlueSoft, CloseUp); autenticação API Key + OAuth 2.0; validação de CPF e deduplicação |
| Dev Backend (Lucas Batista) | .NET 8 / C# backend; correções e PRs finais; apoio às integrações e ao worker de anonimização LGPD |
| QA / Automação (Caroline Sousa) | Testes unitários xUnit (273 cenários); análise de cobertura (≥ 80%; resultado 84%); apoio à execução dos cenários de homologação; testes de regressão e de performance |
| GQA independente (Jonathan Barbosa) | Processo de GQA/GPC e MPS-SW; condução de auditoria independente de processo por fase; verificação de não conformidades e ações corretivas; aderência ao processo-padrão Timeware (não codifica e não executa testes) |

## 4. Trilhas de capacitação

| Trilha / sessão | Público | Conteúdo |
|---|---|---|
| Trilha Backend — .NET 8 / Clean Architecture | Mateus Veloso, Raony Chagas, Lucas Batista | Camadas Domain/Application/Infrastructure/API; CPF como chave primária (VARCHAR(11)); validação de dígitos verificadores; auditoria e LGPD (inativação lógica e worker de expurgo) |
| Trilha de Dados — PostgreSQL / CQRS light | Mateus Veloso, Raony Chagas | Azure Database for PostgreSQL Flexible Server; EF Core (escrita) + Dapper (leitura SQL parametrizado); índices para o SLA p95 ≤ 200 ms; migrations e baseline de schema |
| Trilha de Integração Assíncrona | Mateus Veloso, Raony Chagas | Outbox pattern com worker de polling e backoff exponencial (ITEC, at-least-once); Azure Service Bus com worker dedicado e dead-letter (Propz CRM); contratos REST (VTEX, Call Center, PBM, BlueSoft, CloseUp) |
| Trilha Arquitetura e DevOps — Azure | Cézar Hiraki Velázquez | Arquitetura cloud-native (AKS, Service Bus, Key Vault); pipelines Azure DevOps (build + xUnit + análise estática + publicação Docker); Git Flow (`feature/* → develop → release/* → main`); baselines/tags (`YY.MM.N.PATCH`); observabilidade Datadog/Prometheus; revisão e aprovação de PR |
| Trilha QA / V&V | Caroline Sousa | Testes unitários xUnit, cobertura ≥ 80%, cenários de homologação (PDV, Balcão, OMNI, Call Center, Propz), testes de performance (500 req/s) e de regressão |
| Trilha de Processo — MPS-SW Nível C | Toda a equipe | GPR, REQ, PCP, ITP, VV, GCO, MED, GDE, CAP e GQA(GPC); política de revisão de código (1 revisor padrão / 2 para mudanças críticas), segregação de aprovação, rastreabilidade e medição por sprint |

## 5. Integração e disseminação de conhecimento

A entrada de novos integrantes ao longo do projeto foi apoiada por transferência de contexto: **Lucas Batista** integrou-se ao squad no Sprint 13 (apoio ao desenvolvimento e PRs finais) e **Caroline Sousa** no Sprint 15 (QA/automação e homologação). A disseminação contínua de conhecimento foi sustentada pelas práticas abaixo.

| Prática | Descrição |
|---|---|
| Revisão de código (code review) | Revisão de Merge Requests com aprovação do Tech Lead (Cézar) e segregação autor≠revisor — garante ciência das mudanças pela equipe |
| Cerimônias de sprint | Planning, daily (11h30 Teams), review e retrospectiva por sprint, com decisões técnicas compartilhadas e registradas (ATAs) |
| Documentação técnica | Documentação de API (Swagger/OpenAPI gerada automaticamente), documento de design (PCP), registro de decisões de arquitetura (GDE-001 a GDE-005) e migrations de banco |
| Auditorias de GQA | Auditorias independentes de processo por fase (GQA-P01 Sprint 5, GQA-P02 homologação, GQA-P03 encerramento), conduzidas por Jonathan Barbosa — reforçando a aderência ao processo |

## 6. Evidências de competência

| Membro | Evidência de competência demonstrada |
|---|---|
| Cézar Hiraki Velázquez | Arquitetura Clean Architecture .NET 8 aprovada (REV-001); decisões GDE-001 a GDE-004; pipelines CI/CD e baselines `25.12.1.1`/`26.1.1.1`; aprovação de PRs como revisor |
| Mateus Veloso | Endpoints core e integrações entregues; Outbox ITEC e worker Propz; consolidação do histórico de tickets de defeitos |
| Raony Chagas | Integrações (VTEX, Call Center, BlueSoft, CloseUp) e PRs finais (correções de teste no fechamento) |
| Lucas Batista | Worker de anonimização LGPD e PRs de apoio nas fases finais |
| Caroline Sousa | 273 testes unitários (84% de cobertura) e apoio aos cenários de homologação sem defeitos S1 no aceite |
| Jonathan Barbosa | 3 auditorias de processo concluídas (2 não conformidades menores identificadas e resolvidas); parecer final de conformidade |
| Abraão Oliveira | Gestão dos 19 sprints; aprovação dos 12 change requests; comunicação formal e aceite do cliente (29/01/2026) |

## 7. Parecer

A equipe demonstrou as competências exigidas para os papéis ao longo do projeto, com capacitação técnica aderente ao stack (.NET 8, PostgreSQL/Azure, integrações assíncronas) e ao processo MPS-SW Nível C. As competências foram evidenciadas pelos artefatos de projeto (PCP, GDE, REV, REL-VV) e pelas entregas concluídas, sem lacunas de capacitação que tenham comprometido o cronograma ou a qualidade.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — reconstituída consolidando a composição da equipe, as competências por papel, as trilhas de capacitação e as evidências de competência do projeto |
