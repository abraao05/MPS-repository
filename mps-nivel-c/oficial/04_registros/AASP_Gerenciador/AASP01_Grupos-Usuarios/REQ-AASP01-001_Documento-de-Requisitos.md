# REQ-AASP01-001 — Documento de Requisitos

| Campo         | Valor                                                                 |
|---------------|-----------------------------------------------------------------------|
| Documento     | REQ-AASP01-001                                                        |
| Projeto       | AASP01 — Grupos de Usuários (Feature AG)                              |
| Cliente       | AASP — Associação dos Advogados de São Paulo                          |
| Produto       | ms.auxo.usuarios                                                |
| Versão        | 1.4                                                                   |
| Data          | 01/07/2026                                                            |
| Autor         | Abraão Oliveira                                                       |
| Status        | Aprovado                                                              |

---

## 1. Objetivo

Este documento descreve os requisitos funcionais, não funcionais e regras de negócio do microsserviço **ms.auxo.usuarios**, desenvolvido para o sistema Gerenciador da AASP como parte da Feature AG — Grupos de Usuários. Os endpoints citados refletem o controller real `GerenciarGruposController` (rota base `api/gerenciar/grupos`).

## 2. Glossário

| Termo       | Definição                                                                                   |
|-------------|---------------------------------------------------------------------------------------------|
| Grupo       | Entidade que agrupa usuários do sistema, registrada no banco `auxo3`                         |
| Membro      | Usuário associado a um grupo, enviado na lista `GrupoDeUsuarios` do payload do grupo         |
| Função      | Papel de um usuário dentro de um grupo: `Usuario` (0) ou `Administrador` (1), conforme o enum `FuncaoUsuariosEnum` |
| Envelope    | Formato de resposta padrão da API: `{ Sucesso, MensagemPublica, RetornaDados, HoraExecucao }` |
| Soft Delete | Exclusão/inativação lógica: registro marcado como inativo, sem remoção física do banco        |
| auxo3       | Banco de dados SQL Server principal do sistema Gerenciador da AASP                          |
| temis3      | Banco de dados SQL Server de integração, acessado via `ms.temis.vinculos`                   |

## 3. Requisitos Funcionais

> Todos os endpoints usam a rota base `api/gerenciar/grupos`, apenas verbos GET/POST, e respondem no envelope padrão com HTTP 200 (sucesso) ou 400 (erro/validação).

| ID    | Descrição                                                                                                           | Backlog | Prioridade | Sprint | SP  |
|-------|---------------------------------------------------------------------------------------------------------------------|---------|------------|--------|-----|
| RF-01 | Criação de grupo via `POST incluirgrupo` (nome + lista de membros); validar unicidade do nome                       | AG-20   | Alta       | S1     | 5   |
| RF-02 | Listagem de grupos via `GET listargrupo` (paginada) e consulta dos usuários de um grupo via `GET buscargrupoporid`  | AG-20   | Alta       | S1     | 4   |
| RF-03 | Atualização de grupo via `POST alterargrupo` (nome e membros) e ativação/desativação via `POST ativardesativar`     | AG-20   | Alta       | S1     | 2   |
| RF-04 | Exclusão de grupo via `POST excluirgrupo`, com opção de notificar os membros (campo `NotificarMembros`)             | AG-20   | Alta       | S1     | 2   |
| RF-05 | Definição da função (`Usuario`/`Administrador`) de um usuário no grupo via `POST alterarfuncaodousuario`            | AG-21   | Alta       | S1     | 11  |
| RF-06 | Vinculação de usuário ao grupo pela lista de membros em `incluirgrupo`/`alterargrupo` e remoção via `POST removerusuario` | AG-22 | Alta    | S1     | 10  |
| RF-07 | Registro automático de auditoria em tabela `AuditoriaGrupos` para operações de escrita — ✅ Entregue 20/06/2026     | AG-23   | Média      | S2     | 14  |
| RF-08 | Integração com `ms.temis.vinculos` para sincronização de vínculos na base `temis3` — ✅ Entregue 20/06/2026         | AG-24   | Alta       | S2     | 14  |
| RF-09 | *(Planejado — Sprint 3)* Geração de relatório consolidado de grupos com exportação CSV                              | AG-25   | Média      | S3     | 20  |

## 4. Requisitos Não Funcionais

| ID    | Categoria         | Descrição                                                                              |
|-------|-------------------|----------------------------------------------------------------------------------------|
| RNF-01 | Performance      | Tempo de resposta ≤ 500 ms para 95% das requisições em condições normais de carga      |
| RNF-02 | Segurança        | Autenticação via JWT; comunicação exclusivamente por HTTPS                             |
| RNF-03 | Rastreabilidade  | Operações de escrita devem ser rastreáveis via auditoria (entrega planejada na Sprint 2) |
| RNF-04 | Compatibilidade  | Stack obrigatória: .NET 5.0 (net5.0) e Dapper; SQL Server como SGBD                |
| RNF-05 | Manutenibilidade | Cobertura mínima de 60% de testes unitários por módulo                                 |

## 5. Regras de Negócio

| ID    | Regra                                                                                                                  |
|-------|------------------------------------------------------------------------------------------------------------------------|
| RN-01 | O nome do grupo deve ser único no banco `auxo3`; tentativa de criação com nome duplicado retorna HTTP 400 com mensagem `Grupo já existe` |
| RN-02 | A exclusão de grupo (`POST excluirgrupo`) pode notificar os membros do grupo quando `NotificarMembros = true`          |
| RN-03 | A função atribuída a um usuário no grupo deve pertencer ao enum `FuncaoUsuariosEnum` (`Usuario`, `Administrador`)       |
| RN-04 | Os registros de auditoria de `AuditoriaGrupos` são imutáveis — não podem ser alterados ou excluídos (append-only) — implementado na Sprint 2 |
| RN-05 | A sincronização com `ms.temis.vinculos` é acionada após alteração de vínculo; falha gera log sem interromper a operação — implementado na Sprint 2 |

## 6. Critérios de Aceite

| RF    | Critério de Aceite                                                                                                        |
|-------|---------------------------------------------------------------------------------------------------------------------------|
| RF-01 | `POST incluirgrupo` retorna HTTP 200 com `Sucesso=true` e `MensagemPublica="Grupo incluído com sucesso"`; nome duplicado retorna HTTP 400 `"Grupo já existe"` |
| RF-02 | `GET listargrupo` retorna lista paginada (HTTP 200); `GET buscargrupoporid` retorna os usuários do grupo (HTTP 200); parâmetro inválido retorna HTTP 400 |
| RF-03 | `POST alterargrupo` retorna HTTP 200 com os dados atualizados; `POST ativardesativar` altera o status (ativo 0/1) e retorna HTTP 200 |
| RF-04 | `POST excluirgrupo` retorna HTTP 200 após a exclusão; notifica os membros quando `NotificarMembros = true`               |
| RF-05 | `POST alterarfuncaodousuario` altera a função (`Usuario`/`Administrador`) do usuário e retorna HTTP 200; dados inválidos retornam HTTP 400 |
| RF-06 | Vincular usuário (na lista `GrupoDeUsuarios` de `incluirgrupo`/`alterargrupo`) e `POST removerusuario` retornam HTTP 200 |
| RF-07 | Toda operação de escrita gera registro de auditoria em `AuditoriaGrupos` com usuário operador, timestamp e operação; registro imutável; consulta paginada disponível — ✅ Entregue e aceito 20/06/2026 |
| RF-08 | Após alteração de vínculo, `ms.temis.vinculos` é chamado via HTTP REST; falha gera log e não interrompe a operação (comportamento fault-tolerant); timeout + retry implementados — ✅ Entregue e aceito 20/06/2026 |
| RF-09 | *(Planejado — Sprint 3)* Relatório consolidado de grupos disponível para consulta + exportação em formato CSV                |

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
| 1.2    | 15/06/2026 | Abraão  | Alinhamento dos endpoints e regras à API real (GerenciarGruposController) |
| 1.3 | 24/06/2026 | Silvio Baroni (SEPG) | Reconciliação com o estado real do GitLab (produto/repositório ms.auxo.usuarios; framework net5.0 onde aplicável; entregas da Sprint 1 integradas em develop com baseline pela tag sprint-1-aceite). |
| 1.4 | 01/07/2026 | Silvio Baroni (SEPG) | Correção de NCs de auditoria: RF-07 e RF-08 marcados como entregues (20/06/2026); SP corrigidos (14+14=28 SP Sprint 2); RN-04 e RN-05 atualizados como implementados; RF-09 expandido com CSV; critérios de aceite RF-07/RF-08 detalhados; autor corrigido. |
