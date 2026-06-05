# Matriz de Rastreabilidade — [preencher: NOME DO PROJETO]

> **O que é este documento.** A Matriz de Rastreabilidade conecta, em um único lugar, a cadeia completa: necessidade da parte interessada → requisito especificado → item de design → item no backlog/Jira → caso de teste → situação. Ela permite perguntar, a qualquer momento, "tudo que prometemos foi construído?" e "tudo que foi construído tinha requisito?". Itens sem requisito (órfãos de construção) e requisitos sem cobertura de teste (órfãos de verificação) são evidências de risco.
>
> **Como usar.** Mantenha esta matriz viva durante a construção — não como registro feito no final. A cada história implementada, vincule o caso de teste e atualize a situação. A seção de Cobertura é o termômetro de saúde: se houver muitos itens sem cobertura, a qualidade do produto está em risco.
>
> **Regra de ouro.** A rastreabilidade bidirecional significa: dado um requisito, consegue-se chegar ao código (para frente); dado o código, consegue-se chegar ao requisito (para trás). Ambas as direções precisam funcionar.

---

## Identificação

| Campo | Valor |
|---|---|
| Documento | `[preencher — ex.: MR-PROJ-001]` |
| Projeto | `[preencher — nome do projeto]` |
| Versão | `[preencher — ex.: v1]` |
| Data | `[preencher — dd/mm/aaaa]` |
| Responsável | `[preencher — Gerente de Projeto ou Analista de Requisitos]` |

---

## Matriz

> Cada linha representa um requisito rastreado da necessidade até o caso de teste. Use uma linha por requisito. Se um requisito cobre múltiplos casos de teste, adicione linhas com o mesmo ID de requisito.

| Necessidade (ID) | Requisito (ID) | Descrição do requisito | Item de design | Item no backlog / Jira | Caso de teste (ID) | Situação |
|---|---|---|---|---|---|---|
| `[preencher — ex.: N-01]` | `[preencher — ex.: OWN-01]` | `[preencher — descrição concisa do requisito]` | `[preencher — componente / serviço / tela]` | `[preencher — ex.: TCON-12 ou link Jira]` | `[preencher — ex.: CT-OWN-01]` | `[preencher — Verificado / Atendido / Em desenvolvimento / Não coberto]` |

---

## Cobertura

### Requisitos sem cobertura de teste

> Liste os requisitos que estão implementados mas não têm caso de teste associado. Esta seção deve ser vazia ao final do projeto — se não estiver, é risco.

| Requisito (ID) | Motivo da ausência de cobertura | Ação prevista |
|---|---|---|
| `[preencher — ou "Nenhum"]` | `[preencher]` | `[preencher]` |

### Itens desenvolvidos sem requisito associado (órfãos de construção)

> Liste os itens de backlog ou código que foram construídos mas não têm requisito rastreável. Órfãos indicam escopo não planejado implementado silenciosamente.

| Item no backlog / Jira | Descrição | Ação prevista |
|---|---|---|
| `[preencher — ou "Nenhum"]` | `[preencher]` | `[preencher — ex.: criar requisito retroativamente ou remover o item]` |
