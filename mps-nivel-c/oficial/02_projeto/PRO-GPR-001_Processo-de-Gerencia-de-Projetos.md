# Processo de Gerência de Projetos — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | PRO-GPR-001 — Processo de Gerência de Projetos |
| **Versão** | 1.2 |
| **Data** | `<dd/mm/aaaa>` |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | COO (Operações) |
| **Processos MPS-SW relacionados** | GPR 1 a GPR 20 |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Este processo define como a Timeware planeja, monitora e controla seus projetos de software sob medida, garantindo que o escopo, as estimativas, os recursos, os riscos e os compromissos sejam estabelecidos, acompanhados e ajustados ao longo do ciclo de vida do projeto.

Este processo opera em conjunto com o Processo-Padrão Organizacional (PRO-GPC-001), que descreve o fluxo de fases do projeto, e é adaptado a cada projeto conforme o Guia de Adaptação (GUIA-GPC-001).

> **Mapa de resultados atendidos neste documento:**
> - Seção 4 → **GPR 1** (escopo), **GPR 2** (adaptação do processo)
> - Seção 5 → **GPR 3, 4** (estimativas), **GPR 5** (orçamento e cronograma)
> - Seção 6 → **GPR 6, 7** (recursos), **GPR 8** (transição), **GPR 9** (partes interessadas)
> - Seção 7 → **GPR 10** (riscos), **GPR 11** (viabilidade)
> - Seção 8 → **GPR 12, 13** (plano integrado e compromisso)
> - Seção 9 → **GPR 14 a 18** (monitoramento e ações corretivas)
> - Seção 10 → **GPR 19, 20** (análise de causas e melhoria)

## 2. Planejamento ágil e o plano de projeto

A Timeware adota abordagem ágil (Scrum). O **Plano de Projeto** é fechado ao final da concepção, a partir dos insumos das trilhas de projeto e de produto (escopo detalhado, design, estimativas), e é **aprovado pelo cliente** na reunião de Apresentação e Aprovação do Plano — momento em que passa a ser a **linha de base (baseline)** do projeto. O aceite é registrado em ata, sem documento de assinatura separado.

A partir da baseline, o plano é mantido enxuto e vivo: é detalhado incrementalmente nas sprints (por meio do backlog e do planning) e atualizado quando há mudança relevante; mudanças de escopo em relação à baseline seguem o fluxo de change request. O plano não é um documento congelado, mas a baseline é a referência de compromisso com o cliente.

O Plano de Projeto é registrado no template TPL-GPR-001.

## 3. Papéis

| Papel | Atuação |
|---|---|
| **Gerente de Projeto** | Responsável pelo planejamento, monitoramento e controle do projeto. |
| **Product Owner** | Mantém e prioriza o backlog; representa o cliente. |
| **Tech Lead / Arquiteto** | Apoia estimativas técnicas e decisões; conduz o time tecnicamente. |
| **Equipe** | Participa das estimativas (planning poker) e executa o trabalho. |

## 4. Escopo e adaptação (GPR 1, GPR 2)

- O **escopo** do projeto parte do escopo macro do contrato, é formalizado no **Termo de Abertura** (kickoff gerencial) e detalhado no trabalho de requisitos (REQ) e na concepção, sendo mantido atualizado conforme mudanças aprovadas (change request sobre a baseline).
- No início, o processo-padrão é **adaptado** ao projeto conforme o Guia de Adaptação (GUIA-GPC-001), e a adaptação é registrada (Registro de Adaptação do Processo). A adaptação define, por exemplo, se há etapa de UX/UI, o nível de formalidade da documentação e a combinação de papéis.

## 5. Estimativas, orçamento e cronograma (GPR 3, 4, 5)

- **Estimativa de tamanho:** os itens são estimados em **story points**, por meio de *planning poker*, durante o refinamento.
- **Estimativa de esforço, prazo e custo:** derivada do tamanho com base na **velocity histórica** das sprints e em dados de projetos anteriores (mantidos pela Medição — PLA-MED-001). As estimativas são registradas no Jira.
- **Orçamento e cronograma:** o cronograma é organizado em sprints e **marcos** (incluindo os marcos de kickoff gerencial e de aprovação do plano), com o orçamento correspondente. As datas apresentadas no kickoff são datas-alvo; o cronograma é fechado no plano aprovado e ajustado conforme o andamento.

As estimativas baseadas em histórico aumentam a previsibilidade e são posteriormente comparadas com o realizado (estimado × real), realimentando a base histórica.

## 6. Recursos, transição e partes interessadas (GPR 6, 7, 8, 9)

- **Recursos humanos (GPR 6):** definidos no planejamento, considerando a alocação dos recursos compartilhados conforme a gestão de portfólio (PRO-OSW-002).
- **Recursos materiais e ambiente (GPR 7):** ambientes e ferramentas necessários (conforme ambientes-padrão, PLA-GPC-001).
- **Transição (GPR 8):** quando aplicável, planeja-se a transição para operação/sustentação, que é assumida por unidade de negócio específica.
- **Partes interessadas (GPR 9):** identificadas, com um plano de comunicação e envolvimento ao longo do projeto.

## 7. Riscos e viabilidade (GPR 10, 11)

- **Riscos (GPR 10):** identificados, analisados e tratados conforme a Estratégia de Gerência de Riscos (EST-GPC-002), registrados e acompanhados no Jira.
- **Viabilidade (GPR 11):** a viabilidade do projeto é avaliada, considerando escopo, estimativas, recursos e riscos, antes da assunção dos compromissos.

## 8. Plano integrado e compromisso (GPR 12, 13)

- O **Plano de Projeto** integra escopo, estimativas, cronograma, recursos, riscos e comunicação em um documento coerente (TPL-GPR-001), mantido atualizado.
- O plano é **revisado com as partes interessadas** e o **compromisso** da equipe e dos envolvidos é obtido e registrado.

## 9. Abertura e encerramento do projeto (camada de gestão)

A gestão do projeto delimita-se por dois marcos formais, distintos das entregas de produto:

- **Abertura:** o projeto é formalmente aberto no kickoff gerencial, registrado no **Termo de Abertura** (objetivo, escopo inicial, equipe, partes interessadas).
- **Encerramento:** concluídas as entregas do contrato, o projeto é formalmente encerrado com o **Termo de Encerramento**, o **Relatório de Encerramento**, o registro de **Lições Aprendidas** e o **Termo de Aceite** do cliente.

Estes marcos pertencem à camada de **gestão de projetos** e não se confundem com o aceite das entregas de **produto**, que ocorre incrementalmente nas Reviews de sprint (e, em épicos grandes, pode ocorrer história a história).

## 10. Monitoramento e controle (GPR 14 a 18)

O projeto é monitorado continuamente, comparando o planejado com o realizado:

- **Acompanhamento (GPR 14):** realizado a cada sprint (planning, review, retrospectiva) e nos marcos, registrado em Relatório de Acompanhamento. Indicadores do projeto (prazo, esforço, escopo, defeitos) são acompanhados conforme a Medição.
- **Partes interessadas e transição (GPR 15, 16):** o envolvimento das partes interessadas e a transição são monitorados.
- **Riscos (GPR 17):** monitorados e comunicados continuamente.
- **Ações corretivas (GPR 18):** desvios identificados geram ações corretivas, acompanhadas até a conclusão (Jira).

## 11. Análise de causas e melhoria (GPR 19, 20)

- **Análise (GPR 19):** resultados significativos (positivos ou negativos) têm suas causas analisadas, especialmente na retrospectiva e no encerramento.
- **Melhoria (GPR 20):** mudanças e lições aprendidas eficazes são encaminhadas como oportunidades de melhoria à organização (alimentando o ciclo de melhoria de processos, PLA-GPC-001).

## 12. Documentos e artefatos relacionados

- PRO-GPC-001 — Processo-Padrão Organizacional
- GUIA-GPC-001 — Guia de Adaptação do Processo-Padrão
- TPL-GPR-001 — Template de Plano de Projeto
- EST-GPC-002 — Estratégia de Gerência de Riscos
- PLA-MED-001 — Plano de Medição
- PRO-OSW-002 — Gestão de Portfólio de Projetos

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | `<dd/mm/aaaa>` | Time de Melhoria Contínua | Definição inicial do processo de gerência de projetos |
| 1.1 | `<dd/mm/aaaa>` | Time de Melhoria Contínua | Alinhamento ao novo fluxo: kickoff gerencial, concepção em trilhas, aprovação do plano e baseline |
| 1.2 | `<dd/mm/aaaa>` | Time de Melhoria Contínua | Inclusão dos marcos de abertura/encerramento de projeto (Termo de Encerramento) e distinção entre aceite de produto (review) e encerramento de projeto |
