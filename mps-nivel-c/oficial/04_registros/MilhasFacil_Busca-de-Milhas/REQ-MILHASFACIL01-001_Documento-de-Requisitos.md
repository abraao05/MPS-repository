# Documento de Requisitos — Hub de Milhas · MilhasFacil (Busca de Milhas)

| Campo | Valor |
|---|---|
| **Documento** | REQ-MILHASFACIL01-001 |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Código do projeto** | MILHASFACIL01 |
| **Cliente** | Hub de Milhas |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Situação** | Aprovado |
| **Gerente de Projeto** | Abraão |
| **Processo MPS-SW** | REQ (evidência de projeto) |

---

## 1. Objetivo

Registrar os requisitos funcionais e não funcionais da plataforma MilhasFacil — sistema de busca e alerta de passagens aéreas resgatáveis por milhas. Os requisitos servem de base para o desenvolvimento, os testes e a rastreabilidade do projeto. Foram levantados e refinados de forma iterativa ao longo das sprints S1 a S9 (09/02/2026 a 14/06/2026), com o projeto aberto na Sprint 9 de um total previsto de 12 sprints (término previsto 26/07/2026). Os critérios de aceite descritos refletem o comportamento real do código entregue até a presente data.

A solução é composta por três serviços independentes: **API** (Spring Boot 3.2.5 / Java 21), **Web** (Angular 17.3) e **Crawler** (FastAPI 0.111 / SeleniumBase 4.27.4). O detalhamento arquitetural consta no documento PCP-MILHASFACIL01-001.

> **Estado dos ramos em 15/06/2026 (release v0.9.0):** após a promoção `develop → homolog → main` (tag **v0.9.0**), a linha `main` contém os requisitos RF01–RF14 e a melhoria MF-64 (released), com migrations **V1–V5 + V9** (`V9__airport_search_index`). RF13, RF14 e MF-64 passaram a status **Entregue**, como os demais RF01–RF12. A padronização de nomenclatura de banco (MF-73, migration `V10__fix_naming_conventions.sql`, incluindo `route_preferences.is_active` e índices completos) está no **PR #29 ativo**, ainda não mergeado em `main`. RF15 não foi iniciado.

---

## 2. Glossário

| Termo | Definição |
|---|---|
| Milhas | Pontos de programas de fidelidade resgatáveis por passagens aéreas |
| Smiles / Azul / Latam | Programas de milhas das companhias cujos portais são consultados pelo Crawler |
| IATA | Código de três letras que identifica um aeroporto (ex.: GRU, GIG) |
| JWT | JSON Web Token — token de autenticação assinado (HS256) usado pela API |
| Access token | Token JWT de curta duração (30 minutos) que autoriza chamadas à API |
| Refresh token | Token JWT de longa duração (7 dias) usado para renovar o access token |
| jti | JWT ID — identificador único do token, usado na blacklist de logout |
| BCrypt | Algoritmo de hash de senhas usado pelo `BCryptPasswordEncoder` |
| Blacklist Redis | Conjunto de `jti` invalidados, armazenado em Redis com TTL de 7 dias |
| Exclusão lógica | Inativação de um registro (`active = false`) sem remoção física |
| Z-API | Provedor de mensageria WhatsApp consumido pelo `WhatsAppClient` |
| Cron | Expressão de agendamento do Spring Scheduler (`@Scheduled`) |
| Crawler | Serviço FastAPI que consulta os portais das companhias e devolve resultados |
| CompletableFuture | Mecanismo Java de execução assíncrona usado na busca paralela |
| ILIKE / unaccent | Operador de comparação case-insensitive e extensão do PostgreSQL para busca insensível a acentos |
| CABIN_MAP | Mapeamento de tipos de cabine (`cabin_type`) usado pelos crawlers |
| BOM | Byte Order Mark — marca inicial em arquivos UTF-8 (usada na exportação CSV) |

---

## 3. Requisitos Funcionais

| ID | Descrição | Critério de aceite (comportamento real) | Sprint | Responsável | Status |
|---|---|---|---|---|---|
| RF01 | Cadastro de usuário com senha protegida por hash BCrypt. | `POST /api/v1/auth/register` recebe `RegisterRequest{name, email, phone, password (≥8 caracteres, `@Size(min = 8)`)}`; a senha é persistida via `BCryptPasswordEncoder`; e-mail duplicado é rejeitado (`existsByEmail` → erro); retorna `AuthResponse{accessToken, refreshToken, email, name}` com HTTP 200 (400 em validação inválida). | S1 | Lucas Batista | Entregue |
| RF02 | Login com emissão de access token e refresh token JWT. | `POST /api/v1/auth/login` recebe `LoginRequest{email, password}`; autentica via `AuthenticationManager`; retorna `AuthResponse` com access token (30 min) e refresh token (7 dias). HTTP 200 em sucesso, 401 em credenciais inválidas. | S1 | Lucas Batista | Entregue |
| RF03 | Busca paralela de voos por milhas nas companhias Smiles, Azul e Latam. | `POST /api/v1/search` recebe `SearchRequest{origin, destination, departureDate, returnDate?, adults}`; o `SearchService` dispara 3 `CompletableFuture` (smiles, azul, latam) ao Crawler; cada um com timeout de 40 s; resultados são unidos, com `distinct()` para remover duplicatas e ordenados por `milesPrice` (crescente). Retorna `List<FlightResult>`. HTTP 200/400/401. | S2–S3 | Felipe Santos | Entregue |
| RF04 | Tela de busca (SearchPage) com estado de carregamento (skeleton). | Rota `/search` (Angular standalone, protegida por `authGuard`); exibe `LoadingSpinner`/skeleton durante a chamada e `EmptyState` quando não há resultados. | S2 | Lucas Batista | Entregue |
| RF05 | Histórico de buscas paginado, com exclusão individual. | `GET /api/v1/flight-history?page&size` retorna `Page<FlightHistory>` do usuário autenticado ordenado por `searchedAt` decrescente (HTTP 200/401); `DELETE /api/v1/flight-history/{id}` remove o registro do próprio usuário e retorna HTTP 204. | S3 | Henry Oliveira | Entregue |
| RF06 | Rotas favoritas com preferência de alerta. | `GET /api/v1/route-preferences` lista as rotas ativas do usuário (`findByUserAndActiveTrue`); `POST` cria uma rota (HTTP 201) com `origin`, `destination`, `alertFrequency` (HOURLY/DAILY/WEEKLY), `maxMiles`; `DELETE /{id}` aplica exclusão lógica (`active = false`) e retorna HTTP 204. | S3–S4 | Lucas Batista | Entregue |
| RF07 | Perfil do usuário — consulta e atualização parcial. | `GET /api/v1/users/me` retorna o usuário autenticado; `PATCH /api/v1/users/me` recebe `UpdateUserRequest{name?, phone?}` e atualiza somente os campos informados (não-nulos). HTTP 200/401. | S4 | Henry Oliveira | Entregue |
| RF08 | Alertas automáticos de queda de milhas via Spring Scheduler. | `ScheduledAlertService` executa `@Scheduled(cron = "0 0 */6 * * *")` (a cada 6 horas); para cada rota ativa, refaz a busca, seleciona o melhor resultado e aplica dedupe pela chave `origem-destino-milhas` (`existsByUserIdAndMessageContaining`) para não notificar repetido; persiste `Notification`. | S4 | Lucas Batista | Entregue |
| RF09 | Notificação por WhatsApp via Z-API. | `WhatsAppClient` faz `POST /send-text` (WebClient) ao endpoint Z-API com header `Client-Token`; falha no envio é registrada em log e **não interrompe** o fluxo de alertas. | S7 | Felipe Santos | Entregue |
| RF10 | Assinatura do usuário com plano e status. | Entidade `Subscription` (1:1 com usuário) com `status` (default `TRIAL`) e `plan` (`BASIC`, `PRO`, `ENTERPRISE`; default `BASIC`), `expiresAt` e `createdAt`. | S5 | Henry Oliveira | Entregue |
| RF11 | Rotação de refresh token. | `POST /api/v1/auth/refresh` recebe `RefreshRequest{refreshToken}`; valida o token (`isValid`) e emite um novo par access+refresh (`AuthResponse`), rotacionando o refresh token. | S5 | Felipe Santos | Entregue |
| RF12 | Logout com invalidação do token (blacklist Redis por jti). | `POST /api/v1/auth/logout` (header `Authorization: Bearer`) extrai o `jti` e o invalida; o `RedisTokenBlacklist` grava a chave `token:invalidated:{jti}` com TTL de 7 dias; o `JwtAuthenticationFilter` consulta a blacklist e descarta tokens invalidados. Retorna HTTP 204. | S8 | Lucas Batista | Entregue |
| RF13 | Filtros avançados de busca (maxMiles e cabinType). | `POST /api/v1/search/filtered` recebe `SearchRequestV2` (com `maxMiles` e `cabinType`); o `FilteredSearchService` aplica os filtros e integra o `CABIN_MAP` dos crawlers (o DTO do Crawler já contempla `max_miles` e `cabin_type`, default `ECONOMY`). Testes do `FilteredSearchService` integrados, build verde. **Released em `main` na v0.9.0**. | S9 | Henry Oliveira | Entregue |
| RF14 | Exportação do histórico em CSV (UTF-8 com BOM). | `GET /api/v1/export/history/csv` (`CsvExportController`/`CsvExportService`) faz streaming do histórico de buscas em CSV codificado em UTF-8 com BOM. **Released em `main` na v0.9.0**. | S8–S9 | Lucas Batista | Entregue |
| MF-64 | Busca de aeroportos case-insensitive e insensível a acentos. | `GET /api/v1/airports?q=` (`AirportController`/`AirportRepository`) faz busca paginada por `ILIKE` com a extensão `unaccent` do PostgreSQL, suportada pela migration `V9__airport_search_index.sql`. Substitui a lista fixa do `SearchService` como fonte de aeroportos. **Released em `main` na v0.9.0**. | S9 | — | Entregue |
| RF15 | Notificações push via PWA. | Envio de notificações push pelo navegador (Progressive Web App) como canal alternativo ao WhatsApp. | S10 | (a alocar) | Não iniciado |

---

## 4. Requisitos Não Funcionais

| ID | Descrição | Critério de aceite | Categoria | Status |
|---|---|---|---|---|
| RNF01 | A busca de voos deve concluir em até 30 segundos. | `SearchService` aplica timeout de 40 s por companhia, mas o tempo de resposta observado mantém-se dentro de 30 s (média medida de 8,3 s). | Performance | Atendido |
| RNF02 | A cobertura de testes deve ser de no mínimo 80%. | Cobertura medida por JaCoCo (API), Karma (Web) e pytest (Crawler), com gate de CI ativo a partir da Sprint 4 (pipeline da API exige JaCoCo ≥ 80%). | Qualidade | Atendido |
| RNF03 | A segurança deve combinar BCrypt, JWT, Redis e CORS. | Senhas em BCrypt; JWT HS256 stateless (access 30 min / refresh 7 dias); blacklist de logout em Redis; CORS do Crawler restrito à origem da API; `SecurityConfig` com CSRF desabilitado e sessão STATELESS. | Segurança | Atendido |
| RNF04 | Toda entrega deve ser rastreável por convenção de branches. | Branches seguem o padrão `feat/` e `fix/` com o código do cartão Jira (`MF-XX`); PR obrigatório para `develop` com aprovação do GP e gate de CI (branch policy de revisor ativa nos 3 repositórios). | Rastreabilidade | Atendido |
| RNF05 | A solução deve ser disponibilizável via Docker Compose. | Os três serviços (API, Web, Crawler) sobem por Docker Compose; janela de indisponibilidade de 3 h registrada na Sprint 6. | Disponibilidade | Atendido |

---

## 5. Regras de negócio (verdade do código)

### 5.1 Segurança e autenticação

- **Hash de senha:** o `SecurityConfig` registra `BCryptPasswordEncoder` como `PasswordEncoder`; o cadastro e o login persistem somente o hash BCrypt da senha.
- **Tokens JWT (HS256, stateless):** o `JwtService` emite access token com expiração de 30 minutos (`1800000 ms`) e refresh token com 7 dias (`604800000 ms`); cada token carrega a claim `type` (`access`/`refresh`) e um `jti` (UUID) único.
- **Rotas públicas:** `SecurityConfig` libera `/api/v1/auth/**` e `/actuator/health`; todas as demais exigem autenticação.
- **Logout / blacklist:** o `RedisTokenBlacklist` grava a chave `token:invalidated:{jti}` com TTL de 7 dias; o `JwtAuthenticationFilter` rejeita tokens cujo `jti` esteja na blacklist.

### 5.2 Busca

- **Paralelismo:** o `SearchService` dispara 3 `CompletableFuture` (smiles, azul, latam) e coleta cada resultado com timeout de **40 segundos**; erro ou timeout de uma companhia devolve lista vazia e não interrompe as demais.
- **Deduplicação e ordenação:** os resultados são unidos, passam por `distinct()` (evita duplicatas de retentativas da Smiles) e são ordenados de forma crescente por `milesPrice`.
- **Busca de aeroportos (`main`, MF-64):** o pacote `airport` (`AirportController`/`AirportRepository`) expõe `GET /api/v1/airports?q=` com busca paginada por `ILIKE` + extensão `unaccent` do PostgreSQL (migration `V9__airport_search_index.sql`), sendo a fonte de aeroportos da plataforma após a release v0.9.0 (substitui a lista fixa em memória do `SearchService`).
- **Busca filtrada (`main`, RF13):** `POST /api/v1/search/filtered` (`FilteredSearchService`) recebe `SearchRequestV2` com `maxMiles`/`cabinType` e integra o `CABIN_MAP` dos crawlers.

### 5.3 Alertas

- **Agendamento:** `ScheduledAlertService` executa a cada 6 horas (cron `0 0 */6 * * *`).
- **Dedupe:** a chave `origem-destino-milhas` evita reenviar o mesmo alerta (`existsByUserIdAndMessageContaining`).
- **WhatsApp resiliente:** o `WhatsAppClient` envia via Z-API (`POST /send-text`, header `Client-Token`); a falha de envio é apenas registrada em log e não interrompe o processamento.

### 5.4 Exclusão lógica

- A remoção de uma rota favorita (`DELETE /api/v1/route-preferences/{id}`) define `active = false` e persiste o registro, preservando-o (exclusão lógica). A listagem considera apenas rotas com `active = true`.

### 5.5 Exportação de histórico (`main`, RF14)

- `GET /api/v1/export/history/csv` (`CsvExportController`/`CsvExportService`) faz streaming do histórico de buscas do usuário em arquivo CSV codificado em UTF-8 com BOM.

---

## 6. Endpoints da API (resumo)

A API expõe os endpoints REST reais abaixo, sob a base `/api/v1` (JWT HS256 stateless). Após a release v0.9.0, todos os endpoints de negócio listados estão em `main`.

| # | Método | Rota | Descrição | RF relacionado | Ramo |
|---|---|---|---|---|---|
| 1 | POST | /api/v1/auth/register | Cadastro de usuário (BCrypt) | RF01 | main |
| 2 | POST | /api/v1/auth/login | Login (access + refresh) | RF02 | main |
| 3 | POST | /api/v1/auth/refresh | Rotação de refresh token | RF11 | main |
| 4 | POST | /api/v1/auth/logout | Logout (blacklist Redis por jti) | RF12 | main |
| 5 | POST | /api/v1/search | Busca paralela Smiles/Azul/Latam | RF03 | main |
| 6 | GET | /api/v1/search/airports?q= | Autocomplete IATA (lista fixa do SearchService) | RF03 | main |
| 7 | GET | /api/v1/flight-history?page&size | Histórico paginado | RF05 | main |
| 8 | DELETE | /api/v1/flight-history/{id} | Exclusão de item do histórico | RF05 | main |
| 9 | GET / PATCH | /api/v1/users/me | Consulta / atualização de perfil | RF07 | main |
| 10 | GET / POST | /api/v1/route-preferences | Lista / cria rota favorita | RF06 | main |
| 11 | DELETE | /api/v1/route-preferences/{id} | Exclusão lógica de rota favorita | RF06 | main |
| 12 | POST | /api/v1/search/filtered | Busca filtrada (`SearchRequestV2`, CABIN_MAP) | RF13 | main (v0.9.0) |
| 13 | GET | /api/v1/export/history/csv | Exportação do histórico em CSV (UTF-8 BOM) | RF14 | main (v0.9.0) |
| 14 | GET | /api/v1/airports?q= | Busca de aeroportos (ILIKE + unaccent) | MF-64 | main (v0.9.0) |

---

## 7. Restrições e premissas

- Os requisitos foram refinados de forma iterativa ao longo das sprints S1–S9; a antecipação dos filtros avançados (RF13) da S10 para a S9 foi formalizada pela mudança de escopo CR-MF-001 (28/05/2026), solicitada pelo PO do Hub de Milhas, com impacto de +10 h e sem atraso macro, aprovada por Abraão (GP).
- RF13, RF14 e MF-64 foram promovidos a `main` na **release v0.9.0** (15/06/2026), pela promoção `develop → homolog → main` com tag v0.9.0; estão **Entregues**, como RF01–RF12. Os PRs correspondentes foram concluídos em 15/06/2026 com aprovação de Cézar Velazquez (Tech Lead — Approved, vote 10; conta legada `Mateus Veloso` no Azure DevOps).
- A padronização de nomenclatura de banco (MF-73, migration `V10__fix_naming_conventions.sql`, incluindo a coluna `route_preferences.is_active` e a complementação dos índices) está no **PR #29 ativo**, ainda não mergeado em `main`.
- A consulta de milhas depende dos portais das companhias (Smiles, Azul, Latam); o redesenho de portal é um risco conhecido (R-01) que ocorreu na Sprint 8 (MF-59) e foi corrigido.
- O canal de notificação primário é o WhatsApp via Z-API; em caso de indisponibilidade (R-03), há fallback por e-mail.
- A migração de schema é controlada por Flyway: em `main`, as versões **V1–V5** (users, flight_history, route_preferences, notifications, subscriptions) **+ V9** (`V9__airport_search_index.sql`, índice de busca de aeroportos). Não há V6/V7/V8. A migration V10 está pendente no PR #29.

---

## 8. Confirmação de entendimento dos requisitos

| Envolvido | Papel | Forma de confirmação |
|---|---|---|
| Abraão | Gerente de Projeto (gestão) | Aprovação do escopo e da mudança CR-MF-001 (28/05/2026); aprovação das baselines de release |
| Cézar Velazquez | Tech Lead / Arquiteto / DevOps (revisor de PR) | Revisão e aprovação dos 6 PRs da Sprint 9 (assinatura `Mateus Veloso` — Approved, vote 10, no Jira/Azure DevOps = Cézar) |
| Jonathan Alves | QA (teste manual; geração de evidências) | Execução dos casos de teste e validação dos critérios de aceite nas sprints |
| Carol (Caroline) | GQA independente (auditoria) | Auditorias de GQA S1–S4 (Conforme com ressalva — NC-001) e S5–S8 (Conforme) |
| PO Hub de Milhas | Product Owner (cliente) | Solicitante da mudança de escopo CR-MF-001; participação nas Sprint Reviews |

> Nota de equivalência: os registros de projeto usam os nomes reais do time atual — GP **Abraão**, Tech Lead/Arquiteto/aprovador de PR **Cézar Velazquez**, QA **Jonathan Alves**, GQA **Carol (Caroline)**, devs **Felipe Santos / Lucas Batista / Henry Oliveira**. Nas evidências legadas do Azure DevOps a aprovação de PR aparece sob a conta `Mateus Veloso` (= Cézar Velazquez); a aprovação do escopo/CR cabe ao GP Abraão.

Os requisitos RF01–RF14 foram confirmados pela entrega e verificação nas sprints correspondentes (todos com status Entregue, em `main`); RF13, RF14 e MF-64 foram promovidos a `main` na release v0.9.0 (15/06/2026), com PRs concluídos e aprovados por Cézar Velazquez (conta legada `Mateus Veloso`); RF15 não foi iniciado (planejado para a Sprint 10).

A GQA registrou a NC-001 (cobertura de testes abaixo de 80% — JaCoCo 74% na S2); a ação corretiva (priorização de testes unitários + gate de CI a partir da S4) foi executada e a NC encerrada na Sprint 5 com JaCoCo de 82%.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Emissão inicial — evidência do ciclo S1–S9 (MR-MPS-SW:2024 Nível C). |
