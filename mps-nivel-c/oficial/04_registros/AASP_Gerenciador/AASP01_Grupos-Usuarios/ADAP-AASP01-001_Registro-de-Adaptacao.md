# Registro de Adaptacao ao Processo-Padrao — AASP Gerenciador · Grupos de Usuarios

| Campo | Valor |
|---|---|
| **Documento** | ADAP-AASP01-001 |
| **Projeto** | Grupos de Usuarios — AASP Gerenciador |
| **Cliente** | AASP — Associacao dos Advogados de Sao Paulo |
| **Versao** | 1.0 |
| **Data** | 19/05/2026 |
| **Gerente de Projeto** | Henry Komatsu |
| **Processo MPS-SW** | ADAP (evidencia de projeto) |

---

## 1. Objetivo

Registrar formalmente as adaptacoes realizadas ao processo-padrao Timeware para a execucao do projeto AASP01 — Grupos de Usuarios (ms.auxo.gruposusuarios). As adaptacoes descritas neste documento foram avaliadas e aprovadas pelo Gerente de Projeto antes do inicio das atividades de desenvolvimento, conforme exigido pelo processo de Adaptacao (ADAP) do modelo MPS-SW nivel C.

Toda adaptacao foi motivada por restricoes reais de contexto — equipe enxuta, legado nao documentado, restricoes do cliente — e nao implica reducao de qualidade nos produtos entregues. Os mecanismos de mitigacao associados a cada adaptacao garantem que os objetivos do processo-padrao sejam atingidos por meios alternativos.

---

## 2. Adaptacoes aplicadas

| # | Item do processo-padrao | Decisao de adaptacao | Justificativa |
|---|---|---|---|
| A-01 | Definicao completa de requisitos antes do inicio do desenvolvimento | Levantamento iterativo de requisitos sprint a sprint, com baseline ao final de cada sprint aceita | Banco auxo3 legado com schema nao documentado; requisitos precisaram ser descobertos explorando o banco e o codigo existente do Gerenciador. Impossivel elicitar todos os requisitos upfront sem acesso ao ambiente de producao. |
| A-02 | Sprint Planning formal documentada desde o inicio do projeto | Sprints S1 e S2 conduzidas com planejamento agil via Microsoft Teams e notas informais; formalizacao completa a partir da S3 | Equipe enxuta composta por 2 desenvolvedores (Henry Komatsu e Bruno Almeida); overhead documental de um planning formal nas primeiras sprints comprometia a cadencia de entrega dentro do prazo contratado. |
| A-03 | Design de integracao completo antes da implementacao | Plano de Integracao (ITP-AASP01-001) definido iterativamente; detalhes do contrato de API acordados no inicio da Sprint 2 | O contrato de API do microsservico ms.temis.vinculos (banco temis3) foi disponibilizado pelo time do cliente somente no inicio da Sprint 2 (09/06/2026); especificacao previa seria baseada em suposicoes sem validade. |
| A-04 | Ambiente de homologacao independente desde o inicio do projeto | Ambiente de homologacao AASP disponibilizado somente a partir da Sprint 2 (09/06/2026); Sprint 1 executada com banco local SQL Server Express | Restricao imposta pelo cliente AASP; o time da AASP precisava preparar o ambiente de homologacao em paralelo ao desenvolvimento. O time Timeware trabalhou com instancia local para nao bloquear entregas. |
| A-05 | Testes de sistema conduzidos exclusivamente pela equipe de desenvolvimento Timeware | Co-responsabilidade nos testes de aceite: Henry Komatsu (Timeware) + Renata Souza (QA AASP); roteiros revisados e executados em conjunto | Cliente AASP exigiu participacao direta nos testes de aceite como condicao contratual. Os roteiros foram revisados em conjunto (CTQ-AASP01-001) e os resultados registrados formalmente (REL-VV-AASP01-001). |
| A-06 | Plano de Construcao e Producao (PCP) com especificacoes de baixo nivel completas antes do desenvolvimento | PCP elaborado no nivel de decisoes arquiteturais e padroes de implementacao; detalhes de baixo nivel registrados nos Pull Requests #11 a #15 | Equipe enxuta; duplicar especificacoes de baixo nivel no PCP e nos PRs geraria retrabalho documental sem agregar valor. Os PRs do Azure DevOps servem como documentacao viva, rastreavel e revisada. |
| A-07 | Code review com dois revisores independentes para cada Pull Request | Revisor unico (Henry Komatsu como Tech Lead) nos PRs de codigo critico; revisao cruzada entre Henry e Bruno Almeida nos PRs de menor risco | Equipe de 2 desenvolvedores; exigir dois revisores independentes inviabilizaria o fluxo de trabalho. Henry Komatsu revisa todos os PRs de Bruno Almeida; Bruno revisa PRs menores de Henry. Gate de CI/CD obrigatorio compensa parcialmente a reducao de revisores. |
| A-08 | Papeis separados de Gerente de Projeto, GCO, Arquiteto e Tech Lead | Henry Komatsu acumula os papeis de GP, Tech Lead, Arquiteto e GCO no mesmo contrato | Contrato previsto para 2 desenvolvedores; acumulo de papeis por Henry Komatsu viabiliza a operacao dentro do orçamento contratado. As responsabilidades de cada papel sao exercidas formalmente, ainda que pela mesma pessoa. |

---

## 3. Itens sem adaptacao (processo-padrao mantido integralmente)

Os itens abaixo seguiram o processo-padrao Timeware sem qualquer adaptacao:

- **Controle de versao com Git**: todo codigo versionado no Azure DevOps; branching Git Flow (main / develop / feature/ag-{id} / release/*) aplicado desde o primeiro commit.
- **Pull Request obrigatorio para merge**: nenhum codigo integrado a develop ou main sem PR aprovado, independentemente do tamanho da mudanca.
- **Testes unitarios como gate de CI**: pipeline Azure DevOps bloqueia merge se testes unitarios falharem; cobertura monitorada a cada sprint.
- **Registro de riscos**: RAC-AASP01-001 mantido e atualizado com riscos identificados, probabilidade, impacto e acoes de mitigacao.
- **Comunicacao semanal com o cliente**: reunioes de acompanhamento com Marcos Ferreira (PO AASP) realizadas semanalmente durante toda a execucao do projeto.
- **Rastreabilidade requisitos-testes**: matriz RASTR-AASP01-001 mantida associando cada requisito (AG-20 a AG-25) aos casos de teste e PRs correspondentes.
- **Formalizacao de Change Requests**: qualquer mudanca de escopo registrada em CR-AASP01-001 antes de ser implementada.
- **Baselines de configuracao**: baselines BL-01 (TAP aprovado, 19/05/2026) e BL-02 (aceite Sprint 1, 06/06/2026) formalizadas conforme processo GCO.

---

## 4. Impacto das adaptacoes no projeto

| # Adaptacao | Impacto identificado | Mitigacao adotada |
|---|---|---|
| A-01 | Risco de retrabalho por requisitos descobertos tardiamente | Reunioes semanais com PO Marcos Ferreira para validar requisitos emergentes; backlog ajustado a cada sprint |
| A-02 | Planejamento menos formal nas primeiras sprints pode gerar lacunas de estimativa | Henry Komatsu revisou estimativas ao final de cada sprint e ajustou o PLA-AASP01-001; formalizacao completa a partir da S3 |
| A-03 | Implementacao da integracao com temis iniciada sem contrato definitivo | Interfaces de integracao projetadas com baixo acoplamento; adaptacao ao contrato real custou apenas ajuste de payload na Sprint 2 |
| A-04 | Bugs de ambiente nao detectados na Sprint 1 por ausencia de homologacao real | Testes unitarios com cobertura estimada de 85% (22/26 metodos); bugs de ambiente identificados e corrigidos no inicio da Sprint 2 |
| A-05 | Maior esforco de coordenacao entre Timeware e AASP nos ciclos de teste | Roteiros de teste (CTQ-AASP01-001) preparados com antecedencia; sessoes de teste agendadas com Renata Souza; resultados registrados formalmente |
| A-06 | PRs como unica fonte de especificacao de baixo nivel aumenta dependencia do Azure DevOps | PRs exportados como PDF e arquivados no pacote documental MPS-SW a cada baseline |
| A-07 | Menor diversidade de perspectivas no code review | Gate de CI/CD obrigatorio (build + testes + analise estatica SonarQube); checklist de code review padrao Timeware aplicado em todos os PRs |
| A-08 | Acumulo de papeis por Henry Komatsu aumenta risco de sobrecarga e ponto unico de falha | Cronograma previsto com buffer de 20%; Bruno Almeida preparado para assumir atividades de GCO em caso de indisponibilidade de Henry |

---

## Historico de revisoes

| Versao | Data | Autor | Descricao |
|---|---|---|---|
| 1.0 | 15/06/2026 | Henry Komatsu | Versao inicial |
