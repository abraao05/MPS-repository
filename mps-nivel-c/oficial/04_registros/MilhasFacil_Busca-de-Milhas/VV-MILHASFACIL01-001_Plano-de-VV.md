# Plano de Verificação e Validação — MilhasFacil · Busca e Alerta de Passagens por Milhas

| Campo | Valor |
|---|---|
| **Documento** | VV-MILHASFACIL01-001 |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Cliente** | Hub de Milhas |
| **Versão** | 1.1 |
| **Data** | 26/06/2026 |
| **Gerente de Projeto** | Abraão |
| **Processo MPS-SW** | VV (evidência de projeto) |

---

## 1. Objetivo

Definir a estratégia e as atividades de Verificação e Validação (V&V) da plataforma MilhasFacil — Busca e Alerta de Passagens por Milhas, garantindo que o produto atende aos requisitos especificados (verificação) e às necessidades de negócio do Hub de Milhas (validação). O plano cobre os três repositórios do produto (API Spring Boot, Web Angular e Crawler FastAPI) e as atividades de teste executadas ao longo dos sprints S1–S9.

---

## 2. Escopo do plano

Este plano cobre as atividades de V&V aplicadas ao longo dos sprints do projeto, desde os testes unitários durante o desenvolvimento até os testes de integração, a revisão de código por pares (Merge Request), a validação de cobertura no pipeline de CI e os testes de aceitação/exploratórios manuais da QA. O projeto está ABERTO (Sprint 10 de 12, em andamento de 15–28/06/2026); este registro consolida a estratégia e a evidência do ciclo S1–S9, incluindo a release v0.9.0 (15/06/2026), que promoveu RF13, RF14 e MF-64 para `main`.

Componentes no escopo:

- **API** (MilhasFacil_api) — Spring Boot 3.2.5 / Java 21, base `/api/v1`, JWT HS256 stateless.
- **Web** (MilhasFacil_web) — Angular 17.3 standalone / Tailwind 3.4.
- **Crawler** (MilhasFacil_crawler) — FastAPI 0.111 / SeleniumBase 4.27.4, parsers Smiles/Azul/Latam.

---

## 3. Estratégia de verificação e validação

### 3.1 Níveis de teste

| Nível | Tipo | Responsável | Ferramenta | Critério de entrada | Critério de saída |
|---|---|---|---|---|---|
| 1 | Testes unitários (API) | Time Timeware (Dev + QA) | JUnit 5 + Mockito + AssertJ | Código da feature concluído | Cobertura JaCoCo ≥ 80%; todos os testes passando |
| 2 | Testes de integração (API) | Time Timeware (Dev + QA) | Spring Boot Test + Testcontainers (PostgreSQL) | Testes unitários passando | Fluxos críticos (auth, busca, segurança) executados sem falha |
| 3 | Testes unitários (Web) | Time Timeware (Dev + QA) | Karma + Jasmine | Componente/serviço concluído | Cobertura Karma ≥ 80%; specs passando |
| 4 | Testes unitários (Crawler) | Time Timeware (Dev + QA) | pytest | Parser/endpoint concluído | Cobertura pytest ≥ 80%; testes passando |
| 5 | Revisão de código (peer review) | Autor + Revisor (Tech Lead) | GitLab Merge Requests | MR aberto com CI verde | MR aprovado pelo Tech Lead (Cézar Velazquez) e gate de CI atendido (ver REV-MILHASFACIL01-001) |
| 6 | Gate de cobertura no CI | DevOps (Cézar Velazquez — Tech Lead) | Pipeline Docker (runner-vm-docker) + JaCoCo | Build executado no pipeline | Cobertura ≥ 80% na API; pipeline verde para merge em `develop` |
| 7 | Testes de aceitação / exploratórios MANUAIS (validação) | QA — Jonathan Alves | **Execução manual; evidências geradas à mão (capturas de tela e registros). Sem ferramenta de gestão de testes (Xray / Azure Test Plans)** | Funcionalidade integrada no ambiente de homologação | Cenários CT-01–CT-12 validados manualmente; evidências anexadas ao registro de execução (REL-VV-MILHASFACIL01-001) |

> A validação funcional do produto é conduzida **manualmente** pela QA Jonathan Alves, que executa os cenários de teste (CT) na aplicação em homologação e **gera as evidências à mão** (capturas de tela, registros de resultado). O projeto **não utiliza ferramenta de gestão de testes** (Xray / Azure Test Plans); os casos e os resultados são mantidos neste plano e no relatório de execução (REL-VV-MILHASFACIL01-001). A validação manual da QA na release v0.9.0 sustentou a aprovação dos casos CT-11 e CT-12 (filtros avançados e busca de aeroporto por ILIKE).

### 3.2 Critérios de qualidade do projeto

| Critério | Meta | Base |
|---|---|---|
| Cobertura de testes (JaCoCo / Karma / pytest) | ≥ 80% | RNF02 |
| Gate de cobertura no CI | Ativo a partir da Sprint 4 | RNF02 |
| Tempo de resposta da busca | ≤ 30 s (média observada 8,3 s) | RNF01 |
| Não conformidades em aberto | 0 | Meta de qualidade (GQA) |
| Merge Requests sem revisor | 0 | RNF04 / política de branch |
| Velocity por sprint | ≥ 30 SP | Meta de gestão |

---

## 4. Estratégia por repositório

### 4.1 API (MilhasFacil_api)

A API concentra as regras de negócio (autenticação JWT, agregação de busca paralela, alertas agendados) e por isso recebe os dois primeiros níveis de teste:

- **Unitários (JUnit 5 + Mockito + AssertJ):** isolam serviços com dependências mockadas. Cobrem `AuthService` (codificação de senha BCrypt, e-mail duplicado, geração de tokens), `SearchService` (agregação das 3 companhias e ordenação por milhas, autocomplete de aeroportos case-insensitive), `FilteredSearchService` (filtros avançados maxMiles + cabinType da busca filtrada) e `ScheduledAlertService` (dedupe de alertas já enviados e disparo de WhatsApp em alerta novo).
- **Integração (Spring Boot Test + Testcontainers):** sobem o contexto completo com MockMvc. Cobrem o fluxo HTTP real de `AuthController` (registro válido retornando tokens; login com senha inválida retornando 401), de `SearchController` (busca não autenticada retornando 401) e o teste de integração do `AirportRepository` (busca case-insensitive ILIKE/`unaccent`, ex.: `q=gru` → GRU Guarulhos).

### 4.2 Web (MilhasFacil_web)

Testes unitários de componentes e serviços standalone com Karma + Jasmine: `AuthService` (signals + localStorage), `jwtInterceptor` (401 → refresh → retry via switchMap), `ThemeService` (dark mode) e componentes compartilhados (LoadingSpinner, EmptyState, Pagination). Cobertura medida por Karma.

### 4.3 Crawler (MilhasFacil_crawler)

Testes unitários com pytest sobre os parsers BeautifulSoup. O `SmilesParser` é validado quanto à extração de voos a partir de HTML de exemplo, leitura de milhas com 6 dígitos (ex.: 120.000), leitura de taxa (R$) e retorno de lista vazia para HTML sem cards. Os endpoints FastAPI (`GET /health`, `POST /search/{airline}` com 404 para companhia inválida) também são exercitados.

---

## 5. Casos de teste (CT-01 a CT-12)

Os casos de teste a seguir representam os cenários de V&V do projeto, mapeados a sprint, tipo e resultado. Os **12 casos estão APROVADOS**. CT-11 e CT-12 referem-se a funcionalidades entregues na Sprint 9 (filtros avançados e busca de aeroporto por ILIKE), promovidas para `main` na **release v0.9.0**, com testes integrados, builds verdes e validação manual da QA Jonathan Alves.

| CT | Cenário | Sprint | Tipo | Resultado |
|---|---|---|---|---|
| CT-01 | Cadastro (register) seguido de login com credenciais válidas | S1 | Happy | Aprovado |
| CT-02 | Login/credenciais inválidas retornam HTTP 401 | S1 | Sad | Aprovado |
| CT-03 | Busca paralela nas 3 companhias (Smiles/Azul/Latam) concluída em < 30 s | S2/S3 | Happy | Aprovado |
| CT-04 | Histórico de buscas paginado (MF-38) | S3 | Happy | Aprovado |
| CT-05 | Refresh token com rotação | S5 | Happy | Aprovado |
| CT-06 | Logout invalida token via blacklist Redis → 401 em reuso | S8 | Happy | Aprovado |
| CT-07 | Alerta WhatsApp enviado sem duplicata | S7 | Happy | Aprovado |
| CT-08 | Regressão do LatamParser após redesign de companhia (MF-59) | S8 | Regressão | Aprovado |
| CT-09 | Smiles — milhas com 6 dígitos (MF-58) | S8 | Happy | Aprovado |
| CT-10 | Gate de cobertura ≥ 80% no CI | S6+ | CI/CD | Aprovado |
| CT-11 | Filtros avançados maxMiles + cabinType | S9 | Happy | Aprovado |
| CT-12 | Busca de aeroporto por ILIKE (MF-64) | S9 | Sad | Aprovado |

CT-11 é sustentado pelos testes de `FilteredSearchService` (build verde) e CT-12 pelo teste de integração do `AirportRepository` (`q=gru` → GRU Guarulhos; build verde). Ambos foram integrados em `develop` na Sprint 9 e promovidos para `main` na **release v0.9.0** (15/06/2026), com **validação manual da QA Jonathan Alves** sobre a aplicação em homologação.

---

## 6. Gestão de defeitos

| Severidade | Definição | Tratamento | Impacto no aceite |
|---|---|---|---|
| Crítico | Funcionalidade principal inoperante; perda de dados | Correção imediata; bloqueia merge | Bloqueia fechamento do sprint |
| Alto | Funcionalidade principal com comportamento incorreto, com workaround | Correção no sprint | Bloqueia se não resolvido |
| Médio | Funcionalidade secundária com comportamento incorreto | Próximo sprint | Não bloqueia; registrado no backlog |
| Baixo | Melhorias cosméticas, textos, formatação | A critério | Não bloqueia |

Os defeitos (type Bug no GitLab) identificados ao longo do projeto — MF-17, MF-18, MF-28, MF-36, MF-37, MF-38, MF-46, MF-47, MF-56, MF-58, MF-59 — são registrados no GitLab (board 614) e triados pelo time. O risco R-01 (redesign de companhias quebra os parsers) materializou-se na Sprint 8 (MF-59) e foi corrigido, com cobertura de regressão garantida por CT-08.

---

## 7. Verificação contínua e pipeline de CI

- **Revisão de código:** todo MR para `develop` passa por revisão antes do merge, com aprovação do Tech Lead (Cézar Velazquez) e gate de CI verde. A **proteção de branch com revisores obrigatórios está ativa em `develop`** nos três repositórios, exigindo ao menos um revisor por MR. O registro da revisão é o próprio Merge Request (ver REV-MILHASFACIL01-001).
- **Pipeline CI:** a cada push, os pipelines "MilhasFacil API/Web/Crawler - Pipeline" (GitLab CI/CD, Docker runner-vm-docker; triggers `develop`/`homolog`/`main`) executam build e testes. O pipeline da API inclui **gate JaCoCo de 80%**, ativo a partir da Sprint 4 — o merge no branch principal só é permitido com o gate atendido (CT-10).
- **Rastreabilidade:** branches seguem o padrão `feat/`/`fix/` + `MF-XX` (RNF04), vinculando cada entrega ao issue GitLab correspondente.

---

## 8. Não conformidade NC-001 (cobertura)

A não conformidade NC-001 foi aberta na Sprint 2, quando a cobertura JaCoCo da API caiu a 74%, abaixo da meta de 80% (RNF02 / risco R-02). O plano de tratamento priorizou a escrita de testes unitários e a ativação do gate de cobertura no CI a partir da Sprint 4. A NC-001 foi encerrada na Sprint 5, com a cobertura JaCoCo atingindo 82%. A auditora de GQA independente do projeto é Carol (Caroline).

---

## 9. Análise e comunicação dos resultados (VV 5)

Os resultados de V&V são analisados e comunicados ao longo do projeto conforme a cadência abaixo:

| Frequência | Conteúdo | Canal | Destinatários |
|---|---|---|---|
| A cada sprint | Resultado dos casos de teste, cobertura (JaCoCo/Karma/pytest) e bugs abertos/fechados | Sprint Review | GP, equipe, PO Hub de Milhas |
| A cada sprint | Indicadores de qualidade consolidados (cobertura, bugs, NCs, MRs sem revisor) | Planilha de gestão (GEST-MILHASFACIL01-001) | GP, Time de Melhoria Contínua |
| Por ciclo | Análise consolidada de execução de testes | Repositório oficial (REL-VV-MILHASFACIL01-001) | GP, Time de Melhoria Contínua |

Indicadores reportados ao processo de Medição (MED):

- Velocity por sprint (meta ≥ 30 SP).
- Cobertura de testes JaCoCo, Karma e pytest (meta ≥ 80%).
- Bugs por sprint e não conformidades em aberto (meta NCs = 0).
- Merge Requests sem revisor (meta = 0).

---

## 10. Cenários de teste (Gherkin) e evidências

Os cenários de teste em formato Gherkin (happy path e sad path), derivados do código de teste real (JUnit 5, Karma e pytest), estão documentados integralmente em **REL-VV-MILHASFACIL01-001 §4**. Os resultados de execução por sprint, com cobertura e registro de bugs, constam em **REL-VV-MILHASFACIL01-001 §2 e §3**. As evidências da validação manual da QA Jonathan Alves, geradas à mão, são anexadas ao registro de execução.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Emissão inicial — evidência do ciclo S1–S9 (MR-MPS-SW:2024 Nível C). |
| 1.1 | 26/06/2026 | Time de Melhoria Contínua | Correção de referências de CI: PowerShell@2/agente Windows substituído por Docker (runner-vm-docker); Azure Pipelines substituído por GitLab CI/CD. |
| 1.2 | 29/06/2026 | Auditoria MPS.BR Nível C | Status atualizado para Sprint 10 em andamento (S10 de 12, 15–28/06/2026) em §2; terminologia "PRs sem revisor" → "MRs sem revisor" em §9 (tabela de comunicação). |
