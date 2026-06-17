# Plano de Regeneração AASP01 — Alinhar documentos à API real

> **Decisão do cliente (15/06/2026):** manter a estrutura de sprints exatamente como estava
> (Sprint 1 concluída/evidenciada · Sprint 2 em andamento · Sprint 3 futuro). Corrigir **apenas o
> conteúdo técnico** (endpoints, verbos, status HTTP, conceitos) para bater com o código real.
> Regra de ouro: **docs = sistemas**. O código é a fonte canônica.

---

## 1. A verdade do código (fonte: `GerenciarGruposController.cs`, rota `api/gerenciar/grupos`)

8 endpoints reais. **Só os verbos GET e POST. Só os status 200 (Ok) e 400 (BadRequest).**
Toda resposta vem num envelope `{ Sucesso, MensagemPublica, RetornaDados, HoraExecucao }`.

| # | Endpoint real | Verbo | DTO de entrada | O que faz |
|---|---|---|---|---|
| 1 | `listargrupo` | GET | `FiltroPaginacaoListasDTO` (query) | Lista grupos paginado |
| 2 | `buscargrupoporid` | GET | `FiltroPaginacaoListasDTO` (query) | Lista usuários de um grupo |
| 3 | `incluirgrupo` | POST | `IncluirGruposDTO` (nome + lista de membros) | Cria grupo já com membros |
| 4 | `alterargrupo` | POST | `AlterarGruposDTO` (id + nome + membros) | Altera grupo e seus membros |
| 5 | `excluirgrupo` | POST | `ExcluirGruposDTO` (id + notificarMembros) | Exclui grupo |
| 6 | `ativardesativar` | POST | `AtivarGruposDTO` (id + ativo 0/1) | Ativa/desativa grupo |
| 7 | `removerusuario` | POST | `RemoverUsuarioDoGrupoDTO` (id + grupoId) | Remove um usuário do grupo |
| 8 | `alterarfuncaodousuario` | POST | `AlterarFuncaoDoUsuarioDTO` (funcaoId, usuarioId, funcao) | Altera a função de um usuário |

**Conceito "função":** enum `FuncaoUsuariosEnum { Usuario = 0, Administrador = 1 }`.
É um **papel binário por usuário no grupo** — NÃO é a lista de permissões `[Leitura, Escrita, Exclusao,
Administracao, Relatorio]` que os documentos inventaram.

**Como um usuário entra num grupo:** não há endpoint "adicionar usuário". Os membros são enviados
**dentro do payload do grupo** — `incluirgrupo`/`alterargrupo` recebem `GrupoDeUsuarios: [{ id, funcaoId }]`.
Remoção individual = `removerusuario`. Mudança de papel = `alterarfuncaodousuario`.

**Validação real de nome duplicado:** `incluirgrupo` retorna **400 "Grupo já existe"** (não 409).

---

## 2. Estrutura de sprints (MANTIDA — sem mudança)

| Sprint | Estado | Cards | Evidência |
|---|---|---|---|
| Sprint 1 | **Concluída** | AG-20, AG-21, AG-22 | SIM — Swagger/commits/PRs dos endpoints reais |
| Sprint 2 | **Em andamento** | AG-23, AG-24 | Não (trabalho em progresso, sem merge/aceite) |
| Sprint 3 | **Futuro/Planejado** | AG-25 | Não |

> Hoje só existem **3 sprints**. Não há Sprint 4. Se quiser uma, é só pedir.

---

## 3. O que muda em cada CARD da Sprint 1 (o conteúdo, não a estrutura)

### AG-20 — CRUD de Grupos (Sprint 1, Concluído)
- **Antes (fictício):** `POST /grupos`→201, `GET /grupos`, `GET /grupos/{id}`, `PUT /grupos/{id}`→200, `DELETE /grupos/{id}`→204.
- **Depois (real):** `GET listargrupo`, `GET buscargrupoporid`, `POST incluirgrupo`, `POST alterargrupo`, `POST excluirgrupo`, `POST ativardesativar`. Todos 200/400.
- **Novidade:** entra o `ativardesativar` (ativa/desativa grupo), que existe no código e não estava documentado.

### AG-21 — passa a se chamar "Função do Usuário no Grupo" (era "Permissões RBAC")
- **Antes (fictício):** `PUT /grupos/{id}/permissoes` com enum `[Leitura, Escrita, Exclusao, Administracao, Relatorio]`.
- **Depois (real):** `POST alterarfuncaodousuario`; função = `Usuario` ou `Administrador`. 200/400.

### AG-22 — Vínculo Usuário-Grupo (Sprint 1, Concluído)
- **Antes (fictício):** `POST /grupos/{id}/usuarios`→201, `DELETE /grupos/{id}/usuarios/{uid}`→204.
- **Depois (real):** vincular = enviar usuário na lista `GrupoDeUsuarios` em `incluirgrupo`/`alterargrupo`; desvincular = `POST removerusuario`. 200/400.

### AG-23, AG-24, AG-25 (Sprint 2/3) — texto de escopo mantido
- Permanecem como **em andamento / planejado**. Não recebem contrato de endpoint "pronto" nem evidência de execução. (Observação: esse trabalho não existe no código hoje — por isso fica como futuro, o que é honesto e normal.)

---

## 4. O que muda em cada DOCUMENTO

| Documento | Mudança |
|---|---|
| `fonte_verdade_aasp01.py` | Endpoints reais por card; status 200/400; enum de função; modelo de membros. É a base de tudo. |
| **REQ** | RFs da Sprint 1 reescritos para os endpoints reais e o conceito de função. |
| **RASTR** | Matriz RF ↔ endpoint real ↔ card ↔ PR. |
| **PCP** (design) | Contratos reais dos 8 endpoints (rota, verbo, DTO request/response, envelope). Diagrama de arquitetura mantido. |
| **CTQ** | Cenários da Sprint 1 reescritos: endpoints e status reais (200/400), mensagens reais do código (ex.: "Grupo já existe"). |
| **VV / ITP / REL-VV** | Plano, estratégia e relatório de execução alinhados aos endpoints/status reais. |
| **GCO** | Ajustar qualquer citação de endpoint. |
| **Commits / PRs (Git + Azure)** | Mensagens e títulos passam a citar endpoints reais (ex.: "feat: incluirgrupo" em vez de "POST /grupos"). Reaplicar no Azure. |
| **.docx** | Reconverter todos os .md alterados. |

---

## 5. O que NÃO muda

- A estrutura de 3 sprints e os estados (concluída / em andamento / futuro).
- A equipe (regra única já aplicada).
- A narrativa de projeto (kickoff, aceite, achados de revisão RV-xxx, velocity).
- O diagrama de arquitetura.

---

## 6. Brinde: a divergência de números de PR

Os documentos citam **PRs #11–#17**; o Azure subiu com **#44+**. Como vou regenerar commits/PRs
de qualquer forma, aproveito para alinhar os números num passo só (decidimos o critério na hora de aplicar).

---

## 7. Ordem de execução (tasks)

1. `fonte_verdade_aasp01.py` (base)
2. REQ + RASTR
3. PCP
4. CTQ
5. VV + ITP + REL-VV
6. GCO + commits/PRs (Azure)
7. Reconverter .docx + verificação final (nenhum endpoint/verbo/status fictício remanescente)
