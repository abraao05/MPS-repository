# Plano de Medição — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | PLA-MED-001 — Plano de Medição |
| **Versão** | 1.2 |
| **Data** | 14/05/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | COO (Operações), com patrocínio do Founder e CEO |
| **Nota de auditoria** | Para a correspondência deste documento com o modelo de referência, ver a seção final "Rastreabilidade e instrução para auditoria". |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Este plano define como a Timeware coleta, verifica, armazena, analisa e comunica medidas relacionadas aos seus projetos e processos, de forma a apoiar decisões e o alcance dos objetivos de negócio.

## 2. Objetivos de medição

Os objetivos de medição da Timeware derivam do objetivo de negócio central — **crescer com qualidade e previsibilidade** — e das necessidades de informação da gestão. São eles:

| # | Objetivo de medição | Deriva de |
|---|---|---|
| OM1 | Aumentar a previsibilidade de prazo e esforço dos projetos | Previsibilidade |
| OM2 | Acompanhar e melhorar a capacidade de entrega das equipes | Previsibilidade |
| OM3 | Reduzir defeitos e retrabalho, entregando com qualidade | Qualidade |
| OM4 | Antecipar a detecção de defeitos antes da entrega ao cliente | Qualidade |

Os objetivos de medição são revisados na análise crítica trimestral (PRO-OSW-001), garantindo que permaneçam alinhados aos objetivos de negócio.

## 3. Catálogo de medidas

As medidas abaixo são derivadas dos objetivos de medição e possuem definição operacional. Todas são coletáveis a partir das ferramentas em uso (Jira, Azure DevOps, Xray).

### Medidas de previsibilidade

**M1 — Aderência ao prazo**
- *Objetivo:* OM1
- *Definição:* relação entre o prazo planejado e o prazo realizado das entregas/marcos.
- *Fórmula:* (prazo realizado − prazo planejado) / prazo planejado.
- *Fonte:* Jira. *Frequência de coleta:* por entrega/marco.

**M2 — Esforço estimado × realizado**
- *Objetivo:* OM1
- *Definição:* relação entre o esforço estimado e o esforço efetivamente gasto.
- *Fórmula:* esforço real / esforço estimado.
- *Fonte:* Jira. *Frequência de coleta:* por sprint e por entrega.

**M3 — Velocity**
- *Objetivo:* OM2
- *Definição:* quantidade de pontos (ou itens) concluídos por sprint.
- *Fonte:* Jira. *Frequência de coleta:* por sprint.

**M4 — Itens entregues × planejados**
- *Objetivo:* OM2
- *Definição:* proporção de itens concluídos em relação aos itens planejados para a sprint.
- *Fórmula:* itens concluídos / itens planejados na sprint.
- *Fonte:* Jira. *Frequência de coleta:* por sprint.

### Medidas de qualidade

**M5 — Densidade de defeitos**
- *Objetivo:* OM3
- *Definição:* número de defeitos identificados por entrega ou por sprint.
- *Fonte:* Jira / Xray. *Frequência de coleta:* por sprint e por entrega.

**M6 — Defeitos em homologação × produção**
- *Objetivo:* OM4
- *Definição:* comparação entre defeitos detectados em homologação e defeitos que escaparam para produção.
- *Fonte:* Jira / Xray. *Frequência de coleta:* por entrega.

**M7 — Retrabalho**
- *Objetivo:* OM3
- *Definição:* proporção de itens reabertos (devolvidos após considerados concluídos) em relação ao total de itens.
- *Fórmula:* itens reabertos / total de itens concluídos.
- *Fonte:* Jira. *Frequência de coleta:* por sprint.
- *Captura:* os defeitos encontrados em teste são registrados como itens vinculados à história/tarefa (por exemplo, subtarefas de bug no Jira), o que permite contabilizar quantas vezes um item retornou para correção e dá origem ao indicador de retrabalho.

> O *burndown* da sprint é utilizado pelas equipes como ferramenta de acompanhamento diário, não constituindo medida organizacional consolidada.

## 4. Coleta, verificação e armazenamento

- As medidas são **coletadas continuamente** ao longo das sprints, a partir do Jira e demais ferramentas, conforme as definições operacionais do catálogo.
- Os dados de cada projeto ficam registrados no **Jira** (repositório por projeto).
- O **repositório organizacional de medidas** é mantido pelo Time de Melhoria Contínua, que consolida as medidas dos projetos em uma **planilha/dashboard organizacional**, permitindo a visão histórica e comparativa entre projetos.
- Antes de serem consolidadas, as medidas são **verificadas** quanto à integridade e à consistência (ver seção 8).

## 5. Análise do desempenho organizacional

- O Time de Melhoria Contínua **analisa as medidas mensalmente**, em sua reunião, identificando tendências, desvios e necessidades de melhoria.
- A análise compara o desempenho com os objetivos de medição e entre projetos.
- Os resultados consolidados constituem as **informações de governança** utilizadas pela direção, sendo levados à **análise crítica trimestral** (PRO-OSW-001) para apoiar decisões organizacionais.

## 6. Ações corretivas

Quando a análise das medidas indica desvios em relação aos objetivos, são definidas **ações corretivas**, com responsável e prazo, acompanhadas como itens rastreáveis no Jira até a conclusão. Ações que impliquem mudança de processo são encaminhadas ao ciclo de melhoria (PLA-GPC-001).

## 7. Comunicação dos resultados

Os resultados de desempenho são comunicados periodicamente à organização:

- **Mensalmente**, os resultados consolidados são compartilhados pelo Time de Melhoria Contínua (Confluence).
- **Trimestralmente**, integram a análise crítica pela direção.
- Resultados relevantes a um projeto específico são comunicados à respectiva equipe.

## 8. Garantia da qualidade das medidas

O repositório organizacional de medidas é avaliado periodicamente para assegurar a qualidade dos dados:

- verificação de **integridade** (dados completos), **consistência** (mesma definição operacional aplicada) e **atualidade** (dados no período correto);
- correção de medidas inconsistentes na origem (Jira);
- a avaliação da qualidade das medidas é realizada pelo Time de Melhoria Contínua, no mínimo a cada consolidação mensal, e registrada.

## 9. Papéis

| Papel | Responsabilidade |
|---|---|
| **Equipes de Projeto** | Registram os dados no Jira ao longo das sprints. |
| **Gerente de Projeto** | Garante que as medidas do projeto sejam coletadas e estejam corretas. |
| **Time de Melhoria Contínua** | Mantém o catálogo e o repositório; consolida, analisa, verifica a qualidade e comunica as medidas. |
| **COO (Operações)** | Usa as medidas na governança e na análise crítica; reporta ao CEO. |

## 10. Documentos relacionados

- POL-ORG-001 — Política Organizacional de Processos
- PRO-OSW-001 — Governança Organizacional de Processos
- PLA-GPC-001 — Plano de Gestão e Melhoria de Processos
- EST-GPC-001 — Estratégia de Garantia da Qualidade
- CONV-ORG-001 — Convenção de Nomenclatura e Versionamento

## 11. Rastreabilidade e instrução para auditoria

*Esta seção é destinada à equipe de avaliação e relaciona o conteúdo deste documento aos resultados esperados do modelo de referência MR-MPS-SW. No corpo, o conteúdo é descrito na linguagem operacional da Timeware; o quadro abaixo indica onde cada resultado é atendido.*

Este documento corresponde aos resultados do processo **Medição (MED)** do MR-MPS-SW:2024.

| Resultado | Onde é atendido neste documento |
|---|---|
| MED 1 — objetivos de medição derivados dos objetivos de negócio | Seção 2 |
| MED 2 — medidas definidas com definições operacionais | Seção 3 |
| MED 3 — procedimentos de coleta e armazenamento das medidas | Seção 4 |
| MED 4 — procedimentos de análise das medidas | Seção 5 |
| MED 5 — coleta e análise realizadas; ações a partir das medidas | Seções 4, 5 e 6 |
| MED 6 — resultados comunicados aos interessados | Seção 7 |
| MED 7 — repositório de medidas avaliado periodicamente (qualidade das medidas) | Seção 8 |

Este documento também sustenta o repositório organizacional de medidas (GPC 9) e o uso de medidas pela governança (OSW 6).

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 08/09/2025 | Time de Melhoria Contínua | Definição inicial do plano de medição |
| 1.1 | 20/01/2026 | Time de Melhoria Contínua | Detalhamento da captura do indicador de retrabalho (subtarefas de bug no Jira) |
| 1.2 | 14/05/2026 | Time de Melhoria Contínua | Revisão das definições operacionais dos indicadores |
