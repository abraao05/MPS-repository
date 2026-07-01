# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Documento de Design (PCP)
**Código:** PCP-AASP01-001
**Versão auditada:** 1.3
**Data do documento:** 24/06/2026
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 0 | 0 |
| Conteúdo (CNT) | 0 | 1 | 2 | 1 |
| Datas (DT) | 0 | 0 | 0 | 0 |
| Papéis (PAP) | 0 | 0 | 0 | 0 |
| Coerência (CON) | 0 | 1 | 0 | 0 |
| MPS.BR (MPS) | 0 | 0 | 0 | 0 |
| **TOTAL** | **0** | **2** | **2** | **1** |

**Veredicto:** NÃO-CONFORME

---

## OBSERVAÇÕES POSITIVAS

O PCP-AASP01-001 é um documento de design tecnicamente sólido. O modelo de dados está bem definido com tipos, restrições e semântica de cada campo. O diagrama de camadas (seção 2.2) é claro e a separação de responsabilidades (Controller/Service/Repository) é corretamente descrita. As decisões arquiteturais referenciam corretamente o GDE.

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-PCP-01 — Seção 6 (Integração ms.temis.vinculos) é completamente vazia de conteúdo técnico
**Severidade:** 🟡 Moderada
**RAP impactado:** PCP — design técnico cobrindo todas as entregas planejadas
**Localização:** Seção 6 — Integração com ms.temis.vinculos
**Problema:** A seção 6 afirma que a integração "está planejada para a Sprint 2 (AG-24) e ainda não foi implementada no código" e delega toda a especificação para o ITP-AASP01-001. Na data do documento (24/06/2026), a Sprint 2 deveria estar próxima do encerramento ou já encerrada. Se a integração foi implementada, o PCP deve ser atualizado com o design técnico real (contrato, cliente HTTP, tratamento de erros). Se não foi, o design pendente para a Sprint 3 deve ser documentado aqui.
**Evidência:** > "A sincronização de vinculos com o microsserviço ms.temis.vinculos (banco temis3) esta planejada para a Sprint 2 (AG-24) e ainda não foi implementada no código."
**Referência normativa:** PCP — o documento de design deve cobrir as decisões técnicas de todas as features entregues ou planejadas.
**Ação corretiva:** Atualizar a seção 6 com o design técnico da integração: endpoint de destino (`api/gerenciar/grupos/vinculados`), DTO de chamada, tratamento de falhas (retry policy, fallback), mecanismo de autenticação service-to-service, e timeout configurado.

---

### NC-PCP-02 — Tabela grupos_usuarios_funcao não tem PK definida
**Severidade:** 🟡 Moderada
**RAP impactado:** PCP — modelo de dados completo
**Localização:** Seção 3.3 — Tabela grupos_usuarios_funcao
**Problema:** A tabela `grupos_usuarios_funcao` não tem uma coluna de chave primária definida. As colunas listadas são `usuario_id`, `função`, `escritorio_id` e `excluido`. A ausência de PK explícita pode indicar que a chave é composta (usuario_id + escritorio_id) ou que existe uma coluna `id` não documentada. Para um design técnico, a definição completa da PK é obrigatória.
**Evidência:** > "| usuario_id | int | NOT NULL | Usuario | | função | int | NOT NULL | [...] | escritorio_id | int | NOT NULL | [...] | excluido | int | NOT NULL, DEFAULT 0 |" — sem coluna PK.
**Referência normativa:** PCP — modelo de dados deve especificar chaves primárias e relacionamentos.
**Ação corretiva:** Adicionar a PK da tabela `grupos_usuarios_funcao` (ex.: `id int PK IDENTITY(1,1)` ou `(usuario_id, escritorio_id) composite PK`). Verificar consistência com o schema real do banco auxo3.

---

### NC-PCP-03 — Endpoint "buscargrupoporid" descrito como "Listar os usuários de um grupo" — nome vs. semântica confusos
**Severidade:** 🟢 Leve
**RAP impactado:** PCP — clareza do contrato de API
**Localização:** Seção 4 — Endpoints, linha buscargrupoporid
**Problema:** O endpoint `GET buscargrupoporid` é descrito como "Listar os usuários de um grupo" — mas o nome sugere "buscar grupo por ID". Esta ambiguidade semântica pode dificultar a manutenção e o entendimento do contrato por consumidores futuros. O REQ-AASP01-001 também descreve `buscargrupoporid` como "consulta dos usuários de um grupo", confirmando que o nome não reflete o comportamento.
**Evidência:** > "GET | buscargrupoporid | Listar os usuários de um grupo | AG-20 (RF-02)"
**Referência normativa:** PCP — contratos de API devem ser claramente documentados.
**Ação corretiva:** Observação (não é NC estrutural, pois o código é a fonte da verdade): documentar explicitamente no PCP que `buscargrupoporid` retorna os **membros (usuários)** do grupo identificado pelo ID, não os atributos do grupo em si. Considerar renomear o endpoint em versão futura.

---

### NC-PCP-04 — Diagrama de arquitetura referenciado mas sem garantia de consistência com o texto
**Severidade:** 🔵 Obs
**RAP impactado:** —
**Localização:** Seção 2 — referência ao PNG
**Problema:** O documento referencia `PCP-AASP01-001_Diagrama-Arquitetura.png` (e .svg). Os arquivos existem no repositório. O diagrama foi gerado mas não há evidência de revisão formal do diagrama contra o texto do PCP.
**Evidência:** > "![Diagrama de Arquitetura — ms.auxo.usuarios](PCP-AASP01-001_Diagrama-Arquitetura.png)"
**Referência normativa:** PCP — consistência entre diagramas e texto.
**Ação corretiva:** Observação: verificar que o diagrama SVG/PNG reflete a arquitetura descrita no texto (4 camadas, ms.temis.vinculos como integração externa planejada).
