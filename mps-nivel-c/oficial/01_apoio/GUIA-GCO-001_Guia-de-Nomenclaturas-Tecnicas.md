# Guia de Nomenclaturas Técnicas — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | GUIA-GCO-001 — Guia de Nomenclaturas Técnicas |
| **Versão** | 1.1 |
| **Data** | 15/11/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | Tech Lead / Arquiteto, COO (Operações) |
| **Responsável** | Cézar Velázquez |
| **Nota de auditoria** | Para a correspondência deste documento com o modelo de referência, ver a seção final "Rastreabilidade e instrução para auditoria". |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Este guia define os **padrões de nomenclatura técnica** adotados pela Timeware em todas as ferramentas de desenvolvimento e infraestrutura — repositórios, código, banco de dados, recursos Azure, pipelines e segredos. Uma convenção consistente facilita comunicação, busca, integração entre ferramentas e onboarding de novos colaboradores.

Este documento complementa o **Plano de Gerência de Configuração (PLA-GCO-001)**, que define o sistema de controle de configuração, e a **Convenção de Nomenclatura e Versionamento (CONV-ORG-001)**, que define o padrão para artefatos de processo. Aqui o foco é a nomenclatura de artefatos técnicos dos projetos.

---

## 2. Nomenclatura de Projetos e Repositórios

### 2.1. Identificação de projetos

O nome de um projeto define como ele é referenciado em todas as ferramentas — Jira, Confluence, Azure DevOps. A convenção adotada é **kebab-case**:

```
[cliente|domínio]-[sistema]-[módulo]
```

| Componente | Descrição |
|---|---|
| `cliente\|domínio` | Identificador do cliente ou área de negócio |
| `sistema` | Nome do sistema ou produto (`portal`, `erp`, `api`, `gateway`) |
| `modulo` | Módulo ou sub-componente — opcional (`auth`, `relatorios`, `integracao`) |

**Princípios:**
- Letras minúsculas separadas por hífen
- Máximo de 4 segmentos
- Sem espaços, acentos ou caracteres especiais
- Siglas documentadas no README do projeto

### 2.2. Repositórios no GitHub / Azure DevOps

O nome do repositório deve refletir o propósito do código. Padrão:

```
[dominio]-[sistema]-[camada]
```

**Camadas recomendadas:**

| Sufixo | Descrição | Exemplo |
|---|---|---|
| `-api` | Backend REST ou gRPC | `timeware-portal-api` |
| `-frontend` | Aplicação web (Angular, React) | `timeware-portal-frontend` |
| `-worker` | Serviço de processamento assíncrono | `timeware-portal-worker` |
| `-shared` | Biblioteca compartilhada / SDK | `timeware-shared` |
| `-infra` | Infraestrutura como código (Terraform, Bicep) | `timeware-portal-infra` |
| `-pipeline` | Templates de pipeline reutilizáveis | `timeware-devops-pipeline` |
| `-docs` | Documentação técnica | `timeware-arquitetura-docs` |

Use o mesmo nome-base para repositórios relacionados: `timeware-portal-api`, `timeware-portal-frontend`, `timeware-portal-infra`.

Nunca crie repositórios com letras maiúsculas — o GitHub é case-sensitive em alguns sistemas.

### 2.3. Organização por Projects no Azure DevOps

Organize repositórios dentro de Projects por domínio de negócio:

| Project (Azure DevOps) | Repositórios |
|---|---|
| `timeware-[cliente-a]` | `[cliente-a]-portal-api`, `[cliente-a]-portal-frontend`, `[cliente-a]-infra` |
| `timeware-[cliente-b]` | `[cliente-b]-erp-api`, `[cliente-b]-erp-worker` |
| `timeware-plataforma` | `timeware-shared`, `timeware-devops-pipeline` |

---

## 3. Estrutura Interna de Projetos

### 3.1. .NET — Estrutura de Solution

Padrão: `[Empresa].[Produto].[Camada]`

| Projeto (`.csproj`) | Responsabilidade |
|---|---|
| `Timeware.[Produto].Api` | Camada de apresentação (Controllers, Middleware) |
| `Timeware.[Produto].Application` | Casos de uso, Commands, Queries (CQRS) |
| `Timeware.[Produto].Domain` | Entidades, Value Objects, Interfaces de repositório |
| `Timeware.[Produto].Infrastructure` | Implementações de repositório, integrações externas |
| `Timeware.[Produto].Shared` | DTOs, extensões, helpers compartilhados |
| `Timeware.[Produto].Tests.Unit` | Testes unitários |
| `Timeware.[Produto].Tests.Integration` | Testes de integração |

Mantenha `Domain` sem dependências de frameworks externos — apenas lógica de negócio pura.

### 3.2. Node.js / TypeScript — Estrutura de Pastas

Padrão para projetos NestJS ou Express:

| Pasta | Responsabilidade |
|---|---|
| `src/modules/[feature]/` | Feature module (controller, service, dto, entity) |
| `src/shared/` | Guards, interceptors, filters, pipes compartilhados |
| `src/config/` | Configurações de ambiente e conexões |
| `src/database/` | Migrations, seeds, configuração ORM |
| `test/` | Testes e2e |

---

## 4. Nomenclatura de Arquivos

| Contexto | Convenção | Exemplos |
|---|---|---|
| C# / .NET | PascalCase | `UserService.cs`, `OrderController.cs` |
| TypeScript / JavaScript | camelCase ou kebab-case | `userService.ts`, `user-controller.ts` |
| Angular | kebab-case + sufixo | `user-list.component.ts`, `auth.service.ts` |
| React | PascalCase (componentes) | `UserCard.tsx`, `OrderSummary.tsx` |
| Python | snake_case | `user_service.py`, `order_repository.py` |
| SQL (scripts de migration) | kebab-case com numeração sequencial | `0001-create-users-table.sql` |
| YAML / JSON config | kebab-case | `azure-pipelines.yml`, `app-settings.json` |
| Terraform / Bicep | kebab-case | `main.tf`, `storage-account.bicep` |
| Dockerfile | Capitalizado por convenção | `Dockerfile`, `Dockerfile.prod` |

Para scripts SQL de migração, use numeração sequencial obrigatória: `0001-`, `0002-`...

Nunca use espaços em nomes de arquivo — use hífen ou underscore conforme a linguagem.

---

## 5. Nomenclatura de Variáveis e Campos

### 5.1. Por linguagem

| Linguagem | Variáveis locais | Propriedades de classe | Constantes | Campos privados |
|---|---|---|---|---|
| C# | camelCase | PascalCase | `UPPER_SNAKE_CASE` | `_camelCase` |
| TypeScript | camelCase | camelCase | `UPPER_SNAKE_CASE` | `_camelCase` |
| Java | camelCase | camelCase | `UPPER_SNAKE_CASE` | camelCase |
| Python | snake_case | snake_case | `UPPER_SNAKE_CASE` | `_snake_case` |
| Go | camelCase | PascalCase (exportado) | `UPPER_SNAKE_CASE` | camelCase |

### 5.2. Boas práticas de nomenclatura

- **Nomes devem revelar intenção** — evite abreviações obscuras
- **Booleanos:** prefixe com `is`, `has`, `can`, `should` — ex.: `isActive`, `hasPermission`
- **Coleções:** use o plural — ex.: `users`, `orderItems`, `productList`
- **Métodos:** use verbos — ex.: `getUser`, `calculateTotal`, `sendEmail`
- **Evite notação húngara:** não use `strName`, `intAge`
- **Constantes de configuração:** `MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT_MS`
- **Contexto explícito:** prefira `orderId` a `id` dentro de um contexto de `Order`

Variáveis de loop simples (`i`, `j`, `k`) são aceitáveis. Para loops complexos, nomeie semanticamente: `userIndex`, `pageNumber`.

---

## 6. Nomenclatura de Banco de Dados

### 6.1. Schemas

Schemas agrupam objetos por domínio de negócio e devem refletir bounded contexts:

| Schema | Uso | Exemplo de objeto |
|---|---|---|
| `auth` | Autenticação e autorização | `auth.users`, `auth.roles` |
| `financial` | Dados financeiros | `financial.invoices` |
| `catalog` | Catálogo de produtos | `catalog.products` |
| `audit` | Logs e rastreabilidade | `audit.change_log` |
| `integration` | Dados de integração e staging | `integration.erp_orders` |

Evite usar `public` / `dbo` em produção — prefira schemas de domínio.

### 6.2. Tabelas

Convenção: `snake_case`, plural, sem prefixo de schema no nome.

| Padrão | Exemplo correto | Evitar |
|---|---|---|
| snake_case plural | `order_items` | `OrderItems`, `tblOrderItems`, `ORDERITEMS` |
| Substantivos | `users`, `products`, `invoices` | `get_user`, `manage_product` |
| Sem prefixos | `customers` | `tbl_customers`, `tb_customers` |
| Relacionamento N:N | `user_roles` | `userrole`, `UserRole` |

### 6.3. Colunas

| Tipo de coluna | Convenção | Exemplos |
|---|---|---|
| Chave primária | `id` (serial/uuid) | `id BIGSERIAL`, `id UUID DEFAULT gen_random_uuid()` |
| Chave estrangeira | `[tabela_singular]_id` | `customer_id`, `order_id`, `product_id` |
| Booleanos | `is_` ou `has_` | `is_active`, `is_deleted`, `has_discount` |
| Datas | sufixo `_at` ou `_date` | `created_at`, `updated_at`, `deleted_at`, `due_date` |
| Status / Tipo | sufixo `_status` ou `_type` | `order_status`, `payment_type` |
| Valor monetário | sufixo `_amount` ou `_value` | `total_amount`, `discount_value` |
| JSON / JSONB | sufixo `_data` ou `_metadata` | `extra_data`, `audit_metadata` |

### 6.4. Constraints, índices e outros objetos

| Objeto | Padrão de nome | Exemplo |
|---|---|---|
| Primary Key | `pk_[tabela]` | `pk_orders` |
| Foreign Key | `fk_[tabela]_[coluna]` | `fk_orders_customer_id` |
| Unique | `uq_[tabela]_[coluna(s)]` | `uq_users_email` |
| Índice | `idx_[tabela]_[coluna(s)]` | `idx_orders_created_at` |
| Índice composto | `idx_[tabela]_[col1]_[col2]` | `idx_orders_status_customer_id` |
| Check Constraint | `ck_[tabela]_[regra]` | `ck_products_price_positive` |
| Trigger | `trg_[tabela]_[acao]` | `trg_orders_before_update` |
| View | `vw_[descricao]` | `vw_active_customers` |
| Stored Procedure | `sp_[acao]_[entidade]` | `sp_calculate_invoice_total` |
| Function | `fn_[acao]_[retorno]` | `fn_get_customer_balance` |

Nunca use prefixos como `tbl_`, `sp_`, `vw_` nas próprias tabelas/procedures — use schemas para segregação. Evite abreviações em nomes de colunas: prefira `user_name`, `order_date` a `usr_nm`, `ord_dt`.

---

## 7. Nomenclatura de Recursos no Azure

A Microsoft recomenda uma convenção padronizada para todos os recursos Azure (Cloud Adoption Framework). Seguir esse padrão garante consistência em subscription, resource groups, IAM e billing.

### 7.1. Padrão geral

```
[tipo]-[workload]-[ambiente]-[região]-[instância]
```

| Segmento | Descrição | Valores comuns |
|---|---|---|
| `tipo` | Abreviação do tipo de recurso | `aks`, `acr`, `kv`, `st`, `func` |
| `workload` | Nome do sistema ou produto | `timeware-portal`, `timeware-erp` |
| `ambiente` | Ambiente de implantação | `dev`, `hml`, `prd`, `stg` |
| `região` | Código da região Azure | `brs` (Brazil South), `eus` (East US) |
| `instância` | Número sequencial quando necessário | `01`, `02` |

### 7.2. Abreviações por tipo de recurso

| Recurso Azure | Abreviação | Exemplo completo |
|---|---|---|
| Resource Group | `rg-` | `rg-timeware-portal-prd-brs` |
| AKS Cluster | `aks-` | `aks-timeware-portal-prd-brs-01` |
| Azure Container Registry | `acr` | `acrtimewareportalprdbrs` (sem hífen) |
| Azure Container App | `ca-` | `ca-timeware-portal-api-prd-brs` |
| Azure Container Apps Environment | `cae-` | `cae-timeware-prd-brs` |
| Key Vault | `kv-` | `kv-timeware-portal-prd-brs` |
| Storage Account | `st` | `sttimewareportalprdbrs` (sem hífen) |
| Service Bus | `sb-` | `sb-timeware-portal-prd-brs` |
| App Service / Web App | `app-` | `app-timeware-portal-api-prd-brs` |
| App Service Plan | `asp-` | `asp-timeware-portal-prd-brs` |
| Virtual Network | `vnet-` | `vnet-timeware-prd-brs` |
| Subnet | `snet-` | `snet-timeware-aks-prd-brs` |
| NSG | `nsg-` | `nsg-timeware-prd-brs` |
| Log Analytics Workspace | `log-` | `log-timeware-prd-brs` |
| Application Insights | `appi-` | `appi-timeware-portal-prd-brs` |
| Managed Identity | `id-` | `id-timeware-aks-prd-brs` |
| PostgreSQL Flexible Server | `psql-` | `psql-timeware-portal-prd-brs` |
| Azure DevOps Agent Pool | `pool-` | `pool-timeware-prd-brs` |

**Atenção:** Storage Account e ACR não suportam hífens — use apenas letras minúsculas e números (máximo 24 e 50 caracteres, respectivamente).

Resource Groups devem agrupar recursos pelo ciclo de vida, não pelo tipo. Exemplo: todos os recursos do portal em produção ficam em `rg-timeware-portal-prd-brs`.

### 7.3. Tags obrigatórias em todos os recursos

| Tag | Descrição | Exemplo de valor |
|---|---|---|
| `Environment` | Ambiente do recurso | `production`, `homologation`, `development` |
| `Project` | Nome do projeto/produto | `timeware-portal` |
| `Owner` | Time ou responsável | `team-devops` |
| `CostCenter` | Centro de custo para billing | `CC-0042` |
| `ManagedBy` | Método de provisionamento | `terraform`, `bicep`, `manual` |

---

## 8. Nomenclatura de Pipelines — Azure DevOps

### 8.1. Nome do pipeline

Padrão: `[projeto]-[camada]-[acao]-[ambiente]`

| Tipo de pipeline | Padrão de nome | Exemplo |
|---|---|---|
| CI (Build) | `[projeto]-[camada]-ci` | `timeware-portal-api-ci` |
| CD (Deploy) | `[projeto]-[camada]-cd-[ambiente]` | `timeware-portal-api-cd-prd` |
| CI/CD unificado | `[projeto]-[camada]-cicd-[ambiente]` | `timeware-portal-api-cicd-hml` |
| Infra (IaC) | `[projeto]-infra-[acao]-[ambiente]` | `timeware-portal-infra-deploy-prd` |
| Release de lib | `[lib]-release` | `timeware-shared-release` |
| Template reutilizável | `template-[funcao]` | `template-docker-build` |

### 8.2. Variáveis em pipelines YAML

| Tipo | Convenção | Exemplos |
|---|---|---|
| Variável de ambiente | `UPPER_SNAKE_CASE` | `DOCKER_IMAGE_NAME`, `ACR_LOGIN_SERVER` |
| Variável de pipeline (`var:`) | camelCase | `imageTag`, `buildNumber` |
| Parâmetro de template | camelCase | `environment`, `containerAppName` |
| Variável de grupo (`variable group`) | `UPPER_SNAKE_CASE` | `SQL_CONNECTION_STRING` |
| Variável sensível (secret) | `UPPER_SNAKE_CASE` | `ACR_PASSWORD`, `SQL_PASSWORD` |

Nunca armazene segredos diretamente no YAML — use Variable Groups linkados ao Azure Key Vault.

Prefixe variáveis de grupo por ambiente em cenários multi-env: `PRD_SQL_CONNECTION_STRING`, `HML_SQL_CONNECTION_STRING`.

### 8.3. Stages, jobs e steps

| Elemento | Convenção | Exemplos |
|---|---|---|
| `stage:` | PascalCase descritivo | `Build`, `Test`, `DeployHml`, `DeployPrd` |
| `job:` | PascalCase descritivo | `BuildDockerImage`, `RunUnitTests` |
| `step` (displayName) | Descrição em PT/EN | `'Build Docker Image'`, `'Push to ACR'` |

---

## 9. Nomenclatura de Segredos no Azure Key Vault

### 9.1. Restrições do Key Vault

- Apenas letras, números e hífens (`-`)
- Sem underscore, sem ponto
- Máximo de 127 caracteres
- Prefira kebab-case consistente em letras minúsculas

### 9.2. Padrão para secrets

```
[aplicacao]--[Categoria]--[Chave]
```

O duplo hífen (`--`) funciona como separador de hierarquia. O .NET Configuration Provider converte automaticamente `--` em `:` (dois pontos) na configuração da aplicação.

| Categoria | Padrão | Exemplos de secret name |
|---|---|---|
| Banco de dados | `[app]--ConnectionStrings--[db]` | `timeware-portal--ConnectionStrings--Default` |
| API Keys externas | `[app]--ExternalApis--[servico]--ApiKey` | `timeware-portal--ExternalApis--Correios--ApiKey` |
| Credenciais de serviço | `[app]--[servico]--[credencial]` | `timeware-portal--Smtp--Password` |
| JWT / Auth | `[app]--Jwt--[chave]` | `timeware-portal--Jwt--SecretKey` |
| Azure Services | `[app]--Azure--[servico]--[chave]` | `timeware-portal--Azure--ServiceBus--ConnectionString` |
| Compartilhado (multi-app) | `shared--[categoria]--[chave]` | `shared--Smtp--Password` |

Não inclua o ambiente no nome do secret — use Key Vaults diferentes por ambiente (`kv-timeware-portal-hml-brs`, `kv-timeware-portal-prd-brs`).

Nunca coloque valores de secret em YAML de pipeline, `appsettings.json` ou código-fonte, mesmo em ambientes de desenvolvimento.

### 9.3. Nomenclatura de keys (criptografia)

| Tipo de key | Padrão | Exemplo |
|---|---|---|
| Chave de criptografia de dados | `[app]-data-encryption-key` | `timeware-portal-data-encryption-key` |
| Chave de assinatura de token | `[app]-token-signing-key` | `timeware-portal-token-signing-key` |
| Chave de wrap (KEK) | `[app]-kek-[versao]` | `timeware-portal-kek-v1` |

### 9.4. Nomenclatura de certificados

| Tipo | Padrão | Exemplo |
|---|---|---|
| TLS/SSL de domínio | `[dominio]-tls` | `timeware-portal-tls` |
| mTLS cliente | `[app]-client-[servico]` | `timeware-portal-client-erp` |
| Assinatura de código | `[app]-codesign` | `timeware-codesign` |

---

## 10. Referência Rápida

| Contexto | Convenção | Exemplo |
|---|---|---|
| Projetos | kebab-case: `[dominio]-[sistema]-[modulo]` | `timeware-portal-api` |
| Repositórios GitHub/DevOps | kebab-case: `[dominio]-[sistema]-[camada]` | `timeware-portal-frontend` |
| Projetos .NET | PascalCase com pontos: `Empresa.Produto.Camada` | `Timeware.Portal.Application` |
| Arquivos C# | PascalCase | `OrderService.cs` |
| Arquivos TypeScript | kebab-case com sufixo | `user-list.component.ts` |
| Arquivos SQL migration | numeração + kebab-case | `0001-create-orders-table.sql` |
| Variáveis (C# / TS) | camelCase (local) / PascalCase (propriedade) | `orderId` / `OrderId` |
| Constantes | `UPPER_SNAKE_CASE` | `MAX_RETRY_COUNT` |
| Tabelas BD | snake_case plural | `order_items` |
| Colunas BD — FK | `[tabela_singular]_id` | `customer_id` |
| Colunas BD — datas | `[campo]_at` | `created_at`, `deleted_at` |
| Recursos Azure | `[tipo]-[workload]-[env]-[regiao]-[inst]` | `aks-timeware-portal-prd-brs-01` |
| Resource Group | `rg-[workload]-[env]-[regiao]` | `rg-timeware-portal-prd-brs` |
| Key Vault Secret | `[app]--[Categoria]--[Chave]` | `timeware-portal--Jwt--SecretKey` |
| Pipeline YAML var | `UPPER_SNAKE_CASE` | `ACR_LOGIN_SERVER` |
| Pipeline stage/job | PascalCase | `DeployPrd`, `BuildDockerImage` |

Este documento deve ser revisado a cada 6 meses ou quando houver mudança relevante de stack.

---

## 11. Documentos relacionados

- PLA-GCO-001 — Plano de Gerência de Configuração
- CONV-ORG-001 — Convenção de Nomenclatura e Versionamento
- PRO-GPC-001 — Processo-Padrão Organizacional

---

## 12. Rastreabilidade e instrução para auditoria

*Esta seção é destinada à equipe de avaliação e relaciona o conteúdo deste documento aos resultados esperados do modelo de referência MR-MPS-SW. No corpo, o conteúdo é descrito na linguagem operacional da Timeware; o quadro abaixo indica onde cada resultado é atendido.*

Este documento complementa os resultados do processo **Gerência de Configuração (GCO)** do MR-MPS-SW:2024, especificamente no que diz respeito à identificação e padronização dos itens de configuração e ao ambiente-padrão de trabalho.

| Resultado | Onde é atendido neste documento |
|---|---|
| GCO 1 — itens de configuração identificados com níveis de controle | §2 (repositórios), §7 (recursos Azure), §8 (pipelines), §9 (segredos/Key Vault) |
| GCO 2 — sistema de GC e controle de mudanças estabelecido | §2.3 (organização Azure DevOps), §8 (nomenclatura de pipelines) |
| GPC 8 — ambientes-padrão de trabalho estabelecidos | §7 (recursos Azure) e §8 (pipelines) complementam o PLA-GPC-001 §3 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Campo "Responsável" adicionado ao cabeçalho: Cézar Velázquez |
| 1.0 | 15/11/2025 | Tech Lead / Arquiteto | Definição inicial do guia de nomenclaturas técnicas |
