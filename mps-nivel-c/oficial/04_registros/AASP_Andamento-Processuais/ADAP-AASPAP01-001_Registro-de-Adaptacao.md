# Registro de Adaptação do Processo — AASP_AndamentosProcessuais

| Campo | Valor |
|---|---|
| **Documento** | ADAP-AASPAP01-001 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Responsável pela adaptação** | Cezar Hiraki Velazquez |
| **Processo MPS-SW** | GPC (evidência de projeto) |

---

## 1. Decisões de adaptação

Adaptação do processo-padrão (PRO-GPC-001) a este projeto, conforme o GUIA-GPC-001.

| Eixo de adaptação | Decisão | Justificativa |
|---|---|---|
| Tipo de produto (com/sem front-end) | Sem UX/UI — apenas back-end/refatoração e arquitetura | A solução é a refatoração de serviços de retaguarda (API e CapturaServer); não há interface de usuário |
| Origem dos requisitos e do design | Timeware elabora; AASP valida e homologa | Os requisitos derivam de necessidades operacionais da captura; o cliente valida resultados e aceita as entregas por fase |
| Nível de documentação | Reforçado | Projeto sob avaliação de certificação MPS-SW Nível C |
| Porte do projeto | Médio → formalidade padrão | ~348 h estimadas, ~6,5 meses, ciclo compartilhado com o projeto irmão AASP_CNJ |
| Equipe e papéis (acúmulo) | Tech Lead acumula Arquiteto e Gerência de Projeto | Equipe enxuta; Cezar Hiraki Velazquez concentra GP, Tech Lead e Arquiteto |
| Estimativa e cadência | Gestão por horas/cards no ClickUp; sem story points (gestão por fases) | A solução legada e o ciclo compartilhado com o AASP_CNJ favorecem a gestão por atividades (ver GEST-AASPAP01) |
| Processo de revisão de código | PR no Azure DevOps, revisada por ≥1 membro além do autor (GitFlow) | Garantia de qualidade do código e rastreabilidade |
| Processo de entrega | GMUD — pacotes versionados + DDL no Azure DevOps | Solução legada em produção; mudanças controladas por GMUD |
| Ambiente de stage | Não adotado — homologação por amostragem, ambiente compartilhado com AASP_CNJ | Não há Elasticsearch dedicado para testes; ciclo coordenado entre os dois projetos |

## 2. Etapas aplicáveis e não aplicáveis

| Etapa / artefato | Aplicável? | Observação |
|---|---|---|
| Design de UX/UI | Não | Projeto sem front-end |
| Mapa de teste por história (story) | Não | Projeto não usa histórias/SP; testes organizados por cenário (CT-01 a CT-12) e fase (ver VV-AASPAP01-001) |
| Documento de Design (arquitetura) | Sim | PCP-AASPAP01-001 |
| Estratégia de Integração | Sim | ITP-AASPAP01-001 |
| Plano e execução de V&V | Sim | VV-AASPAP01-001 e REL-VV-AASPAP01-001 |
| Gerência de Configuração | Sim | GCO-AASPAP01-001 (GitFlow + GMUD) |
| Registro de decisões (GDE) | Sim | GDE-AASPAP01-001 (decisões D01–D07) |
| Aquisição (AQU) | Não | Não há subcontratação de desenvolvimento; APIs/infra de terceiros são insumos de serviço, tratados em ITP/PCP e Riscos |

## 3. Pontos de controle obrigatórios (não adaptáveis)

- [x] Requisitos especificados e validados (REQ-AASPAP01-001)
- [x] Plano de Projeto aprovado (baseline REG-AASPAP01-001 v1.0, 08/06/2026)
- [x] Definição de Pronto aplicada (cenários de aceite CT-01 a CT-12, 100% aprovados — ver VV)
- [x] Verificação e validação realizadas (VV / REL-VV)
- [ ] Encerramento formal com aceite total — encerramento previsto 30/06/2026 (Fase 5 — implantação em andamento)

O ponto em aberto refere-se ao marco de encerramento total e será registrado ao final do projeto (TAE-AASPAP01-001 e a ata de aceite), conforme o estágio atual. O aceite por fase já ocorreu (Fases 1–2: Mar/2026; Fases 3–4: Jun/2026).

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Registro de adaptação consolidado a partir do Registro de Projeto AASP_AndamentosProcessuais (REG-AASPAP01-001 v1.0, 08/06/2026) e do levantamento de projeto (INTAKE-PROJETO_AASPAP01 v1.0). |
