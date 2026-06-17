# Estratégia de Integração — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | ITP-AASP01-001 |
| **Projeto** | AG — Grupos de Usuários |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Produto** | ms.auxo.gruposusuarios |
| **Repositório** | Azure DevOps · komatsuhenry67/gerenciador-aasp/ms.auxo.gruposusuarios |
| **GP / Tech Lead** | Abraão Oliveira (GP) · Cézar Velázquez (TL) — Timeware Brasil |
| **Desenvolvedores** | Renan Kioshi, Henry Komatsu, Mateus Veloso — Timeware Brasil |
| **PO** | Marcos Turnes — AASP |
| **QA** | Leonardo Francisco Pereira — AASP |
| **Data base** | 26/05/2026 |
| **Versão** | 1.0 |
| **Status** | Ativo |

---

## 1. Objetivo

Descrever a estratégia de integração do microsserviço ms.auxo.gruposusuarios com os demais componentes do sistema Gerenciador AASP, definindo a ordem de integração, os critérios de prontidão de cada fase, os ambientes utilizados e os resultados esperados. Este documento serve como evidência dos processos de Integração do Produto (ITP) e Verificação e Validação (VV) do nível C do MPS.BR.

---

## 2. Visão Geral da Integração

O ms.auxo.gruposusuarios é um microsserviço REST desenvolvido em .NET Framework 4.7.2 com Dapper e SQL Server, responsável pelo gerenciamento de grupos de usuários no ecossistema do Gerenciador AASP. Ele se integra com os seguintes componentes:

- **Internamente (banco auxo3):** endpoints REST auto-contidos para CRUD de grupos, gerenciamento de permissões RBAC e vínculos usuário-grupo. Tabelas: Grupos, PermissoesGrupo, UsuariosGrupo, AuditoriaGrupos.
- **ms.temis.vinculos (banco temis3):** microsserviço externo responsável pela sincronização de vínculos usuário-grupo no domínio Temis, acessado via HTTP REST síncrono.
- **Sistema Gerenciador AASP (frontend/BFF):** consumidor dos endpoints REST do ms.auxo.gruposusuarios, autenticado via JWT Bearer Token emitido pelo sistema de autenticação central.

**Abordagem geral:** integração incremental por componente e por sprint. A Sprint 1 valida os componentes internos (CRUD, permissões, vínculos). A Sprint 2 integra o ms.temis.vinculos e implementa a auditoria. A Sprint 3 valida os relatórios consolidados com dados integrados. A Sprint 4 realiza a homologação final com o ambiente AASP.

---

## 3. Ordem de Integração dos Componentes

| Fase | Sprint | Componente Integrado | Interface | Critério de Prontidão | Status |
|---|---|---|---|---|---|
| Fase 1 | S1 | CRUD base de grupos (AG-20) | Endpoints REST /grupos (POST, GET, PUT, DELETE) | Build verde + PRs #11 e #12 aprovados + casos GRP-01 a GRP-05 passando | ✅ Concluído |
| Fase 1 | S1 | Permissões por grupo (AG-21) | PUT /grupos/{id}/permissoes | Validação de enum de permissões + PR #13 aprovado + casos PERM-01 e PERM-02 passando | ✅ Concluído |
| Fase 1 | S1 | Vínculo usuário-grupo (AG-22) | POST /grupos/{id}/usuarios · DELETE /grupos/{id}/usuarios/{uid} | FK validada no banco + PRs #14 e #15 aprovados + casos VINC-01, VINC-02, VINC-03 passando | ✅ Concluído |
| Fase 2 | S2 | Auditoria de ações (AG-23) | Escrita na tabela AuditoriaGrupos via triggers | Tabela AuditoriaGrupos criada + trigger de INSERT ativo em toda operação de escrita + caso AUD-01 passando | ⏳ Em andamento |
| Fase 2 | S2 | Integração ms.temis.vinculos (AG-24) | HTTP POST para ms.temis.vinculos/api/vinculos | Contrato de API definido + cliente HTTP implementado + caso INT-01 passando + comportamento de retry testado | ⏳ Em andamento |
| Fase 3 | S3 | Relatório consolidado (AG-25) | GET /grupos/relatorio (JOIN entre Grupos, PermissoesGrupo e UsuariosGrupo) | Endpoint retornando payload correto + caso REL-01 aprovado | 📅 Planejado |
| Fase 4 | S4 | Homologação final | Todos os endpoints integrados + ms.temis.vinculos em ambiente AASP | Leonardo Francisco Pereira (AASP/QA) valida todos os cenários de aceite em ambiente de homologação | 📅 Planejado |

---

## 4. Descrição das Interfaces de Integração

### 4.1 Interface INT-01 — ms.auxo.gruposusuarios → ms.temis.vinculos

Esta interface é acionada sempre que um vínculo usuário-grupo é criado ou removido no ms.auxo.gruposusuarios. O objetivo é manter o banco temis3 sincronizado com o estado do banco auxo3.

| Atributo | Valor |
|---|---|
| **Tipo** | HTTP REST síncrono |
| **Endpoint destino** | POST http://ms.temis.vinculos/api/vinculos |
| **Quando é chamado** | Ao executar POST /grupos/{id}/usuarios (operacao: ADD) ou DELETE /grupos/{id}/usuarios/{uid} (operacao: REMOVE) |
| **Payload request** | `{"usuarioId": int, "grupoId": int, "operacao": "ADD" ou "REMOVE"}` |
| **Response de sucesso** | HTTP 200 ou 201 com body `{"vinculoId": int, "status": "OK"}` |
| **Response de erro** | HTTP 4xx ou 5xx com mensagem descritiva no body |
| **Timeout** | 5 segundos |
| **Retry** | 1 tentativa adicional em caso de timeout ou resposta HTTP 5xx |
| **Comportamento após retry** | Log de erro registrado + exceção propagada ao chamador (operação não é confirmada no auxo3) |
| **Autenticação** | Service-to-service via chave compartilhada no header `X-Service-Key` |
| **Caso de teste** | INT-01 — Sprint 2 |
| **Status** | ⏳ Em andamento (contrato definido; cliente HTTP implementado) |

### 4.2 Interface INT-02 — Sistema Gerenciador AASP → ms.auxo.gruposusuarios

Esta interface representa o consumo dos endpoints REST do ms.auxo.gruposusuarios pelo frontend ou BFF do Gerenciador AASP.

| Atributo | Valor |
|---|---|
| **Tipo** | HTTP REST |
| **Autenticação** | JWT Bearer Token emitido pelo sistema de autenticação central do Gerenciador AASP |
| **Escopo** | Todos os endpoints /grupos/* exigem token JWT válido e com as claims apropriadas |
| **Validação** | Middleware de autenticação implementado nos PRs #11 e #12 (Sprint 1) |
| **Status** | ✅ Validado em Sprint 1 (testes de integração e code review) |

---

## 5. Ambiente de Integração

| Ambiente | Descrição | Banco de Dados | Disponibilidade |
|---|---|---|---|
| **Desenvolvimento** | Máquinas dos desenvolvedores (Timeware) + ms.temis.vinculos em ambiente dev compartilhado | SQL Server local — auxo3 dev | Sprint 1 e Sprint 2 |
| **Integração contínua** | Pipeline Azure DevOps — build + testes automatizados a cada PR | SQL Server em container (CI) | Sprint 1 em diante |
| **Homologação** | Ambiente AASP — instância dedicada com dados anonimizados | SQL Server AASP — auxo3 e temis3 | A partir de Sprint 2 (aguardando confirmação Leonardo Francisco Pereira) |

**Observação de segurança:** as connection strings e a chave de serviço X-Service-Key são gerenciadas exclusivamente via variáveis de ambiente, sem nenhum valor hardcoded no código-fonte ou nos arquivos de configuração versionados.

---

## 6. Critérios de Aceite de Integração

| Interface | Critério de Aceite | Meta | Status Atual |
|---|---|---|---|
| INT-01 (ms.temis.vinculos) | Chamada HTTP bem-sucedida em cenário ADD e em cenário REMOVE; comportamento correto de retry em caso de falha | 100% dos cenários do caso INT-01 passando | ⏳ Sprint 2 |
| INT-01 (ms.temis.vinculos) | Falha após retry deve gerar log de erro e não confirmar a operação no auxo3 | Validado por teste de falha simulada | ⏳ Sprint 2 |
| INT-02 (Gerenciador AASP) | Todos os endpoints respondem corretamente com JWT válido e rejeitam requisições sem token | 100% dos testes de autenticação passando | ✅ Sprint 1 |
| Relatório (AG-25) | GET /grupos/relatorio retorna dados consolidados corretos com JOIN entre as três tabelas | Caso REL-01 aprovado por QA | 📅 Sprint 3 |
| Homologação final | Todos os cenários de aceite validados por Leonardo Francisco Pereira em ambiente AASP | 100% dos cenários aprovados | 📅 Sprint 4 |

---

## Histórico de Revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão Oliveira | Versão inicial — estratégia de integração definida para as quatro fases do projeto |
