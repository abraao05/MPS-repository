# Tabela de Proveniência — Registro de Adaptação do Processo (TPL-GPR-003)

> **Para que serve.** Esta tabela diz, para cada campo do Registro de Adaptação, **de onde o dado vem** e **quem o preenche**. É o insumo que torna a automação construível: a skill sabe quais campos pode pré-preencher com base em artefatos existentes e quais deve solicitar ao gestor.
>
> **As quatro origens:**
> - **[GSD]** — extraível dos artefatos do GSD (PROJECT, REQUIREMENTS, ROADMAP etc.). A skill lê e preenche.
> - **[Jira]** — extraível do rastreador de tarefas. A skill lê e preenche.
> - **[Manual]** — não existe em ferramenta nenhuma; vem de rotina gerencial (decisão, ata, definição do gestor). A skill **não preenche** — emite um **gatilho** pedindo a entrada.
> - **[Derivado]** — calculado a partir de campos anteriores. A skill calcula.
>
> **(confirmado)** = fonte comprovada no diagnóstico real do repositório Trainer Connect. **(hipótese)** = depende de confirmar como a Timeware estrutura seus artefatos.

---

| Campo | Origem | Fonte exata | Confiança |
|---|---|---|---|
| Nome / código do documento | [Manual] | gatilho: "Qual o código do Registro de Adaptação?" | confirmado |
| Projeto / versão / data | [Manual] | gatilho no momento de emitir o registro | confirmado |
| Responsável pela adaptação | [Manual] | gatilho: "Quem é o GP responsável pela adaptação?" | confirmado |
| **1. Eixo — Tipo de produto** | [Manual] + [GSD] | `PROJECT.md` (stack, tipo de produto) sugere o rótulo; classificação formal é decisão do GP | confirmado |
| **1. Eixo — Origem dos requisitos** | [Manual] | decisão gerencial sobre quem define/especifica; GSD pode sugerir, mas a decisão é deliberada | confirmado |
| **1. Eixo — Porte** | [Manual] + [GSD] | estimativa inicial de pontos/duração do `ROADMAP.md` informa; classificação final é do GP | confirmado |
| **1. Eixo — Equipe / papéis** | [Manual] | gatilho: "Quais papéis estão sendo acumulados e por quem?" (Timeware tem equipe definida; projeto solo não tinha) | confirmado |
| **1. Eixo — Criticidade / regulação** | [Manual] + [GSD] | `PROJECT.md` §Constraints e `CONTEXT.md` (restrições de segurança) informam; classificação de criticidade é do GP | confirmado |
| **1. Eixo — Cadência de entrega** | [Manual] + [GSD] | `ROADMAP.md` (milestones) informa a cadência; decisão formal é do GP | confirmado |
| **1. Eixo — Ambiente de stage** | [GSD] + [Manual] | `PROJECT.md` §Constraints + arquivos de configuração de deploy (preview automático); decisão de adotar ou não é manual | confirmado |
| **2. Etapas aplicáveis** | [Manual] baseado em GUIA-GPC-001 | o processo-padrão está definido no GUIA-GPC-001; a avaliação de aplicabilidade é decisão do GP para cada projeto | confirmado |
| **2. Justificativas de não aplicação** | [Manual] | gatilho: justificativa para cada etapa omitida | confirmado |
| **3. Checklist de pontos de controle** | [Manual] | baseado no processo-padrão; pontos adicionais específicos do projeto são definidos pelo GP | confirmado |
