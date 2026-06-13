# Tabela de Proveniência — Ata de Reunião

> **Para que serve.** Esta tabela diz, para cada campo da Ata de Reunião, **de onde o dado vem** e **quem o preenche**. A ata é o artefato mais manual do conjunto — quase tudo vem do registro em tempo real feito pelo responsável durante a reunião.
>
> **Origens:** **[GSD]** lê artefatos do GSD · **[Jira]** lê rastreador · **[Manual]** gatilho ao responsável · **[Derivado]** calculado. **(confirmado)** = fonte comprovada; **(hipótese)** = depende da estrutura da Timeware.

| Campo | Origem | Fonte exata | Confiança |
|---|---|---|---|
| Tipo de reunião | [Manual] | julgamento do responsável pela ata | confirmado |
| Projeto / contexto | [GSD] / [Manual] | `PROJECT.md` (nome) ou "Organizacional" | confirmado |
| Data | [Manual] | data da reunião | confirmado |
| Local / meio | [Manual] | informação do convite/calendário | confirmado |
| Responsável pela ata | [Manual] | designado antes da reunião | confirmado |
| Participantes | [Manual] | lista de presentes (conferida na reunião) | confirmado |
| Pauta | [Manual] | preparada antes da reunião; pode derivar do cronograma GSD/Jira | confirmado |
| Discussões e definições | [Manual] | registro em tempo real ou imediatamente após | confirmado |
| Decisões e aceites | [Manual] | consenso expresso na reunião — não existe em ferramenta | confirmado |
| Ações (ação, responsável, prazo) | [Manual] | comprometimento na reunião | confirmado |
| Próximos passos | [Manual] / [GSD] | derivados do cronograma do projeto; complementados na reunião | confirmado |

---

## Resumo: o que a skill faz sozinha vs. o que pede ao responsável

**A skill preenche sozinha:** projeto (GSD), data (calendário), pauta padrão para marcos conhecidos (ex.: "Aprovação do Plano" tem pauta previsível derivada do processo-padrão).

**A skill emite gatilho pedindo:** tudo que depende do que aconteceu na reunião — discussões, decisões, ações, participantes. A ata é intrinsecamente humana; a skill oferece a estrutura e o gatilho no momento certo do processo.

**Nota sobre automação de marcos:** a skill pode identificar que um marco obrigatório ocorreu (ex.: Plano aprovado = baseline estabelecida no GSD) e gerar automaticamente um rascunho de ata com pauta padrão + data + participantes conhecidos — deixando as seções 3–5 para preenchimento manual. Isso reduz o atrito de criar a ata do zero.
