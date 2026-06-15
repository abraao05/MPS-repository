# REQ-AASP01-001 — Documento de Requisitos

| Campo         | Valor                                                                 |
|---------------|-----------------------------------------------------------------------|
| Documento     | REQ-AASP01-001                                                        |
| Projeto       | AASP01 — Grupos de Usuários (Feature AG)                              |
| Cliente       | AASP — Associação dos Advogados de São Paulo                          |
| Produto       | ms.auxo.gruposusuarios                                                |
| Versão        | 1.1                                                                   |
| Data          | 26/05/2026                                                            |
| Autor         | Abraão                                                         |
| Status        | Aprovado                                                              |

---

## 1. Objetivo

Este documento descreve os requisitos funcionais, não funcionais e regras de negócio do microsserviço **ms.auxo.gruposusuarios**, desenvolvido para o sistema Gerenciador da AASP como parte da Feature AG — Grupos de Usuários.

## 2. Glossário

| Termo       | Definição                                                                                   |
|-------------|---------------------------------------------------------------------------------------------|
| Grupo       | Entidade que agrupa usuários do sistema sob um conjunto comum de permissões                 |
| Permissão   | Direito de acesso atribuído a um grupo, seguindo o modelo RBAC                              |
| Vínculo     | Associação entre um usuário e um grupo, registrada no banco `auxo3`                         |
| RBAC        | Role-Based Access Control — controle de acesso baseado em papéis/permissões                 |
| Soft Delete | Exclusão lógica: registro marcado como inativo, sem remoção física do banco de dados        |
| auxo3       | Banco de dados SQL Server principal do sistema Gerenciador da AASP                          |
| temis3      | Banco de dados SQL Server de integração, acessado via `ms.temis.vinculos`                   |

## 3. Requisitos Funcionais

| ID    | Descrição                                                                                                           | Backlog | Prioridade | Sprint | SP  |
|-------|---------------------------------------------------------------------------------------------------------------------|---------|------------|--------|-----|
| RF-01 | Criação de grupo via `POST /grupos` com nome, descrição e status ativo; validar unicidade do nome                   | AG-20   | Alta       | S1     | 5   |
| RF-02 | Listagem e consulta de grupos via `GET /grupos` (lista paginada) e `GET /grupos/{id}` (detalhes)                    | AG-20   | Alta       | S1     | 4   |
| RF-03 | Atualização de grupo via `PUT /grupos/{id}`; campos editáveis: nome, descrição, status                              | AG-20   | Alta       | S1     | 2   |
| RF-04 | Exclusão lógica de grupo via `DELETE /grupos/{id}` (soft delete); bloqueada se houver usuários vinculados ativos    | AG-20   | Alta       | S1     | 2   |
| RF-05 | Atribuição e substituição de permissões RBAC via `PUT /grupos/{id}/permissoes`; valores validados por enum          | AG-21   | Alta       | S1     | 11  |
| RF-06 | Vinculação de usuário a grupo via `POST /grupos/{id}/usuarios` e remoção via `DELETE /grupos/{id}/usuarios/{uid}`   | AG-22   | Alta       | S1     | 10  |
| RF-07 | Registro automático de auditoria em tabela `AuditoriaGrupos` para todas as operações de escrita (imutável)          | AG-23   | Média      | S2     | 13  |
| RF-08 | Integração com `ms.temis.vinculos` via chamada HTTP para sincronização de vínculos na base `temis3`                 | AG-24   | Alta       | S2     | 15  |
| RF-09 | Geração de relatório consolidado via `GET /grupos/relatorio` com exportação em formato CSV                          | AG-25   | Média      | S3     | 10  |

## 4. Requisitos Não Funcionais

| ID    | Categoria         | Descrição                                                                              |
|-------|-------------------|----------------------------------------------------------------------------------------|
| RNF-01 | Performance      | Tempo de resposta ≤ 500 ms para 95% das requisições em condições normais de carga      |
| RNF-02 | Segurança        | Autenticação via JWT; comunicação exclusivamente por HTTPS                             |
| RNF-03 | Rastreabilidade  | Todas as operações de escrita devem ser rastreáveis via tabela `AuditoriaGrupos`       |
| RNF-04 | Compatibilidade  | Stack obrigatória: .NET Framework 4.7.2 e Dapper; SQL Server como SGBD                |
| RNF-05 | Manutenibilidade | Cobertura mínima de 70% de testes unitários por módulo                                 |

## 5. Regras de Negócio

| ID    | Regra                                                                                                                  |
|-------|------------------------------------------------------------------------------------------------------------------------|
| RN-01 | O nome do grupo deve ser único no banco `auxo3`; tentativa de criação/atualização com nome duplicado retorna HTTP 409  |
| RN-02 | A operação de soft delete (`DELETE /grupos/{id}`) é bloqueada se existirem usuários vinculados e ativos ao grupo       |
| RN-03 | As permissões atribuídas a um grupo devem pertencer ao enum de permissões válido definido na camada de domínio         |
| RN-04 | Os registros da tabela `AuditoriaGrupos` são imutáveis — não podem ser alterados ou excluídos por nenhuma operação     |
| RN-05 | A sincronização com `ms.temis.vinculos` deve ser acionada automaticamente após qualquer alteração de vínculo           |

## 6. Critérios de Aceite

| RF    | Critério de Aceite                                                                                                        |
|-------|---------------------------------------------------------------------------------------------------------------------------|
| RF-01 | `POST /grupos` retorna HTTP 201 com o recurso criado; retorna HTTP 409 em caso de nome duplicado                          |
| RF-02 | `GET /grupos` retorna lista paginada; `GET /grupos/{id}` retorna HTTP 200 ou HTTP 404 se não encontrado                   |
| RF-03 | `PUT /grupos/{id}` retorna HTTP 200 com dados atualizados; HTTP 404 se grupo inexistente                                  |
| RF-04 | `DELETE /grupos/{id}` retorna HTTP 204 após soft delete; HTTP 409 se houver usuários vinculados                           |
| RF-05 | `PUT /grupos/{id}/permissoes` substitui permissões e retorna HTTP 200; HTTP 400 para valores de enum inválidos            |
| RF-06 | `POST /grupos/{id}/usuarios` retorna HTTP 201; `DELETE /grupos/{id}/usuarios/{uid}` retorna HTTP 204                     |
| RF-07 | Toda operação de escrita gera registro em `AuditoriaGrupos` com usuário, timestamp e operação realizada                  |
| RF-08 | Após criação/remoção de vínculo, `ms.temis.vinculos` é chamado com sucesso; falha gera log e não interrompe a operação   |
| RF-09 | `GET /grupos/relatorio` retorna JSON consolidado; com `?formato=csv` retorna arquivo CSV com cabeçalho correto           |

## 7. Referências

| Documento      | Descrição                     |
|----------------|-------------------------------|
| TAP-AASP01-001 | Termo de Abertura do Projeto  |
| PLA-AASP01-001 | Plano de Projeto              |

---

## Histórico de Revisões

| Versão | Data       | Autor          | Descrição                                        |
|--------|------------|----------------|--------------------------------------------------|
| 1.0    | 19/05/2026 | Abraão  | Levantamento inicial dos requisitos (kickoff)    |
| 1.1    | 26/05/2026 | Abraão  | Refinamento dos requisitos para Sprint 1         |
