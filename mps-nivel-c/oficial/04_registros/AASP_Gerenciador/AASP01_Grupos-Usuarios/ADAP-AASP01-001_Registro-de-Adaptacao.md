# Registro de Adaptação ao Processo-Padrão — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | ADAP-AASP01-001 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 19/05/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | ADAP (evidência de projeto) |

---

## 1. Objetivo

Registrar formalmente as adaptações realizadas ao processo-padrão Timeware para a execução do projeto AASP01 — Grupos de Usuários (ms.auxo.gruposusuarios). As adaptações descritas neste documento foram avaliadas e aprovadas pelo Gerente de Projeto antes do início das atividades de desenvolvimento, conforme exigido pelo processo de Adaptação (ADAP) do modelo MPS-SW nível C.

Toda adaptação foi motivada por restrições reais de contexto — equipe enxuta, legado não documentado, restrições do cliente — e não implica redução de qualidade nos produtos entregues. Os mecanismos de mitigação associados a cada adaptação garantem que os objetivos do processo-padrão sejam atingidos por meios alternativos.

---

## 2. Nível de adaptação do projeto

Conforme o Guia de Adaptação do Processo-Padrão (GUIA-GPC-001, §5), o projeto é classificado em um nível de adaptação a partir dos critérios de calibração, aplicando-se a regra do **nível mais alto atingido em qualquer critério**.

| Critério | Situação do AASP01 | Nível |
|---|---|---|
| Duração | ~7 semanas (19/05 a 11/07/2026) — até 3 meses | 1 |
| Tamanho da equipe | 5 pessoas (Gerente de Projeto, Tech Lead/Arquiteto e 3 desenvolvedores) | 2 |
| Complexidade técnica | Média — microsserviço REST com RBAC, auditoria e integração com o ms.temis.vinculos sobre banco legado (auxo3) | 2 |
| Criticidade / SLA contratual | Sem SLA contratual rígido | 1 |
| Regulação / compliance | Dados de usuários e permissões (LGPD básico); sem regulação setorial | 1 |

**Nível resultante: 2 — Padrão.**

Decorrências do Nível 2 (GUIA-GPC-001, §5.2), coerentes com os produtos de trabalho gerados no projeto:

- **Requisitos:** Documento de Requisitos completo (REQ-AASP01-001).
- **Design técnico:** Documento de Design completo (PCP-AASP01-001).
- **Verificação e Validação:** Plano de V&V com execução registrada (VV-AASP01-001, REL-VV-AASP01-001).
- **Gerência de Projetos:** Plano de Projeto completo com Relatório de Acompanhamento periódico (PLA-AASP01-001, RAC-AASP01-001).
- **GQA:** uma auditoria intermediária e a auditoria de encerramento. A verificação intermediária está registrada em GQA-AASP01-001; a auditoria de encerramento ocorrerá na Sprint 4, junto ao Termo de Encerramento.

---

## 3. Adaptações aplicadas

| # | Item do processo-padrão | Decisão de adaptação | Justificativa |
|---|---|---|---|
| A-01 | Definição completa de requisitos antes do início do desenvolvimento | Levantamento iterativo de requisitos sprint a sprint, com baseline ao final de cada sprint aceita | Banco auxo3 legado com schema não documentado; requisitos precisaram ser descobertos explorando o banco e o código existente do Gerenciador. Impossível elicitar todos os requisitos upfront sem acesso ao ambiente de produção. |
| A-02 | Sprint Planning formal documentada desde o início do projeto | Sprints S1 e S2 conduzidas com planejamento ágil via Microsoft Teams e notas informais; formalização completa a partir da S3 | Equipe enxuta composta por 3 desenvolvedores (Renan Kioshi, Henry Komatsu e Mateus Veloso); overhead documental de um planning formal nas primeiras sprints comprometia a cadência de entrega dentro do prazo contratado. |
| A-03 | Design de integração completo antes da implementação | Plano de Integração (ITP-AASP01-001) definido iterativamente; detalhes do contrato de API acordados no início da Sprint 2 | O contrato de API do microsserviço ms.temis.vinculos (banco temis3) foi disponibilizado pelo time do cliente somente no início da Sprint 2 (09/06/2026); especificação prévia seria baseada em suposições sem validade. |
| A-04 | Ambiente de homologação independente desde o início do projeto | Ambiente de homologação AASP disponibilizado somente a partir da Sprint 2 (09/06/2026); Sprint 1 executada com banco local SQL Server Express | Restrição imposta pelo cliente AASP; o time da AASP precisava preparar o ambiente de homologação em paralelo ao desenvolvimento. O time Timeware trabalhou com instância local para não bloquear entregas. |
| A-05 | Testes de sistema conduzidos exclusivamente pela equipe de desenvolvimento Timeware | Co-responsabilidade nos testes de aceite: Caroline Jenifer (QA Timeware) + Leonardo Francisco Pereira (QA AASP); roteiros revisados e executados em conjunto | Cliente AASP exigiu participação direta nos testes de aceite como condição contratual. Os roteiros foram revisados em conjunto (CTQ-AASP01-001) e os resultados registrados formalmente (REL-VV-AASP01-001). |
| A-06 | Plano de Construção e Produção (PCP) com especificações de baixo nível completas antes do desenvolvimento | PCP elaborado no nível de decisões arquiteturais e padrões de implementação; detalhes de baixo nível registrados nos Pull Requests #11 a #15 | Equipe enxuta; duplicar especificações de baixo nível no PCP e nos PRs geraria retrabalho documental sem agregar valor. Os PRs do Azure DevOps servem como documentação viva, rastreável e revisada. |
| A-07 | Code review com dois revisores independentes para cada Pull Request | Revisor único (Cézar Velázquez como Tech Lead) nos PRs de código crítico; revisão cruzada entre os desenvolvedores (Renan, Henry e Mateus Veloso) nos PRs de menor risco | Equipe de 3 desenvolvedores; exigir dois revisores independentes inviabilizaria o fluxo de trabalho. Cézar Velázquez revisa todos os PRs dos desenvolvedores. Gate de CI/CD obrigatório compensa parcialmente a redução de revisores. |
| A-08 | Papeis separados de Gerente de Projeto, GCO, Arquiteto e Tech Lead | Cézar Velázquez acumula os papeis de Arquiteto, Tech Lead, DevOps, Revisor e GCO; a Gerência de Projeto e exercida por Abraão Oliveira | Contrato previsto para equipe enxuta de desenvolvimento; acumulo de papeis por Cézar Velázquez viabiliza a operação dentro do orçamento contratado. As responsabilidades de cada papel são exercidas formalmente, ainda que pela mesma pessoa. |

---

## 4. Itens sem adaptação (processo-padrão mantido integralmente)

Os itens abaixo seguiram o processo-padrão Timeware sem qualquer adaptação:

- **Controle de versão com Git**: todo código versionado no Azure DevOps; branching Git Flow (main / develop / feature/ag-{id} / release/*) aplicado desde o primeiro commit.
- **Pull Request obrigatório para merge**: nenhum código integrado a develop ou main sem PR aprovado, independentemente do tamanho da mudança.
- **Testes unitários como gate de CI**: pipeline Azure DevOps bloqueia merge se testes unitários falharem; cobertura monitorada a cada sprint.
- **Registro de riscos**: RAC-AASP01-001 mantido e atualizado com riscos identificados, probabilidade, impacto e acoes de mitigação.
- **Comunicação semanal com o cliente**: reunioes de acompanhamento com Marcos Turnes (PO AASP) realizadas semanalmente durante toda a execução do projeto.
- **Rastreabilidade requisitos-testes**: matriz RASTR-AASP01-001 mantida associando cada requisito (AG-20 a AG-25) aos casos de teste e PRs correspondentes.
- **Formalização de Change Requests**: qualquer mudança de escopo registrada em CR-AASP01-001 antes de ser implementada.
- **Baselines de configuração**: baselines BL-01 (TAP aprovado, 19/05/2026) e BL-02 (aceite Sprint 1, 06/06/2026) formalizadas conforme processo GCO.

---

## 5. Impacto das adaptações no projeto

| # Adaptação | Impacto identificado | Mitigação adotada |
|---|---|---|
| A-01 | Risco de retrabalho por requisitos descobertos tardiamente | Reunioes semanais com PO Marcos Turnes para validar requisitos emergentes; backlog ajustado a cada sprint |
| A-02 | Planejamento menos formal nas primeiras sprints pode gerar lacunas de estimativa | Abraão Oliveira revisou estimativas ao final de cada sprint e ajustou o PLA-AASP01-001; formalização completa a partir da S3 |
| A-03 | Implementação da integração com temis iniciada sem contrato definitivo | Interfaces de integração projetadas com baixo acoplamento; adaptação ao contrato real custou apenas ajuste de payload na Sprint 2 |
| A-04 | Bugs de ambiente não detectados na Sprint 1 por ausência de homologação real | Testes unitários com cobertura estimada de 85% (22/26 métodos); bugs de ambiente identificados e corrigidos no início da Sprint 2 |
| A-05 | Maior esforco de coordenação entre Timeware e AASP nos ciclos de teste | Roteiros de teste (CTQ-AASP01-001) preparados com antecedência; sessões de teste agendadas com Leonardo Francisco Pereira; resultados registrados formalmente |
| A-06 | PRs como única fonte de especificação de baixo nível aumenta dependência do Azure DevOps | PRs exportados como PDF e arquivados no pacote documental MPS-SW a cada baseline |
| A-07 | Menor diversidade de perspectivas no code review | Gate de CI/CD obrigatório (build + testes + análise estática SonarQube); checklist de code review padrão Timeware aplicado em todos os PRs |
| A-08 | Acumulo de papeis por Cézar Velázquez aumenta risco de sobrecarga e ponto único de falha | Cronograma previsto com buffer de 20%; Renan Kioshi preparado para assumir atividades de GCO em caso de indisponibilidade de Cézar |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Abraão Oliveira | Versão inicial |
