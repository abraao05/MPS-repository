# Tabela de Proveniência — Termo de Abertura do Projeto (TPL-GPR-002)

> **Para que serve.** Esta tabela diz, para cada campo do Termo de Abertura, **de onde o dado vem** e **quem o preenche**. É o insumo que torna a automação construível: a skill sabe quais campos pode preencher sozinha (lendo GSD ou Jira), quais precisa calcular, e quais tem de pedir ao gestor por meio de um gatilho.
>
> **As quatro origens:**
> - **[GSD]** — extraível dos artefatos do GSD (PROJECT, REQUIREMENTS, ROADMAP etc.). A skill lê e preenche.
> - **[Jira]** — extraível do rastreador de tarefas. A skill lê e preenche.
> - **[Manual]** — não existe em ferramenta nenhuma; vem de rotina gerencial (decisão comercial, ata, definição do gestor). A skill **não preenche** — emite um **gatilho** pedindo a entrada.
> - **[Derivado]** — calculado a partir de campos anteriores. A skill calcula.
>
> **(confirmado)** = fonte comprovada no diagnóstico real do repositório Trainer Connect. **(hipótese)** = depende de confirmar como a Timeware estrutura seus artefatos.

---

| Campo | Origem | Fonte exata | Confiança |
|---|---|---|---|
| Nome / código do documento | [Manual] | gatilho: "Qual o código do TAP?" (ex.: TAP-TCON-001) | confirmado |
| Nome do projeto | [GSD] | `PROJECT.md` (título) | confirmado |
| Cliente / patrocinador | [Manual] | gatilho: "Quem é o cliente ou patrocinador?" | confirmado (não existe em ferramenta) |
| Versão | [Manual] | gatilho no momento de emitir/revisar o TAP | confirmado |
| Data de abertura | [Manual] | gatilho: data da decisão de iniciar / kickoff | confirmado |
| Gerente de Projeto | [Manual] | gatilho: "Quem é o gerente de projeto nomeado?" | confirmado |
| **1. Objetivo do projeto** | [GSD] | `PROJECT.md` §objetivo/visão + §problema resolvido | confirmado |
| **2.1 Escopo incluído** | [GSD] + [Manual] | `PROJECT.md` §Requirements + `REQUIREMENTS.md` §In Scope; síntese em nível macro pode exigir revisão manual | confirmado |
| **2.2 Escopo excluído** | [GSD] + [Manual] | `PROJECT.md` §Out of Scope + `REQUIREMENTS.md` (Out of Scope); exclusões formais (ex.: gateway) exigem decisão manual registrada | confirmado |
| **3. Partes interessadas** | [Manual] | gatilho: matriz de stakeholders (no GSD aparece de forma dispersa no DISCUSSION-LOG — não estruturado o suficiente para extração automática) | confirmado |
| **4. Equipe do projeto** | [Manual] | gatilho: "Quem está na equipe e em qual papel?" (Timeware tem equipe; projeto solo original não tinha) | confirmado |
| **5. Macroplanejamento — marcos** | [GSD] + [Manual] | `ROADMAP.md` (milestones e datas-alvo) + confirmação manual de datas para a abertura do projeto | confirmado |
| **6. Agenda das próximas atividades** | [Manual] | gatilho: ações imediatas definidas no kickoff | confirmado |
| **7.1 Premissas** | [GSD] + [Manual] | `PROJECT.md` §Constraints + `CONTEXT.md` (restrições técnicas conhecidas); premissas de negócio/contratuais são manuais | confirmado |
| **7.2 Restrições** | [GSD] + [Manual] | `PROJECT.md` §Constraints (prazo, infra); orçamento e restrições contratuais são manuais | confirmado |
| **Registro de abertura — data do kickoff** | [Manual] | gatilho: data real do kickoff | confirmado |
| **Registro de abertura — ref. ata** | [Manual] | gatilho: código/link da ata de kickoff gerada | confirmado |
| **Registro de abertura — aprovado por** | [Manual] | gatilho: quem aprovou formalmente | confirmado |
