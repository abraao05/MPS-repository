# Tabela de Proveniência — De onde vem cada campo

> **Para que serve.** Esta tabela diz, para cada campo dos dois documentos (Plano e Relatório), **de onde o dado vem** e **quem o preenche**. É o insumo que torna as skills de automação construíveis: a skill sabe quais campos pode preencher sozinha (lendo GSD ou Jira), quais precisa calcular, e quais tem de pedir ao gestor por meio de um gatilho.
>
> **As quatro origens:**
> - **[GSD]** — extraível dos artefatos do GSD (PROJECT, REQUIREMENTS, ROADMAP, STATE, CONTEXT, SUMMARY, REVIEW, VERIFICATION, VALIDATION, RETROSPECTIVE, MILESTONE-AUDIT, git log). A skill lê e preenche.
> - **[Jira]** — extraível do rastreador de tarefas (histórias, pontos, status, responsáveis, datas). A skill lê e preenche.
> - **[Manual]** — não existe em ferramenta nenhuma; vem de rotina gerencial (decisão comercial, ata, definição do gestor). A skill **não preenche** — emite um **gatilho** pedindo a entrada.
> - **[Derivado]** — calculado a partir de campos anteriores. A skill calcula.
>
> **Marcação de confiança.** Células marcadas **(confirmado)** têm fonte comprovada pelo diagnóstico real do repositório Trainer Connect. Células marcadas **(hipótese)** dependem de confirmar como a Timeware estrutura seu Jira e seus artefatos GSD — a confirmar com você.

---

## Plano do Projeto

| Campo | Origem | Fonte exata | Confiança |
|---|---|---|---|
| Nome do projeto | [GSD] | `PROJECT.md` (título) | confirmado |
| Código / chave no rastreador | [Jira] | chave do projeto no Jira | hipótese |
| Gestor responsável | [Manual] | gatilho: "Quem é o gestor responsável?" | confirmado (não existe em ferramenta) |
| Data de abertura | [Manual] | gatilho: data da ata de kick-off | hipótese (pode vir do Jira se houver issue de abertura) |
| Versão / data / mudança | [Manual] | gatilho no momento de versionar o plano | confirmado |
| **1. Objetivo de negócio** | [GSD] | `PROJECT.md` §objetivo/visão | confirmado |
| **1. Escopo incluído** | [GSD] | `PROJECT.md` §Requirements + `REQUIREMENTS.md` | confirmado |
| **1. Escopo excluído** | [GSD] | `PROJECT.md` §Out of Scope + `REQUIREMENTS.md` (Out of Scope) | confirmado |
| **1. Critério de pronto** | [GSD] / [Manual] | `acceptance_criteria` agregados; pode exigir síntese manual | hipótese |
| **2. Abordagem-padrão** | [Manual] | ‹padrão organizacional Timeware — texto fixo definido uma vez› | confirmado |
| **2. Adaptações do projeto** | [GSD] | `ROADMAP.md` (estrutura de fases) + config/toggles; justificativa pode exigir gatilho | hipótese |
| **3.1 Método de dimensão** | [Manual] | texto-padrão (Story Points / Planning Poker) | confirmado |
| **3.2 Tabela de histórias (ID, texto)** | [Jira] | issues tipo História no Jira | hipótese |
| **3.2 Pontos por história** | [Jira] | campo Story Points da issue | hipótese |
| **3.2 Fase alocada** | [Jira] / [GSD] | vínculo história↔fase (a definir: campo Jira ou mapeamento) | hipótese |
| **3.2 Status da história** | [Jira] | status da issue | hipótese |
| **3.2 Total de pontos** | [Derivado] | soma da coluna Pontos | confirmado |
| **3.3 Esforço/duração agregados** | [Derivado] | total de pontos × esforço-por-ponto ÷ capacidade | confirmado |
| **3.3 Premissas** | [Manual] | gatilho: "Quais premissas da estimativa?" | confirmado |
| **3.4 Esforço por ponto / velocidade** | [Derivado] / [GSD] | da referência de medidas; enquanto não há, das durações em `SUMMARY` + `RETROSPECTIVE` | confirmado (fonte existe; referência consolidada em construção) |
| **4. Orçamento total** | [Manual] | gatilho: "Qual o orçamento comercial contratado?" | confirmado (decisão comercial, fora de ferramenta) |
| **4. Cronograma macro** | [GSD] | `ROADMAP.md` (datas) | confirmado |
| **4.1 Marcos** | [GSD] | `MILESTONES.md` + tags git por milestone | confirmado |
| **4.2 Fases (linhas)** | [GSD] | `ROADMAP.md` (fases) | confirmado |
| **4.2 Histórias por fase** | [Jira]+[GSD] | cruzamento história↔fase | hipótese |
| **4.2 Esforço por fase** | [Derivado] | soma de pontos da fase × esforço-por-ponto | confirmado |
| **4.2 Datas por fase** | [GSD] | `ROADMAP.md` / `STATE.md` | confirmado |
| **4.2 Parcela de orçamento por fase** | [Manual] | gatilho: alocação gerencial do total pelas fases | confirmado |
| **5. Recursos humanos** | [Manual] | gatilho: "Quem está alocado e em quais papéis?" | confirmado (solo não tinha; Timeware tem) |
| **6. Ambientes/ferramentas** | [GSD] | `PROJECT.md` §Constraints + arquivos de config do repo | confirmado |
| **6. Padrão organizacional** | [Manual] | ‹ambiente-padrão Timeware — texto fixo (processo OSW)› | confirmado |
| **7. Estratégia de transição** | [GSD]+[Manual] | evidência de deploy (commits/config); plano de suporte exige gatilho | confirmado (lado técnico) / confirmado (lado suporte = manual) |
| **8. Partes interessadas** | [Manual] | gatilho: matriz de stakeholders (no GSD só aparece de forma dispersa no DISCUSSION-LOG) | confirmado |
| **9. Riscos e oportunidades** | [GSD]+[Manual] | STRIDE nos `PLAN`, `SECURITY.md`, `TECH-DEBT.md` (severidade) alimentam; probabilidade/prioridade exigem complemento manual | confirmado |
| **10.1 Viabilidade** | [GSD]+[Manual] | `RESEARCH`/`CONTEXT` (restrições e ajustes) + julgamento do gestor | confirmado |
| **10.2 Consistência** | [Manual] | gatilho: confirmação do gestor de que o plano é consistente | confirmado |
| **10.3 Revisão e compromisso** | [Manual] | gatilho: data da revisão + quem se comprometeu (no GSD o compromisso solo é implícito) | confirmado |

---

## Relatório de Acompanhamento

| Campo | Origem | Fonte exata | Confiança |
|---|---|---|---|
| Identificação do ciclo | [Manual]+[GSD] | qual milestone/período (GSD dá o milestone; período é manual) | confirmado |
| **1.1 Histórias concluídas** | [Jira] | contagem de issues concluídas | hipótese |
| **1.1 Fases concluídas** | [GSD] | `STATE.md` (% fases) + `MILESTONE-AUDIT` | confirmado |
| **1.2 Pontos estimados** | [Jira] | pontos do baseline (do Plano) | hipótese |
| **1.2 Pontos entregues** | [Jira] | pontos das issues concluídas | hipótese |
| **1.2 Esforço estimado** | [Derivado] | do Plano (3.3) | confirmado |
| **1.2 Esforço real** | [GSD] | durações nos `SUMMARY.md` por fase | confirmado |
| **1.2 Velocidade/esforço real por ponto** | [Derivado] | pontos entregues ÷ período; esforço real ÷ pontos | confirmado |
| **1.3 Orçamento realizado** | [Manual] | gatilho: custo real incorrido (financeiro, fora do GSD/Jira) | confirmado |
| **1.3 Marcos (datas reais)** | [GSD] | `ROADMAP.md` (datas reais) + tags git | confirmado |
| **1.4 Recursos** | [Manual]+[Jira] | alocação real (manual); responsáveis (Jira) | hipótese |
| **2. Partes interessadas** | [GSD]+[Manual] | `UAT.md`/`HUMAN-UAT.md` (participação); plano de comunicação é manual | confirmado |
| **3. Transição** | [GSD] | commits de deploy + `SUMMARY` da fase de transição | confirmado |
| **4. Riscos (situação)** | [GSD]+[Manual] | `SECURITY.md`/`TECH-DEBT.md` (status); comunicação a interessados é manual | confirmado |
| **5. Ações corretivas** | [GSD] | `REVIEW.md`→`REVIEW-FIX.md`→commit; gaps de `MILESTONE-AUDIT`; `TECH-DEBT` aberto/fechado | confirmado |
| **6. Análise de resultados** | [GSD] | `RETROSPECTIVE.md` (What Worked / Inefficient / Key Lessons / causa-raiz) | confirmado |
| **7. Melhorias propostas** | [GSD] | `RETROSPECTIVE` ("Patterns Established") + `PATTERNS.md` | confirmado |

---

## Resumo: o que a skill faz sozinha vs. o que pede ao gestor

**A skill preenche sozinha (origens [GSD], [Jira], [Derivado]):** objetivo, escopo incluído/excluído, cronograma, marcos, fases e datas, ambientes/ferramentas, esforço real, fases concluídas, ações corretivas, análise de resultados, melhorias propostas, e todos os cálculos agregados.

**A skill emite gatilho pedindo ao gestor (origem [Manual]):** gestor responsável, data de abertura, orçamento comercial (total e parcelas por fase), premissas de estimativa, recursos humanos, plano de partes interessadas, probabilidade/prioridade de riscos, confirmação de viabilidade/consistência, revisão e compromisso, custo real incorrido.

**Pendências a confirmar com você (marcadas "hipótese") antes de codar a skill:**
1. Como as histórias são representadas no Jira da Timeware (tipo de issue, campo de Story Points, campo de status)?
2. Como a história se vincula à fase do GSD (campo no Jira? mapeamento à parte? convenção de nome)?
3. A abertura do projeto gera uma issue no Jira, ou é só ata manual?
