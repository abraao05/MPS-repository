# Tabela de Proveniência — Revisão por Pares

> **Para que serve.** Esta tabela diz, para cada campo do Registro de Revisão por Pares, **de onde o dado vem** e **quem o preenche**. A revisão por pares é o artefato mais manual do processo — quase tudo vem do julgamento humano durante a revisão; a skill tem papel menor aqui.
>
> **Origens:** **[GSD]** lê artefatos do GSD · **[Jira]** lê rastreador · **[Manual]** gatilho ao responsável · **[Derivado]** calculado. **(confirmado)** = fonte comprovada; **(hipótese)** = depende da estrutura da Timeware.

| Campo | Origem | Fonte exata | Confiança |
|---|---|---|---|
| ID / referência | [GSD] / [Manual] | link do Pull Request ou ID gerado | confirmado |
| Projeto | [GSD] | `PROJECT.md` (nome do projeto) | confirmado |
| Item revisado | [GSD] | nome do arquivo/módulo + ID da história (Jira) | confirmado |
| Tipo de revisão | [Manual] | julgamento do autor ao abrir o registro | confirmado |
| Data | [GSD] | data do Pull Request | confirmado |
| Autor | [GSD] | autor dos commits do PR | confirmado |
| Revisor(es) | [GSD] / [Manual] | reviewer atribuído ao PR; se não houver campo, gatilho | hipótese |
| Itens revisados | [GSD] | lista de arquivos modificados no PR | confirmado |
| Apontamentos (descrição) | [Manual] | preenchidos pelo revisor durante a análise | confirmado |
| Apontamentos (severidade) | [Manual] | julgamento do revisor | confirmado |
| Apontamentos (tratamento) | [Manual] | preenchido pelo autor após corrigir | confirmado |
| Apontamentos (situação) | [Manual] / [GSD] | resolvido = commit de correção no PR; aberto = pendente | confirmado |
| Resultado | [Manual] | decisão do revisor ao final | confirmado |
| Decisão de merge | [GSD] | merge do PR (confirmado) ou bloqueio (comentário de rejeição) | confirmado |

---

## Resumo: o que a skill faz sozinha vs. o que pede ao revisor

**A skill preenche sozinha:** ID do PR, projeto, itens revisados (lista de arquivos), autor, data, status de resolução (commit existe?).

**A skill emite gatilho pedindo:** apontamentos (conteúdo da revisão), severidade, tratamento, resultado — esses campos dependem do julgamento humano e não podem ser gerados automaticamente.
