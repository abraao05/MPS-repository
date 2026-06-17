# Cenários de Teste e Homologação — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | CTQ-AASP01-001 |
| **Versão** | 1.1 |
| **Data** | 26/05/2026 |
| **Projeto** | AG — ms.auxo.gruposusuarios |
| **Cliente** | AASP |
| **GP/TL** | Abraão Oliveira (GP) · Cézar Velázquez (TL) (Timeware) |
| **Dev** | Renan Kioshi (Timeware) |
| **PO** | Marcos Turnes (AASP) |
| **QA** | Leonardo Francisco Pereira (AASP) |
| **Executado por** | Leonardo Francisco Pereira (AASP) + Abraão Oliveira (Timeware) |
| **Ambiente de execução** | Homologação AASP |
| **Data de execução Sprint 1** | 06/06/2026 |

---

## 1. Contexto

Cenários de teste executados durante a homologação da Sprint 1 (AG-20, AG-21, AG-22). Definidos em conjunto entre Abraão Oliveira (Timeware) e Leonardo Francisco Pereira (AASP). Todos os 10 cenários da Sprint 1 foram executados e aprovados em 06/06/2026, sem ressalvas, conforme registrado na ATA-AASP01-002.

A feature AG — ms.auxo.gruposusuarios e desenvolvida em .NET Framework 4.7.2, com acesso ao banco SQL Server auxo3 via Dapper. Os cenários cobrem os endpoints implementados nos PRs #11 a #15 da Sprint 1.

---

## 2. Resumo de cobertura por sprint

| Sprint | Histórias cobertas | Cenários totais | OK | Não OK | Não testados | Status |
|---|---|---|---|---|---|---|
| Sprint 1 | AG-20, AG-21, AG-22 | 10 | 10 | 0 | 0 | Aprovado 100% |
| Sprint 2 | AG-23, AG-24 | 3 (planejados) | — | — | 3 | A executar |
| Sprint 3 | AG-25 | 2 (planejados) | — | — | 2 | Planejado |
| Sprint 4 | Regressão geral | TBD | — | — | — | Planejado |

---

## 3. Cenários — Sprint 1 — AG-20 CRUD Grupos

5 cenários definidos e executados para a história AG-20, cobrindo criação, listagem, atualização e exclusão lógica de grupos.

| ID | Cenário | Tipo | Pre-condição | Passos / Quando | Resultado Esperado | Status | Observação |
|---|---|---|---|---|---|---|---|
| GRP-01 | Criar grupo com dados válidos — happy path | Happy | Nenhum grupo com nome "Gestores" existe no banco | Enviar POST /grupos com body {"nome":"Gestores","descrição":"Grupo de gestores"} e JWT válido no header | HTTP 201; body com id gerado, nome="Gestores", descrição preenchida, ativo=true, DataCriacao preenchida | OK | 3 testes unitários cobrindo este cenário no GrupoService |
| GRP-02 | Listar todos os grupos ativos — happy path | Happy | Existem 3 grupos cadastrados e com Ativo=true no banco auxo3 | Enviar GET /grupos com JWT válido | HTTP 200; array com 3 objetos contendo id, nome, descrição, ativo=true para cada grupo | OK | |
| GRP-03 | Atualizar nome e descrição de grupo — happy path | Happy | Grupo com id=5 existe e possui Ativo=true | Enviar PUT /grupos/5 com body {"nome":"Gestores Senior","descrição":"Atualizado"} e JWT válido | HTTP 200; grupo retornado com nome="Gestores Senior", descrição="Atualizado" e DataAtualizacao preenchida com o timestamp atual | OK | |
| GRP-04 | Exclusao lógica (soft delete) de grupo sem usuários — happy path | Happy | Grupo com id=7 existe, Ativo=true e não possui usuários vinculados ativos | Enviar DELETE /grupos/7 com JWT válido | HTTP 204; campo Ativo=false no banco (registro permanece); grupo com id=7 não aparece em GET /grupos (que filtra WHERE Ativo=1) | OK | Soft delete validado — registro permanece fisicamente no banco; apenas marcado como inativo |
| GRP-05 | Tentar criar grupo com nome já existente — sad path | Sad | Grupo com nome "Administradores" já existe no banco com Ativo=true | Enviar POST /grupos com body {"nome":"Administradores","descrição":"Qualquer"} | HTTP 409 Conflict; body com mensagem "Nome de grupo já existe" | OK | Validação de unicidade implementada após achado RV-001-01 — antes do fix retornava exceção do banco |

---

## 4. Cenários — Sprint 1 — AG-21 Permissões por Grupo

2 cenários definidos e executados para a história AG-21, cobrindo associação de permissões validas e rejeição de permissões invalidas.

| ID | Cenário | Tipo | Pre-condição | Passos / Quando | Resultado Esperado | Status | Observação |
|---|---|---|---|---|---|---|---|
| PERM-01 | Associar permissões validas a grupo — happy path | Happy | Grupo id=3 existe e possui Ativo=true | Enviar PUT /grupos/3/permissoes com body {"permissões":["Leitura","Escrita"]} e JWT válido | HTTP 200; permissões "Leitura" e "Escrita" registradas em PermissoesGrupo; GET /grupos/3 retorna as permissões atualizadas | OK | Validação de enum adicionada no controller após RV-002-01; antes do fix, inválidos lançavam exceção SQL |
| PERM-02 | Tentar associar permissão inválida — sad path | Sad | Grupo id=3 existe e possui Ativo=true | Enviar PUT /grupos/3/permissoes com body {"permissões":["SuperAdmin"]} e JWT válido | HTTP 400 Bad Request; mensagem indicando que o valor "SuperAdmin" e inválido e listando os valores aceitos: Leitura, Escrita, Exclusao, Administracao, Relatorio | OK | Enum validado no controller antes de chamar o service; mensagem amigável retornada |

---

## 5. Cenários — Sprint 1 — AG-22 Vínculo Usuário-Grupo

3 cenários definidos e executados para a história AG-22, cobrindo vínculo, desvínculo e tentativa com usuário inexistente.

| ID | Cenário | Tipo | Pre-condição | Passos / Quando | Resultado Esperado | Status | Observação |
|---|---|---|---|---|---|---|---|
| VINC-01 | Vincular usuário ativo a grupo — happy path | Happy | Usuário id=42 existe e possui Ativo=true; Grupo id=3 existe e ativo; vínculo entre eles não existe | Enviar POST /grupos/3/usuarios com body {"usuarioId":42} e JWT válido | HTTP 201; registro criado em UsuariosGrupo com GrupoId=3, UsuarioId=42, Ativo=true e DataVinculo preenchida | OK | Validação de usuário ativo adicionada após RV-003-01 — antes do fix, usuários inativos podiam ser vinculados |
| VINC-02 | Desvincular usuário de grupo — happy path | Happy | Usuário id=42 esta vinculado ao Grupo id=3 com Ativo=true em UsuariosGrupo | Enviar DELETE /grupos/3/usuarios/42 com JWT válido | HTTP 204; campo Ativo=false no registro de UsuariosGrupo (soft delete do vínculo); usuário id=42 não aparece em GET /grupos/3/usuarios | OK | Soft delete do vínculo — histórico preservado em UsuariosGrupo |
| VINC-03 | Tentar vincular usuário inexistente — sad path | Sad | Grupo id=3 existe e ativo; usuário id=999 não existe no banco | Enviar POST /grupos/3/usuarios com body {"usuarioId":999} e JWT válido | HTTP 404; body com mensagem "Usuário não encontrado" | OK | FK validada via consulta Dapper antes do INSERT; evita exceção de FK violation no banco |

---

## 6. Cenários planejados — Sprint 2 (a executar)

Cenários previstos para a Sprint 2, cobrindo as histórias AG-23 (Auditoria) e AG-24 (Integração com ms.temis.vinculos).

| ID | História | Cenário | Tipo | Status |
|---|---|---|---|---|
| AUD-01 | AG-23 | Registrar log ao criar grupo — toda operação INSERT/UPDATE/DELETE em Grupos deve gerar registro em AuditoriaGrupos com campos: GrupoId, UsuarioOperadorId, Acao, DataHora e Detalhe preenchidos corretamente | Happy | A executar — Sprint 2 |
| AUD-02 | AG-23 | Verificar que registros de auditoria não podem ser deletados ou alterados — a tabela AuditoriaGrupos deve ser append-only; tentativas de DELETE ou UPDATE devem ser bloqueadas | Segurança | A executar — Sprint 2 |
| INT-01 | AG-24 | Vincular usuário a grupo dispara sincronização com ms.temis.vinculos — um HTTP POST /vinculos bem-sucedido deve ser realizado no ms.temis.vinculos após cada vínculo de usuário criado com sucesso | Integração | A executar — Sprint 2 |

---

## 7. Cenários planejados — Sprint 3 (a executar)

Cenários previstos para a Sprint 3, cobrindo a história AG-25 (Relatório consolidado).

| ID | História | Cenário | Tipo | Status |
|---|---|---|---|---|
| REL-01 | AG-25 | Listar grupos com usuários e permissões via GET /grupos/relatorio — endpoint retorna estrutura consolidada com todos os grupos ativos, seus membros (UsuariosGrupo) e permissões (PermissoesGrupo) em uma única resposta | Happy | Planejado — Sprint 3 |
| REL-02 | AG-25 | Exportar relatório em CSV — parâmetro de query string "?formato=csv" faz com que o endpoint retorne o relatório como arquivo para download no formato CSV com Content-Disposition adequado | Happy | Planejado — Sprint 3 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão Oliveira | Criação do documento; cenários da Sprint 1 definidos em conjunto com Leonardo Francisco Pereira (AASP) |
| 1.1 | 09/06/2026 | Abraão Oliveira | Resultado da execução Sprint 1 registrado (100% aprovado em 06/06/2026); cenários das Sprints 2 e 3 planejados |
