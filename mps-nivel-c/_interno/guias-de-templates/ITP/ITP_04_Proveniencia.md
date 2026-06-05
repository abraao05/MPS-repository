# Tabela de Proveniência — Integração do Produto

> Origens: **[GSD]** / **[Jira]** / **[Manual]** / **[Derivado]**. **(confirmado)** comprovado no diagnóstico; **(hipótese)** depende da Timeware.

| Campo | Origem | Fonte exata | Confiança |
|---|---|---|---|
| Identificação | [GSD]+[Manual] | `PROJECT.md` / gatilho | confirmado |
| 1. Procedimentos/critérios de integração | [Manual] | gatilho (no GSD a estratégia formal a priori era lacuna) | confirmado |
| 1. Ordem de integração | [GSD] | `ROADMAP.md` (dependências entre fases, build order) | confirmado |
| 1.1 Interfaces | [GSD] | `UI-SPEC.md`, "Contract Verification" do audit | confirmado |
| 2. Ambiente de integração | [GSD] | config de build no repo, ambiente de preview | confirmado |
| 3. Prontidão dos componentes | [GSD] | `VERIFICATION.md` ("truths"), `REVIEW.md` | confirmado |
| 4. Execução da integração | [GSD] | "Integration Check" do `MILESTONE-AUDIT.md`, merges no git log | confirmado |
| 5. Teste do produto integrado | [GSD] | "E2E Flows" do audit + resultados da suíte de testes | confirmado |
| 6. Produto entregue | [GSD] | commits de deploy, tag de milestone | confirmado |
| 6. Material de apoio | [Manual] | gatilho (lacuna no projeto solo) | confirmado |
