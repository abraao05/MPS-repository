# Matriz de Rastreabilidade — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | RASTR-AASP-GOV-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |

---

## Matriz

Rastreabilidade requisito × fase de implementação × critério de aceite que o verifica (ver REQ-AASP-GOV-001 e VV-AASP-GOV-001).

| Requisito | Descrição resumida | Fase de implementação | Critério de aceite | Situação |
|---|---|---|---|---|
| RF01 | Autenticação no Sensr por desenvolvedor | Fase 2 — Autenticação | CA07 — Resiliência por dev | ✅ Verificado |
| RF02 | Criar ou reutilizar Epic no Jira por projeto | Fase 3 — Desenvolvimento | CA02 — Fidelidade da hierarquia | ✅ Verificado |
| RF03 | Criar Task com `#ID` e campos preservados | Fase 3 — Desenvolvimento | CA02, CA03 — Hierarquia e conteúdo | ✅ Verificado |
| RF04 | Criar Subtask vinculada à Task pai | Fase 3 — Desenvolvimento | CA02 — Fidelidade da hierarquia | ✅ Verificado |
| RF05 | Verificar e atualizar status de card existente | Fase 3 — Desenvolvimento | CA05 — Sincronização incremental | ✅ Verificado |
| RF06 | Migrar histórico como comentários | Fase 3 — Desenvolvimento | CA06 — Migração do histórico | ✅ Verificado |
| RF07 | Converter HTML para ADF/texto plano | Fase 3 — Desenvolvimento | CA03 — Fidelidade do conteúdo | ✅ Verificado |
| RF08 | Mapear status Sensr → Jira | Fase 2/3 — Mapeamento/Dev | CA04, CA05 — Status | ✅ Verificado |
| RF09 | Sanitizar labels | Fase 3 — Desenvolvimento | CA03 — Fidelidade do conteúdo | ✅ Verificado |
| RF10 | Configuração via `appsettings.json` | Fase 1/3 — Arquitetura/Dev | CA07 — Resiliência | ✅ Verificado |
| RF11 | Executável compatível com Azure Scheduler | Fase 3 — Desenvolvimento | Entrega ao cliente | ✅ Verificado |
| RNF01 | Idempotência sem duplicatas | Fase 3/4 — Dev/Homologação | CA01 — Sem duplicatas | ✅ Verificado |
| RNF02 | Confiabilidade por desenvolvedor | Fase 3 — Desenvolvimento | CA07 — Resiliência | ✅ Verificado |
| RNF03 | Log estruturado de operações | Fase 3 — Desenvolvimento | Auditoria de execução | ✅ Verificado |
| RNF04 | Separação em camadas | Fase 1 — Arquitetura | Decisão D01 | ✅ Verificado |
| RNF05 | Credenciais fora do código | Fase 1/3 — Arquitetura/Dev | Decisão D02 | ✅ Verificado |
| RNF06 | Compatibilidade .NET 8 / Azure | Fase 3 — Desenvolvimento | Entrega ao cliente | ✅ Verificado |

## Cobertura

- **Requisitos sem cobertura de critério:** nenhum — todos os RF e RNF têm critério de aceite ou marco de verificação associado.
- **Itens desenvolvidos sem requisito associado:** nenhum identificado.
- Os critérios de aceite CA01–CA07 estão detalhados em VV-AASP-GOV-001; as decisões de arquitetura D01 e D02 estão em GDE-AASP-GOV-001.

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Matriz de rastreabilidade consolidada a partir do Registro de Projeto AASP_Automacao-Governanca v2.0 (08/06/2026). |
