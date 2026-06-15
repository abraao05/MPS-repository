# Plano de Projeto — AASP_AndamentosProcessuais

| Campo | Valor |
|---|---|
| **Documento** | PLA-AASPAP01-001 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto** | Cezar Hiraki Velazquez |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Identificação e objetivo do projeto

O projeto refatora a solução legada .NET de captura de andamentos processuais da AASP (API AndamentosProcessuais + CapturaServer), em operação há cerca de 20 anos, para suportar o novo modelo de captura DataJud/CNJ via WorkerAndamentos. A evolução é cirúrgica e delimitada, sem reescrita do sistema legado, e entrega: fila unificada (RabbitMQ), webhook de indexação multi-fonte, histórico de movimentações por instância, verificação e desligamento nas APIs parceiras após captura via CNJ e controle de erros e segredo de justiça por instância. Os requisitos detalhados (RF01–RF12 e RNF01–RNF05) constam em REQ-AASPAP01-001.

## 2. Escopo (GPR 1)

- **Incluído:** refatoração do CapturaServer (publicação na fila WorkerAndamentos + `SegmentoTribunal`); webhook de indexação multi-fonte; histórico de movimentações por instância; verificação e desligamento nas APIs parceiras; campo `CodigoFonteAPI` e endpoint de atualização; tratamento de erros por instância (`Observacao`); segredo de justiça por instância (`Segredo`); desmembramento do RunUpdater para priorização.
- **Não incluído:** o restante da solução AndamentosProcessuais permanece inalterado; sem migração de dados no Elasticsearch; sem alteração estrutural do `IModelElastic`; sem reescrita do sistema legado.

Detalhamento em REQ-AASPAP01-001.

## 3. Adaptação do processo (GPR 2)

O processo-padrão (PRO-GPC-001) foi adaptado a este projeto conforme o GUIA-GPC-001. Registro completo em ADAP-AASPAP01-001. Principais decisões:

| Item de adaptação | Decisão | Justificativa |
|---|---|---|
| Design UX/UI | Não aplicável | Projeto de back-end/refatoração, sem interface de usuário |
| Nível de documentação | Reforçado | Projeto sob avaliação de certificação MPS-SW Nível C |
| Combinação de papéis | Tech Lead acumula Arquiteto e Gerência | Equipe enxuta; Cezar Hiraki Velazquez concentra GP, Tech Lead e Arquiteto |
| Estimativa e cadência | Gestão por horas/fases no ClickUp; sem story points | A solução legada e o ciclo compartilhado com o AASP_CNJ favorecem a gestão por atividades (ver GEST-AASPAP01) |
| Processo de entrega | GMUD — pacotes versionados + DDL no Azure DevOps | Solução legada em produção; mudanças controladas por GMUD |
| Ambiente de stage | Homologação por amostragem, ambiente compartilhado com AASP_CNJ | Não há Elasticsearch dedicado para testes |

## 4. Estimativas (GPR 3, 4)

O projeto foi estimado e acompanhado por **horas de esforço** registradas no sistema de gestão (ClickUp). O projeto não utilizou story points (gestão por fases). A base de estimativa foi a experiência do time na solução legada e o projeto irmão AASP_CNJ (mesmo time e ciclo). Detalhamento em GEST-AASPAP01 (abas Backlog, Tarefas e Acompanhamento).

**Esforço estimado × realizado por fase**

| Fase | Esforço estimado (h) | Esforço realizado (h) | Desvio |
|---|---|---|---|
| Fase 1 — Webhook e CapturaServer (EPROC) | 44 | 48 | +9% |
| Fase 2 — Estabilização e integração RabbitMQ | 66 | 72 | +9% |
| Fase 3 — Refatoração para suporte ao CNJ | 130 | 144 | +11% |
| Fase 4 — Tratamento de erros e validação | 90 | 98 | +9% |
| Fase 5 — Implantação | 18 | Em apuração | — |
| **Total** | **~348** | **~362 (parcial)** | **+9,7%** |

## 5. Cronograma, marcos e orçamento (GPR 5)

**Marcos**

| Marco | Data prevista | Data realizada / situação |
|---|---|---|
| Kickoff / início do ciclo | Dez/2025 | 15/12/2025 |
| Fim das Fases 1–2 (Webhook/CapturaServer/RabbitMQ) | Mar/2026 | Mar/2026 |
| Aprovação do Plano (baseline REG v1.0) | — | 08/06/2026 |
| Fim da Fase 3 (Refatoração CNJ) | Mai/2026 | Mai/2026 |
| Fim da Fase 4 (Tratamento de erros e validação) | Jun/2026 | Jun/2026 |
| Piloto / Homologação (por amostragem) | Jan–Mai/2026 | Jan–Mai/2026 |
| Aceite final / Encerramento | 30/06/2026 | Em andamento (Fase 5 — implantação) |

**Estrutura de fases**

| Fase | Período | Status |
|---|---|---|
| Fase 1 — Webhook e CapturaServer (EPROC) | Dez/2025 – Jan/2026 | Concluída |
| Fase 2 — Estabilização e integração RabbitMQ | Jan/2026 – Mar/2026 | Concluída |
| Fase 3 — Refatoração para suporte ao CNJ | Abr/2026 – Mai/2026 | Concluída |
| Fase 4 — Tratamento de erros e validação | Mai/2026 – Jun/2026 | Concluída |
| Fase 5 — Implantação | Jun/2026 | Em andamento |

**Orçamento total (esforço)**

| Item | Valor |
|---|---|
| Horas totais estimadas | ~348 h |
| Horas realizadas (parcial) | ~362 h (Fase 5 em apuração) |
| Período | 15/12/2025 a 30/06/2026 (previsto) |

## 6. Recursos (GPR 6, 7)

- **Equipe:** Cezar Hiraki Velazquez (Gerente de Projeto / Tech Lead / Arquiteto, todas as fases); Raony Chagas (Desenvolvedor Sênior Principal); Mateus Veloso (Desenvolvedor de Suporte, a partir de Abr/2026); Caroline Sousa (Analista de QA, Fase 4); Lucas Batista (Infraestrutura/DevOps, Fases 2 e 5); Jonathan Barbosa (Auditor GQA, independente).
- **Ambiente e ferramentas:** Azure DevOps (código, GMUD), ambiente de desenvolvimento local (.NET) + SQL Server, ambiente de homologação compartilhado com AASP_CNJ, produção AASP (SQL Server + Elasticsearch + RabbitMQ), ClickUp (gestão de atividades). Tecnologias: .NET / C#, SQL Server, RabbitMQ, Elasticsearch. Ver GCO-AASPAP01-001.

## 7. Partes interessadas e comunicação (GPR 9)

| Parte interessada | Interesse | Comunicação |
|---|---|---|
| Marcos Correa Fernandez Turnes (Representante / Sponsor / PO — AASP) | Validação, homologação e aceite | Homologação e devolutivas de resultado por fase |
| Patrocinador interno (Timeware) | Resultado operacional e de portfólio | Acompanhamento por marco |
| Time de desenvolvimento | Execução e decisões técnicas | Reuniões / atividades de alinhamento registradas no ClickUp |

## 8. Transição e suporte pós-go-live (GPR 8, GPR 16)

### 8.1 Estratégia de transição para produção

| Item | Descrição |
|---|---|
| Fluxo de deploy | Homologação por amostragem → montagem de pacote GMUD (+ scripts DDL) → agendamento com Infraestrutura → produção |
| Responsável pela execução | Equipe de Infraestrutura / DevOps (Lucas Batista) |
| Aprovador do go-live | Gerente de Projeto |
| Processo de mudança | GMUD — pacotes versionados e DDL no Azure DevOps |
| Plano de rollback | Reversão para a versão anterior; retrocompatibilidade preserva o fluxo de captura existente durante a transição |

### 8.2 Critérios de prontidão para go-live

| Critério | Obrigatório? | Verificado por |
|---|---|---|
| Fluxo de captura validado (sucesso, fallback/erro parcial e segredo por instância) | Sim | Raony Chagas / Caroline Sousa |
| Histórico de movimentações por instância validado | Sim | Caroline Sousa |
| Regressão do fluxo EPROC/ESAJ sem impacto | Sim | Caroline Sousa |
| Baseline de configuração registrada (tag de versão) | Sim | Lucas Batista (DevOps) / Cezar Hiraki Velazquez (GCO) |
| Pacote GMUD montado e agendado | Sim | Cezar Hiraki Velazquez / Lucas Batista |

### 8.3 Suporte e monitoramento pós-go-live

| Item | Descrição |
|---|---|
| Monitoramento | Monitoramento da fila RabbitMQ e dos registros de status/erro por instância nas tabelas de controle |
| Responsável | Raony Chagas + Cezar Hiraki Velazquez |
| O que monitorar | Erros por instância (`Observacao`); status de captura; integridade do histórico de movimentações |

## 9. Riscos (GPR 10)

Exposição = Probabilidade × Impacto (escala 1–3 por dimensão), conforme EST-GPC-002.

| Risco | Prob. | Impacto | Exposição | Resposta | Status final |
|---|---|---|---|---|---|
| R-01 Refatoração do webhook causar regressão no fluxo EPROC em produção | 2 | 3 | 6 | Mitigar — testes de regressão por amostragem; retrocompatibilidade | Controlado — não ocorreu |
| R-02 APIs parceiras com comportamento inconsistente nos endpoints de exclusão | 3 | 3 | 9 | Mitigar — tratamento específico por parceira + registro do retorno | Ocorreu — tratado |
| R-03 Perda de histórico de movimentações durante a migração do modelo | 1 | 3 | 3 | Mitigar — modelo só adiciona registros; nada é sobrescrito | Controlado — não ocorreu |
| R-04 Impacto no desempenho pela verificação nas APIs parceiras | 2 | 2 | 4 | Mitigar — verificação só após captura CNJ; EPROC não afetado | Controlado — não ocorreu |
| R-05 Falhas transitórias no envio do webhook causando perda de dados | 2 | 3 | 6 | Mitigar — retry no worker antes de registrar erro | Ocorreu — tratado |

## 10. Viabilidade (GPR 11)

O projeto é viável: a refatoração reaproveita a solução legada por evolução cirúrgica (esforço estimado ~348 h, ~6,5 meses), compartilhando time e ciclo com o projeto irmão AASP_CNJ, e prepara o pipeline para o modelo multi-fonte DataJud/CNJ sem reescrita. As principais restrições (ausência de Elasticsearch dedicado e comportamento heterogêneo das APIs parceiras) são endereçadas por homologação por amostragem e por controladores específicos por parceira.

## 11. Aprovação do Plano (GPR 13)

| Envolvido | Papel | Aceite | Data | Ref. da ata |
|---|---|---|---|---|
| Marcos Correa Fernandez Turnes | AASP — Sponsor / PO | Aceite por fase (Fases 1–2: Mar/2026; Fases 3–4: Jun/2026) | — | Aceite total a registrar no encerramento |

> A baseline do Plano foi aprovada em 08/06/2026 (REG-AASPAP01-001 v1.0). O aceite final do projeto será registrado no encerramento, conforme o estágio atual (Fase 5 — implantação em andamento).

---

## Controle de atualizações do plano

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Plano consolidado a partir do Registro de Projeto AASP_AndamentosProcessuais (REG-AASPAP01-001 v1.0, 08/06/2026) e do levantamento de projeto (INTAKE-PROJETO_AASPAP01 v1.0). |
