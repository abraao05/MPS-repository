# Registro de Revisão Técnica — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | REV-AASP01-001 |
| **Versão** | 1.0 |
| **Data** | 06/06/2026 |
| **Projeto** | AG — ms.auxo.gruposusuarios |
| **Cliente** | AASP |
| **GP/TL** | Abraão Oliveira (GP) · Cézar Velázquez (TL) (Timeware) |
| **Dev** | Renan Kioshi (Timeware) |
| **PO** | Marcos Turnes (AASP) |
| **QA** | Leonardo Francisco Pereira (AASP) |
| **Processo MPS-SW** | VV — Verificação e Validação (evidência de revisão por pares) |

---

## 1. Objetivo

Registrar as revisões técnicas formais (code reviews via Pull Requests) realizadas durante a Sprint 1 da feature AG — ms.auxo.gruposusuarios, constituindo evidência do processo MPS-SW VV (Verificação e Validação). Cada revisão cobriu PRs específicos com o objetivo de identificar defeitos antes do merge na branch develop. Todos os achados foram classificados por severidade e resolvidos antes da integração.

---

## 2. REV-001 — Revisão de PR #11 e #12 (AG-20 — CRUD base e endpoints GET/PUT/DELETE)

| Campo | Valor |
|---|---|
| **Data** | 30/05/2026 (PR #11) e 02/06/2026 (PR #12) |
| **Tipo** | Code review — implementação de feature |
| **PRs revisados** | #11 (POST /grupos — CRUD base), #12 (GET /grupos, GET /grupos/{id}, PUT /grupos/{id}, DELETE /grupos/{id}) |
| **Revisor responsável** | Cézar Velázquez (Tech Lead — Timeware) |
| **Autor do código** | Renan Kioshi (Timeware) |
| **Resultado** | Aprovado com correções |

### 2.1 Achados

| ID | Descrição | Severidade | Ação tomada | Status |
|---|---|---|---|---|
| RV-001-01 | Validação de nome duplicado ausente no controller — o endpoint POST /grupos aceitava nomes já existentes, lançando exceção do banco (constraint de unicidade) ao inves de retornar HTTP 409 com mensagem amigável ao consumidor da API | P2 — Alto | Adicionada verificação prévia no GrupoService antes do INSERT: se nome já existir com Ativo=true, retornar HTTP 409 com mensagem "Nome de grupo já existe" | Resolvido antes do merge final |
| RV-001-02 | Retorno HTTP 404 faltando em GET /grupos/{id} para id inexistente — o endpoint retornava HTTP 500 (exceção não tratada) quando o id solicitado não existia no banco, ao inves de HTTP 404 com mensagem clara | P3 — Médio | Adicionado "null check" no GrupoService após a consulta Dapper; quando retorno e null, o controller retorna HTTP 404 com mensagem "Grupo não encontrado" | Resolvido antes do merge final |

**Total de achados REV-001: 2 — P1: 0 | P2: 1 | P3: 1 | Resolvidos: 2/2**

---

## 3. REV-002 — Revisão de PR #13 (AG-21 — Permissões por Grupo)

| Campo | Valor |
|---|---|
| **Data** | 03/06/2026 |
| **Tipo** | Code review — implementação de feature |
| **PR revisado** | #13 (PUT /grupos/{id}/permissoes) |
| **Revisor responsável** | Cézar Velázquez (Tech Lead — Timeware) |
| **Autor do código** | Henry Komatsu (Timeware) |
| **Resultado** | Aprovado com correções |

### 3.1 Achados

| ID | Descrição | Severidade | Ação tomada | Status |
|---|---|---|---|---|
| RV-002-01 | Enum de permissão validado apenas no banco (constraint de coluna), não no controller — valores inválidos enviados pela API lançavam exceção SQL ao inves de retornar HTTP 400 com mensagem clara. Valores aceitos: Leitura, Escrita, Exclusao, Administracao, Relatorio | P2 — Alto | Adicionada validação do enum no controller antes de chamar o PermissaoService: se o valor enviado não pertencer ao enum, retornar HTTP 400 com mensagem "Permissao inválida: {valor}. Valores aceitos: Leitura, Escrita, Exclusao, Administracao, Relatorio" | Resolvido antes do merge |

**Total de achados REV-002: 1 — P1: 0 | P2: 1 | P3: 0 | Resolvidos: 1/1**

---

## 4. REV-003 — Revisão de PR #14 e #15 (AG-22 — Vínculo Usuário-Grupo)

| Campo | Valor |
|---|---|
| **Data** | 05/06/2026 |
| **Tipo** | Code review — implementação de feature |
| **PRs revisados** | #14 (POST /grupos/{id}/usuarios), #15 (DELETE /grupos/{id}/usuarios/{uid}) |
| **Revisor responsável** | Cézar Velázquez (Tech Lead — Timeware) |
| **Autor do código** | Mateus Veloso (Timeware) |
| **Resultado** | Aprovado com correções |

### 4.1 Achados

| ID | Descrição | Severidade | Ação tomada | Status |
|---|---|---|---|---|
| RV-003-01 | Falta de validação se usuário está ativo antes de vincular — o endpoint POST /grupos/{id}/usuarios aceitava vincular usuários com Ativo=false no banco, criando vínculos inválidos em UsuariosGrupo | P2 — Alto | Adicionada consulta prévia no UsuarioGrupoService: se usuario.Ativo == false, retornar HTTP 422 Unprocessable Entity com mensagem "Usuário inativo não pode ser vinculado a grupo" | Resolvido antes do merge |
| RV-003-02 | Tratamento de FK violation em DELETE vínculo não retornava mensagem amigável — quando o vínculo já havia sido removido (Ativo=false) ou o usuário não estava vinculado, o endpoint lançava exceção SQL ao inves de HTTP 404 | P3 — Médio | Adicionado "null check" no repositório Dapper antes do UPDATE de soft delete; quando vínculo não encontrado, retornar HTTP 404 com mensagem "Vínculo não encontrado" | Resolvido antes do merge |

**Total de achados REV-003: 2 — P1: 0 | P2: 1 | P3: 1 | Resolvidos: 2/2**

---

## 5. Consolidado da Sprint 1

| Revisão | PRs cobertos | Total achados | P2 — Alto | P3 — Médio | Resolvidos antes merge | Status final |
|---|---|---|---|---|---|---|
| REV-001 | #11, #12 | 2 | 1 | 1 | 2/2 | Aprovado |
| REV-002 | #13 | 1 | 1 | 0 | 1/1 | Aprovado |
| REV-003 | #14, #15 | 2 | 1 | 1 | 2/2 | Aprovado |
| **TOTAL** | **5 PRs** | **5** | **3** | **2** | **5/5 (100%)** | **Todos resolvidos** |

Nenhum achado P1 (crítico) identificado na Sprint 1. Todos os achados P2 e P3 foram resolvidos antes do merge final em develop. Nenhum defeito foi para o ambiente de homologação sem correção prévia. Resultado confirmado pelo aceite sem ressalvas de Leonardo Francisco Pereira (AASP) em 06/06/2026.

---

## 6. Próximas revisões — Sprint 2

Revisões técnicas previstas para a Sprint 2, cobrindo as histórias AG-23 (Auditoria via tabela AuditoriaGrupos) e AG-24 (Integração com ms.temis.vinculos). Estimativa de PRs a serem revisados: #16 (AG-23 — implementação da auditoria) e #17 (AG-24 — integração HTTP com ms.temis.vinculos). O processo de revisão seguirá o mesmo padrão desta Sprint: revisão pelo Tech Lead antes de qualquer merge em develop, com registro formal de achados e acompanhamento até resolução.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 06/06/2026 | Abraão Oliveira | Criação do documento; registro formal das revisões técnicas da Sprint 1 (PRs #11 a #15); todos os achados resolvidos e documentados |
