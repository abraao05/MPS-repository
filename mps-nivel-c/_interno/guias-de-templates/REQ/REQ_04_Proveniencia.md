# Tabela de Proveniência — Especificação de Requisitos

> Origens: **[GSD]** lê artefato GSD · **[Jira]** lê rastreador · **[Manual]** gatilho ao gestor · **[Derivado]** calculado. **(confirmado)** = fonte comprovada no diagnóstico; **(hipótese)** = depende da estrutura Jira/GSD da Timeware.

| Campo | Origem | Fonte exata | Confiança |
|---|---|---|---|
| Identificação/versão | [Manual] | gatilho ao versionar | confirmado |
| 1. Critérios de parte interessada | [Manual] | texto-padrão organizacional | confirmado |
| 1. Tabela de partes interessadas | [Manual] | gatilho (no GSD aparece disperso no DISCUSSION-LOG) | confirmado |
| 2. Necessidades levantadas | [GSD] | `DISCUSSION-LOG.md`, `PROJECT.md` §Requirements | confirmado |
| 2. Confirmação de entendimento | [GSD] | `acceptance_criteria` nos planos de fase | confirmado |
| 3. Tabela de requisitos (ID, descrição) | [GSD]+[Jira] | `REQUIREMENTS.md` (IDs) / issues no Jira | confirmado (GSD) / hipótese (Jira) |
| 3. Prioridade | [Jira]+[GSD] | prioridade da issue / ordem no milestone | hipótese |
| 3. Alocação para fase | [GSD] | `PLAN.md` (`requirements:` → fase) | confirmado |
| 3. Status | [Jira] | status da issue | hipótese |
| 3.1 Conceitos/cenários/interfaces | [GSD] | `RESEARCH.md`, `UI-SPEC.md`, "E2E Flows" do audit | confirmado |
| 4. Compromisso da equipe | [Manual] | gatilho (no GSD é implícito na execução) | confirmado |
| 5. Rastreabilidade bidirecional | [GSD] | `PLAN` (`requirements`) + `VERIFICATION` (cobertura) + commits citam ID | confirmado |
| 5. Verificação de órfãos | [GSD] | `MILESTONE-AUDIT.md` (orphan detection, cruzamento 3 fontes) | confirmado |
| 6. Análise de suficiência | [GSD]+[Manual] | `RESEARCH`/`CONTEXT` + julgamento | confirmado |
| 7. Validação | [GSD] | `UAT.md`/`HUMAN-UAT.md` + `VALIDATION.md` | confirmado |
