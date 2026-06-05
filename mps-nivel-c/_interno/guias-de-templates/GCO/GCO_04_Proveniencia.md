# Tabela de Proveniência — Gerência de Configuração

> Origens: **[GSD]** / **[Jira]** / **[Manual]** / **[Derivado]**. **(confirmado)** comprovado no diagnóstico; **(hipótese)** depende da Timeware.

| Campo | Origem | Fonte exata | Confiança |
|---|---|---|---|
| Identificação | [GSD]+[Manual] | `PROJECT.md` / gatilho | confirmado |
| 1. Itens de configuração (lista) | [GSD] | repositório Git (arquivos), migrações, artefatos de fase | confirmado |
| 1. Campos do IC (situação, relações) | [GSD]+[Manual] | `SUMMARY` frontmatter (`requires/provides/affects`, tags) + consolidação manual no registro formal | confirmado (parcial) / manual (consolidação) |
| 2. Sistema de GC e controle de mudanças | [GSD] | Git (commits convencionais, branches, tags); fluxo de PR | confirmado |
| 3. Baselines | [GSD] | tags git por milestone + `milestones/` | confirmado |
| 4. Registros e modificações | [GSD] | `git log` completo; `SUMMARY` por plano | confirmado |
| 5. Auditorias de configuração | [GSD] | `MILESTONE-AUDIT.md` (integridade, órfãos, integração) | confirmado |
