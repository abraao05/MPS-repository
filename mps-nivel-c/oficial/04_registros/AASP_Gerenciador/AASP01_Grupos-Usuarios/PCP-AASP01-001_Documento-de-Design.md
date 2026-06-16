# Documento de Design — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | PCP-AASP01-001 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.1 |
| **Data** | 26/05/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | PCP (evidência de projeto) |

---

## 1. Visão geral da solução

O microsserviço **ms.auxo.gruposusuarios** e uma Web API RESTful desenvolvida em .NET Framework 4.7.2 com Dapper como ORM e SQL Server (banco principal auxo3) como banco de dados. Integra-se ao microsserviço **ms.temis.vinculos** (banco temis3) via HTTP REST para sincronização de vínculos de usuários.

A solução provém funcionalidades completas de gestao de grupos de usuários do sistema Gerenciador da AASP, incluindo:

- **CRUD de grupos**: criação, listagem, busca por ID, atualização e remoção lógica (soft delete) de grupos.
- **Controle de permissões RBAC**: definição e alteração das permissões associadas a cada grupo (Leitura, Escrita, Exclusao, Administracao, Relatorio).
- **Vínculo usuário-grupo**: associação e desassociação de usuários a grupos, com propagação automática ao ms.temis.vinculos.
- **Auditoria e log**: registro automático de todas as operações críticas (CREATE, UPDATE, DELETE, ADD_USER, REMOVE_USER) na tabela AuditoriaGrupos.
- **Relatórios**: endpoint consolidado para exportação de dados de grupos e usuários para fins gerenciais.

A API segue o padrão arquitetural estabelecido no sistema Gerenciador da AASP, utilizando autenticação via JWT Bearer Token e expondo documentação interativa via Swagger/OpenAPI.

---

## 2. Arquitetura da solução

### 2.1 Stack tecnológico

| Camada | Tecnologia | Justificativa |
|---|---|---|
| Framework de API | ASP.NET Web API (.NET Framework 4.7.2) | Padrão do projeto Gerenciador AASP; compatibilidade com infraestrutura existente do cliente |
| ORM / Acesso a dados | Dapper 2.x | Ver GDE-AASP01-001 (GDE-001) — compatibilidade com .NET FW 4.7.2, performance superior ao EF Core em queries complexas, padrão já adotado no projeto Gerenciador |
| Banco de dados principal | SQL Server — banco auxo3 | Banco existente do sistema Gerenciador da AASP; tabelas do módulo criadas via migrations versionadas |
| Banco de integração | SQL Server — banco temis3 (acesso indireto via ms.temis.vinculos) | Banco do microsserviço de vínculos; acesso exclusivamente via HTTP REST, nunca por query direta |
| Integração externa | HTTP REST — ms.temis.vinculos | Ver GDE e ITP-AASP01-001; desacoplamento entre domínios, contrato de API versionado |
| Autenticação | JWT Bearer Token | Padrão do Gerenciador AASP; tokens emitidos pelo serviço de autenticação central |
| Documentação de API | Swagger / OpenAPI (Swashbuckle) | Gerado automaticamente a partir das anotações do código; validado em cada sprint |
| CI/CD | Azure DevOps Pipelines | Padrão Timeware; pipeline automatiza build, testes e análise estática a cada PR |
| Controle de versão | Git (Azure DevOps) — Git Flow | Padrão Timeware; rastreabilidade completa de mudanças por feature e sprint |

### 2.2 Diagrama de camadas

```
+----------------------------------+
|         Controllers (API)         |
|  /grupos · /grupos/{id} · etc.    |
+----------------------------------+
               |
+----------------------------------+
|       Services / UseCases         |
|  GrupoService                     |
|  PermissaoService                 |
|  VinculoService                   |
|  RelatorioService                 |
+----------------------------------+
               |
+----------------------------------+
|   Repositories (Dapper Queries)   |
|  GrupoRepository                  |
|  PermissaoRepository              |
|  VinculoRepository                |
|  AuditoriaRepository              |
+----------------------------------+
               |
+----------------------------------+
|   SQL Server -- banco auxo3       |
|  Grupos                           |
|  PermissoesGrupo                  |
|  UsuariosGrupo                    |
|  AuditoriaGrupos                  |
+----------------------------------+
               |
          HTTP REST
               |
+----------------------------------+
| ms.temis.vinculos (banco temis3)  |
+----------------------------------+
```

**Descrição das camadas:**

- **Controllers**: recebem requisições HTTP, validam o modelo de entrada (DataAnnotations), delegam ao Service correspondente e retornam responses padronizados (200/201/400/404/500). Nenhuma lógica de negócio nos controllers.
- **Services / UseCases**: contém toda a lógica de negócio — validações de domínio, orquestração de chamadas a repositories e ao cliente HTTP do ms.temis.vinculos, disparo de auditoria.
- **Repositories**: encapsulam queries SQL via Dapper. Cada repository corresponde a uma entidade do banco. Queries parametrizadas para prevenção de SQL Injection. Sem lógica de negócio.
- **Banco auxo3**: banco principal do sistema Gerenciador. Tabelas do módulo criadas via migrations versionadas em /sql/migrations/.
- **ms.temis.vinculos**: microsserviço externo acessado via HttpClient. Comunicação assíncrona com timeout configurado (5s) e retry automático (1 tentativa adicional em caso de falha de rede).

---

## 3. Modelo de dados (banco auxo3)

### 3.1 Tabela Grupos

| Campo | Tipo | Restrição | Descrição |
|---|---|---|---|
| Id | int | PK, IDENTITY(1,1), NOT NULL | Identificador único do grupo, gerado automaticamente pelo banco |
| Nome | nvarchar(100) | NOT NULL, UNIQUE | Nome do grupo — deve ser único no sistema; usado como identificador legível |
| Descricao | nvarchar(500) | NULL | Descrição opcional do propósito e escopo do grupo |
| Ativo | bit | NOT NULL, DEFAULT 1 | Flag de soft delete: 1 = ativo, 0 = removido logicamente. Grupos inativos não aparecem nas listagens padrão |
| DataCriacao | datetime | NOT NULL, DEFAULT GETDATE() | Timestamp de criação do registro, preenchido automaticamente pelo banco |
| DataAtualizacao | datetime | NULL | Timestamp da última atualização; preenchido pelo sistema a cada PUT /grupos/{id} |

### 3.2 Tabela PermissoesGrupo

| Campo | Tipo | Restrição | Descrição |
|---|---|---|---|
| Id | int | PK, IDENTITY(1,1), NOT NULL | Identificador único da permissão |
| GrupoId | int | FK -> Grupos.Id, NOT NULL | Referência ao grupo ao qual a permissão pertence |
| Permissao | nvarchar(50) | NOT NULL | Código da permissão. Valores válidos: Leitura, Escrita, Exclusao, Administracao, Relatorio |

**Regra de negócio:** A atualização de permissões (PUT /grupos/{id}/permissoes) realiza substituição completa — remove todas as permissões existentes do grupo e insere as novas fornecidas no payload. Operação atomica em transação SQL.

### 3.3 Tabela UsuariosGrupo

| Campo | Tipo | Restrição | Descrição |
|---|---|---|---|
| Id | int | PK, IDENTITY(1,1), NOT NULL | Identificador único do vínculo usuário-grupo |
| GrupoId | int | FK -> Grupos.Id, NOT NULL | Referência ao grupo |
| UsuarioId | int | FK -> Usuarios.Id, NOT NULL | Referência ao usuário do sistema Gerenciador |
| DataVinculo | datetime | NOT NULL | Timestamp em que o vínculo foi criado |
| Ativo | bit | NOT NULL, DEFAULT 1 | Flag de soft delete para o vínculo: 1 = ativo, 0 = desvinculado |

**Restrição de unicidade:** Par (GrupoId, UsuarioId) deve ser único para registros com Ativo = 1. Vínculo duplicado e rejeitado com HTTP 409 Conflict.

### 3.4 Tabela AuditoriaGrupos

| Campo | Tipo | Restrição | Descrição |
|---|---|---|---|
| Id | int | PK, IDENTITY(1,1), NOT NULL | Identificador único do registro de auditoria |
| GrupoId | int | FK -> Grupos.Id, NULL | Referência ao grupo afetado; NULL em operações que destroem o grupo |
| UsuarioOperadorId | int | NOT NULL | ID do usuário autenticado que realizou a operação (extraido do JWT) |
| Acao | nvarchar(20) | NOT NULL | Tipo da operação: CREATE, UPDATE, DELETE, ADD_USER, REMOVE_USER |
| DataHora | datetime | NOT NULL | Timestamp da operação (UTC) |
| Detalhe | nvarchar(max) | NULL | Payload JSON com detalhes da mudança (valores anteriores e novos para UPDATE) |

**Nota:** A tabela AuditoriaGrupos é implementada na Sprint 2 (AG-23). O endpoint POST /grupos/{id}/auditoria é interno — chamado pelo próprio Service, nunca exposto diretamente ao cliente.

---

## 4. Endpoints da API

| Método | Endpoint | Descrição | Requisito (AG) | Status |
|---|---|---|---|---|
| POST | /grupos | Criar novo grupo com nome, descrição e permissões iniciais | AG-20 (RF-01) | Implementado Sprint 1 (PR #11) |
| GET | /grupos | Listar todos os grupos ativos (Ativo = 1); suporta paginação e filtro por nome | AG-20 (RF-02) | Implementado Sprint 1 (PR #12) |
| GET | /grupos/{id} | Buscar grupo específico por ID, retornando dados completos incluindo permissões e lista de usuários | AG-20 (RF-02) | Implementado Sprint 1 (PR #12) |
| PUT | /grupos/{id} | Atualizar nome e/ou descrição do grupo | AG-20 (RF-03) | Implementado Sprint 1 (PR #12) |
| DELETE | /grupos/{id} | Soft delete do grupo (Ativo = 0); não remove fisicamente o registro | AG-20 (RF-04) | Implementado Sprint 1 (PR #12) |
| PUT | /grupos/{id}/permissoes | Substituir completamente as permissões do grupo; operação atomica em transação | AG-21 (RF-05) | Implementado Sprint 1 (PR #13) |
| POST | /grupos/{id}/usuarios | Vincular usuário ao grupo; propaga ao ms.temis.vinculos | AG-22 (RF-06) | Implementado Sprint 1 (PR #14) |
| DELETE | /grupos/{id}/usuarios/{uid} | Desvincular usuário do grupo; propaga ao ms.temis.vinculos | AG-22 (RF-06) | Implementado Sprint 1 (PR #15) |
| POST | /grupos/{id}/auditoria | (Interno) Registrar entrada de auditoria para operação crítica | AG-23 (RF-07) | Em desenvolvimento Sprint 2 |
| GET | /grupos/relatorio | Relatório consolidado de grupos, usuários e permissões; suporta filtros e exportação CSV | AG-25 (RF-09) | Previsto Sprint 3 |

---

## 5. Decisões arquiteturais

### GDE-001 — Dapper vs Entity Framework Core

**Decisão:** Dapper adotado como ORM para todas as operações de acesso a dados.

**Contexto:** O projeto Gerenciador AASP roda em .NET Framework 4.7.2. O Entity Framework Core em suas versões modernas tem suporte limitado ao .NET FW 4.7.2, requerendo o uso de versões antigas com recursos reduzidos. Além disso, o banco auxo3 possui schema legado com convenções de nomenclatura que dificultam o mapeamento automático do EF Core.

**Consequências:** Queries SQL escritas manualmente nos Repositories, o que aumenta o controle sobre performance mas exige disciplina no uso de queries parametrizadas para prevenção de SQL Injection. Toda query revisada no code review com checklist específico para segurança de dados.

**Referência completa:** GDE-AASP01-001_Registro-de-Análise-de-Decisao.docx

### GDE-002 — Soft Delete vs Hard Delete

**Decisão:** Soft Delete adotado para grupos e para vínculos usuário-grupo (campo Ativo bit).

**Contexto:** O sistema Gerenciador AASP precisa manter rastreabilidade histórica para fins de auditoria e conformidade. Hard delete de grupos comprometeria a integridade referencial da tabela AuditoriaGrupos e impossibilitaria a reconstrução do histórico de operações.

**Consequências:** Queries de listagem sempre filtram por `Ativo = 1`. Operações de DELETE retornam HTTP 200 com o registro atualizado (não HTTP 204 No Content), para confirmar o estado após a operação. Necessidade de mecanismo de expurgo futuro a ser definido pelo cliente.

**Referência completa:** GDE-AASP01-001_Registro-de-Análise-de-Decisao.docx

---

## 6. Integração com ms.temis.vinculos

### 6.1 Visão geral

Quando um usuário e vinculado ou desvinculado de um grupo via API do ms.auxo.gruposusuarios, o serviço realiza automaticamente uma chamada HTTP ao microsserviço ms.temis.vinculos para manter a consistência dos dados no banco temis3.

Esta integração é unidirecional: ms.auxo.gruposusuarios chama ms.temis.vinculos; nunca o contrário. O ms.temis.vinculos não conhece a existência de grupos — ele opera sobre vínculos genéricos de usuário.

### 6.2 Contrato de chamada

- **Endpoint:** POST /api/vinculos (ms.temis.vinculos)
- **Payload:**
  ```json
  {
    "usuarioId": 123,
    "grupoId": 45,
    "operacao": "ADD"
  }
  ```
  Valores válidos para "operação": `"ADD"` (vínculo) ou `"REMOVE"` (desvínculo).

- **Autenticação:** Bearer Token repassado do contexto da requisição original (token do usuário operador).
- **Timeout:** 5 segundos. Ultrapassado o timeout, a chamada é considerada falha.
- **Retry:** 1 tentativa adicional automática após falha de rede (não replicado em erros HTTP 4xx).
- **Comportamento em caso de falha persistente:** A operação no banco auxo3 é confirmada (o vínculo é registrado localmente); a falha na integração com temis3 é registrada como log de erro e como entrada na tabela AuditoriaGrupos (Acao: "TEMIS_SYNC_ERROR"). Um mecanismo de reconciliação manual é documentado no ITP-AASP01-001.

### 6.3 Referência

Para a especificação completa do contrato de integração, cenários de erro, exemplos de payload e procedimento de reconciliação, consultar: **ITP-AASP01-001_Estrategia-de-Integracao.docx**.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão Oliveira | Arquitetura inicial — Sprint 1; stack, modelo de dados, endpoints S1 |
| 1.1 | 15/06/2026 | Abraão Oliveira | Adição da seção 6 (integração ms.temis.vinculos) após disponibilização do contrato de API no início da Sprint 2 |
