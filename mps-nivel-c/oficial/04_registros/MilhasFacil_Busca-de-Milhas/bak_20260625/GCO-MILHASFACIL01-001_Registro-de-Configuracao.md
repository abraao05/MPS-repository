# Registro de Gerência de Configuração — MilhasFacil · Hub de Milhas

| Campo | Valor |
|---|---|
| **Documento** | GCO-MILHASFACIL01-001 |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Cliente** | Hub de Milhas |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Gerente de Projeto** | Abraão |
| **Processo MPS-SW** | GCO (evidência de projeto) |

---

## 1. Objetivo

Registrar o gerenciamento de configuração do projeto MilhasFacil: itens de configuração (ICs), estratégia de controle de versão e ramificação, política de pull request, baselines por sprint e auditoria de configuração. O controle de versão e a esteira de integração contínua são mantidos no Azure DevOps, com três repositórios independentes (API, Web e Crawler), todos com branch padrão `main`. A gestão do projeto é conduzida pelo Gerente de Projeto (Abraão), que aprova escopo e mudanças; a operação de DevOps/Infra (pipelines, Docker e branch policy) e a aprovação técnica de pull request cabem ao Tech Lead / Arquiteto / DevOps (Cézar Velazquez).

---

## 2. Estratégia de gerência de configuração

| Item | Descrição |
|---|---|
| Plataforma | Azure DevOps (controle de versão, pull requests e pipelines CI/CD) |
| Repositórios | Três repositórios independentes — `MilhasFacil_api`, `MilhasFacil_web`, `MilhasFacil_crawler` (branch padrão `main`) |
| Modelo de ramificação | `develop` (integração) → `homolog` (homologação) → `main` (produção); branches de trabalho `feat/MF-XX-*` e `fix/MF-XX-*` originadas de `develop` |
| Convenção de nomes de branch | `feat/`-`fix/` + identificador `MF-XX` do Jira (RNF04 — rastreabilidade), ex.: `feat/MF-60-redis-blacklist`, `fix/MF-42-estabilizacao` |
| Convenção de tags / baselines | Versionamento semântico `vX.Y.Z` por sprint; a release v0.9.0 (S9) foi promovida a `main` com tag `v0.9.0` (released) |
| Política de PR | Pull request obrigatório para integração em `develop`; aprovação técnica do Tech Lead Cézar Velazquez; gate de CI (build verde; gate de cobertura JaCoCo 80% no repositório da API a partir da S4) |
| Branch policy de revisor | Política de branch exigindo no mínimo 1 revisor aprovador para merge em `develop`, ativada em 15/06/2026 nos três repositórios (controle prospectivo) |
| Gestão de segredos | Credenciais de Z-API (Client-Token), conexões Postgres/Redis e chaves JWT mantidas fora do código, sem exposição em logs (RNF03) |
| Documentação | Coleções/contratos de API (Swagger), Docker Compose e scripts Flyway (`V1`–`V5` + `V9` em `main`; `V10` no PR #29 ativo) versionados no Azure DevOps |

---

## 3. Itens de configuração (ICs)

| ID | Tipo | Descrição | Repositório / Localização |
|---|---|---|---|
| IC-01 | Código-fonte (Java / Spring Boot 3.2.5 · Java 21) | API REST base `/api/v1`, JWT HS256 stateless | Azure DevOps — repositório `MilhasFacil_api` |
| IC-02 | Código-fonte (Angular 17.3 standalone · Tailwind 3.4) | Aplicação Web (login, register, search, history, preferences) | Azure DevOps — repositório `MilhasFacil_web` |
| IC-03 | Código-fonte (FastAPI 0.111 · SeleniumBase 4.27.4) | Crawler de cias (parsers Smiles/Azul/Latam) | Azure DevOps — repositório `MilhasFacil_crawler` |
| IC-04 | Banco de dados | Migrations Flyway — `V1`–`V5` + `V9__airport_search_index.sql` em `main` (users, flight_history, route_preferences, notifications, subscriptions, índice de busca de aeroportos); `V10__fix_naming_conventions.sql` (MF-73) no PR #29 ativo | Azure DevOps — repositório `MilhasFacil_api` |
| IC-05 | Infraestrutura de execução | Docker Compose (Postgres + Redis + API + Web + Crawler) | Azure DevOps — repositórios da solução |
| IC-06 | Definição de pipeline | Pipelines "MilhasFacil API/Web/Crawler - Pipeline" (PowerShell@2) | Azure DevOps — Pipelines |
| IC-07 | Artefato de gestão | Planilha de gestão (backlog, sprints, tarefas) — fonte da verdade de gestão | GEST-MILHASFACIL01-001 (xlsx) |

---

## 4. Estratégia de ramificação e política de pull request

A integração de novas funcionalidades ocorre exclusivamente via pull request, segundo a política de branch do projeto (RNF04):

- **`main`** — código de produção; recebe promoção a partir de `homolog`. A release v0.9.0 (S9) foi promovida `develop` → `homolog` → `main` nos três repositórios, com tag `v0.9.0`.
- **`homolog`** — ambiente de homologação; recebe promoção a partir de `develop`.
- **`develop`** — branch de integração contínua; alvo de todos os PRs de funcionalidade e correção.
- **`feat/MF-XX-*` / `fix/MF-XX-*`** — branches de trabalho originadas de `develop`, nomeadas com o identificador `MF-XX` da issue correspondente no Jira.

**Regras da política de branch:**

1. Pull request obrigatório para integrar qualquer branch de trabalho em `develop`.
2. Aprovação técnica do Tech Lead Cézar Velazquez como revisor (nas evidências legadas do Azure DevOps a aprovação aparece sob a conta `Mateus Veloso` = Cézar). A aprovação de escopo/CR cabe ao Gerente de Projeto Abraão.
3. Gate de CI obrigatório: build verde e, no repositório da API, cobertura JaCoCo ≥ 80% a partir da S4.
4. Nome da branch sempre referenciando a issue do Jira no padrão `feat/`-`fix/` + `MF-XX`.

**Branch policy de revisor (controle prospectivo):** em 15/06/2026 foi ativada, nos três repositórios, a política de branch que exige no mínimo 1 revisor aprovador para merge em `develop`. Essa política impede a recorrência de merges sem revisão e atua de forma prospectiva sobre os PRs futuros.

> **Nota de equivalência:** a aprovação de PR no Azure DevOps aparece sob a conta legada `Mateus Veloso` — corresponde ao Tech Lead **Cézar Velazquez**. Os demais membros do time (Felipe Siqueira, Henry Komatsu, Lucas Batista, Yan Dallacqua, Jonathan Alves, Caroline Sousa) operam com suas contas nominais. Commits de serviço de consolidação de histórico usam conta de infra do ambiente (`raony.chagas@timeware.com.br`) e não correspondem a um colaborador nomeado do projeto.

---
            
## 5. Baselines estabelecidas

Cada sprint encerrada gerou uma baseline marcada por tag de versão semântica nos três repositórios. A release v0.9.0 (S9) foi promovida a `main` (released) com tag `v0.9.0`.

| Baseline | Sprint | Descrição | Situação |
|---|---|---|---|
| v0.1.0 | S1 (09–22/02/2026) | Cadastro BCrypt + login JWT (access/refresh) | Estável (`main`) |
| v0.2.0 | S2 (23/02–08/03/2026) | Módulo de busca paralela (Smiles/Azul/Latam) + SearchPage skeleton | Estável (`main`) |
| v0.3.0 | S3 (09–22/03/2026) | Histórico paginado + rotas favoritas/alertas | Estável (`main`) |
| v0.4.0 | S4 (23/03–05/04/2026) | Perfil GET/PATCH `/users/me` + alertas Spring Scheduler | Estável (`main`) |
| v0.5.0 | S5 (06–19/04/2026) | Assinaturas + refresh token rotation | Estável (`main`) |
| v0.6.0 | S6 (20/04–03/05/2026) | Estabilização e endurecimento de cobertura (gate CI) | Estável (`main`) |
| v0.7.0 | S7 (04–17/05/2026) | Notificações WhatsApp Z-API | Estável (`main`) |
| v0.8.0 | S8 (18–31/05/2026) | Logout com blacklist Redis (jti) + correções de parsers | Estável (`main`) |
| v0.9.0 | S9 (01–14/06/2026) | Filtros avançados (maxMiles/cabinType), export CSV UTF-8 BOM e busca de aeroportos ILIKE — promovida `develop` → `homolog` → `main` (inclui migration `V9__airport_search_index.sql`) | Released (`main`, tag `v0.9.0`, 15/06/2026) |

> A baseline `v0.9.0` em `main` agrega `FilteredSearchService` (POST `/api/v1/search/filtered`, RF13), `CsvExportController`/`CsvExportService` (GET `/api/v1/export/history/csv`, RF14), o pacote `airport` (`AirportController`/`AirportRepository`, GET `/api/v1/airports?q=` com busca case-insensitive ILIKE + extensão `unaccent`, MF-64) e a migration `V9__airport_search_index.sql`. Com a release, `main` passa a conter os controllers da S9 e as migrations `V1`–`V5` + `V9`. A migration `V10__fix_naming_conventions.sql` (padronização de nomenclatura de BD, MF-73) está no PR #29 ativo, ainda não mergeado.

![IMG-DEVOPS-03 — tags/baselines do projeto](evidencias/IMG-DEVOPS-03_tags-baselines.png)

*Figura — Tags de versão (`v0.1.0`–`v0.9.0`, released em `main`) nos repositórios do Azure DevOps.*

---

## 6. Pull requests do projeto

Até 15/06/2026 a API do Azure DevOps registra **29 pull requests** nos três repositórios: **28 concluídos** e **1 ativo** (PR #29). Os 22 PRs históricos (S1–S8) foram integrados de forma retroativa na inicialização do histórico e, conforme a API, **não possuem revisor registrado**. Os 6 PRs da S9 foram concluídos (merge em `develop`) **com revisor Mateus Veloso — Approved (vote 10)** — conta legada correspondente ao Tech Lead Cézar Velazquez. O **PR #29 (MF-73)** está **ativo**, **aprovado pelo Tech Lead Cézar Velazquez na conta própria dele no Azure DevOps (vote 10)**, aguardando merge. As datas reais de PR e build concentram-se em 13–15/06/2026 (histórico inicializado retroativamente).

### 6.1 22 PRs históricos S1–S8 (sem revisor registrado)

| PR | Repositório | Branch de origem | Situação | Revisor |
|---|---|---|---|---|
| #1 | MilhasFacil_api | feat/MF-2-auth-register | Concluído (merge) | (sem revisor registrado) |
| #2 | MilhasFacil_api | feat/MF-3-auth-login | Concluído (merge) | (sem revisor registrado) |
| #3 | MilhasFacil_api | feat/MF-8-search-module | Concluído (merge) | (sem revisor registrado) |
| #4 | MilhasFacil_api | feat/MF-13-flight-history | Concluído (merge) | (sem revisor registrado) |
| #5 | MilhasFacil_api | feat/MF-21-route-preferences | Concluído (merge) | (sem revisor registrado) |
| #6 | MilhasFacil_api | feat/MF-29-alerts-profile | Concluído (merge) | (sem revisor registrado) |
| #7 | MilhasFacil_api | feat/MF-35-subscriptions | Concluído (merge) | (sem revisor registrado) |
| #8 | MilhasFacil_api | fix/MF-42-estabilizacao | Concluído (merge) | (sem revisor registrado) |
| #9 | MilhasFacil_api | feat/MF-49-whatsapp-notifications | Concluído (merge) | (sem revisor registrado) |
| #10 | MilhasFacil_api | feat/MF-60-redis-blacklist | Concluído (merge) | (sem revisor registrado) |
| #13 | MilhasFacil_web | feat/MF-8-search-page | Concluído (merge) | (sem revisor registrado) |
| #14 | MilhasFacil_web | feat/MF-13-history-preferences | Concluído (merge) | (sem revisor registrado) |
| #15 | MilhasFacil_web | feat/MF-29-profile-notifications | Concluído (merge) | (sem revisor registrado) |
| #16 | MilhasFacil_web | fix/MF-38-ux-token-refresh | Concluído (merge) | (sem revisor registrado) |
| #17 | MilhasFacil_web | feat/MF-43-search-filters-ui | Concluído (merge) | (sem revisor registrado) |
| #18 | MilhasFacil_web | feat/MF-52-dark-mode | Concluído (merge) | (sem revisor registrado) |
| #19 | MilhasFacil_web | feat/MF-61-ux-onboarding | Concluído (merge) | (sem revisor registrado) |
| #20 | MilhasFacil_web | feat/MF-29-profile-notifications | Concluído (merge) | (sem revisor registrado) |
| #23 | MilhasFacil_crawler | feat/MF-8-crawler-setup | Concluído (merge) | (sem revisor registrado) |
| #24 | MilhasFacil_crawler | fix/MF-8-smiles-fixes | Concluído (merge) | (sem revisor registrado) |
| #25 | MilhasFacil_crawler | feat/MF-crawler-refactor | Concluído (merge) | (sem revisor registrado) |
| #26 | MilhasFacil_crawler | fix/MF-crawler-regex-smiles-redesign | Concluído (merge) | (sem revisor registrado) |

> Os 22 PRs históricos foram criados na inicialização retroativa do histórico, antes da ativação da branch policy de revisor. Por serem PRs concluídos (estado travado, imutável), não recebem revisor a posteriori e são tratados como ressalva com causa-raiz documentada (integração retroativa do histórico).

### 6.2 6 PRs da S9 concluídos COM revisor Mateus Veloso — Approved (10)

| PR | Repositório | Branch de origem | Situação | Revisor |
|---|---|---|---|---|
| #11 | MilhasFacil_api | feat/MF-65-search-filters | Concluído — merge em `develop` | Mateus Veloso — Approved (10) |
| #12 | MilhasFacil_api | feat/MF-69-csv-export | Concluído — merge em `develop` | Mateus Veloso — Approved (10) |
| #28 | MilhasFacil_api | feat/MF-64-airport-ilike | Concluído — merge em `develop` | Mateus Veloso — Approved (10) |
| #21 | MilhasFacil_web | feat/MF-65-search-filters | Concluído — merge em `develop` | Mateus Veloso — Approved (10) |
| #22 | MilhasFacil_web | feat/MF-69-csv-ui | Concluído — merge em `develop` | Mateus Veloso — Approved (10) |
| #27 | MilhasFacil_crawler | feat/MF-65-cabin-type-filter | Concluído — merge em `develop` | Mateus Veloso — Approved (10) |

### 6.3 PR ativo — PR #29 (MF-73, padronização de nomenclatura de BD)

| PR | Repositório | Branch de origem | Situação | Revisor |
|---|---|---|---|---|
| #29 | MilhasFacil_api | fix/MF-73-fix-naming-conventions | Ativo — aprovado, aguardando merge | Cézar Velazquez — Approved (10) |

> O PR #29 (MF-73, card de Chore — padronização de nomenclatura de BD conforme GUIA-GCO-001, responsável Cézar Velazquez (DevOps/TL; card reatribuído para `cezar.hiraki` no Jira)) introduz a migration `V10__fix_naming_conventions.sql` (padronização de índices + coluna `is_active`). É o único PR ativo do projeto, **aprovado pelo Tech Lead Cézar Velazquez na conta própria dele (vote 10)**; aguardando merge.

![IMG-DEVOPS-02 — lista de pull requests do projeto](evidencias/IMG-DEVOPS-02_lista-prs.png)

*Figura — Lista de pull requests (22 históricos S1–S8 + 6 da S9, todos concluídos; PR #29 ativo) nos três repositórios do Azure DevOps.*

> **Nota de equivalência:** Mateus Veloso (revisor registrado na API do Azure DevOps) corresponde ao Tech Lead / Arquiteto / DevOps Cézar Velazquez no time atual (aprovador de PR). A reatribuição da conta no Azure aguarda provisionamento de Cézar no projeto MF.

---

## 7. Auditoria de configuração

| Item verificado | Resultado | Observação |
|---|---|---|
| ICs versionados no Azure DevOps | Conforme | IC-01 a IC-06 nos três repositórios; pipelines e Docker Compose versionados |
| Branch padrão definida por repositório | Conforme | `main` em `MilhasFacil_api`, `MilhasFacil_web` e `MilhasFacil_crawler` |
| Estratégia de ramificação aplicada | Conforme | `develop` → `homolog` → `main`; branches `feat/`-`fix/` + `MF-XX` (RNF04) |
| Nomes de branch rastreáveis ao Jira | Conforme | Branches nomeadas com identificador `MF-XX` da issue correspondente |
| Baselines marcadas por tag | Conforme | `v0.1.0`–`v0.9.0` em `main`; `v0.9.0` released (tag) após promoção `develop` → `homolog` → `main` |
| Migrations de banco controladas | Conforme | `V1`–`V5` + `V9` em `main`; `V10` (MF-73) no PR #29 ativo, aprovado pelo Cézar (vote 10), aguardando merge |
| Branch policy de revisor ativa em `develop` | Conforme | Política de ≥1 revisor aprovador ativada nos 3 repositórios em 15/06/2026 (controle prospectivo) |
| Gate de CI no merge | Conforme | Build verde obrigatório; gate de cobertura JaCoCo 80% na API a partir da S4 |
| Segredos não expostos em logs | Conforme | Z-API Client-Token, conexões e chave JWT mantidas fora do código (RNF03) |
| PRs sem revisor = 0 (meta organizacional) | Conforme com ressalva | Meta cumprida pelos 6 PRs da S9 (concluídos com revisor Mateus Veloso — Approved 10) e reforçada pela branch policy de revisor ativada em `develop`; o PR #29 ativo (MF-73) também possui revisor — Cézar Velazquez (conta própria, Approved/vote 10). Os 22 PRs históricos S1–S8 permanecem como ressalva imutável (PR concluído é travado), com causa-raiz na inicialização retroativa do histórico |

> A meta "PRs sem revisor = 0" é cumprida pelos PRs da S9 e pelo PR #29 ativo (ambos com revisor) e reforçada, em caráter prospectivo, pela branch policy de revisor em `develop`. Os 22 PRs históricos S1–S8 são imutáveis (PR concluído é travado) e não recebem revisor a posteriori — tratados como ressalva com causa-raiz documentada (integração retroativa do histórico). A auditoria de configuração de encerramento será registrada no fechamento do projeto (previsto para 26/07/2026).

---

### Evidências referenciadas

| Código | O que capturar | Fonte/URL |
|---|---|---|
| IMG-DEVOPS-02 | Lista de pull requests (22 históricos S1–S8 + 6 da S9 concluídos; PR #29 ativo MF-73), com revisor Mateus Veloso (Approved 10) nos 6 da S9 e revisor Cézar Velazquez (Approved, vote 10) no #29 | Azure DevOps — Pull Requests (MilhasFacil_api/web/crawler) |
| IMG-DEVOPS-03 | Tags de baseline (`v0.1.0`–`v0.9.0`, com `v0.9.0` released em `main`) e branch policy de revisor ativa em `develop` | Azure DevOps — Repos / Tags / Branch policies dos três repositórios |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Emissão inicial — evidência do ciclo S1–S9 (MR-MPS-SW:2024 Nível C). |
