# Tabela de Proveniência — Registro de Verificação de GQA

> **Para que serve.** Esta tabela diz, para cada campo do Registro de Verificação de GQA, **de onde o dado vem** e **quem o preenche**. O GQA é o artefato mais manual do conjunto — o conteúdo da verificação depende do julgamento do auditor; a skill tem papel principalmente na identificação do projeto e dos produtos a verificar.
>
> **Origens:** **[GSD]** lê artefatos do GSD · **[Jira]** lê rastreador · **[Manual]** gatilho ao auditor · **[Derivado]** calculado. **(confirmado)** = fonte comprovada; **(hipótese)** = depende da estrutura da Timeware.

| Campo | Origem | Fonte exata | Confiança |
|---|---|---|---|
| Projeto | [GSD] / [Jira] | `PROJECT.md` (nome) / chave Jira | confirmado |
| Marco / tipo de verificação | [Manual] | gatilho: qual marco está sendo auditado | confirmado |
| Data da verificação | [Manual] | data do ato da auditoria | confirmado |
| Auditor (GQA) | [Manual] | papel definido em EST-GPC-001 §3; nome = Manual | confirmado |
| Gerente de Projeto | [Manual] / [Jira] | responsável pelo projeto | hipótese |
| Escopo da verificação | [Manual] | auditor descreve o que será verificado | confirmado |
| Itens verificados (aderência) | [Manual] | checklist derivado do PRO-GPC-001 + PRO-GPR-001; preenchimento = julgamento do auditor | confirmado |
| Resultado de cada item (✅/⚠/N/A) | [Manual] | julgamento do auditor ao examinar as evidências | confirmado |
| Produtos de trabalho (existência) | [GSD] / [Manual] | a skill pode verificar se os arquivos existem no repo; completude = julgamento | confirmado (existência) / hipótese (completude) |
| Achados (desvio, severidade) | [Manual] | julgamento do auditor | confirmado |
| Achados (responsável, prazo) | [Manual] | definidos com o GP na reunião de GQA | confirmado |
| Achados (status) | [Manual] / [Jira] | atualizado pelo responsável; pode ter issue no Jira | hipótese |
| Resultado geral | [Manual] | síntese do auditor com base nos achados | confirmado |
| Oportunidades de melhoria | [Manual] | identificadas pelo auditor; encaminhadas ao Time de Melhoria | confirmado |

---

## Resumo: o que a skill faz sozinha vs. o que pede ao auditor

**A skill preenche sozinha:** projeto (GSD), lista de artefatos existentes no repositório (GSD), data, marco (a partir do calendário/roadmap do GSD).

**A skill emite gatilho pedindo:** tudo relativo ao julgamento — resultado de cada item verificado, achados, severidade, responsáveis, resultado geral. O GQA é intrinsecamente humano; a skill serve de estrutura, não de substituto.
