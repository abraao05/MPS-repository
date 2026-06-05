# Tabela de Proveniência — Change Request (TPL-GPR-006)

> **Para que serve.** Esta tabela diz, para cada campo do Change Request, **de onde o dado vem** e **quem o preenche**. É o insumo que torna a automação construível: a skill sabe quais campos pode pré-preencher com base em artefatos existentes e quais deve solicitar ao gestor ou ao solicitante da mudança.
>
> **As quatro origens:**
> - **[GSD]** — extraível dos artefatos do GSD (PROJECT, ROADMAP, REQUIREMENTS etc.). A skill lê e preenche.
> - **[Jira]** — extraível do rastreador de tarefas. A skill lê e preenche.
> - **[Manual]** — não existe em ferramenta nenhuma; vem de rotina gerencial (solicitação, decisão, ata). A skill **não preenche** — emite um **gatilho** pedindo a entrada.
> - **[Derivado]** — calculado a partir de campos anteriores. A skill calcula.
>
> **(confirmado)** = fonte comprovada no diagnóstico real do repositório Trainer Connect. **(hipótese)** = depende de confirmar como a Timeware estrutura seus artefatos.

---

| Campo | Origem | Fonte exata | Confiança |
|---|---|---|---|
| Projeto / código do documento | [Manual] + [Jira] | código do projeto no Jira + gatilho para código sequencial do CR | hipótese |
| Título da mudança | [Manual] | gatilho: "Qual é o título da mudança?" (definido pelo solicitante) | confirmado |
| Solicitante | [Manual] | gatilho: "Quem está solicitando esta mudança?" | confirmado |
| Data da solicitação | [Manual] | gatilho: data real da solicitação | confirmado |
| Gerente de Projeto | [Manual] | gatilho (papel gerencial, não existe em ferramenta de forma estruturada) | confirmado |
| **1. Descrição da mudança** | [Manual] | gatilho: descrição detalhada da mudança, fornecida pelo solicitante | confirmado |
| **2. Justificativa** | [Manual] | gatilho: justificativa do solicitante | confirmado |
| **3. Impacto no escopo** | [GSD] + [Manual] | `PROJECT.md` + `REQUIREMENTS.md` (o que está no escopo atual); análise de impacto é julgamento do GP | confirmado |
| **3. Impacto no prazo** | [Derivado] | estimativa de esforço adicional × capacidade da equipe; alimentada pelo `ROADMAP.md` atual via GSD | confirmado |
| **3. Impacto no esforço / custo** | [Derivado] | estimativa de pontos/horas adicionais; custo derivado do esforço × taxa horária (manual se taxa não estiver em ferramenta) | confirmado |
| **3. Riscos introduzidos** | [Manual] | julgamento do GP com base no contexto técnico; riscos técnicos podem ser sugeridos pelo `TECH-DEBT.md` ou `CONTEXT.md` do GSD | hipótese |
| **4. Tipo de tratamento** | [Manual] | decisão gerencial — o GP propõe, o decisor aprova | confirmado (decisão é sempre manual) |
| **5. Decisão — aprovado/rejeitado** | [Manual] | gatilho: "Qual foi a decisão? Quem decidiu? Em que data?" | confirmado |
| **5. Referência à ata** | [Manual] | código/link da ata ou e-mail de decisão formal | confirmado |
| **6. Reflexo no backlog** | [Jira] | issues criadas/movidas/fechadas no Jira após a decisão | hipótese |
| **6. Reflexo na rastreabilidade** | [GSD] | `REQUIREMENTS.md` atualizado com status "fora do escopo — ref. CR" | confirmado |
| **6. Reflexo na baseline** | [Manual] | nova versão do Plano do Projeto gerada, se necessário; gatilho para confirmar | confirmado |
