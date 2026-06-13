# Tabela de Proveniência — Matriz de Rastreabilidade

> **Para que serve.** Esta tabela diz, para cada campo da Matriz de Rastreabilidade, **de onde o dado vem** e **quem o preenche**. A matriz é o artefato mais dependente de ferramentas externas: a maioria dos campos vem diretamente do Jira ou do GSD — a skill pode preenchê-los sozinha.
>
> **Origens:** **[GSD]** lê artefatos do GSD · **[Jira]** lê rastreador · **[Manual]** gatilho ao responsável · **[Derivado]** calculado. **(confirmado)** = fonte comprovada; **(hipótese)** = depende da estrutura Jira/GSD da Timeware.

| Campo | Origem | Fonte exata | Confiança |
|---|---|---|---|
| Identificação/versão | [Manual] | gatilho ao versionar | confirmado |
| Necessidade | [GSD] | `DISCUSSION-LOG.md`, `PROJECT.md` §Requirements | confirmado |
| Requisito (ID + descrição) | [GSD] | `REQUIREMENTS.md` (IDs e textos) | confirmado |
| Item de design | [GSD] | `UI-SPEC.md`, `RESEARCH.md`, documentação de arquitetura | confirmado |
| Item no backlog/Jira | [Jira] | issue vinculada ao requisito (épico/história) | hipótese |
| Caso de teste | [Jira] / [Azure Test Plans] | caso de teste vinculado à história | hipótese |
| Situação (pendente/atendido/verificado) | [Jira] | status da issue + status do caso de teste | hipótese |
| Requisitos sem cobertura de teste | [Derivado] | IDs sem caso de teste vinculado | confirmado |
| Itens desenvolvidos sem requisito | [Derivado] | issues no Jira sem link + `VERIFICATION.md` (orphan detection) | confirmado |

---

## Resumo: o que a skill faz sozinha vs. o que pede ao responsável

**A skill preenche sozinha:** necessidades (GSD), requisitos (GSD), itens de design (GSD), itens no Jira (Jira), status de implementação (Jira), detecção automática de órfãos.

**A skill emite gatilho pedindo:** casos de teste quando não há integração com Azure Test Plans/Xray — o responsável de QA informa os IDs manualmente.

**Pendências (hipótese) a confirmar:**
1. Como o Jira da Timeware vincula história ao requisito (campo customizado? convenção de nome? link de issue)?
2. Azure Test Plans ou Xray está integrado ao Jira? Os casos de teste têm ID rastreável?
