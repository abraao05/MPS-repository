# Registro de Adaptação do Processo — [preencher: NOME DO PROJETO]

> **O que é este documento.** Registra as decisões conscientes de adaptação do processo-padrão da organização para este projeto específico. A adaptação não é exceção nem esquecimento — é uma decisão deliberada, feita antes do planejamento detalhado, com justificativa documentada. Sem este registro, não há como distinguir "decidimos não fazer" de "esquecemos de fazer".
>
> **Como usar.** Preencha logo após o Termo de Abertura, antes de iniciar o Plano do Projeto. Para cada eixo de adaptação, registre a decisão e justifique com base nas características do projeto. Se um eixo não requer adaptação, registre "Segue o padrão" — o silêncio não é evidência.
>
> **Regra de ouro.** Toda etapa ou prática omitida do processo-padrão precisa estar neste documento, com justificativa. O auditor GQA verificará este registro como evidência de que a adaptação foi consciente.

---

## Identificação

| Campo | Valor |
|---|---|
| Documento | `[preencher — ex.: ADAP-PROJ-001]` |
| Projeto | `[preencher — nome do projeto]` |
| Versão | `[preencher — ex.: v1]` |
| Data | `[preencher — dd/mm/aaaa]` |
| Responsável pela adaptação | `[preencher — Gerente de Projeto]` |

---

## 1. Decisões de adaptação

> Para cada eixo abaixo, registre a decisão tomada para este projeto e a justificativa. Use "Segue o padrão" quando não houver adaptação necessária.

| Eixo | Decisão para este projeto | Justificativa |
|---|---|---|
| Tipo de produto | `[preencher — ex.: produto web, serviço, componente interno]` | `[preencher — por que esta classificação afeta o processo]` |
| Origem dos requisitos | `[preencher — ex.: cliente externo define; organização elabora; requisitos emergem da pesquisa]` | `[preencher]` |
| Porte | `[preencher — ex.: pequeno / médio / grande; critério: número de histórias, duração, equipe]` | `[preencher]` |
| Equipe / papéis | `[preencher — ex.: equipe dedicada; papéis acumulados; dev full-stack acumula arquiteto]` | `[preencher — justificar acúmulo se houver]` |
| Criticidade / regulação | `[preencher — ex.: produto sem regulação específica; produto com requisitos de segurança de dados]` | `[preencher]` |
| Cadência de entrega | `[preencher — ex.: entrega contínua por milestone; sprints fixos; entrega única no encerramento]` | `[preencher]` |
| Ambiente de stage / homologação | `[preencher — ex.: preview automático; ambiente dedicado de homologação; sem ambiente de stage]` | `[preencher]` |

---

## 2. Etapas aplicáveis e não aplicáveis

> Liste as etapas do processo-padrão da organização (conforme GUIA-GPC-001) e indique para cada uma se é aplicável neste projeto. Justifique toda não aplicação.

| Etapa do processo-padrão | Aplicável? | Observação / justificativa |
|---|---|---|
| Levantamento de contexto e pesquisa | `[Sim / Não / Parcial]` | `[preencher]` |
| Planejamento detalhado da fase | `[Sim / Não / Parcial]` | `[preencher]` |
| Execução e construção | `[Sim / Não / Parcial]` | `[preencher]` |
| Revisão técnica (verificação) | `[Sim / Não / Parcial]` | `[preencher]` |
| Validação com usuário / UAT | `[Sim / Não / Parcial]` | `[preencher]` |
| Aceite formal do cliente por milestone | `[Sim / Não / Parcial]` | `[preencher]` |
| Registro de lições aprendidas | `[Sim / Não / Parcial]` | `[preencher]` |
| `[preencher — outras etapas do padrão organizacional]` | `[Sim / Não / Parcial]` | `[preencher]` |

---

## 3. Pontos de controle obrigatórios (checklist)

> Itens que devem ser verificados pelo GQA nos marcos do projeto. Não remova itens sem justificativa formal neste mesmo documento.

- [ ] Termo de Abertura emitido antes do início do planejamento detalhado
- [ ] Registro de Adaptação aprovado antes do Plano do Projeto
- [ ] Plano do Projeto com baseline estabelecida e aprovada
- [ ] Relatório de Acompanhamento emitido a cada ciclo conforme definido no Plano
- [ ] Change Requests formalizados para toda mudança de escopo, prazo ou custo
- [ ] Revisão por pares realizada nos produtos de trabalho selecionados
- [ ] Verificação GQA nos marcos obrigatórios do projeto
- [ ] Termo de Encerramento emitido com aceite formal do cliente
- [ ] `[preencher — pontos de controle adicionais específicos deste projeto]`
