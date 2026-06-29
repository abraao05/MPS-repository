# Registro de Revisão Técnica — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | REV-AASP01-001 |
| **Versão** | 1.3 |
| **Data** | 24/06/2026 |
| **Projeto** | AG — ms.auxo.usuarios |
| **Cliente** | AASP |
| **GP/TL** | Abraão (GP) · Cezar Hiraki (TL) (Timeware) |
| **Dev** | Renan Kiyoshi (Timeware) |
| **PO** | Marcos Turnes (AASP) |
| **QA** | Caroline Sousa (AASP) |
| **Processo MPS-SW** | VV — Verificação e Validação (evidência de revisão por pares) |

---

## 1. Objetivo

Registrar as revisões técnicas formais (code reviews via Merge Requests) realizadas durante a Sprint 1 da feature AG — ms.auxo.usuarios, constituindo evidência do processo MPS-SW VV (Verificação e Validação). Cada revisão cobriu MRs específicos com o objetivo de identificar defeitos antes do merge na branch develop. Todos os achados foram classificados por severidade e resolvidos antes da integração. Os endpoints referem-se ao controller real `GerenciarGruposController` (rota base `api/gerenciar/grupos`, HTTP 200/400).

---

## 2. REV-001 — Revisão de MR !1 e !2 (AG-20 — CRUD de grupos)

| Campo | Valor |
|---|---|
| **Data** | 30/05/2026 (MR !1) e 02/06/2026 (MR !2) |
| **Tipo** | Code review — implementação de feature |
| **MRs revisados** | !1 (`incluirgrupo`, `listargrupo` — CRUD base), !2 (`buscargrupoporid`, `alterargrupo`, `excluirgrupo`, `ativardesativar`) |
| **Revisor responsável** | Cezar Hiraki (Tech Lead — Timeware) e Abraão (GP — Timeware) |
| **Autor do código** | Renan Kiyoshi (Timeware) |
| **Resultado** | Aprovado com correções |

### 2.1 Achados

| ID | Descrição | Severidade | Ação tomada | Status |
|---|---|---|---|---|
| RV-001-01 | Validação de nome duplicado ausente no service — `incluirgrupo` aceitava nomes já existentes, lancando exceção do banco (constraint de unicidade) ao inves de retornar erro tratado | P2 — Alto | Adicionada verificação previa `ExisteGrupo` no service antes do INSERT: se o nome já existir, retornar HTTP 400 com `MensagemPublica = "Grupo ja existe"` | Resolvido antes do merge final |
| RV-001-02 | Retorno de campos desnecessarios no DTO de listagem (`listargrupo`) — a resposta expunha campos internos não usados pelo consumidor | P3 — Medio | Ajustado o DTO de listagem para retornar apenas os campos necessários | Resolvido antes do merge final |

**Total de achados REV-001: 2 — P1: 0 | P2: 1 | P3: 1 | Resolvidos: 2/2**

---

## 3. REV-002 — Revisão de MR !3 (AG-21 — Função do Usuario no Grupo)

| Campo | Valor |
|---|---|
| **Data** | 03/06/2026 |
| **Tipo** | Code review — implementação de feature |
| **MR revisado** | !3 (`alterarfuncaodousuario`) |
| **Revisor responsável** | Cezar Hiraki (Tech Lead — Timeware) e Abraão (GP — Timeware) |
| **Autor do código** | Henry Komatsu (Timeware) |
| **Resultado** | Aprovado com correções |

### 3.1 Achados

| ID | Descrição | Severidade | Ação tomada | Status |
|---|---|---|---|---|
| RV-002-01 | Função validada apenas no banco, não no controller — valores fora do enum `FuncaoUsuariosEnum` (Usuario, Administrador) lancavam exceção SQL ao inves de erro tratado | P2 — Alto | Adicionada validação do enum antes de chamar o service: valor invalido retorna HTTP 400 com mensagem clara | Resolvido antes do merge |

**Total de achados REV-002: 1 — P1: 0 | P2: 1 | P3: 0 | Resolvidos: 1/1**

---

## 4. REV-003 — Revisão de MR !4 e !5 (AG-22 — Vinculo Usuario-Grupo)

| Campo | Valor |
|---|---|
| **Data** | 05/06/2026 |
| **Tipo** | Code review — implementação de feature |
| **MRs revisados** | !4 (vinculo de usuários via `GrupoDeUsuarios` em `incluirgrupo`/`alterargrupo`), !5 (`removerusuario`) |
| **Revisor responsável** | Cezar Hiraki (Tech Lead — Timeware) e Abraão (GP — Timeware) |
| **Autor do código** | Mateus Veloso (Timeware) |
| **Resultado** | Aprovado com correções |

### 4.1 Achados

| ID | Descrição | Severidade | Ação tomada | Status |
|---|---|---|---|---|
| RV-003-01 | Falta de verificação de vinculo duplicado antes do INSERT em `grupos_usuarios_vinculos` — o mesmo usuário podia ser vinculado duas vezes ao grupo | P2 — Alto | Adicionada verificação previa: vinculo já existente não e reinserido; operação retorna HTTP 200 com o estado consistente | Resolvido antes do merge |
| RV-003-02 | Soft delete do vinculo (`excluido`) não aplicado em todos os caminhos de `removerusuario` — em um caso o registro não era marcado como `excluido = 1` | P3 — Medio | Corrigido o UPDATE de soft delete para marcar `excluido = 1` consistentemente | Resolvido antes do merge |

**Total de achados REV-003: 2 — P1: 0 | P2: 1 | P3: 1 | Resolvidos: 2/2**

---

## 5. Consolidado da Sprint 1

| Revisão | MRs cobertos | Total achados | P2 — Alto | P3 — Medio | Resolvidos antes merge | Status final |
|---|---|---|---|---|---|---|
| REV-001 | !1, !2 | 2 | 1 | 1 | 2/2 | Aprovado |
| REV-002 | !3 | 1 | 1 | 0 | 1/1 | Aprovado |
| REV-003 | !4, !5 | 2 | 1 | 1 | 2/2 | Aprovado |
| **TOTAL** | **5 MRs** | **5** | **3** | **2** | **5/5 (100%)** | **Todos resolvidos** |

Nenhum achado P1 (critico) identificado na Sprint 1. Todos os achados P2 e P3 foram resolvidos antes do merge final em develop. Nenhum defeito foi para o ambiente de homologação sem correção previa. Resultado confirmado pelo aceite sem ressalvas de Caroline Sousa (AASP) em 06/06/2026.

---

## 6. Proximas revisões — Sprint 2

Revisões técnicas previstas para a Sprint 2, cobrindo as historias AG-23 (Auditoria das operações de escrita) e AG-24 (Integração com ms.temis.vinculos) — ambas ainda não implementadas. Estimativa de MRs a serem revisados: !6 (AG-23) e !7 (AG-24). O processo de revisão seguira o mesmo padrão desta Sprint: revisão pelo Tech Lead antes de qualquer merge em develop, com registro formal de achados e acompanhamento até resolução.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 06/06/2026 | Abraão | Criação do documento; registro formal das revisões técnicas da Sprint 1 (MRs !1 a !5) |
| 1.1 | 15/06/2026 | Abraão | Achados e endpoints alinhados a API real (HTTP 200/400; função Usuario/Administrador; tabelas reais) |
| 1.2 | 24/06/2026 | Time de Melhoria Contínua | Reconciliação com o GitLab: 2 revisores por MR — Cezar (TL) + Abraão (GP) (antes 1). |
| 1.3 | 24/06/2026 | Time de Melhoria Contínua | Reconciliação com o estado real do GitLab (produto/repositório ms.auxo.usuarios; framework net5.0 onde aplicável; entregas da Sprint 1 integradas em develop com baseline pela tag sprint-1-aceite). |
