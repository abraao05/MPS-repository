# Cenarios de Teste e Homologacao — AASP Gerenciador · Grupos de Usuarios

| Campo | Valor |
|---|---|
| **Documento** | CTQ-AASP01-001 |
| **Versao** | 1.1 |
| **Data** | 26/05/2026 |
| **Projeto** | AG — ms.auxo.gruposusuarios |
| **Cliente** | AASP |
| **GP/TL** | Abraão Oliveira (GP) · Cézar Velázquez (TL) (Timeware) |
| **Dev** | Renan Kioshi (Timeware) |
| **PO** | Marcos Turnes (AASP) |
| **QA** | Leonardo Francisco Pereira (AASP) |
| **Executado por** | Leonardo Francisco Pereira (AASP) + Abraão Oliveira (Timeware) |
| **Ambiente de execucao** | Homologacao AASP |
| **Data de execucao Sprint 1** | 06/06/2026 |

---

## 1. Contexto

Cenarios de teste executados durante a homologacao da Sprint 1 (AG-20, AG-21, AG-22). Definidos em conjunto entre Abraão Oliveira (Timeware) e Leonardo Francisco Pereira (AASP). Todos os 10 cenarios da Sprint 1 foram executados e aprovados em 06/06/2026, sem ressalvas, conforme registrado na ATA-AASP01-002.

A feature AG — ms.auxo.gruposusuarios e desenvolvida em .NET Framework 4.7.2, com acesso ao banco SQL Server auxo3 via Dapper. Os cenarios cobrem os endpoints implementados nos PRs #11 a #15 da Sprint 1.

---

## 2. Resumo de cobertura por sprint

| Sprint | Historias cobertas | Cenarios totais | OK | Nao OK | Nao testados | Status |
|---|---|---|---|---|---|---|
| Sprint 1 | AG-20, AG-21, AG-22 | 10 | 10 | 0 | 0 | Aprovado 100% |
| Sprint 2 | AG-23, AG-24 | 3 (planejados) | — | — | 3 | A executar |
| Sprint 3 | AG-25 | 2 (planejados) | — | — | 2 | Planejado |
| Sprint 4 | Regressao geral | TBD | — | — | — | Planejado |

---

## 3. Cenarios — Sprint 1 — AG-20 CRUD Grupos

5 cenarios definidos e executados para a historia AG-20, cobrindo criacao, listagem, atualizacao e exclusao logica de grupos.

| ID | Cenario | Tipo | Pre-condicao | Passos / Quando | Resultado Esperado | Status | Observacao |
|---|---|---|---|---|---|---|---|
| GRP-01 | Criar grupo com dados validos — happy path | Happy | Nenhum grupo com nome "Gestores" existe no banco | Enviar POST /grupos com body {"nome":"Gestores","descricao":"Grupo de gestores"} e JWT valido no header | HTTP 201; body com id gerado, nome="Gestores", descricao preenchida, ativo=true, DataCriacao preenchida | OK | 3 testes unitarios cobrindo este cenario no GrupoService |
| GRP-02 | Listar todos os grupos ativos — happy path | Happy | Existem 3 grupos cadastrados e com Ativo=true no banco auxo3 | Enviar GET /grupos com JWT valido | HTTP 200; array com 3 objetos contendo id, nome, descricao, ativo=true para cada grupo | OK | |
| GRP-03 | Atualizar nome e descricao de grupo — happy path | Happy | Grupo com id=5 existe e possui Ativo=true | Enviar PUT /grupos/5 com body {"nome":"Gestores Senior","descricao":"Atualizado"} e JWT valido | HTTP 200; grupo retornado com nome="Gestores Senior", descricao="Atualizado" e DataAtualizacao preenchida com o timestamp atual | OK | |
| GRP-04 | Exclusao logica (soft delete) de grupo sem usuarios — happy path | Happy | Grupo com id=7 existe, Ativo=true e nao possui usuarios vinculados ativos | Enviar DELETE /grupos/7 com JWT valido | HTTP 204; campo Ativo=false no banco (registro permanece); grupo com id=7 nao aparece em GET /grupos (que filtra WHERE Ativo=1) | OK | Soft delete validado — registro permanece fisicamente no banco; apenas marcado como inativo |
| GRP-05 | Tentar criar grupo com nome ja existente — sad path | Sad | Grupo com nome "Administradores" ja existe no banco com Ativo=true | Enviar POST /grupos com body {"nome":"Administradores","descricao":"Qualquer"} | HTTP 409 Conflict; body com mensagem "Nome de grupo ja existe" | OK | Validacao de unicidade implementada apos achado RV-001-01 — antes do fix retornava excecao do banco |

---

## 4. Cenarios — Sprint 1 — AG-21 Permissoes por Grupo

2 cenarios definidos e executados para a historia AG-21, cobrindo associacao de permissoes validas e rejeicao de permissoes invalidas.

| ID | Cenario | Tipo | Pre-condicao | Passos / Quando | Resultado Esperado | Status | Observacao |
|---|---|---|---|---|---|---|---|
| PERM-01 | Associar permissoes validas a grupo — happy path | Happy | Grupo id=3 existe e possui Ativo=true | Enviar PUT /grupos/3/permissoes com body {"permissoes":["Leitura","Escrita"]} e JWT valido | HTTP 200; permissoes "Leitura" e "Escrita" registradas em PermissoesGrupo; GET /grupos/3 retorna as permissoes atualizadas | OK | Validacao de enum adicionada no controller apos RV-002-01; antes do fix, invalidos lancavam excecao SQL |
| PERM-02 | Tentar associar permissao invalida — sad path | Sad | Grupo id=3 existe e possui Ativo=true | Enviar PUT /grupos/3/permissoes com body {"permissoes":["SuperAdmin"]} e JWT valido | HTTP 400 Bad Request; mensagem indicando que o valor "SuperAdmin" e invalido e listando os valores aceitos: Leitura, Escrita, Exclusao, Administracao, Relatorio | OK | Enum validado no controller antes de chamar o service; mensagem amigavel retornada |

---

## 5. Cenarios — Sprint 1 — AG-22 Vinculo Usuario-Grupo

3 cenarios definidos e executados para a historia AG-22, cobrindo vinculo, desvinculo e tentativa com usuario inexistente.

| ID | Cenario | Tipo | Pre-condicao | Passos / Quando | Resultado Esperado | Status | Observacao |
|---|---|---|---|---|---|---|---|
| VINC-01 | Vincular usuario ativo a grupo — happy path | Happy | Usuario id=42 existe e possui Ativo=true; Grupo id=3 existe e ativo; vinculo entre eles nao existe | Enviar POST /grupos/3/usuarios com body {"usuarioId":42} e JWT valido | HTTP 201; registro criado em UsuariosGrupo com GrupoId=3, UsuarioId=42, Ativo=true e DataVinculo preenchida | OK | Validacao de usuario ativo adicionada apos RV-003-01 — antes do fix, usuarios inativos podiam ser vinculados |
| VINC-02 | Desvincular usuario de grupo — happy path | Happy | Usuario id=42 esta vinculado ao Grupo id=3 com Ativo=true em UsuariosGrupo | Enviar DELETE /grupos/3/usuarios/42 com JWT valido | HTTP 204; campo Ativo=false no registro de UsuariosGrupo (soft delete do vinculo); usuario id=42 nao aparece em GET /grupos/3/usuarios | OK | Soft delete do vinculo — historico preservado em UsuariosGrupo |
| VINC-03 | Tentar vincular usuario inexistente — sad path | Sad | Grupo id=3 existe e ativo; usuario id=999 nao existe no banco | Enviar POST /grupos/3/usuarios com body {"usuarioId":999} e JWT valido | HTTP 404; body com mensagem "Usuario nao encontrado" | OK | FK validada via consulta Dapper antes do INSERT; evita excecao de FK violation no banco |

---

## 6. Cenarios planejados — Sprint 2 (a executar)

Cenarios previstos para a Sprint 2, cobrindo as historias AG-23 (Auditoria) e AG-24 (Integracao com ms.temis.vinculos).

| ID | Historia | Cenario | Tipo | Status |
|---|---|---|---|---|
| AUD-01 | AG-23 | Registrar log ao criar grupo — toda operacao INSERT/UPDATE/DELETE em Grupos deve gerar registro em AuditoriaGrupos com campos: GrupoId, UsuarioOperadorId, Acao, DataHora e Detalhe preenchidos corretamente | Happy | A executar — Sprint 2 |
| AUD-02 | AG-23 | Verificar que registros de auditoria nao podem ser deletados ou alterados — a tabela AuditoriaGrupos deve ser append-only; tentativas de DELETE ou UPDATE devem ser bloqueadas | Seguranca | A executar — Sprint 2 |
| INT-01 | AG-24 | Vincular usuario a grupo dispara sincronizacao com ms.temis.vinculos — um HTTP POST /vinculos bem-sucedido deve ser realizado no ms.temis.vinculos apos cada vinculo de usuario criado com sucesso | Integracao | A executar — Sprint 2 |

---

## 7. Cenarios planejados — Sprint 3 (a executar)

Cenarios previstos para a Sprint 3, cobrindo a historia AG-25 (Relatorio consolidado).

| ID | Historia | Cenario | Tipo | Status |
|---|---|---|---|---|
| REL-01 | AG-25 | Listar grupos com usuarios e permissoes via GET /grupos/relatorio — endpoint retorna estrutura consolidada com todos os grupos ativos, seus membros (UsuariosGrupo) e permissoes (PermissoesGrupo) em uma unica resposta | Happy | Planejado — Sprint 3 |
| REL-02 | AG-25 | Exportar relatorio em CSV — parametro de query string "?formato=csv" faz com que o endpoint retorne o relatorio como arquivo para download no formato CSV com Content-Disposition adequado | Happy | Planejado — Sprint 3 |

---

## Historico de revisoes

| Versao | Data | Autor | Descricao |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão Oliveira | Criacao do documento; cenarios da Sprint 1 definidos em conjunto com Leonardo Francisco Pereira (AASP) |
| 1.1 | 09/06/2026 | Abraão Oliveira | Resultado da execucao Sprint 1 registrado (100% aprovado em 06/06/2026); cenarios das Sprints 2 e 3 planejados |
