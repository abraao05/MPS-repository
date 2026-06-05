# Tabela de Proveniência — Verificação e Validação

> Origens: **[GSD]** / **[Jira]** / **[Manual]** / **[Derivado]**. **(confirmado)** comprovado no diagnóstico; **(hipótese)** depende da Timeware.

| Campo | Origem | Fonte exata | Confiança |
|---|---|---|---|
| Identificação | [GSD]+[Manual] | `PROJECT.md` / gatilho | confirmado |
| 1. Produtos selecionados para V&V | [GSD] | `VALIDATION.md` (seleção de WPs) | confirmado |
| 2. Procedimento de revisão por pares | [Manual] | gatilho — padrão "revisão humana no PR antes do merge" (no GSD o procedimento documentado era lacuna) | confirmado |
| 2. Material de apoio (checklist) | [Manual] | texto-padrão organizacional | confirmado |
| 3. Métodos/critérios/ambientes | [GSD] | `VALIDATION.md` (infra de teste), config de teste, `acceptance_criteria` | confirmado |
| 4. Execução e tratamento | [GSD] | `VERIFICATION.md`, `REVIEW.md`→`REVIEW-FIX.md`, commits de correção | confirmado |
| 4. Revisão por pares (registro) | [GSD/Jira] | PR aprovado por revisor humano (Jira/repo); achados por severidade | hipótese (depende de onde a Timeware registra o PR) |
| 5. Análise/registro/comunicação | [GSD]+[Manual] | `VERIFICATION` + audits (registro); comunicação a interessados = manual | confirmado |
