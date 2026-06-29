# Estratégia de Integração — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | ITP-AASP01-001 |
| **Projeto** | AG — Grupos de Usuários |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Produto** | ms.auxo.usuarios |
| **Repositório** | GitLab · http://191.234.192.153/aasp/ms.auxo.usuarios |
| **GP / Tech Lead** | Abraão (GP) · Cezar Hiraki (TL) — Timeware Brasil |
| **Desenvolvedores** | Renan Kiyoshi, Henry Komatsu, Mateus Veloso — Timeware Brasil |
| **PO** | Marcos Turnes — AASP |
| **QA** | Caroline Sousa — AASP |
| **Data base** | 24/06/2026 |
| **Versão** | 1.2 |
| **Status** | Ativo |

---

## 1. Objetivo

Descrever a estratégia de integração do microsserviço ms.auxo.usuarios com os demais componentes do sistema Gerenciador AASP, definindo a ordem de integração, os critérios de prontidão de cada fase, os ambientes utilizados e os resultados esperados. Este documento serve como evidência do processo de Integração (INT) e Verificação (VER) do nível C do MPS.BR.

---

## 2. Visão Geral da Integração

O ms.auxo.usuarios é um microsserviço desenvolvido em .NET 5.0 (net5.0) com Dapper e SQL Server, responsável pelo gerenciamento de grupos de usuários no ecossistema do Gerenciador AASP. Os endpoints são expostos pelo controller `GerenciarGruposController` (rota base `api/gerenciar/grupos`, verbos GET/POST). Ele se integra com os seguintes componentes:

- **Internamente (banco auxo3):** endpoints auto-contidos para CRUD de grupos, função do usuário no grupo e vínculo usuário-grupo. Tabelas: `grupos_usuarios`, `grupos_usuarios_vinculos`, `grupos_usuarios_funcao`.
- **ms.temis.vinculos (banco temis3):** *(planejado — Sprint 2)* microsserviço externo para sincronização de vínculos no domínio Temis, a ser acessado via HTTP REST.
- **Sistema Gerenciador AASP (frontend/BFF):** consumidor dos endpoints do ms.auxo.usuarios, autenticado via JWT Bearer Token emitido pelo sistema de autenticação central.

**Abordagem geral:** integração incremental por componente e por sprint. A Sprint 1 valida os componentes internos (CRUD, função, vínculos). A Sprint 2 integra o ms.temis.vinculos e implementa a auditoria. A Sprint 3 valida o relatório consolidado.

---

## 3. Ordem de Integração dos Componentes

| Fase | Sprint | Componente Integrado | Interface | Critério de Prontidão | Status |
|---|---|---|---|---|---|
| Fase 1 | S1 | CRUD de grupos (AG-20) | `listargrupo`, `buscargrupoporid`, `incluirgrupo`, `alterargrupo`, `excluirgrupo`, `ativardesativar` | Build verde + MRs !1 e !2 aprovados + casos GRP-01 a GRP-07 passando | ✅ Concluído |
| Fase 1 | S1 | Função do usuário no grupo (AG-21) | `alterarfuncaodousuario` | MR !3 aprovado + caso FUNC-01 passando | ✅ Concluído |
| Fase 1 | S1 | Vínculo usuário-grupo (AG-22) | `incluirgrupo`/`alterargrupo` (GrupoDeUsuarios) · `removerusuario` | MRs !4 e !5 aprovados + casos VINC-01, VINC-02 passando | ✅ Concluído |
| Fase 2 | S2 | Auditoria de ações (AG-23) | *(planejado — não implementado)* | Trilha de auditoria implementada + caso AUD-01 passando | ⏳ Em andamento |
| Fase 2 | S2 | Integração ms.temis.vinculos (AG-24) | *(planejado — não implementado)* | Contrato definido + cliente HTTP implementado + caso INT-01 passando | ⏳ Em andamento |
| Fase 3 | S3 | Relatório consolidado (AG-25) | *(planejado — não implementado)* | Relatório retornando dados corretos + caso REL-01 aprovado | 📅 Planejado |

---

## 4. Descrição das Interfaces de Integração

### 4.1 Interface INT-01 — ms.auxo.usuarios → ms.temis.vinculos — *(Planejado — Sprint 2)*

Esta interface está **planejada para a Sprint 2 (AG-24) e ainda não foi implementada** no código. O objetivo é manter o banco temis3 sincronizado com o estado dos vínculos no banco auxo3 sempre que um membro de grupo é alterado.

| Atributo | Valor |
|---|---|
| **Tipo** | HTTP REST (a definir na Sprint 2) |
| **Componente destino** | ms.temis.vinculos (superfície real disponível: `api/gerenciar/grupos/vinculados`) |
| **Quando será chamado** | Após alteração de vínculo de usuário (inclusão/alteração/remoção de membro) |
| **Contrato** | A finalizar no início da Sprint 2 |
| **Autenticação** | Service-to-service (mecanismo a definir; segredos exclusivamente via variáveis de ambiente) |
| **Caso de teste** | INT-01 — Sprint 2 |
| **Status** | ⏳ Planejado (não implementado) |

### 4.2 Interface INT-02 — Sistema Gerenciador AASP → ms.auxo.usuarios

Esta interface representa o consumo dos endpoints do ms.auxo.usuarios pelo frontend ou BFF do Gerenciador AASP.

| Atributo | Valor |
|---|---|
| **Tipo** | HTTP REST |
| **Autenticação** | JWT Bearer Token emitido pelo sistema de autenticação central do Gerenciador AASP |
| **Escopo** | Todos os endpoints `api/gerenciar/grupos/*` exigem token JWT válido com as claims apropriadas |
| **Validação** | Middleware de autenticação validado nos MRs !1 e !2 (Sprint 1) |
| **Status** | ✅ Validado em Sprint 1 (testes de integração e code review) |

---

## 5. Ambiente de Integração

| Ambiente | Descrição | Banco de Dados | Disponibilidade |
|---|---|---|---|
| **Desenvolvimento** | Máquinas dos desenvolvedores (Timeware) | SQL Server local — auxo3 dev | Sprint 1 em diante |
| **Integração contínua** | Pipeline GitLab CI (build + testes a cada MR) | SQL Server em container (CI) | *(previsto — ver GCO/MED)* |
| **Homologação** | Ambiente AASP — instância dedicada com dados anonimizados | SQL Server AASP — auxo3 (e temis3 na Sprint 2) | A partir de Sprint 2 (aguardando confirmação Caroline Sousa) |

**Observação de segurança:** as connection strings e quaisquer segredos de integração são gerenciados exclusivamente via variáveis de ambiente, sem nenhum valor hardcoded no código-fonte ou nos arquivos de configuração versionados.

---

## 6. Critérios de Aceite de Integração

| Interface | Critério de Aceite | Meta | Status Atual |
|---|---|---|---|
| INT-01 (ms.temis.vinculos) | Sincronização bem-sucedida após alteração de vínculo; comportamento correto em caso de falha | 100% dos cenários do caso INT-01 passando | ⏳ Sprint 2 (planejado) |
| INT-02 (Gerenciador AASP) | Todos os endpoints respondem corretamente com JWT válido e rejeitam requisições sem token | 100% dos testes de autenticação passando | ✅ Sprint 1 |
| Relatório (AG-25) | Relatório consolidado retorna dados corretos | Caso REL-01 aprovado por QA | 📅 Sprint 3 (planejado) |

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão | Versão inicial — estratégia de integração do projeto |
| 1.1 | 15/06/2026 | Abraão | Alinhado à API real (endpoints `api/gerenciar/grupos`); integração ms.temis e auditoria marcadas como planejadas (Sprint 2); 3 sprints |
| 1.2 | 24/06/2026 | Time de Melhoria Contínua | Reconciliação com o estado real do GitLab (produto/repositório ms.auxo.usuarios; framework net5.0 onde aplicável; entregas da Sprint 1 integradas em develop com baseline pela tag sprint-1-aceite). |
