# Processo-Padrão Organizacional de Desenvolvimento de Software — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | PRO-GPC-001 — Processo-Padrão Organizacional |
| **Versão** | 2.2 |
| **Data** | 12/05/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | Time de Melhoria Contínua |
| **Nota de auditoria** | Para a correspondência deste documento com o modelo de referência, ver a seção final "Rastreabilidade e instrução para auditoria". |
| **Classificação** | Ativo de processo organizacional |
| **Escopo de aplicação** | Projetos de software sob medida para clientes |

---

## 1. Propósito

Este documento define o processo-padrão de desenvolvimento de software sob medida da Timeware: o conjunto ordenado de fases, atividades, papéis, produtos de trabalho e pontos de controle que todos os projetos de software sob medida da organização seguem.

O processo-padrão é a referência única a partir da qual cada projeto define o seu próprio processo, por meio de adaptação (ver documento de Guia de Adaptação, GUIA-GPC-001). É também a espinha dorsal que conecta os demais processos da organização — gerência de projetos, engenharia de requisitos, projeto e construção, integração, verificação e validação, e os processos de apoio.

## 2. Escopo e abrangência

Este processo-padrão aplica-se aos projetos de **software sob medida para clientes**. O desenvolvimento de produto próprio e a sustentação de sistemas em produção não estão cobertos por esta versão; a sustentação, quando contratada, é assumida por unidade de negócio específica da Timeware.

A abordagem de desenvolvimento adotada é **ágil, baseada em Scrum**, com sprints de duas semanas. As atividades descritas neste processo são compatíveis com essa dinâmica e devem ser conduzidas dentro dela.

## 3. Visão geral do processo

O processo-padrão organiza-se em sete fases, da originação do projeto ao seu encerramento:

| # | Fase | Marco / resultado principal |
|---|---|---|
| 1 | Originação | Negócio fechado e demanda transferida ao Escritório de Projetos |
| 2 | Abertura (Kickoff gerencial) | Projeto formalmente aberto (Termo de Abertura) |
| 3 | Discovery e Requisitos | Escopo e requisitos entendidos e especificados |
| 4 | Concepção (trilhas paralelas) | Insumos de projeto e de produto para o plano |
| 5 | Planejamento e Aprovação do Plano | Plano de Projeto fechado e aprovado pelo cliente (baseline) |
| 6 | Desenvolvimento (Sprints) | Produto construído e testado |
| 7 | Homologação, Entrega e Encerramento | Produto aprovado, em produção e projeto encerrado |

Os processos de apoio — Gerência de Configuração, Medição, Gerência de Decisões, Gerência de Riscos e Capacitação — atravessam todas as fases.

**Há dois momentos de trabalho em paralelo, que não devem ser confundidos:**

- **Concepção paralela (Fase 4):** após o Discovery, a **trilha de projeto** (gestão — escopo, marcos, partes interessadas) e a **trilha de produto** (técnico — arquitetura, design, estimativa) correm em paralelo. Elas produzem os **insumos** que alimentam o fechamento do plano (Fase 5). É um trabalho de concepção, anterior à construção.
- **Design adiantado nas sprints (Fase 6):** durante a construção, o design continua operando de uma a duas sprints à frente do desenvolvimento, de modo que o que é construído já foi previamente desenhado e validado. É um adiantamento *dentro* da execução.

A primeira é concepção que antecede o plano; a segunda é uma dinâmica de execução. São distintas.

## 4. Papéis

| Papel | Atuação no processo |
|---|---|
| **Comercial** | Origina o projeto; formaliza o fechamento com o cliente; define o escopo macro (o que entra e o que não entra). |
| **Escritório de Projetos / Gerente de Projeto** | Recebe a demanda do Comercial (passagem de bastão); monta a equipe; planeja, monitora e controla o projeto; gerencia riscos, escopo, cronograma e partes interessadas. O Escritório de Projetos é a função de gestão de projetos da organização, porta de entrada das demandas. |
| **Product Owner (PO)** | Conduz o levantamento com o cliente; mantém e prioriza o backlog; valida entregas. |
| **Tech Lead** | Conduz o Discovery com o PO; lidera tecnicamente o time; participa do design técnico. Pode ser acumulado com o papel de Arquiteto. |
| **Arquiteto** | Define a arquitetura técnica, modelo de dados e integrações; acompanha o design adiantado quanto a impactos estruturais. Pode ser a mesma pessoa que o Tech Lead. |
| **UX/UI** | Elabora wireframes e protótipos; valida o design com o cliente. |
| **Equipe de Desenvolvimento** | Constrói o produto conforme o design e os critérios de aceite. |
| **QA** | Aplica metodologias de teste e valida o produto antes da entrega. |
| **Garantia da Qualidade de Processo (GQA)** | Verifica objetivamente a aderência ao processo e a qualidade dos produtos de trabalho. |
| **Time de Melhoria Contínua** | Mantém e melhora este processo-padrão; apoia os projetos no seu uso. |

## 5. Fases do processo

### Fase 1 — Originação

**Entrada:** oportunidade fechada pelo Comercial (cliente novo ou existente).

**Atividades:**
- O Comercial formaliza o fechamento do negócio e gera o contrato, com o **escopo macro** definido (incluindo o que está e o que não está no escopo).
- Realiza-se a **passagem de bastão** ao Escritório de Projetos, que recebe a demanda e assume a condução.

**Produtos de trabalho:** contrato / escopo macro; registro da passagem de bastão.

**Pontos de controle:** demanda formalmente recebida pelo Escritório de Projetos.

### Fase 2 — Abertura (Kickoff gerencial)

**Entrada:** demanda recebida pelo Escritório de Projetos.

**Atividades:**
- O Escritório de Projetos realiza as **primeiras definições** e monta a equipe do projeto (Gerente de Projeto, papéis técnicos).
- Realiza-se a **reunião de Kickoff**, um **marco gerencial de abertura**: formaliza o início, apresenta o macroplanejamento (grandes marcos com datas-alvo, ainda não fechadas), a equipe destacada e a agenda das próximas atividades.
- Registra-se o **Termo de Abertura do Projeto** (objetivo, escopo inicial, partes interessadas, responsáveis), documentado no projeto.
- É preparado o material de apresentação do kickoff ao cliente.

**Produtos de trabalho:** Termo de Abertura do Projeto; material de apresentação do kickoff; ata da reunião de kickoff.

**Pontos de controle:** kickoff realizado, Termo de Abertura registrado e equipe designada.

### Fase 3 — Discovery e Requisitos

**Entrada:** projeto aberto.

**Atividades:**
- Tech Lead e PO conduzem em conjunto o **Discovery / levantamento** junto ao cliente e demais partes interessadas.
- As necessidades são identificadas, analisadas e especificadas como requisitos.
- Produz-se o **Documento de Requisitos**, que reúne a **especificação funcional e técnica** — dele derivam o blueprint técnico (arquitetura, dados, stack), o blueprint de negócio e a necessidade (ou não) de design de UX/UI.
- Estabelece-se a **rastreabilidade** entre necessidades, requisitos e itens de trabalho.
- O entendimento dos requisitos é confirmado com o cliente.

**Produtos de trabalho:** Documento de Requisitos (especificação funcional e técnica); matriz de rastreabilidade.

**Pontos de controle:** requisitos especificados e com entendimento confirmado pelas partes interessadas.

### Fase 4 — Concepção (trilhas paralelas)

A partir dos requisitos, o trabalho de concepção corre em **duas trilhas paralelas**, que geram os insumos necessários para fechar o plano do projeto. Esta fase **antecede a construção**.

**Entrada:** requisitos especificados.

*Trilha de Projeto (gestão):*
- O Gerente de Projeto detalha o escopo, identifica os marcos e entregas, mapeia as partes interessadas e a comunicação.

*Trilha de Produto (técnico):*
- O Arquiteto e o Tech Lead definem a **arquitetura técnica**, o modelo de dados e as integrações (blueprint técnico).
- Quando aplicável (projetos com interface de usuário), a equipe de UX/UI elabora o **design de produto** — wireframes/protótipos validados com o cliente. Projetos sem front-end (APIs, serviços, backend) dispensam o UX/UI e mantêm somente o design técnico; a decisão é registrada na adaptação do projeto (GUIA-GPC-001).
- A equipe **estima** o esforço dos itens (tamanho em story points; esforço/prazo derivado da velocity histórica).

*Integração das trilhas:*
- As duas trilhas trabalham de forma articulada: a estimativa técnica retorna ao Gerente de Projeto para alinhar escopo, marcos e datas. Os insumos das duas trilhas alimentam o planejamento (Fase 5).

**Produtos de trabalho:** Documento de Design/Arquitetura; wireframes/protótipos validados (quando aplicável); estimativas; insumos de escopo e marcos.

**Pontos de controle:** design técnico avaliado; quando há UX/UI, protótipo aceito pelo cliente; estimativas concluídas.

### Fase 5 — Planejamento e Aprovação do Plano

**Entrada:** insumos da concepção (escopo detalhado, design, estimativas).

**Atividades:**
- O Gerente de Projeto consolida os insumos e **fecha o Plano de Projeto**: escopo, entregas e marcos com datas, equipe, riscos, comunicação.
- Realiza-se a reunião de **Apresentação e Aprovação do Plano** com o cliente: o plano é apresentado e o cliente **aprova**, selando escopo e datas.
- O aceite é **registrado em ata** (não há documento de assinatura separado). A partir deste ponto, o plano é a **linha de base (baseline)** do projeto, e mudanças passam a ser tratadas como **change request**.

**Produtos de trabalho:** Plano de Projeto aprovado; ata da reunião de Apresentação e Aprovação (com o aceite registrado).

**Pontos de controle:** plano aprovado pelo cliente e baseline estabelecida antes do início da construção.

### Fase 6 — Desenvolvimento (Sprints)

**Entrada:** plano aprovado (baseline).

**Atividades:**
- O desenvolvimento ocorre em **sprints de duas semanas**, com as cerimônias Scrum completas: **Planning, Daily, Review e Retrospectiva**.
- O backlog é detalhado **incrementalmente** (tipicamente duas a três sprints à frente, não o projeto inteiro de uma vez). A quebra de requisitos em **épicos e histórias** é conduzida por Produto (PO/PM); na **planning** define-se o que entra, a prioridade e os story points.
- O **design segue adiantado** de uma a duas sprints à frente do desenvolvimento, de modo que cada incremento é construído conforme um design já desenhado e validado. Quando o design revela mudança **estrutural**, o escopo e os requisitos são atualizados, com reflexo na rastreabilidade e no backlog.
- O código é versionado e integrado continuamente (Git + Azure DevOps).
- Cada item é concluído quando atende à **Definição de Pronto** (ver seção 6).
- Mudanças de escopo em relação à baseline seguem o fluxo de **change request** (impacto financeiro como aditivo ou crédito, ou troca de prioridade de itens de mesmo tamanho).
- Ao final de cada sprint, a **Review** formaliza o aceite do que foi entregue na sprint, com o PM/PO e as partes interessadas. Em épicos grandes, o aceite pode ocorrer **história a história**, ao longo das sprints. Este é o aceite no nível do **produto** (entrega incremental), distinto do encerramento do projeto (Fase 7).

**Produtos de trabalho:** incrementos de software; código versionado; registros de revisão por pares (code review); registros de teste do QA; artefatos de sprint (backlog da sprint, board); change requests, quando houver.

**Pontos de controle:** Definição de Pronto atendida a cada item; incremento promovido ao ambiente de homologação.

### Fase 7 — Homologação, Entrega e Encerramento

**Entrada:** incrementos prontos em homologação; entregas concluídas conforme o contrato.

**Atividades:**
- O produto é validado internamente em **homologação** e, quando há esse ambiente, disponibilizado em **stage** (réplica de produção) para a apresentação ao cliente. O **cliente avalia e aprova** e, após a aprovação, o produto é promovido para **produção**, com o material de apoio necessário. A promoção para produção pode ser feita pela Timeware ou pelo cliente, conforme o acordado no projeto.
- O encerramento ocorre em dois níveis, que não se confundem: o aceite **das entregas** (produto) é feito incrementalmente nas Reviews de sprint (Fase 6); o encerramento **do projeto** (gestão) é o marco formal realizado quando todas as entregas do contrato foram concluídas.
- Concluídas as entregas, realiza-se o **marco de encerramento formal do projeto**, com o **Termo de Encerramento** (contraparte do Termo de Abertura, na camada de gestão de projetos).
- Produz-se o **Relatório de Encerramento** e o registro de **Lições Aprendidas**; obtém-se o **Termo de Aceite** do cliente.
- Quando há sustentação contratada, a transição é feita para a unidade de negócio responsável.
- As lições aprendidas alimentam a melhoria de processos.

**Produtos de trabalho:** registro de homologação; aprovação do cliente; registro de entrega em produção; Termo de Encerramento; Relatório de Encerramento; Lições Aprendidas; Termo de Aceite.

**Pontos de controle:** aprovação formal do cliente antes da produção; marco de encerramento realizado e Termo de Aceite registrado.

## 6. Definição de Pronto (Definition of Done)

Um item de trabalho só é considerado pronto quando:

1. os **critérios de aceite** estão atendidos;
2. o **code review** foi realizado e aprovado;
3. os **testes do QA** foram executados e aprovados;
4. o item foi **promovido ao ambiente de homologação** (e, quando houver, ao ambiente de stage para validação com o cliente).

## 7. Ambientes

O desenvolvimento da Timeware utiliza, no cenário de referência, quatro ambientes distintos, todos gerenciados dentro do fluxo de controle de versão (Git + Azure DevOps):

| Ambiente | Finalidade | Característica |
|---|---|---|
| **Desenvolvimento** | Trabalho da equipe de desenvolvimento. | Ambiente livre; base de dados pode ser alterada livremente. |
| **QA** | Execução dos testes pelo QA. | Ambiente dedicado às atividades de verificação e validação. |
| **Homologação** | Validação interna antes da exposição ao cliente. | Base de testes com acesso restrito; ainda pode conter dados de teste. |
| **Stage** | Apresentação ao cliente e validação final. | **Réplica de produção** (base e aplicação estáveis); reduz o risco de falhas na demonstração ao cliente. |

Após a aprovação no stage, o produto é promovido para **produção**.

O ambiente de **stage não é obrigatório** em todos os projetos: trata-se de um ponto de adaptação (GUIA-GPC-001). Sua ausência, porém, aumenta o risco de instabilidade nas apresentações ao cliente, uma vez que a validação passaria a ocorrer em homologação.

## 8. Processos de apoio (transversais)

| Processo | Como atravessa o fluxo |
|---|---|
| **Gerência de Configuração** | Código, documentos e itens de configuração versionados (Git/Azure DevOps); baselines estabelecidas; mudanças controladas. |
| **Medição** | Indicadores dos projetos coletados (Jira) e analisados; alimentam o desempenho organizacional. |
| **Gerência de Decisões** | Decisões relevantes (técnicas, de escopo) tomadas com método formal quando aplicável. |
| **Gerência de Riscos** | Riscos e oportunidades identificados e tratados ao longo do projeto. |
| **Capacitação** | Equipes preparadas para os processos e tecnologias dos projetos. |
| **Garantia da Qualidade (GQA)** | Aderência ao processo e qualidade dos produtos verificadas de forma objetiva e independente. |

## 9. Adaptação

Este processo-padrão é adaptado a cada projeto conforme as diretrizes do Guia de Adaptação (GUIA-GPC-001). A adaptação considera fatores como porte, criticidade, duração e características do contrato, podendo ajustar a profundidade dos produtos de trabalho e das atividades, sem eliminar os pontos de controle obrigatórios.

## 10. Documentos relacionados

- POL-ORG-001 — Política Organizacional de Processos
- GUIA-GPC-001 — Guia de Adaptação do Processo-Padrão
- EST-GPC-001 — Estratégia de Garantia da Qualidade
- Processos específicos: Gerência de Projetos, Engenharia de Requisitos, Projeto e Construção, Integração, Verificação e Validação
- CONV-ORG-001 — Convenção de Nomenclatura e Versionamento

## 11. Rastreabilidade e instrução para auditoria

*Esta seção é destinada à equipe de avaliação e relaciona o conteúdo deste documento aos resultados esperados do modelo de referência MR-MPS-SW. No corpo, o conteúdo é descrito na linguagem operacional da Timeware; o quadro abaixo indica onde cada resultado é atendido.*

Este documento corresponde principalmente ao resultado **GPC 2** do processo **Gerência de Processos (GPC)** do MR-MPS-SW:2024.

| Resultado | Onde é atendido neste documento |
|---|---|
| GPC 2 — processo-padrão organizacional definido (fases, papéis, produtos de trabalho) com diretrizes de adaptação | Seções 3 e 5 (visão geral e descrição das fases, com produtos de trabalho e pontos de controle de cada fase); seção 4 (papéis); seções 6 e 7 (Definição de Pronto e ambientes); seção 9 (diretrizes de adaptação) |

Este documento é o Processo-Padrão Organizacional; ele evidencia GPC 2 (existência e descrição do processo-padrão; as diretrizes de adaptação detalhadas estão no GUIA-GPC-001).

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 04/08/2025 | Time de Melhoria Contínua | Definição inicial do processo-padrão organizacional de desenvolvimento de software sob medida |
| 2.0 | 12/12/2025 | Time de Melhoria Contínua | Reestruturação do fluxo: inclusão do Escritório de Projetos, kickoff como marco gerencial, fase de concepção em trilhas paralelas e aprovação do plano (baseline). Sete fases. |
| 2.1 | 15/01/2026 | Time de Melhoria Contínua | Definição dos quatro ambientes (dev, QA, homologação, stage); distinção entre homologação e stage; encerramento de projeto vs. review de sprint |
| 2.2 | 12/05/2026 | Time de Melhoria Contínua | Revisão de consistência geral e alinhamento de terminologia |
