# Registro de Análise de Decisão — Cadastro de Clientes · Rede D1000

| Campo | Valor |
|---|---|
| **Documento** | GDE-PROFARMA01-001 |
| **Projeto** | Cadastro de Clientes — Rede D1000 |
| **Cliente** | Profarma S.A. / Rede D1000 |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GDE (evidência de projeto) |

---

## Decisão GDE-001 — Banco de dados para persistência do cadastro de clientes

### 1. Contexto / problema

O sistema precisa persistir e consultar uma base de ~7 milhões de CPFs com alta frequência de leitura (múltiplos canais simultâneos), suportar JSONB para o mecanismo de outbox de integração e para tabelas de auditoria, e ser hospedado na nuvem Microsoft Azure. A escolha do banco de dados é uma decisão arquitetural irreversível que impacta modelo de dados, infraestrutura, operações e custo ao longo de toda a vida do sistema.

### 2. Alternativas avaliadas

| # | Alternativa | Descrição |
|---|---|---|
| A | PostgreSQL | Banco relacional open-source com suporte nativo a JSONB, disponível no Azure via Azure Database for PostgreSQL Flexible Server. Compatível com o padrão de outbox e auditoria. Forte ecossistema .NET (EF Core, Dapper). |
| B | SQL Server | Banco relacional da Microsoft, nativo no Azure (Azure SQL). Alta integração com o ecossistema MS, mas sem suporte a JSONB nativo; JSON armazenado como NVARCHAR com funções específicas. Custo de licença embutido no serviço. |
| C | MySQL | Banco relacional open-source; suporte a JSON desde v5.7, mas com limitações em indexação e pesquisa de campos JSON comparado ao JSONB do PostgreSQL. Menor adoção no ecossistema .NET corporativo. |
| D | MongoDB | Banco NoSQL orientado a documentos; armazenamento flexível de documentos JSON nativo. Ausência de transações ACID completas em cenários distribuídos complexos e menor maturidade do ORM .NET; maior distância do modelo relacional já dominado pela equipe. |

### 3. Critérios de decisão

| Critério | Peso |
|---|---|
| Suporte nativo a JSONB para outbox e auditoria | Alto |
| Compatibilidade com Azure e disponibilidade como serviço gerenciado | Alto |
| Performance em leitura de chave primária (CPF) em alta volumetria | Alto |
| Integração com o stack .NET da equipe (EF Core + Dapper) | Médio |
| Custo operacional no Azure | Médio |
| Curva de aprendizado da equipe | Baixo |

### 4. Avaliação (matriz de decisão)

| Critério | Peso | A — PostgreSQL | B — SQL Server | C — MySQL | D — MongoDB |
|---|---|---|---|---|---|
| Suporte nativo a JSONB | Alto | Nativo e completo — JSONB indexável, operadores avançados | Parcial — JSON como NVARCHAR, sem indexação nativa eficiente | Parcial — JSON indexável, mas inferior ao JSONB | Nativo — modelo de documentos, mas sem JSONB do tipo relacional |
| Compatibilidade Azure | Alto | Azure Database for PostgreSQL Flexible Server — gerenciado e maduro | Azure SQL — nativo e maduro | Azure Database for MySQL — gerenciado, mas menos adotado no enterprise | Azure Cosmos DB for MongoDB — gerenciado, mas com diferenças de compatibilidade |
| Performance em leitura de CPF | Alto | Excelente — índices B-tree em VARCHAR(11) com planner maduro | Excelente — índices clustered/non-clustered eficientes | Boa — índices similares, mas planner menos sofisticado | Boa para documentos, mas overhead de mapeamento para modelo relacional |
| Integração .NET | Médio | Excelente — EF Core + Npgsql, Dapper totalmente suportados | Excelente — EF Core + SqlClient, stack nativo MS | Boa — EF Core + MySqlConnector disponíveis | Boa — driver oficial MongoDB .NET, mas sem ORM relacional |
| Custo Azure | Médio | Favorável — open-source, sem licença adicional | Desfavorável — licença SQL Server embutida eleva o custo | Favorável — open-source, custo similar ao PostgreSQL | Médio — Cosmos DB com custo por RU/s pode ser imprevisível |
| Curva de aprendizado | Baixo | Baixa — equipe já familiarizada | Baixa — equipe conhece | Baixa | Média — requer mudança de paradigma |
| **Avaliação geral** | | Melhor opção: combina JSONB nativo, custo favorável e stack .NET maduro | Penalizado pelo custo e ausência de JSONB real | Adequado, mas inferior ao PostgreSQL em JSONB e ecossistema | Incompatível com modelo relacional e outbox transacional |

### 5. Decisão tomada

**Alternativa A — PostgreSQL** hospedado no Azure Database for PostgreSQL Flexible Server.

O PostgreSQL é a única alternativa que atende simultaneamente aos três requisitos críticos: JSONB nativo para outbox e auditoria, integração madura com o stack .NET (EF Core para escrita, Dapper para leitura) e custo operacional sem licenciamento adicional. A escolha simplifica o modelo de outbox transacional, que depende de uma tabela de eventos JSONB consultada por worker assíncrono.

- **Responsável pela aprovação:** Armando Junior (Tech Lead / Gestor de TI — Rede D1000)
- **Data da decisão:** 09/05/2025

### 6. Consequências

- O modelo de dados, migrations e scripts de carga inicial são desenvolvidos exclusivamente para PostgreSQL; migração futura para outro banco exigiria reescrita completa.
- O padrão de outbox utiliza uma tabela `outbox_events` com coluna JSONB `payload`, consultada por worker a cada ciclo de polling.
- O Azure Database for PostgreSQL Flexible Server deve ser provisionado com réplica de leitura se o volume de leituras simultâneas exceder a capacidade da instância primária.

---

## Decisão GDE-002 — Chave primária da entidade Cliente

### 1. Contexto / problema

O modelo de dados precisa definir a chave primária da tabela `clientes`. Todos os canais de atendimento (PDV, Balcão, Call Center, OMNI/VTEX) consultam o cadastro exclusivamente por CPF. Usar um identificador interno (UUID) como PK exigiria um índice único no CPF e joins adicionais em todas as consultas dos canais, aumentando a latência e a complexidade das queries.

### 2. Alternativas avaliadas

| # | Alternativa | Descrição |
|---|---|---|
| A | CPF como chave primária (VARCHAR(11)) | CPF como PK natural e direta. Elimina a necessidade de índice separado no CPF; todas as consultas por CPF são lookups diretos na PK. |
| B | UUID como chave primária | UUID gerado internamente como PK técnico. CPF seria coluna com índice único. Joins entre tabelas relacionadas usariam UUID. |

### 3. Critérios de decisão

| Critério | Peso |
|---|---|
| Performance de leitura por CPF (principal operação de todos os canais) | Alto |
| Simplicidade do modelo de dados e das queries | Alto |
| Unicidade garantida do CPF (requisito de negócio) | Alto |
| Portabilidade do identificador entre sistemas | Médio |
| Geração de PK sem dependência de lógica de negócio | Baixo |

### 4. Avaliação (matriz de decisão)

| Critério | Peso | A — CPF como PK | B — UUID como PK |
|---|---|---|---|
| Performance de leitura por CPF | Alto | Máxima — lookup direto na PK, sem índice adicional | Penalizada — lookup no índice do CPF + acesso ao registro pela PK UUID; latência adicional em alta volumetria |
| Simplicidade do modelo | Alto | Alta — CPF identifica o cliente em todas as tabelas relacionadas; sem chave técnica paralela | Média — duas colunas de identificação (UUID + CPF); joins exigem resolução do UUID antes de retornar dados |
| Unicidade do CPF | Alto | Garantida pela própria PK — sem necessidade de constraint adicional | Garantida por UNIQUE constraint separado — equivalente, mas com overhead de manutenção |
| Portabilidade do identificador | Médio | Alta — CPF é o identificador universal no ecossistema D1000 (ITEC, VTEX, Call Center, Propz) | Média — UUID seria exclusivo do sistema novo; sistemas externos continuariam a usar CPF |
| Geração sem dependência de negócio | Baixo | Dependente — CPF é fornecido externamente; inválido ou duplicado levanta erro de negócio | Independente — UUID gerado internamente sem validação de negócio |
| **Avaliação geral** | | Favorável — alinhado ao domínio, performático e sem redundância | Desfavorável — complexidade sem benefício real neste contexto |

### 5. Decisão tomada

**Alternativa A — CPF como chave primária, tipo VARCHAR(11).**

O sistema é multicanal e todos os canais consultam exclusivamente por CPF. Usar CPF como PK elimina um nível de indireção em todas as operações de leitura, o que é crítico para o SLA de latência (p95 ≤ 200ms no endpoint GET /clientes/{cpf}). A unicidade do CPF é requisito de negócio — torná-lo PK reforça essa regra no próprio modelo relacional.

- **Responsável pela aprovação:** Armando Junior (Tech Lead / Gestor de TI — Rede D1000)
- **Data da decisão:** 09/05/2025

### 6. Consequências

- O CPF armazenado deve ser validado antes da inserção (dígitos verificadores); CPF inválido é rejeitado na camada de aplicação antes de atingir o banco.
- Operações de merge de cadastros duplicados da base legada ITEC devem resolver conflitos de CPF antes da carga inicial.
- Sistemas satélites que consultam o cadastro sempre usam CPF como chave de busca, sem necessidade de resolver um identificador interno.

---

## Decisão GDE-003 — Padrão de integração com o sistema legado ITEC

### 1. Contexto / problema

O ITEC é o sistema legado de PDV da Rede D1000 e precisa ser notificado sempre que um cadastro é criado ou atualizado no novo sistema. O ITEC não suporta consumo de eventos; precisa ser chamado (ou ter dados enviados a ele). A integração deve garantir entrega at-least-once (nenhum evento pode ser perdido silenciosamente), e uma falha temporária no ITEC não pode bloquear a operação de cadastro no novo sistema.

### 2. Alternativas avaliadas

| # | Alternativa | Descrição |
|---|---|---|
| A | Outbox pattern com worker de polling e backoff exponencial | A transação de cadastro persiste o evento em uma tabela `outbox_events` (JSONB). Um worker assíncrono polling essa tabela e tenta enviar ao ITEC. Em caso de falha, aplica backoff exponencial. A transação de cadastro nunca espera o ITEC. |
| B | Chamada HTTP síncrona ao ITEC no momento do cadastro | A API de cadastro realiza a chamada HTTP ao ITEC dentro da mesma request do cliente. Cadastro e notificação ITEC são acoplados temporalmente. |
| C | Publicação direta em Azure Service Bus sem outbox | A transação de cadastro publica uma mensagem no Azure Service Bus. Um consumer dedicado ao ITEC consome a fila e chama o ITEC. Sem tabela de outbox no banco relacional. |

### 3. Critérios de decisão

| Critério | Peso |
|---|---|
| Garantia de at-least-once delivery (nenhum evento perdido) | Alto |
| Desacoplamento: falha no ITEC não bloqueia o cadastro | Alto |
| Consistência transacional (evento só existe se o cadastro existir) | Alto |
| Complexidade de implementação e operação | Médio |
| Observabilidade e reprocessamento manual em caso de falha persistente | Médio |

### 4. Avaliação (matriz de decisão)

| Critério | Peso | A — Outbox + worker polling | B — HTTP síncrono | C — Service Bus direto |
|---|---|---|---|---|
| At-least-once delivery | Alto | Garantido — o evento persiste no banco até confirmação de envio; sem risco de perda por crash da aplicação entre o cadastro e o envio | Não garantido — se a chamada falhar após o commit do cadastro, o evento é perdido sem mecanismo de retry estrutural | Parcial — o Service Bus garante entrega ao consumer, mas não há atomicidade entre o cadastro e a publicação da mensagem |
| Desacoplamento do ITEC | Alto | Total — o worker opera de forma assíncrona; latência ou indisponibilidade do ITEC não afeta o response time do cadastro | Nenhum — falha ou timeout do ITEC falha a request de cadastro ou exige timeout agressivo | Bom — a publicação no Service Bus é rápida; falha do ITEC não bloqueia o cadastro, mas falha na publicação pode |
| Consistência transacional | Alto | Máxima — o evento é inserido na mesma transação do cadastro; impossível ter cadastro sem evento correspondente | Alta — mas falha após o commit do cadastro (antes do HTTP) perde o evento | Baixa — publicação no Service Bus é fora da transação do banco; janela de inconsistência em caso de crash |
| Complexidade | Médio | Média — requer tabela outbox, worker, lógica de backoff e marcação de eventos processados | Baixa — uma chamada HTTP dentro da request | Média — requer infraestrutura de Service Bus e consumer dedicado, sem a simplicidade transacional do outbox |
| Observabilidade | Médio | Alta — tabela outbox é auditável; eventos pendentes, em erro e processados visíveis via query | Baixa — falhas são silenciosas sem logging estruturado | Média — Service Bus oferece dead-letter queue, mas requer correlação com o cadastro |
| **Avaliação geral** | | Melhor opção: única que garante consistência transacional + at-least-once delivery + desacoplamento | Inaceitável para produção: falha no ITEC bloqueia o cadastro | Inadequado: falta atomicidade entre cadastro e publicação da mensagem |

### 5. Decisão tomada

**Alternativa A — Outbox pattern com worker de polling e backoff exponencial.**

O Outbox pattern é a única abordagem que garante simultaneamente: (a) que nenhum evento seja perdido mesmo em cenários de crash, (b) que o cadastro nunca aguarde o ITEC e (c) consistência transacional entre o registro do cliente e o evento de integração. O ITEC historicamente apresenta instabilidades e janelas de manutenção; o desacoplamento é um requisito operacional não negociável.

- **Responsável pela aprovação:** Armando Junior (Tech Lead / Gestor de TI — Rede D1000)
- **Data da decisão:** 16/05/2025

### 6. Consequências

- A tabela `outbox_events` é parte central do modelo de dados e deve ser monitorada continuamente; acúmulo de eventos não processados indica problema no ITEC ou no worker.
- O worker de polling deve implementar backoff exponencial com teto (ex.: máximo de 30 minutos entre tentativas) e alertas quando eventos ficam pendentes por tempo superior ao SLA acordado com o ITEC.
- Eventos com falha persistente após N tentativas devem ser movidos para uma fila de dead-letter auditável, sem descarte silencioso.

---

## Decisão GDE-004 — Estratégia de leitura para o endpoint GET /clientes/{cpf}

### 1. Contexto / problema

O endpoint `GET /clientes/{cpf}` é o mais crítico do sistema: é chamado por PDV, Balcão, Call Center e OMNI simultaneamente, com volume estimado de 500 req/s e SLA de latência p95 ≤ 200ms. O desafio é definir a estratégia de acesso a dados para leitura que atenda ao SLA sem over-engineering.

### 2. Alternativas avaliadas

| # | Alternativa | Descrição |
|---|---|---|
| A | CQRS light — Dapper para leitura, EF Core para escrita | Separação lógica de responsabilidades no mesmo banco: EF Core (com change tracking e validações de domínio) para operações de escrita; Dapper (SQL direto, sem overhead de ORM) para operações de leitura. Sem banco separado. |
| B | EF Core puro para leitura e escrita | Utilizar EF Core com `.AsNoTracking()` para leitura. Reduz a complexidade de ter dois ORMs, mas mantém o overhead do mapeamento do EF Core mesmo nas leituras. |
| C | CQRS completo com banco de leitura separado | Banco de dados separado (ex.: réplica de leitura ou Redis) para o lado de consulta. Máxima performance de leitura, mas com eventual consistency e complexidade de sincronização. |

### 3. Critérios de decisão

| Critério | Peso |
|---|---|
| Latência p95 ≤ 200ms no GET /clientes/{cpf} sob 500 req/s | Alto |
| Simplicidade de implementação e manutenção | Alto |
| Consistência de dados (leitura imediatamente após escrita) | Alto |
| Custo de infraestrutura adicional | Médio |
| Esforço de onboarding para novos desenvolvedores | Baixo |

### 4. Avaliação (matriz de decisão)

| Critério | Peso | A — CQRS light (Dapper leitura) | B — EF Core puro | C — CQRS completo |
|---|---|---|---|---|
| Latência p95 ≤ 200ms | Alto | Alta probabilidade — Dapper executa SQL direto sem overhead de materialização de grafo de objetos; lookup por PK (CPF) em PostgreSQL é sub-milissegundo no banco | Média — `.AsNoTracking()` reduz overhead, mas o mapeamento do EF Core ainda é mais lento que Dapper raw SQL para queries simples em alta frequência | Máxima — banco de leitura dedicado ou cache; mas introduce eventual consistency |
| Simplicidade | Alto | Alta — dois ORMs no mesmo projeto, mas o padrão é amplamente conhecido; separação clara de responsabilidades | Máxima — um único ORM para tudo; menor superfície de código | Baixa — sincronização entre bancos, projeções de read models, gestão de lag de replicação |
| Consistência | Alto | Forte — leitura no mesmo banco; dado está disponível imediatamente após commit da escrita | Forte — mesmo banco | Eventual — réplica pode ter lag; leitura imediatamente após escrita pode retornar dado desatualizado |
| Custo de infraestrutura | Médio | Nenhum adicional — mesmo banco | Nenhum adicional | Adicional — réplica de leitura ou Redis; custo mensal recorrente |
| Onboarding | Baixo | Médio — requer entendimento do padrão CQRS light | Baixo — todos conhecem EF Core | Alto — CQRS completo é o padrão mais complexo |
| **Avaliação geral** | | Melhor equilíbrio: performance de leitura próxima ao ótimo sem infraestrutura adicional e com consistência forte | Adequado para volumes menores; risco de não atingir p95 ≤ 200ms sob 500 req/s em pico | Over-engineering para o contexto atual; eventual consistency incompatível com o uso em PDV em tempo real |

### 5. Decisão tomada

**Alternativa A — CQRS light: Dapper para leitura, EF Core para escrita.**

O SLA de latência (p95 ≤ 200ms a 500 req/s) é o requisito não-funcional mais crítico do sistema. O Dapper executa SQL parametrizado diretamente, eliminando o overhead de materialização de grafo de entidades do EF Core nas leituras de alta frequência. A consistência forte (mesmo banco) é indispensável para o PDV, que lê imediatamente após qualquer atualização de cadastro. O CQRS completo com banco separado introduziria complexidade e custo desproporcionais ao benefício marginal.

- **Responsável pela aprovação:** Cézar Hiraki Velázquez (Tech Lead — Timeware)
- **Data da decisão:** 16/05/2025

### 6. Consequências

- As queries de leitura são escritas em SQL parametrizado via Dapper e residem em repositórios de leitura (`IClienteReadRepository`), separados dos repositórios de escrita EF Core.
- Mudanças no schema do banco impactam tanto os repositórios EF Core quanto as queries Dapper — revisão de ambos é obrigatória em migrações de schema.
- O resultado de medição obtido em produção foi p95 de 142ms, 29% abaixo do limite de 200ms, confirmando a adequação da decisão.

---

## Decisão GDE-005 — Integração com Propz CRM

### 1. Contexto / problema

O Propz CRM é a plataforma de relacionamento e fidelidade da Rede D1000. A integração exige sincronizar os dados cadastrais dos ~7 milhões de CPFs da base, além de enviar atualizações incrementais em tempo operacional. O Propz opera de forma assíncrona e tem SLA de processamento que não admite chamadas síncronas de alta frequência. A estratégia de integração foi inicialmente adiada e formalizada via Change Request (CR-07) em agosto de 2025.

### 2. Alternativas avaliadas

| # | Alternativa | Descrição |
|---|---|---|
| A | Azure Service Bus com worker dedicado | Cada evento de criação/atualização de cliente é publicado em uma fila do Azure Service Bus. Um worker dedicado consome a fila e envia os dados ao Propz via API. Carga inicial via publicação em lote na fila. |
| B | Webhook REST síncrono | A cada cadastro ou atualização, a API chama diretamente o endpoint do Propz de forma síncrona dentro da mesma request. |
| C | Polling batch diário | Um job noturno exporta os registros modificados no dia e envia em lote ao Propz via API de importação. |

### 3. Critérios de decisão

| Critério | Peso |
|---|---|
| Capacidade de processar a carga inicial de 7M de CPFs sem degradar o sistema principal | Alto |
| Alinhamento com o SLA assíncrono do Propz | Alto |
| Desacoplamento: falha no Propz não afeta o cadastro | Alto |
| Latência de sincronização (tempo entre cadastro e disponibilidade no Propz) | Médio |
| Complexidade de implementação | Médio |

### 4. Avaliação (matriz de decisão)

| Critério | Peso | A — Azure Service Bus + worker | B — Webhook REST síncrono | C — Polling batch diário |
|---|---|---|---|---|
| Carga inicial de 7M CPFs | Alto | Excelente — publicação controlada na fila com rate limiting no worker; Propz processa no seu ritmo | Inviável — 7M chamadas síncronas saturariam o Propz e o sistema de cadastro; timeout em larga escala | Adequado — batch noturno pode distribuir a carga inicial, mas processo demora dias |
| Alinhamento com SLA do Propz | Alto | Total — o worker respeita o rate limit da API Propz; mensagens não processadas ficam na fila | Incompatível — Propz não garante resposta síncrona em alta frequência | Parcial — batch é assíncrono por natureza, mas sincronização é diária, não em tempo quase real |
| Desacoplamento | Alto | Total — falha no Propz acumula mensagens na fila sem afetar o cadastro | Nenhum — falha no Propz falha a request de cadastro ou exige timeout agressivo | Total — o job é independente do fluxo de cadastro |
| Latência de sincronização | Médio | Baixa — minutos em condição normal | Mínima — síncrono, mas inviável em escala | Alta — até 24h de defasagem; inaceitável para campanhas em tempo real |
| Complexidade | Médio | Média — requer infraestrutura de Service Bus e worker, mas padrão já existente no projeto (outbox) | Baixa — mas inadequada para o volume | Baixa — mas limitada funcionalmente |
| **Avaliação geral** | | Única opção viável: combina desacoplamento, escalabilidade para 7M CPFs e sincronização em tempo quase real | Inviável em escala para a carga inicial e operação contínua | Funcional apenas para sincronização diária; incompatível com o caso de uso de campanha em tempo real |

### 5. Decisão tomada

**Alternativa A — Azure Service Bus com worker dedicado.**

O Azure Service Bus é a única alternativa que suporta simultaneamente a carga inicial de 7 milhões de CPFs (com controle de throughput no worker), o SLA assíncrono do Propz e o desacoplamento operacional necessário. O padrão de worker com Service Bus já estava estabelecido no projeto (integração ITEC via outbox), reduzindo o esforço de implementação. Formalizado no CR-07 após alinhamento com o time de TI do Propz sobre o protocolo de integração.

- **Responsável pela aprovação:** Armando Junior (Tech Lead / Gestor de TI — Rede D1000)
- **Data da decisão:** 15/08/2025 (CR-07)

### 6. Consequências

- Um worker dedicado ao Propz (`PropzSyncWorker`) consome o Azure Service Bus e gerencia o rate limit da API Propz de forma independente dos demais workers do sistema.
- A carga inicial de 7M CPFs é realizada via publicação em lote controlado na fila, sem impacto no sistema principal de cadastro em operação.
- Mensagens rejeitadas pela API Propz (ex.: CPF inválido no contexto do CRM) são movidas para dead-letter queue e auditadas separadamente, sem bloquear a fila principal.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Time de Melhoria Contínua | Versão inicial — cinco decisões de arquitetura registradas: banco de dados, chave primária, integração ITEC, estratégia de leitura e integração Propz CRM |
