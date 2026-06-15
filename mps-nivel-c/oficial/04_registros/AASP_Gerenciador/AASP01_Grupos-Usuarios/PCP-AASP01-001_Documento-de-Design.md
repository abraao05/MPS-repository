# Documento de Design — AASP Gerenciador · Grupos de Usuarios

| Campo | Valor |
|---|---|
| **Documento** | PCP-AASP01-001 |
| **Projeto** | Grupos de Usuarios — AASP Gerenciador |
| **Cliente** | AASP — Associacao dos Advogados de Sao Paulo |
| **Versao** | 1.1 |
| **Data** | 26/05/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | PCP (evidencia de projeto) |

---

## 1. Visao geral da solucao

O microsservico **ms.auxo.gruposusuarios** e uma Web API RESTful desenvolvida em .NET Framework 4.7.2 com Dapper como ORM e SQL Server (banco principal auxo3) como banco de dados. Integra-se ao microsservico **ms.temis.vinculos** (banco temis3) via HTTP REST para sincronizacao de vinculos de usuarios.

A solucao provem funcionalidades completas de gestao de grupos de usuarios do sistema Gerenciador da AASP, incluindo:

- **CRUD de grupos**: criacao, listagem, busca por ID, atualizacao e remocao logica (soft delete) de grupos.
- **Controle de permissoes RBAC**: definicao e alteracao das permissoes associadas a cada grupo (Leitura, Escrita, Exclusao, Administracao, Relatorio).
- **Vinculo usuario-grupo**: associacao e desassociacao de usuarios a grupos, com propagacao automatica ao ms.temis.vinculos.
- **Auditoria e log**: registro automatico de todas as operacoes criticas (CREATE, UPDATE, DELETE, ADD_USER, REMOVE_USER) na tabela AuditoriaGrupos.
- **Relatorios**: endpoint consolidado para exportacao de dados de grupos e usuarios para fins gerenciais.

A API segue o padrao arquitetural estabelecido no sistema Gerenciador da AASP, utilizando autenticacao via JWT Bearer Token e expondo documentacao interativa via Swagger/OpenAPI.

---

## 2. Arquitetura da solucao

### 2.1 Stack tecnologico

| Camada | Tecnologia | Justificativa |
|---|---|---|
| Framework de API | ASP.NET Web API (.NET Framework 4.7.2) | Padrao do projeto Gerenciador AASP; compatibilidade com infraestrutura existente do cliente |
| ORM / Acesso a dados | Dapper 2.x | Ver GDE-AASP01-001 (GDE-001) — compatibilidade com .NET FW 4.7.2, performance superior ao EF Core em queries complexas, padrao ja adotado no projeto Gerenciador |
| Banco de dados principal | SQL Server — banco auxo3 | Banco existente do sistema Gerenciador da AASP; tabelas do modulo criadas via migrations versionadas |
| Banco de integracao | SQL Server — banco temis3 (acesso indireto via ms.temis.vinculos) | Banco do microsservico de vinculos; acesso exclusivamente via HTTP REST, nunca por query direta |
| Integracao externa | HTTP REST — ms.temis.vinculos | Ver GDE e ITP-AASP01-001; desacoplamento entre dominios, contrato de API versionado |
| Autenticacao | JWT Bearer Token | Padrao do Gerenciador AASP; tokens emitidos pelo servico de autenticacao central |
| Documentacao de API | Swagger / OpenAPI (Swashbuckle) | Gerado automaticamente a partir das anotacoes do codigo; validado em cada sprint |
| CI/CD | Azure DevOps Pipelines | Padrao Timeware; pipeline automatiza build, testes e analise estatica a cada PR |
| Controle de versao | Git (Azure DevOps) — Git Flow | Padrao Timeware; rastreabilidade completa de mudancas por feature e sprint |

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

**Descricao das camadas:**

- **Controllers**: recebem requisicoes HTTP, validam o modelo de entrada (DataAnnotations), delegam ao Service correspondente e retornam responses padronizados (200/201/400/404/500). Nenhuma logica de negocio nos controllers.
- **Services / UseCases**: contem toda a logica de negocio — validacoes de dominio, orquestracao de chamadas a repositories e ao cliente HTTP do ms.temis.vinculos, disparo de auditoria.
- **Repositories**: encapsulam queries SQL via Dapper. Cada repository corresponde a uma entidade do banco. Queries parametrizadas para prevencao de SQL Injection. Sem logica de negocio.
- **Banco auxo3**: banco principal do sistema Gerenciador. Tabelas do modulo criadas via migrations versionadas em /sql/migrations/.
- **ms.temis.vinculos**: microsservico externo acessado via HttpClient. Comunicacao assíncrona com timeout configurado (5s) e retry automatico (1 tentativa adicional em caso de falha de rede).

---

## 3. Modelo de dados (banco auxo3)

### 3.1 Tabela Grupos

| Campo | Tipo | Restricao | Descricao |
|---|---|---|---|
| Id | int | PK, IDENTITY(1,1), NOT NULL | Identificador unico do grupo, gerado automaticamente pelo banco |
| Nome | nvarchar(100) | NOT NULL, UNIQUE | Nome do grupo — deve ser unico no sistema; usado como identificador legivel |
| Descricao | nvarchar(500) | NULL | Descricao opcional do proposito e escopo do grupo |
| Ativo | bit | NOT NULL, DEFAULT 1 | Flag de soft delete: 1 = ativo, 0 = removido logicamente. Grupos inativos nao aparecem nas listagens padrao |
| DataCriacao | datetime | NOT NULL, DEFAULT GETDATE() | Timestamp de criacao do registro, preenchido automaticamente pelo banco |
| DataAtualizacao | datetime | NULL | Timestamp da ultima atualizacao; preenchido pelo sistema a cada PUT /grupos/{id} |

### 3.2 Tabela PermissoesGrupo

| Campo | Tipo | Restricao | Descricao |
|---|---|---|---|
| Id | int | PK, IDENTITY(1,1), NOT NULL | Identificador unico da permissao |
| GrupoId | int | FK -> Grupos.Id, NOT NULL | Referencia ao grupo ao qual a permissao pertence |
| Permissao | nvarchar(50) | NOT NULL | Codigo da permissao. Valores validos: Leitura, Escrita, Exclusao, Administracao, Relatorio |

**Regra de negocio:** A atualizacao de permissoes (PUT /grupos/{id}/permissoes) realiza substituicao completa — remove todas as permissoes existentes do grupo e insere as novas fornecidas no payload. Operacao atomica em transacao SQL.

### 3.3 Tabela UsuariosGrupo

| Campo | Tipo | Restricao | Descricao |
|---|---|---|---|
| Id | int | PK, IDENTITY(1,1), NOT NULL | Identificador unico do vinculo usuario-grupo |
| GrupoId | int | FK -> Grupos.Id, NOT NULL | Referencia ao grupo |
| UsuarioId | int | FK -> Usuarios.Id, NOT NULL | Referencia ao usuario do sistema Gerenciador |
| DataVinculo | datetime | NOT NULL | Timestamp em que o vinculo foi criado |
| Ativo | bit | NOT NULL, DEFAULT 1 | Flag de soft delete para o vinculo: 1 = ativo, 0 = desvinculado |

**Restricao de unicidade:** Par (GrupoId, UsuarioId) deve ser unico para registros com Ativo = 1. Vinculo duplicado e rejeitado com HTTP 409 Conflict.

### 3.4 Tabela AuditoriaGrupos

| Campo | Tipo | Restricao | Descricao |
|---|---|---|---|
| Id | int | PK, IDENTITY(1,1), NOT NULL | Identificador unico do registro de auditoria |
| GrupoId | int | FK -> Grupos.Id, NULL | Referencia ao grupo afetado; NULL em operacoes que destroem o grupo |
| UsuarioOperadorId | int | NOT NULL | ID do usuario autenticado que realizou a operacao (extraido do JWT) |
| Acao | nvarchar(20) | NOT NULL | Tipo da operacao: CREATE, UPDATE, DELETE, ADD_USER, REMOVE_USER |
| DataHora | datetime | NOT NULL | Timestamp da operacao (UTC) |
| Detalhe | nvarchar(max) | NULL | Payload JSON com detalhes da mudanca (valores anteriores e novos para UPDATE) |

**Nota:** A tabela AuditoriaGrupos e implementada na Sprint 2 (AG-23). O endpoint POST /grupos/{id}/auditoria e interno — chamado pelo proprio Service, nunca exposto diretamente ao cliente.

---

## 4. Endpoints da API

| Metodo | Endpoint | Descricao | Requisito (AG) | Status |
|---|---|---|---|---|
| POST | /grupos | Criar novo grupo com nome, descricao e permissoes iniciais | AG-20 (RF-01) | Implementado Sprint 1 (PR #11) |
| GET | /grupos | Listar todos os grupos ativos (Ativo = 1); suporta paginacao e filtro por nome | AG-20 (RF-02) | Implementado Sprint 1 (PR #12) |
| GET | /grupos/{id} | Buscar grupo especifico por ID, retornando dados completos incluindo permissoes e lista de usuarios | AG-20 (RF-02) | Implementado Sprint 1 (PR #12) |
| PUT | /grupos/{id} | Atualizar nome e/ou descricao do grupo | AG-20 (RF-03) | Implementado Sprint 1 (PR #12) |
| DELETE | /grupos/{id} | Soft delete do grupo (Ativo = 0); nao remove fisicamente o registro | AG-20 (RF-04) | Implementado Sprint 1 (PR #12) |
| PUT | /grupos/{id}/permissoes | Substituir completamente as permissoes do grupo; operacao atomica em transacao | AG-21 (RF-05) | Implementado Sprint 1 (PR #13) |
| POST | /grupos/{id}/usuarios | Vincular usuario ao grupo; propaga ao ms.temis.vinculos | AG-22 (RF-06) | Implementado Sprint 1 (PR #14) |
| DELETE | /grupos/{id}/usuarios/{uid} | Desvincular usuario do grupo; propaga ao ms.temis.vinculos | AG-22 (RF-06) | Implementado Sprint 1 (PR #15) |
| POST | /grupos/{id}/auditoria | (Interno) Registrar entrada de auditoria para operacao critica | AG-23 (RF-07) | Em desenvolvimento Sprint 2 |
| GET | /grupos/relatorio | Relatorio consolidado de grupos, usuarios e permissoes; suporta filtros e exportacao CSV | AG-25 (RF-09) | Previsto Sprint 3 |

---

## 5. Decisoes arquiteturais

### GDE-001 — Dapper vs Entity Framework Core

**Decisao:** Dapper adotado como ORM para todas as operacoes de acesso a dados.

**Contexto:** O projeto Gerenciador AASP roda em .NET Framework 4.7.2. O Entity Framework Core em suas versoes modernas tem suporte limitado ao .NET FW 4.7.2, requerendo o uso de versoes antigas com recursos reduzidos. Alem disso, o banco auxo3 possui schema legado com convencoes de nomenclatura que dificultam o mapeamento automatico do EF Core.

**Consequencias:** Queries SQL escritas manualmente nos Repositories, o que aumenta o controle sobre performance mas exige disciplina no uso de queries parametrizadas para prevencao de SQL Injection. Toda query revisada no code review com checklist especifico para seguranca de dados.

**Referencia completa:** GDE-AASP01-001_Registro-de-Analise-de-Decisao.docx

### GDE-002 — Soft Delete vs Hard Delete

**Decisao:** Soft Delete adotado para grupos e para vinculos usuario-grupo (campo Ativo bit).

**Contexto:** O sistema Gerenciador AASP precisa manter rastreabilidade historica para fins de auditoria e conformidade. Hard delete de grupos comprometeria a integridade referencial da tabela AuditoriaGrupos e impossibilitaria a reconstrucao do historico de operacoes.

**Consequencias:** Queries de listagem sempre filtram por `Ativo = 1`. Operacoes de DELETE retornam HTTP 200 com o registro atualizado (nao HTTP 204 No Content), para confirmar o estado apos a operacao. Necessidade de mecanismo de expurgo futuro a ser definido pelo cliente.

**Referencia completa:** GDE-AASP01-001_Registro-de-Analise-de-Decisao.docx

---

## 6. Integracao com ms.temis.vinculos

### 6.1 Visao geral

Quando um usuario e vinculado ou desvinculado de um grupo via API do ms.auxo.gruposusuarios, o servico realiza automaticamente uma chamada HTTP ao microsservico ms.temis.vinculos para manter a consistencia dos dados no banco temis3.

Esta integracao e unidirecional: ms.auxo.gruposusuarios chama ms.temis.vinculos; nunca o contrario. O ms.temis.vinculos nao conhece a existencia de grupos — ele opera sobre vinculos genericos de usuario.

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
  Valores validos para "operacao": `"ADD"` (vinculo) ou `"REMOVE"` (desvinculo).

- **Autenticacao:** Bearer Token repassado do contexto da requisicao original (token do usuario operador).
- **Timeout:** 5 segundos. Ultrapassado o timeout, a chamada e considerada falha.
- **Retry:** 1 tentativa adicional automatica apos falha de rede (nao replicado em erros HTTP 4xx).
- **Comportamento em caso de falha persistente:** A operacao no banco auxo3 e confirmada (o vinculo e registrado localmente); a falha na integracao com temis3 e registrada como log de erro e como entrada na tabela AuditoriaGrupos (Acao: "TEMIS_SYNC_ERROR"). Um mecanismo de reconciliacao manual e documentado no ITP-AASP01-001.

### 6.3 Referencia

Para a especificacao completa do contrato de integracao, cenarios de erro, exemplos de payload e procedimento de reconciliacao, consultar: **ITP-AASP01-001_Estrategia-de-Integracao.docx**.

---

## Historico de revisoes

| Versao | Data | Autor | Descricao |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão Oliveira | Arquitetura inicial — Sprint 1; stack, modelo de dados, endpoints S1 |
| 1.1 | 15/06/2026 | Abraão Oliveira | Adicao da secao 6 (integracao ms.temis.vinculos) apos disponibilizacao do contrato de API no inicio da Sprint 2 |
