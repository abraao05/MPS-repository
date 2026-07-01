# Cenários de Teste e Homologação — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | CTQ-AASP01-001 |
| **Versão** | 1.4 |
| **Data** | 01/07/2026 |
| **Projeto** | AG — ms.auxo.usuarios |
| **Cliente** | AASP |
| **GP/TL** | Abraão (GP) · Cezar Hiraki (TL) (Timeware) |
| **Dev** | Renan Kiyoshi (Timeware) |
| **PO** | Marcos Turnes (AASP) |
| **QA** | Leonardo Francisco Pereira (AASP) |
| **Executado por** | Leonardo Francisco Pereira (AASP) + Abraão (Timeware) |
| **Ambiente de execução** | Homologação AASP |
| **Data de execução Sprint 1** | 06/06/2026 |
| **Data de execução Sprint 2** | 20/06/2026 |

---

## 1. Contexto

Cenários de teste executados durante a homologação da Sprint 1 (AG-20, AG-21, AG-22). Definidos em conjunto entre Abraão (Timeware) e Leonardo Francisco Pereira (AASP). Todos os 10 cenários da Sprint 1 foram executados e aprovados em 06/06/2026, sem ressalvas, conforme registrado na ATA-AASP01-002.

A feature AG — ms.auxo.usuarios e desenvolvida em .NET 5.0 (net5.0), com acesso ao banco SQL Server auxo3 via Dapper. Os endpoints são expostos pelo controller `GerenciarGruposController` (rota base `api/gerenciar/grupos`), com verbos GET/POST e resposta num envelope padrão `{ Sucesso, MensagemPublica, RetornaDados }` com HTTP 200 (sucesso) ou 400 (erro/validação). Os cenários cobrem os endpoints implementados nos MRs !1 a !5 da Sprint 1.

---

## 2. Resumo de cobertura por sprint

| Sprint | Historias cobertas | Cenários totais | OK | Não OK | Não testados | Status |
|---|---|---|---|---|---|---|
| Sprint 1 | AG-20, AG-21, AG-22 | 10 | 10 | 0 | 0 | Aprovado 100% |
| Sprint 2 | AG-23, AG-24 | 4 | 4 | 0 | 0 | Aprovado 100% — aceite 20/06/2026 |
| Sprint 3 | AG-25 | 2 (planejados) | — | — | 2 | Planejado |

---

## 3. Cenários — Sprint 1 — AG-20 CRUD Grupos

7 cenários definidos e executados para a historia AG-20, cobrindo criação, listagem, consulta dos usuários do grupo, alteração, exclusão, ativação/desativação e validação de nome duplicado.

| ID | Cenário | Tipo | Pre-condição | Passos / Quando | Resultado Esperado | Status | Observação |
|---|---|---|---|---|---|---|---|
| GRP-01 | Criar grupo com dados válidos — happy path | Happy | Nenhum grupo com nome "Gestores" existe no escritorio | Enviar `POST incluirgrupo` com body {"nome":"Gestores","grupoDeUsuarios":[]} e JWT válido | HTTP 200; `Sucesso=true`, `MensagemPublica="Grupo incluido com sucesso"`, `RetornaDados` com o id gerado | OK | — |
| GRP-02 | Listar grupos — happy path | Happy | Existem grupos cadastrados (excluido=0) no escritorio | Enviar `GET listargrupo` (paginado) com JWT válido | HTTP 200; `RetornaDados` com a lista paginada de grupos ativos | OK | |
| GRP-03 | Consultar usuários de um grupo — happy path | Happy | Grupo id=5 existe e possui membros | Enviar `GET buscargrupoporid` (filtro com o id do grupo) e JWT válido | HTTP 200; `RetornaDados` com os usuários do grupo e suas funções | OK | |
| GRP-04 | Alterar nome e membros do grupo — happy path | Happy | Grupo id=5 existe | Enviar `POST alterargrupo` com body {"id":5,"nome":"Gestores Senior","grupoDeUsuarios":[...]} e JWT válido | HTTP 200; `Sucesso=true`; `data_alteracao` atualizada | OK | |
| GRP-05 | Excluir grupo (soft delete) — happy path | Happy | Grupo id=7 existe | Enviar `POST excluirgrupo` com body {"id":7,"notificarMembros":false} e JWT válido | HTTP 200; `excluido=1` no banco (registro permanece); grupo não aparece em `listargrupo` (filtra excluido=0) | OK | Soft delete validado — registro permanece fisicamente no banco |
| GRP-06 | Ativar/desativar grupo — happy path | Happy | Grupo id=5 existe | Enviar `POST ativardesativar` com body {"id":5,"ativo":0} e JWT válido | HTTP 200; campo `ativo` atualizado para 0 | OK | |
| GRP-07 | Tentar criar grupo com nome já existente — sad path | Sad | Grupo com nome "Administradores" já existe no escritorio | Enviar `POST incluirgrupo` com body {"nome":"Administradores","grupoDeUsuarios":[]} | HTTP 400; `Sucesso=false`, `MensagemPublica="Grupo ja existe"` | OK | Validação de unicidade (`ExisteGrupo`) — achado RV-001-01 |

---

## 4. Cenários — Sprint 1 — AG-21 Função do Usuario no Grupo

1 cenário definido e executado para a historia AG-21, cobrindo a alteração da função (papel) de um usuário no grupo.

| ID | Cenário | Tipo | Pre-condição | Passos / Quando | Resultado Esperado | Status | Observação |
|---|---|---|---|---|---|---|---|
| FUNC-01 | Alterar função do usuário no grupo — happy path | Happy | Usuario id=42 e membro de um grupo com função `Usuario` (0) | Enviar `POST alterarfuncaodousuario` com body {"usuarioId":42,"funcaoId":1,"funcao":1} e JWT válido | HTTP 200; `Sucesso=true`; função do usuário atualizada para `Administrador` (1) | OK | Função validada pelo enum `FuncaoUsuariosEnum` (Usuario/Administrador) — achado RV-002-01 |

---

## 5. Cenários — Sprint 1 — AG-22 Vinculo Usuario-Grupo

2 cenários definidos e executados para a historia AG-22, cobrindo o vinculo de usuários (lista de membros) e a remoção de um usuário do grupo.

| ID | Cenário | Tipo | Pre-condição | Passos / Quando | Resultado Esperado | Status | Observação |
|---|---|---|---|---|---|---|---|
| VINC-01 | Vincular usuários ao grupo — happy path | Happy | Grupo id=3 existe; usuários 42 e 711 existem | Enviar `POST alterargrupo` (ou `incluirgrupo`) com `grupoDeUsuarios:[{"id":42,"funcaoId":0},{"id":711,"funcaoId":1}]` e JWT válido | HTTP 200; vinculos criados em `grupos_usuarios_vinculos` (grupo_id, usuario_id, funcao_id) | OK | Membros enviados na lista do payload do grupo |
| VINC-02 | Remover usuário do grupo — happy path | Happy | Usuario id=711 esta vinculado ao Grupo id=3 | Enviar `POST removerusuario` com body {"id":711,"grupoId":3} e JWT válido | HTTP 200; `excluido=1` no vinculo (soft delete); usuário não aparece em `buscargrupoporid` | OK | Soft delete do vinculo — achado RV-003-01 |

---

## 6. Cenários executados — Sprint 2 (20/06/2026)

Cenários executados na Sprint 2, cobrindo as histórias AG-23 (Auditoria) e AG-24 (Integração com ms.temis.vinculos).

**Executados por:** Leonardo Francisco Pereira (AASP — QA/Homologadora)
**Data de execução:** 20/06/2026
**Ambiente:** Homologação AASP — banco auxo3

| ID | Historia | Cenário | Tipo | Status |
|---|---|---|---|---|
| AUD-01 | AG-23 | Realizar operação de criação/alteração de grupo — verificar registro de trilha de auditoria em `auditoria_grupos` com usuário operador, data/hora e operação | Happy | OK — aprovado em 20/06/2026 |
| AUD-02 | AG-23 | Registros de auditoria devem ser imutáveis (append-only); tentativas de alteração/exclusão bloqueadas | Segurança | OK — aprovado em 20/06/2026 |
| INT-01 | AG-24 | Consultar vínculos de usuário via integração com ms.temis.vinculos — retorno com lista de vínculos ativos | Integração | OK — aprovado em 20/06/2026 |
| INT-02 | AG-24 | Simular indisponibilidade do ms.temis.vinculos — verificar comportamento de fallback (timeout + retry + HTTP 503 com mensagem adequada) | Integração | OK — aprovado em 20/06/2026 |

---

## 7. Cenários planejados — Sprint 3 (a executar)

Cenários previstos para a Sprint 3, cobrindo a historia AG-25 (Relatório consolidado). Funcionalidade **ainda não implementada** no código.

| ID | Historia | Cenário | Tipo | Status |
|---|---|---|---|---|
| REL-01 | AG-25 | Relatório consolidado de grupos com seus membros e funções em uma única resposta | Happy | Planejado — Sprint 3 |
| REL-02 | AG-25 | Exportação do relatório em formato CSV | Happy | Planejado — Sprint 3 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão | Criação do documento; cenários da Sprint 1 definidos em conjunto com Leonardo Francisco Pereira (AASP) |
| 1.1 | 09/06/2026 | Abraão | Resultado da execução Sprint 1 registrado (100% aprovado em 06/06/2026); cenários das Sprints 2 e 3 planejados |
| 1.2 | 15/06/2026 | Abraão | Cenários alinhados aos endpoints e status reais (GerenciarGruposController; HTTP 200/400; função Usuario/Administrador) |
| 1.3 | 24/06/2026 | Silvio Baroni (SEPG) | Reconciliação com o estado real do GitLab (produto/repositório ms.auxo.usuarios; framework net5.0 onde aplicável; entregas da Sprint 1 integradas em develop com baseline pela tag sprint-1-aceite). |
| 1.4 | 01/07/2026 | Silvio Baroni (SEPG) | Correção de NCs de auditoria: Sprint 2 atualizada com resultados reais (4 cenários AUD-01, AUD-02, INT-01, INT-02 aprovados em 20/06/2026); seção 6 reescrita de "planejados" para "executados"; tabela de cobertura corrigida. |
