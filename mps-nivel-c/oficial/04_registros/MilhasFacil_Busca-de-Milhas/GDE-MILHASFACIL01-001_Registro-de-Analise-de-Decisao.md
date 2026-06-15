# Registro de Análise de Decisão — MilhasFacil · Hub de Milhas

| Campo | Valor |
|---|---|
| **Documento** | GDE-MILHASFACIL01-001 |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Cliente** | Hub de Milhas |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Gerente de Projeto** | Abraão |
| **Processo MPS-SW** | GDE (evidência de projeto) |

---

## Decisão GDE-001 — Estratégia de autenticação (JWT stateless vs. sessão)

### 1. Contexto / problema

A plataforma expõe uma API REST (base `/api/v1`) consumida por um frontend Angular standalone e, potencialmente, por outros clientes. A autenticação precisa suportar múltiplos consumidores sem manter estado de sessão no servidor, permitir escalabilidade horizontal sob Docker Compose e habilitar o fluxo de refresh token. A escolha do mecanismo de autenticação é arquitetural e impacta segurança, escalabilidade e o design do filtro de segurança.

### 2. Alternativas avaliadas

| # | Alternativa | Descrição |
|---|---|---|
| A | JWT stateless (HS256) com access + refresh token | Tokens assinados em HS256; access token de curta duração (30 min) e refresh token (7 dias) com rotação. Servidor sem estado de sessão; `SecurityConfig` em modo STATELESS. |
| B | Sessão server-side (cookie + store) | Estado de sessão mantido no servidor (memória ou store compartilhado). Cookie de sessão por cliente; exige store compartilhado para escalar horizontalmente. |

### 3. Critérios de decisão

| Critério | Peso |
|---|---|
| Escalabilidade horizontal sem estado de sessão | Alto |
| Suporte a múltiplos clientes (Web e API) | Alto |
| Compatibilidade com fluxo de refresh token | Alto |
| Simplicidade do filtro de segurança | Médio |
| Capacidade de revogação imediata (logout) | Médio |

### 4. Avaliação (matriz de decisão)

| Critério | Peso | A — JWT stateless | B — Sessão server-side |
|---|---|---|---|
| Escalabilidade horizontal | Alto | Máxima — sem estado de sessão; qualquer instância valida o token localmente | Penalizada — exige store de sessão compartilhado entre instâncias |
| Múltiplos clientes | Alto | Natural — token transportado no header `Authorization` por qualquer cliente | Acoplada a cookies; menos natural para clientes não-browser |
| Fluxo de refresh token | Alto | Direto — access 30 min + refresh 7 dias com rotação (RF11) | Possível, mas redundante frente ao próprio modelo de sessão |
| Simplicidade do filtro | Médio | Boa — `JwtAuthenticationFilter` valida assinatura e claims | Boa — gerenciada pelo container, mas exige store |
| Revogação imediata | Médio | Limitada por natureza — mitigada por blacklist Redis de `jti` (ver GDE-003) | Imediata — basta invalidar a sessão no store |

### 5. Decisão tomada

**Alternativa A — JWT stateless (HS256) com access + refresh token.**

O JWT stateless atende aos requisitos de escalabilidade horizontal e suporte a múltiplos clientes sem manter estado de sessão no servidor. O `JwtService` emite access token de 30 min (1.800.000 ms) e refresh token de 7 dias (604.800.000 ms), com claims `type` e `jti`; o `SecurityConfig` opera em modo STATELESS, com CSRF desabilitado e BCrypt como encoder. A limitação natural de revogação foi tratada com a blacklist de `jti` em Redis (GDE-003).

- **Responsável pela aprovação:** Cézar Velazquez (Tech Lead / Arquiteto)

### 6. Consequências

- O `JwtAuthenticationFilter` valida assinatura e claims a cada request; as rotas `/api/v1/auth/**` e `/actuator/health` permanecem públicas.
- O refresh token rotation (RF11) exige persistir o refresh token corrente do usuário (campo `refreshToken` da entidade User).
- A revogação imediata depende da blacklist Redis de `jti` para o logout seguro (RF12 / GDE-003).

---

## Decisão GDE-002 — Estratégia de busca nas companhias (paralela vs. sequencial)

### 1. Contexto / problema

A busca de passagens consulta três companhias (Smiles, Azul e Latam) via crawler. O requisito não funcional RNF01 exige resposta em até 30 s. Consultar as três companhias em sequência somaria as latências individuais e tenderia a estourar o SLA. É necessário definir a estratégia de orquestração das três consultas no `SearchService`.

### 2. Alternativas avaliadas

| # | Alternativa | Descrição |
|---|---|---|
| A | Busca paralela com `CompletableFuture` | As três consultas são disparadas em paralelo via `CompletableFuture`, com timeout de 40 s por chamada; resultados combinados, deduplicados (`distinct`) e ordenados por `milhasPrice`. |
| B | Busca sequencial | As três consultas são executadas uma após a outra; a latência total é a soma das três chamadas. |

### 3. Critérios de decisão

| Critério | Peso |
|---|---|
| Atendimento ao SLA de busca (RNF01 ≤ 30 s) | Alto |
| Tempo de resposta percebido pelo usuário | Alto |
| Resiliência a lentidão de uma única companhia | Médio |
| Complexidade de implementação e tratamento de erros | Médio |

### 4. Avaliação (matriz de decisão)

| Critério | Peso | A — Paralela (CompletableFuture) | B — Sequencial |
|---|---|---|---|
| Atendimento ao SLA (≤ 30 s) | Alto | Alta — tempo total ≈ maior latência individual; média medida de 8,3 s | Penalizada — soma das três latências; risco de estourar 30 s |
| Tempo percebido | Alto | Baixo — as três consultas avançam simultaneamente | Alto — usuário espera a soma das chamadas |
| Resiliência a lentidão isolada | Médio | Boa — timeout de 40 s isola a chamada lenta sem travar as demais | Baixa — uma companhia lenta atrasa toda a cadeia |
| Complexidade | Médio | Média — orquestração assíncrona e combinação de resultados | Baixa — fluxo linear, porém inadequado ao SLA |

### 5. Decisão tomada

**Alternativa A — busca paralela com `CompletableFuture`.**

A busca paralela é a única abordagem que atende ao RNF01 com margem confortável. O `SearchService` dispara as três consultas em paralelo, aplica timeout de 40 s por chamada, deduplica os resultados (`distinct`) e os ordena por `milhasPrice`. A medição em operação confirmou média de 8,3 s, muito abaixo do limite de 30 s.

- **Responsável pela aprovação:** Cézar Velazquez (Tech Lead / Arquiteto)

### 6. Consequências

- O `SearchService` orquestra três `CompletableFuture`, exigindo tratamento de timeout e combinação de listas de `FlightResult`.
- A lista de aeroportos (`/api/v1/search/airports?q=`) é mantida fixa no `SearchService` (não em tabela), simplificando a autocompletar de IATA.
- A resiliência depende do timeout de 40 s por companhia para evitar que uma fonte lenta degrade a resposta agregada.

---

## Decisão GDE-003 — Logout seguro com blacklist de tokens em Redis

### 1. Contexto / problema

Por ser stateless (GDE-001), o JWT permanece válido até sua expiração natural, mesmo após o usuário efetuar logout. O RF12 exige logout seguro: um token deslogado não pode mais ser aceito pela API. É necessário um mecanismo de revogação que não reintroduza estado de sessão no servidor da aplicação.

### 2. Alternativas avaliadas

| # | Alternativa | Descrição |
|---|---|---|
| A | Blacklist de `jti` em Redis | No logout, o identificador `jti` do token é gravado em Redis com prefixo `token:invalidated:` e TTL de 7 dias. O filtro de autenticação rejeita tokens cujo `jti` consta na blacklist. |
| B | Reduzir drasticamente o TTL do access token | Tornar o access token muito curto, aceitando que o token deslogado expire rapidamente, sem mecanismo de revogação explícita. |
| C | Reintroduzir estado de sessão server-side | Abandonar parcialmente o modelo stateless e validar sessão ativa a cada request. |

### 3. Critérios de decisão

| Critério | Peso |
|---|---|
| Revogação efetiva no logout (RF12) | Alto |
| Preservação do modelo stateless da aplicação | Alto |
| Performance da verificação por request | Alto |
| Complexidade operacional | Médio |

### 4. Avaliação (matriz de decisão)

| Critério | Peso | A — Blacklist Redis (`jti`) | B — TTL curtíssimo | C — Sessão server-side |
|---|---|---|---|---|
| Revogação no logout | Alto | Efetiva — token deslogado é rejeitado imediatamente | Parcial — token continua válido até expirar | Efetiva — sessão invalidada |
| Modelo stateless | Alto | Preservado — estado de revogação fica no Redis, fora da aplicação | Preservado — mas sem revogação real | Quebrado — reintroduz estado de sessão |
| Performance por request | Alto | Alta — lookup O(1) em Redis com TTL | Alta — nenhuma verificação extra | Penalizada — validação de sessão a cada request |
| Complexidade operacional | Médio | Média — depende do Redis já presente no Docker Compose | Baixa — porém insegura | Alta — store de sessão e sincronização |

### 5. Decisão tomada

**Alternativa A — blacklist de `jti` em Redis.**

A blacklist em Redis (`RedisTokenBlacklist`, prefixo `token:invalidated:`, TTL de 7 dias) é a única alternativa que revoga efetivamente o token no logout sem abandonar o modelo stateless. O Redis já compõe a infraestrutura (Docker Compose), e a verificação por `jti` é um lookup de custo constante. Implementada na S8 (RF12).

- **Responsável pela aprovação:** Cézar Velazquez (Tech Lead / Arquiteto)

### 6. Consequências

- O `JwtService` emite o claim `jti`, consumido pelo `RedisTokenBlacklist` e pelo filtro de autenticação.
- O TTL da blacklist (7 dias) acompanha a validade do refresh token, evitando crescimento indefinido do conjunto de chaves.
- A disponibilidade do Redis torna-se requisito de segurança: indisponibilidade do Redis impacta a verificação de logout.

---

## Decisão GDE-004 — Arquitetura do crawler (serviço separado vs. scraping na API)

### 1. Contexto / problema

A coleta de preços em milhas exige automação de navegador (SeleniumBase) e parsing de HTML das companhias (Smiles, Azul, Latam). Esse tipo de carga é volátil, sujeito a redesigns das companhias (risco R-01) e tem stack tecnológico distinto do da API (Java/Spring). É necessário decidir se o scraping reside dentro da própria API ou em um serviço dedicado.

### 2. Alternativas avaliadas

| # | Alternativa | Descrição |
|---|---|---|
| A | Crawler em serviço separado (FastAPI + SeleniumBase) | Serviço Python independente (FastAPI 0.111 / SeleniumBase 4.27.4) com endpoint `POST /search/{airline}` e parsers próprios (Smiles/Azul/Latam via BeautifulSoup). A API consome o crawler via HTTP. |
| B | Scraping embutido na API (Java/Spring) | A automação de navegador e o parsing de HTML residem no próprio serviço Spring Boot, acoplados ao ciclo de vida da API. |

### 3. Critérios de decisão

| Critério | Peso |
|---|---|
| Isolamento de falhas e de redesigns das companhias (R-01) | Alto |
| Aderência da stack à tarefa (automação de navegador / parsing) | Alto |
| Independência de deploy e escalabilidade do crawler | Médio |
| Acoplamento com o ciclo de vida da API | Médio |

### 4. Avaliação (matriz de decisão)

| Critério | Peso | A — Serviço separado (FastAPI/Selenium) | B — Scraping na API |
|---|---|---|---|
| Isolamento de falhas | Alto | Alto — falha ou redesign afeta apenas o crawler; parsers ajustados isoladamente | Baixo — instabilidade de scraping impacta diretamente a API |
| Aderência da stack | Alto | Alta — Python/SeleniumBase/BeautifulSoup é ecossistema natural para scraping | Baixa — automação de navegador é menos idiomática no stack Java |
| Independência de deploy | Médio | Alta — crawler versionado e implantado separadamente (repositório próprio) | Baixa — qualquer ajuste de parser exige redeploy da API |
| Acoplamento com a API | Médio | Baixo — comunicação por HTTP; CORS restrito à origem da API | Alto — scraping compartilha recursos e ciclo de vida da API |

### 5. Decisão tomada

**Alternativa A — crawler em serviço separado (FastAPI + SeleniumBase).**

O crawler em serviço dedicado isola o componente mais volátil do sistema (sujeito a redesigns das companhias — risco R-01, materializado na S8 com MF-59) e usa a stack mais adequada (FastAPI / SeleniumBase / BeautifulSoup). O serviço expõe `GET /health` e `POST /search/{airline}` (404 para companhia inválida), com CORS restrito à origem da API, e é versionado em repositório próprio (`MilhasFacil_crawler`).

- **Responsável pela aprovação:** Cézar Velazquez (Tech Lead / Arquiteto)

### 6. Consequências

- O crawler é mantido em repositório e pipeline próprios, com ajustes de parser independentes do deploy da API (ex.: `fix/MF-crawler-regex-smiles-redesign`).
- O DTO `SearchRequest` do crawler contempla `max_miles` e `cabin_type` (default ECONOMY), suportando os filtros avançados da S9.
- A comunicação entre API e crawler é feita por HTTP com CORS restrito à origem da API, exigindo orquestração de ambos via Docker Compose.

---

## Decisão GDE-005 — Exclusão de rotas favoritas (lógica vs. física)

### 1. Contexto / problema

O recurso de rotas favoritas (RoutePreference) alimenta os alertas agendados. Ao remover uma rota favorita (DELETE `/api/v1/route-preferences/{id}`), é preciso decidir se o registro é apagado fisicamente do banco ou marcado como inativo. A decisão impacta histórico, auditoria e a lógica do agendador de alertas.

### 2. Alternativas avaliadas

| # | Alternativa | Descrição |
|---|---|---|
| A | Exclusão lógica (`active = false`) | O DELETE marca o registro como inativo (`active = false`), preservando-o no banco. O agendador considera apenas rotas ativas. |
| B | Exclusão física | O DELETE remove o registro definitivamente da tabela `route_preferences`. |

### 3. Critérios de decisão

| Critério | Peso |
|---|---|
| Preservação de histórico e auditoria | Alto |
| Possibilidade de reativação/recuperação | Médio |
| Simplicidade do modelo e das queries | Médio |
| Consistência com o agendador de alertas | Alto |

### 4. Avaliação (matriz de decisão)

| Critério | Peso | A — Exclusão lógica (`active=false`) | B — Exclusão física |
|---|---|---|---|
| Preservação de histórico | Alto | Alta — registro permanece para auditoria | Nenhuma — registro é perdido |
| Reativação/recuperação | Médio | Possível — basta retornar `active = true` | Impossível sem recadastro |
| Simplicidade do modelo | Médio | Média — queries filtram por `active` | Alta — sem flag, porém sem histórico |
| Consistência com o agendador | Alto | Alta — `ScheduledAlertService` opera apenas sobre rotas ativas | Adequada, mas sem rastro do que foi removido |

### 5. Decisão tomada

**Alternativa A — exclusão lógica (`active = false`).**

A exclusão lógica preserva o histórico das rotas favoritas e permite reativação, ao custo de filtrar por `active` nas consultas. O DELETE `/api/v1/route-preferences/{id}` retorna 204 e marca `active = false`; o `ScheduledAlertService` (cron `0 0 */6 * * *`, com dedupe origem-destino-milhas) considera apenas rotas ativas ao disparar alertas.

- **Responsável pela aprovação:** Cézar Velazquez (Tech Lead / Arquiteto)

### 6. Consequências

- A entidade `RoutePreference` mantém o campo `active`; todas as consultas de rotas favoritas filtram por `active = true`.
- O agendador de alertas opera exclusivamente sobre rotas ativas, evitando notificações para rotas removidas.
- Registros inativos permanecem disponíveis para auditoria e eventual reativação, sem reuso de identificador.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Emissão inicial — evidência do ciclo S1–S9 (MR-MPS-SW:2024 Nível C). |
