# Registro de Capacitação da Equipe — MilhasFacil · Busca de Milhas

| Campo | Valor |
|---|---|
| **Documento** | CAP-MILHASFACIL01-001 — Registro de Capacitação da Equipe |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Código do projeto** | MILHASFACIL01 |
| **Cliente** | Hub de Milhas |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Gerente de Projeto** | Abraão |
| **Aprovação** | Abraão |
| **Processo MPS-SW** | CAP (evidência de projeto) |

---

## 1. Objetivo

Registrar a composição da equipe alocada ao projeto MilhasFacil — Busca de Milhas, as competências exigidas por papel, as sessões e trilhas de capacitação conduzidas e as evidências de competência demonstradas ao longo do desenvolvimento (S1–S9), em aderência ao processo de Capacitação (CAP) do MR-MPS-SW:2024 Nível C.

## 2. Equipe alocada

| Membro (papel) | Período de atuação | Sprints |
|---|---|---|
| Abraão — Gerente de Projeto (gestão; não codifica; fora do DevOps) | Fev/2026 – Jul/2026 | Todas |
| Cézar Velazquez — Tech Lead / Arquiteto / DevOps (revisor de PR; no DevOps) | Fev/2026 – Jul/2026 | Todas |
| Felipe Santos — Dev Backend Principal (API + crawlers; no DevOps) | Fev/2026 – Jul/2026 | S1–S9 |
| Lucas Batista — Full Stack (S1 Angular; S2+ backend; no DevOps) | Fev/2026 – Jul/2026 | S1–S9 |
| Henry Oliveira — Full Stack (S3 Angular; S4+ backend; no DevOps) | Mar/2026 – Jul/2026 | S3–S9 |
| Jonathan Alves — QA (teste manual; gera evidências; no DevOps) | Fev/2026 – Jul/2026 | Todas |
| Carol (Caroline) — GQA independente (auditoria de processo; não codifica; fora do DevOps) | Fev/2026 – Jul/2026 | Todas |

> **DevOps (Azure) = 5 pessoas:** Cézar Velazquez (Tech Lead) + Felipe Santos / Lucas Batista / Henry Oliveira (devs) + Jonathan Alves (QA). **Abraão (GP) e Carol (GQA independente) ficam fora do DevOps.**
> Equivalência de identidade (time atual → Jira/Azure DevOps, contas legadas): Cézar Velazquez → aprovação de PR sob `Mateus Veloso` e commits de infra/arquitetura sob `Raony Chagas`/`Mateus Sousa`; Felipe Santos → `Felipe Siqueira`; Lucas Batista → `Lucas Batista de Sousa`; Henry Oliveira → `Henry Komatsu`. Abraão (`abraao.oliveira`) e Jonathan Alves (`jonathan@timeware.com.br`) já estão com contas no projeto. Carol (GQA independente) **não assina issues, não commita e não executa testes** — apenas aprova a conformidade e atesta que a QA testou; os 2 commits legados sob `Caroline Sousa` no git são incidentais da consolidação retroativa e **não representam a GQA**.

## 3. Competências exigidas por papel

| Papel | Competências técnicas exigidas |
|---|---|
| Gerente de Projeto (Abraão) | Gestão de projeto e MPS-SW Nível C (GPR, REQ, PCP, ITP, VV, GCO, MED, GDE, CAP, GQA/GPC), gestão de escopo e aprovação de change request (CR), planejamento e medição por sprint; não codifica e não atua no DevOps |
| Tech Lead / Arquiteto / DevOps (Cézar Velazquez) | Arquitetura de soluções (API + Web + Crawler), Spring Boot 3.2.5 / Java 21, Azure DevOps (Pipelines PowerShell@2/agente Windows, gate de cobertura no CI, Docker Compose, política de branch, baselines/tags) e **aprovação de PR** como revisor (Tech Lead) |
| Dev Backend Principal | Spring Boot 3.2.5 / Java 21, segurança JWT HS256 (access/refresh, jti), Redis (blacklist de token), JPA/Flyway, Python FastAPI 0.111 / SeleniumBase 4.27.4 e parsers (Smiles/Azul/Latam) |
| Full Stack | Spring Boot / JWT e JPA no backend; Angular 17.3 standalone, signals, Tailwind 3.4, interceptor JWT (refresh 401) no frontend |
| QA (Jonathan Alves) | **Execução de testes manuais com geração de evidências** (sem ferramenta de gestão de testes), V&V (JUnit5/Mockito/AssertJ, Testcontainers, Karma, pytest como apoio de build) e análise de cobertura JaCoCo/Karma/pytest |
| GQA independente (Carol) | Processo de GQA/GPC e MPS-SW, condução de **auditoria independente de processo** por ciclo, verificação de não conformidades e ações corretivas, e aderência ao processo-padrão Timeware (não codifica e não executa testes) |

## 4. Sessões e trilhas de capacitação

| Trilha / sessão | Público | Conteúdo |
|---|---|---|
| Trilha Backend — Spring Boot 3 / JWT | Felipe Santos, Lucas Batista, Henry Oliveira | Camadas controller/service, autenticação JWT HS256 (access 30 min / refresh 7 dias), JwtAuthenticationFilter, BCrypt e blacklist Redis (prefixo `token:invalidated:`) |
| Trilha Frontend — Angular 17 | Lucas Batista (S1), Henry Oliveira (S3) | Componentes standalone, signals + localStorage no AuthService, jwtInterceptor (401 → refresh → retry), ThemeService (dark mode) e componentes compartilhados (LoadingSpinner, EmptyState, Pagination) |
| Trilha Crawler — SeleniumBase / FastAPI | Felipe Santos | FastAPI 0.111, SeleniumBase 4.27.4, parsers BeautifulSoup (Smiles/Azul/Latam), DTO `SearchRequest` (max_miles, cabin_type) e CORS restrito à origem da API |
| Trilha Arquitetura e DevOps — Azure Pipelines | Cézar Velazquez | Arquitetura da solução (API/Web/Crawler), Pipelines API/Web/Crawler (PowerShell@2, agente Windows), triggers `develop`/`homolog`/`main`, gate JaCoCo 80% na API, baselines/tags por sprint e revisão/aprovação de PR |
| Trilha QA — Teste manual e V&V | Jonathan Alves | Execução manual dos casos de teste com geração de evidências, V&V apoiada por JUnit5/Mockito/AssertJ, Testcontainers, Karma e pytest, e análise de cobertura |
| Trilha de Processo — MPS-SW Nível C | Toda a equipe | GPR, REQ, PCP, ITP, VV, GCO, MED, GDE, CAP e GQA(GPC); política de branch (`feat/fix + MF-XX`), rastreabilidade e medição por sprint |

## 5. Integração e disseminação de conhecimento ao longo do projeto

A entrada de Henry Oliveira ao time ocorreu na S3 (atuando inicialmente em Angular e migrando para backend a partir da S4); a transferência de contexto cobriu a arquitetura da API (`/api/v1`), o fluxo de autenticação JWT e a estrutura dos parsers do crawler. A disseminação contínua de conhecimento foi sustentada pelas práticas abaixo.

| Prática | Descrição |
|---|---|
| Revisão de código (code review) | Revisão de PRs no Azure DevOps com aprovação do Tech Lead (Cézar Velazquez; conta legada `Mateus Veloso`), garantindo ciência das mudanças por todo o time |
| Cerimônias de sprint | Planning, review e retrospectiva por sprint, conduzidas com apoio do GP (Abraão), com decisões técnicas compartilhadas e registradas |
| Documentação técnica | Coleções Swagger da API, migrations Flyway (V1–V5) e configuração de pipelines disponibilizadas no Azure DevOps |
| Auditorias de GQA e teste manual | Auditorias independentes de processo por ciclo (S1–S4, S5–S8, S9) conduzidas pela GQA Carol (Caroline) e execução manual dos casos de teste, com geração de evidências, conduzida pela QA Jonathan Alves — reforçando a aderência ao processo junto à equipe |

## 6. Evidências de competência

| Competência | Evidência demonstrada |
|---|---|
| Spring Boot / JWT (backend) | RF01 (cadastro BCrypt) e RF02 (login JWT access+refresh) entregues na S1 por Lucas Batista; RF11 (refresh token rotation) por Felipe Santos na S5; RF12 (logout blacklist Redis jti) por Lucas Batista na S8 |
| SeleniumBase / crawler | RF03 (busca paralela Smiles/Azul/Latam) entregue por Felipe Santos (S2–S3); estabilização de parsers (MF-58/MF-59) na S8 |
| Angular 17 (frontend) | RF04 (SearchPage skeleton) por Lucas Batista na S2; histórico paginado e dark mode evidenciados nas rotas `/search`, `/history`, `/preferences` |
| Arquitetura e Azure Pipelines (Tech Lead / DevOps) | Gate de cobertura JaCoCo ≥ 80% ativo no CI a partir da S4 (CT-10 aprovado na S6+); pipelines dos três repositórios operacionais; aprovação de PR como revisor (Cézar Velazquez; conta legada `Mateus Veloso`) nos 6 PRs da S9 |
| Teste manual com geração de evidências (QA) | Validação manual dos casos de teste CT-01 a CT-12 por Jonathan Alves, com evidências geradas (sem ferramenta de gestão de testes); CT-11 (filtros maxMiles + cabinType) e CT-12 (airport ILIKE) aprovados na S9 |
| GQA / auditoria de processo (GQA independente) | Auditorias por ciclo (S1–S4 conforme com ressalva; S5–S8 conforme; S9 conforme) conduzidas por Carol (Caroline); acompanhamento da evolução da cobertura JaCoCo de 74% (S2) para 82%+ (S5–S8) e encerramento da NC-001 |
| MPS-SW Nível C (processo / gestão) | Rastreabilidade RF → Jira → branch → PR → build mantida; gestão de escopo (CR-MF-001 aprovado por Abraão) e medição por sprint (velocity média 33,9 em S1–S8) registradas |

### Evidências referenciadas

| Código | O que capturar | Fonte/URL |
|---|---|---|
| IMG-CI-01 | Pipeline com gate de cobertura JaCoCo ≥ 80% na API | Azure DevOps — Pipeline "MilhasFacil API - Pipeline" |
| IMG-JIRA-01 | Issues entregues por responsável (RF01, RF02, RF11, RF12) com assignee | Jira — board 614 |
| IMG-DEVOPS-01 | Repositórios MilhasFacil_api/web/crawler com histórico de PRs revisados | Azure DevOps — Repos |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Emissão inicial — evidência do ciclo S1–S9 (MR-MPS-SW:2024 Nível C). |
