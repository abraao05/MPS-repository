# Registro de Adaptação ao Processo-Padrão — AASP Gerenciador · Grupos de Usuários

| Campo | Valor |
|---|---|
| **Documento** | ADAP-AASP01-001 |
| **Projeto** | Grupos de Usuários — AASP Gerenciador |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.2 |
| **Data** | 01/07/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | ADAP (evidência de projeto) |

---

## 1. Objetivo

Registrar formalmente as adaptações realizadas ao processo-padrão Timeware para a execução do projeto AASP01 — Grupos de Usuários (ms.auxo.usuarios). As adaptações descritas neste documento foram avaliadas e aprovadas pelo Gerente de Projeto antes do inicio das atividades de desenvolvimento, conforme exigido pelo processo de Adaptação (ADAP) do modelo MPS-SW nível C.

Toda adaptação foi motivada por restrições reais de contexto — equipe enxuta, legado não documentado, restrições do cliente — e não implica redução de qualidade nos produtos entregues. Os mecanismos de mitigação associados a cada adaptação garantem que os objetivos do processo-padrão sejam atingidos por meios alternativos.

---

## 2. Adaptações aplicadas

| # | Item do processo-padrão | Decisão de adaptação | Justificativa |
|---|---|---|---|
| A-01 | Definição completa de requisitos antes do inicio do desenvolvimento | Levantamento iterativo de requisitos sprint a sprint, com baseline ao final de cada sprint aceita | Banco auxo3 legado com schema não documentado; requisitos precisaram ser descobertos explorando o banco e o código existente do Gerenciador. Impossível elicitar todos os requisitos upfront sem acesso ao ambiente de produção. |
| A-02 | Sprint Planning formal documentada desde o inicio do projeto | Sprints S1 e S2 conduzidas com planejamento ágil via Microsoft Teams e notas informais; Sprint 3 iniciada com Sprint Planning formal em 23/06/2026 — **adaptação ENCERRADA em 23/06/2026** | Equipe enxuta composta por 3 desenvolvedores (Renan Kiyoshi, Henry Komatsu e Mateus Veloso); overhead documental de um planning formal nas primeiras sprints comprometia a cadência de entrega dentro do prazo contratado. |
| A-03 | Design de integração completo antes da implementação | Plano de Integração (ITP-AASP01-001) definido iterativamente; detalhes do contrato de API acordados no inicio da Sprint 2 | O contrato de API do microsserviço ms.temis.vinculos (banco temis3) foi disponibilizado pelo time do cliente somente no inicio da Sprint 2 (09/06/2026); especificação previa seria baseada em suposições sem validade. |
| A-04 | Ambiente de homologação independente desde o inicio do projeto | Ambiente de homologação AASP disponibilizado somente a partir da Sprint 2 (09/06/2026); Sprint 1 executada com banco local SQL Server Express | Restrição imposta pelo cliente AASP; o time da AASP precisava preparar o ambiente de homologação em paralelo ao desenvolvimento. O time Timeware trabalhou com instancia local para não bloquear entregas. |
| A-05 | Testes de sistema conduzidos exclusivamente pela equipe de desenvolvimento Timeware | Co-responsabilidade nos testes de aceite: equipe de testes da Timeware + Leonardo Francisco Pereira (QA AASP); roteiros revisados e executados em conjunto | Cliente AASP exigiu participação direta nos testes de aceite como condição contratual. Os roteiros foram revisados em conjunto (CTQ-AASP01-001) e os resultados registrados formalmente (REL-VV-AASP01-001). |
| A-06 | Plano de Construção e Produção (PCP) com especificações de baixo nível completas antes do desenvolvimento | PCP elaborado no nível de decisões arquiteturais e padrões de implementação; detalhes de baixo nível registrados nos Merge Requests !1 a !7. Os MRs são acessíveis no GitLab interno (http://gitlab.timeware.local/aasp/ms.auxo.usuarios). | Equipe enxuta; duplicar especificações de baixo nível no PCP e nos MRs geraria retrabalho documental sem agregar valor. Os MRs do GitLab servem como documentação viva, rastreável e revisada. |
| A-07 | Code review com dois revisores independentes para cada Merge Request | Revisor único (Cezar Hiraki como Tech Lead) nos MRs de código critico; revisão cruzada entre os desenvolvedores (Renan, Henry e Mateus Veloso) nos MRs de menor risco | Equipe de 3 desenvolvedores; exigir dois revisores independentes inviabilizaria o fluxo de trabalho. Cezar Hiraki revisa todos os MRs dos desenvolvedores. Gate de CI/CD obrigatório compensa parcialmente a redução de revisores. |
| A-08 | Papeis separados de Gerente de Projeto, GCO, Arquiteto e Tech Lead | Cezar Hiraki acumula os papeis de Arquiteto, Tech Lead, DevOps, Revisor e GCO; a Gerência de Projeto e exercida por Abraão. **Aprovada explicitamente pelo SEPG (Silvio Baroni) em 19/05/2026 após avaliação do risco de conflito de interesse.** Mitigação adicional: auditorias formais de baseline realizadas com supervisão de Silvio Baroni (SEPG) para assegurar independência mínima nas verificações de configuração. | Contrato previsto para equipe enxuta de desenvolvimento; acumulo de papeis por Cezar Hiraki viabiliza a operação dentro do orçamento contratado. As responsabilidades de cada papel são exercidas formalmente, ainda que pela mesma pessoa. |

| A-09 | Documentação de projeto elaborada em paralelo ao desenvolvimento, com produção integral anterior ao início das atividades | Documentação do projeto (dossiê MPS-SW Nível C) elaborada em ciclo de retroconfecção: artefatos iniciais produzidos com base no entendimento do escopo; reconciliados com o estado real do código, GitLab e acordos de equipe ao longo das sprints, com versão formal entregue ao final do projeto. Responsável: Silvio Baroni (SEPG), com apoio de Henry Komatsu. | Equipe de desenvolvimento Timeware não possui tradição de elaboração documental MPS antes do início do código; o custo de produzir documentação completa upfront inviabilizaria o prazo contratado. A retroconfecção controlada, com reconciliação ativa em cada sprint, garante que os artefatos reflitam a realidade do projeto. Aprovada pelo SEPG em 24/06/2026. |

---

## 3. Itens sem adaptação (processo-padrão mantido integralmente)

Os itens abaixo seguiram o processo-padrão Timeware sem qualquer adaptação:

- **Controle de versão com Git**: todo código versionado no GitLab; branching Git Flow (main / develop / feature/ag-{id} / release/*) aplicado desde o primeiro commit.
- **Merge Request obrigatório para merge**: nenhum código integrado a develop ou main sem MR aprovado, independentemente do tamanho da mudança.
- **Testes unitarios como gate de CI**: pipeline GitLab CI bloqueia merge se testes unitarios falharem; cobertura monitorada a cada sprint.
- **Registro de riscos**: RAC-AASP01-001 mantido e atualizado com riscos identificados, probabilidade, impacto e ações de mitigação.
- **Comunicação semanal com o cliente**: reuniões de acompanhamento com Marcos Turnes (PO AASP) realizadas semanalmente durante toda a execução do projeto.
- **Rastreabilidade requisitos-testes**: matriz RASTR-AASP01-001 mantida associando cada requisito (AG-20 a AG-25) aos casos de teste e MRs correspondentes.
- **Formalização de Change Requests**: qualquer mudança de escopo registrada em CR-AASP01-001 antes de ser implementada.
- **Baselines de configuração**: baselines BL-01 (TAP aprovado, 19/05/2026) e BL-02 (aceite Sprint 1, 06/06/2026) formalizadas conforme processo GCO.

---

## 4. Impacto das adaptações no projeto

| # Adaptação | Impacto identificado | Mitigação adotada |
|---|---|---|
| A-01 | Risco de retrabalho por requisitos descobertos tardiamente | Reuniões semanais com PO Marcos Turnes para validar requisitos emergentes; backlog ajustado a cada sprint |
| A-02 | Planejamento menos formal nas primeiras sprints pode gerar lacunas de estimativa | Abraão revisou estimativas ao final de cada sprint e ajustou o PLA-AASP01-001; formalização completa a partir da S3 |
| A-03 | Implementação da integração com temis iniciada sem contrato definitivo | Interfaces de integração projetadas com baixo acoplamento; adaptação ao contrato real custou apenas ajuste de payload na Sprint 2 |
| A-04 | Bugs de ambiente não detectados na Sprint 1 por ausência de homologação real | Testes unitários com 68.4% de cobertura de linha (22 testes, meta ≥ 60%); bugs de ambiente identificados e corrigidos no início da Sprint 2 |
| A-05 | Maior esforço de coordenação entre Timeware e AASP nos ciclos de teste | Roteiros de teste (CTQ-AASP01-001) preparados com antecedência; sessões de teste agendadas com Leonardo Francisco Pereira; resultados registrados formalmente |
| A-06 | MRs como única fonte de especificação de baixo nível aumenta dependência do GitLab | MRs exportados como PDF e arquivados no pacote documental MPS-SW a cada baseline |
| A-07 | Menor diversidade de perspectivas no code review | Gate de CI/CD obrigatório (build + testes unitários + Coverlet coverage check); checklist de code review padrão Timeware aplicado em todos os MRs |
| A-08 | Acumulo de papeis por Cezar Hiraki aumenta risco de sobrecarga e ponto único de falha e conflito de interesse em auditorias de configuração | Cronograma previsto com buffer de 20%; Renan Kiyoshi preparado para assumir atividades de GCO em caso de indisponibilidade de Cezar; auditorias formais de baseline com supervisão de Silvio Baroni (SEPG) |
| A-09 | Rastreabilidade temporal dos documentos pode ser questionada por avaliadores MPS.BR (documentos produzidos com datas de sprint mas reconciliados após o código) | Declaração formal desta adaptação no ADAP; reconciliação documentada com log de alterações ("Time de Melhoria Contínua" → "Silvio Baroni SEPG"); histórico de versões refletindo as datas reais de cada versão; auditoria GQA cobrindo a qualidade dos artefatos reconciliados |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Abraão Oliveira | Versão inicial |
| 1.1 | 24/06/2026 | Silvio Baroni (SEPG) | Reconciliação com o estado real do GitLab (produto/repositório ms.auxo.usuarios; framework net5.0 onde aplicável; entregas da Sprint 1 integradas em develop com baseline pela tag sprint-1-aceite). |
| 1.2 | 01/07/2026 | Silvio Baroni (SEPG) | Correção de NCs de auditoria: A-02 encerrada formalmente (23/06/2026); A-06 mitigação atualizada; A-08 aprovação SEPG registrada + mitigação de independência GCO incluída; A-09 adicionada (retroconfecção documental declarada formalmente). |
