# Registro de Revisao Tecnica — AASP Gerenciador · Grupos de Usuarios

| Campo | Valor |
|---|---|
| **Documento** | REV-AASP01-001 |
| **Versao** | 1.0 |
| **Data** | 06/06/2026 |
| **Projeto** | AG — ms.auxo.gruposusuarios |
| **Cliente** | AASP |
| **GP/TL** | Abraão (GP) · Cezar Hiraki (TL) (Timeware) |
| **Dev** | Renan Kiyoshi (Timeware) |
| **PO** | Marcos Turnes (AASP) |
| **QA** | Leonardo Francisco Pereira (AASP) |
| **Processo MPS-SW** | VV — Verificacao e Validacao (evidencia de revisao por pares) |

---

## 1. Objetivo

Registrar as revisoes tecnicas formais (code reviews via Pull Requests) realizadas durante a Sprint 1 da feature AG — ms.auxo.gruposusuarios, constituindo evidencia do processo MPS-SW VV (Verificacao e Validacao). Cada revisao cobriu PRs especificos com o objetivo de identificar defeitos antes do merge na branch develop. Todos os achados foram classificados por severidade e resolvidos antes da integracao.

---

## 2. REV-001 — Revisao de PR #11 e #12 (AG-20 — CRUD base e endpoints GET/PUT/DELETE)

| Campo | Valor |
|---|---|
| **Data** | 30/05/2026 (PR #11) e 02/06/2026 (PR #12) |
| **Tipo** | Code review — implementacao de feature |
| **PRs revisados** | #11 (POST /grupos — CRUD base), #12 (GET /grupos, GET /grupos/{id}, PUT /grupos/{id}, DELETE /grupos/{id}) |
| **Revisor responsavel** | Cezar Hiraki (Tech Lead — Timeware) |
| **Autor do codigo** | Renan Kiyoshi (Timeware) |
| **Resultado** | Aprovado com correcoes |

### 2.1 Achados

| ID | Descricao | Severidade | Acao tomada | Status |
|---|---|---|---|---|
| RV-001-01 | Validacao de nome duplicado ausente no controller — o endpoint POST /grupos aceitava nomes ja existentes, lancando excecao do banco (constraint de unicidade) ao inves de retornar HTTP 409 com mensagem amigavel ao consumidor da API | P2 — Alto | Adicionada verificacao previa no GrupoService antes do INSERT: se nome ja existir com Ativo=true, retornar HTTP 409 com mensagem "Nome de grupo ja existe" | Resolvido antes do merge final |
| RV-001-02 | Retorno HTTP 404 faltando em GET /grupos/{id} para id inexistente — o endpoint retornava HTTP 500 (excecao nao tratada) quando o id solicitado nao existia no banco, ao inves de HTTP 404 com mensagem clara | P3 — Medio | Adicionado "null check" no GrupoService apos a consulta Dapper; quando retorno e null, o controller retorna HTTP 404 com mensagem "Grupo nao encontrado" | Resolvido antes do merge final |

**Total de achados REV-001: 2 — P1: 0 | P2: 1 | P3: 1 | Resolvidos: 2/2**

---

## 3. REV-002 — Revisao de PR #13 (AG-21 — Permissoes por Grupo)

| Campo | Valor |
|---|---|
| **Data** | 03/06/2026 |
| **Tipo** | Code review — implementacao de feature |
| **PR revisado** | #13 (PUT /grupos/{id}/permissoes) |
| **Revisor responsavel** | Cezar Hiraki (Tech Lead — Timeware) |
| **Autor do codigo** | Henry Komatsu (Timeware) |
| **Resultado** | Aprovado com correcoes |

### 3.1 Achados

| ID | Descricao | Severidade | Acao tomada | Status |
|---|---|---|---|---|
| RV-002-01 | Enum de permissao validado apenas no banco (constraint de coluna), nao no controller — valores invalidos enviados pela API lancavam excecao SQL ao inves de retornar HTTP 400 com mensagem clara. Valores aceitos: Leitura, Escrita, Exclusao, Administracao, Relatorio | P2 — Alto | Adicionada validacao do enum no controller antes de chamar o PermissaoService: se o valor enviado nao pertencer ao enum, retornar HTTP 400 com mensagem "Permissao invalida: {valor}. Valores aceitos: Leitura, Escrita, Exclusao, Administracao, Relatorio" | Resolvido antes do merge |

**Total de achados REV-002: 1 — P1: 0 | P2: 1 | P3: 0 | Resolvidos: 1/1**

---

## 4. REV-003 — Revisao de PR #14 e #15 (AG-22 — Vinculo Usuario-Grupo)

| Campo | Valor |
|---|---|
| **Data** | 05/06/2026 |
| **Tipo** | Code review — implementacao de feature |
| **PRs revisados** | #14 (POST /grupos/{id}/usuarios), #15 (DELETE /grupos/{id}/usuarios/{uid}) |
| **Revisor responsavel** | Cezar Hiraki (Tech Lead — Timeware) |
| **Autor do codigo** | Mateus Veloso (Timeware) |
| **Resultado** | Aprovado com correcoes |

### 4.1 Achados

| ID | Descricao | Severidade | Acao tomada | Status |
|---|---|---|---|---|
| RV-003-01 | Falta de validacao se usuario esta ativo antes de vincular — o endpoint POST /grupos/{id}/usuarios aceitava vincular usuarios com Ativo=false no banco, criando vinculos invalidos em UsuariosGrupo | P2 — Alto | Adicionada consulta previa no UsuarioGrupoService: se usuario.Ativo == false, retornar HTTP 422 Unprocessable Entity com mensagem "Usuario inativo nao pode ser vinculado a grupo" | Resolvido antes do merge |
| RV-003-02 | Tratamento de FK violation em DELETE vinculo nao retornava mensagem amigavel — quando o vinculo ja havia sido removido (Ativo=false) ou o usuario nao estava vinculado, o endpoint lancava excecao SQL ao inves de HTTP 404 | P3 — Medio | Adicionado "null check" no repositorio Dapper antes do UPDATE de soft delete; quando vinculo nao encontrado, retornar HTTP 404 com mensagem "Vinculo nao encontrado" | Resolvido antes do merge |

**Total de achados REV-003: 2 — P1: 0 | P2: 1 | P3: 1 | Resolvidos: 2/2**

---

## 5. Consolidado da Sprint 1

| Revisao | PRs cobertos | Total achados | P2 — Alto | P3 — Medio | Resolvidos antes merge | Status final |
|---|---|---|---|---|---|---|
| REV-001 | #11, #12 | 2 | 1 | 1 | 2/2 | Aprovado |
| REV-002 | #13 | 1 | 1 | 0 | 1/1 | Aprovado |
| REV-003 | #14, #15 | 2 | 1 | 1 | 2/2 | Aprovado |
| **TOTAL** | **5 PRs** | **5** | **3** | **2** | **5/5 (100%)** | **Todos resolvidos** |

Nenhum achado P1 (critico) identificado na Sprint 1. Todos os achados P2 e P3 foram resolvidos antes do merge final em develop. Nenhum defeito foi para o ambiente de homologacao sem correcao previa. Resultado confirmado pelo aceite sem ressalvas de Leonardo Francisco Pereira (AASP) em 06/06/2026.

---

## 6. Proximas revisoes — Sprint 2

Revisoes tecnicas previstas para a Sprint 2, cobrindo as historias AG-23 (Auditoria via tabela AuditoriaGrupos) e AG-24 (Integracao com ms.temis.vinculos). Estimativa de PRs a serem revisados: #16 (AG-23 — implementacao da auditoria) e #17 (AG-24 — integracao HTTP com ms.temis.vinculos). O processo de revisao seguira o mesmo padrao desta Sprint: revisao pelo Tech Lead antes de qualquer merge em develop, com registro formal de achados e acompanhamento ate resolucao.

---

## Historico de revisoes

| Versao | Data | Autor | Descricao |
|---|---|---|---|
| 1.0 | 06/06/2026 | Abraão | Criacao do documento; registro formal das revisoes tecnicas da Sprint 1 (PRs #11 a #15); todos os achados resolvidos e documentados |
