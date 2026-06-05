# Tabela de Proveniência — Termo de Encerramento e Aceite do Projeto (TPL-GPR-004)

> **Para que serve.** Esta tabela diz, para cada campo do Termo de Encerramento, **de onde o dado vem** e **quem o preenche**. É o insumo que torna a automação construível: a skill sabe quais campos pode preencher sozinha (lendo GSD ou Jira) e quais precisa solicitar ao gestor.
>
> **As quatro origens:**
> - **[GSD]** — extraível dos artefatos do GSD (PROJECT, SUMMARY, STATE, MILESTONE-AUDIT, RETROSPECTIVE etc.). A skill lê e preenche.
> - **[Jira]** — extraível do rastreador de tarefas. A skill lê e preenche.
> - **[Manual]** — não existe em ferramenta nenhuma; vem de rotina gerencial (decisão, ata, aceite do cliente). A skill **não preenche** — emite um **gatilho** pedindo a entrada.
> - **[Derivado]** — calculado a partir de campos anteriores. A skill calcula.
>
> **(confirmado)** = fonte comprovada no diagnóstico real do repositório Trainer Connect. **(hipótese)** = depende de confirmar como a Timeware estrutura seus artefatos.

---

| Campo | Origem | Fonte exata | Confiança |
|---|---|---|---|
| Nome / código do documento | [Manual] | gatilho: "Qual o código do TEN?" | confirmado |
| Projeto / cliente / data de encerramento | [GSD] + [Manual] | `PROJECT.md` (nome); data e cliente são manuais (gatilho) | confirmado |
| Gerente de Projeto | [Manual] | gatilho (informação gerencial, não existe em GSD/Jira de forma estruturada) | confirmado |
| **1. Resumo do projeto** | [GSD] | `SUMMARY.md` do milestone final + `PROJECT.md` §objetivo | confirmado |
| **2. Entregas realizadas — linha por entrega** | [GSD] | `STATE.md` (% fases) + `MILESTONE-AUDIT.md` (entregas por milestone) + tags git | confirmado |
| **2. Entregas parqueadas / canceladas** | [GSD] + [Manual] | CRs aprovados referenciados nos artefatos GSD + gatilho para confirmar referência ao CR formal | confirmado |
| **3.1 Escopo entregue conforme planejado** | [GSD] | `MILESTONE-AUDIT.md` + `VERIFICATION.md` (cobertura dos requisitos) | confirmado |
| **3.2 Ajustes via CR aprovado** | [GSD] + [Manual] | CRs formais gerados durante o projeto; gatilho para confirmar referência exata | confirmado |
| **3.3 Escopo excluído** | [GSD] | `PROJECT.md` §Out of Scope + CRs de parqueamento | confirmado |
| **4. Aceite do cliente — existência** | [Manual] | gatilho: "O aceite foi obtido formalmente? Em que data? Qual a referência?" — é o gatilho mais crítico deste documento | confirmado (aceite é sempre manual — não há registro automático) |
| **4. Aceite do cliente — referência à ata** | [Manual] | código/link da ata de encerramento ou e-mail de aceite formal | confirmado |
| **5. Transição — responsável pela sustentação** | [Manual] | gatilho: "Quem assume a sustentação após o encerramento?" | confirmado |
| **5. Transição — o que foi transferido** | [GSD] + [Manual] | `PROJECT.md` (repositório, stack, deploy); acessos e documentação operacional são confirmados manualmente | confirmado |
| **5. Pendências de transição** | [Manual] | gatilho: "Há pendências a registrar?" | confirmado |
| **6. Lições aprendidas** | [GSD] | `RETROSPECTIVE.md` (What Worked / Inefficient / Key Lessons / causa-raiz por milestone) | confirmado |
| **Registro de encerramento — data** | [Manual] | gatilho: data real do encerramento formal | confirmado |
| **Registro de encerramento — ref. ata** | [Manual] | código/link da ata de encerramento | confirmado |
| **Registro de encerramento — aprovado por** | [Manual] | gatilho: quem assinou o encerramento (cliente/patrocinador) | confirmado |
