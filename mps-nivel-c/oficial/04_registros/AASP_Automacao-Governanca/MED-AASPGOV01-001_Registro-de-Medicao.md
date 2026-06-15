# Registro de Medição — AASP_GOV · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | MED-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync (AASPGOV01) |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 02/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | MED (evidência de projeto) |

---

## 1. Objetivo

Registrar os resultados de medição do projeto AASP_Automacao-Governanca — SensrJiraSync, alinhados às 7 medidas oficiais M1–M7 definidas no Plano de Medição Organizacional PLA-MED-001 (v1.3, 05/06/2026). Os indicadores coletados sustentam a análise de desempenho do projeto, a identificação de desvios e suas causas-raiz, o registro de ações corretivas e a comunicação dos resultados ao cliente, à organização e ao Auditor GQA, conforme PLA-MED-001 §7.

## 2. Indicadores M1–M7 do PLA-MED-001

| Medida | Objetivo | Meta | Resultado AASP_GOV | Status |
|---|---|---|---|---|
| M1 — Aderência ao prazo | OM1 — Aumentar a previsibilidade de prazo e esforço | ≤ 5% de desvio | 0% — entregue em 02/06/2026 conforme data prevista no TAP-AASPGOV01-001 | Atingida |
| M2 — Esforço estimado × realizado | OM1 | ≤ 10% de desvio | +9,3% — 216 h estimadas → 236 h realizadas | Atingida |
| M3 — Velocity | OM2 — Acompanhar e melhorar a capacidade de entrega | ≥ 12 SP/sprint | 15 SP/sprint (média das 4 sprints: S0=15, S1=16, S2=16, S3=12) | Atingida |
| M4 — Itens entregues × planejados | OM2 | ≥ 95% por sprint | 100% — 17 itens planejados entregues em 17 itens concluídos | Atingida |
| M5 — Densidade de defeitos | OM3 — Reduzir defeitos e retrabalho | ≤ 1 defeito a cada 4 SP | 0,085 def/SP (5 defeitos em 59 SP — equivalente a ~1 defeito a cada 12 SP) | Atingida |
| M6 — Defeitos em homologação × produção | OM4 — Antecipar detecção de defeitos antes da entrega | 100% de contenção em homologação | 5 defeitos detectados em homologação · 0 defeitos escapados para produção | Atingida |
| M7 — Retrabalho | OM3 | ≤ 5% de itens reabertos | 0% — nenhum item reaberto após conclusão ao longo das 4 sprints | Atingida |

Todas as 7 medidas atingiram as metas definidas no PLA-MED-001 v1.3. Fonte dos dados: Jira (backlog, sprints e registro de defeitos do projeto AASPGOV01).

## 3. Indicadores específicos do projeto

Indicadores complementares às medidas M1–M7, definidos em função dos objetivos de negócio do SensrJiraSync:

| Indicador | Meta | Resultado |
|---|---|---|
| Eliminação de trabalho manual de migração de cards | 100% dos cards migrados automaticamente, sem intervenção manual | 100% — nenhuma migração manual necessária após implantação |
| Idempotência — ausência de duplicatas em execuções repetidas | 0 duplicatas em todos os ciclos de execução | 0 duplicatas verificadas em todos os cenários de teste (CT-01, CT-02) |
| Fidelidade dos dados migrados | 100% de conformidade nos campos verificados (descrição, labels, status, histórico) | 100% — todos os critérios CA01 a CA07 validados |
| Taxa de contenção de defeitos (absoluta) | ≥ 95% dos defeitos contidos antes da entrega ao cliente | 100% — BUG-01 a BUG-05 corrigidos antes da validação com o Sponsor |
| Não-conformidades (NCs) de GQA abertas ao encerramento | 0 NCs abertas | 0 NCs — auditoria GQA encerrada sem pendências (GQA-AASPGOV01-001) |

## 4. Medidas de esforço por fase (M2 detalhado)

| Fase | Período | Esforço estimado (h) | Esforço realizado (h) | Variação | Responsável principal |
|---|---|---|---|---|---|
| Fase 1 — Arquitetura | 14/04 – 16/04/2026 | 16 | 16 | 0% | Cezar Hiraki |
| Fase 2 — Mapeamento e Autenticação | 17/04 – 23/04/2026 | 40 | 44 | +10% | Raony Chagas / Allan Alves |
| Fase 3 — Desenvolvimento dos Serviços | 24/04 – 20/05/2026 | 120 | 128 | +6,7% | Raony Chagas / Allan Alves |
| Fase 4 — Homologação e Correções | 21/05 – 02/06/2026 | 40 | 48 | +20% | Raony Chagas / Caroline Sousa |
| **Total do projeto** | **14/04 – 02/06/2026** | **216** | **236** | **+9,3%** | — |

O esforço foi modelado retroativamente em aproximadamente 59 Story Points distribuídos em 4 sprints (velocity média de 15 SP/sprint), para fins de gestão ágil e carga no Jira. Conversão aplicada: 1 SP = 4 h. Distribuição por sprint: Sprint 0 (15 SP) · Sprint 1 (16 SP) · Sprint 2 (16 SP) · Sprint 3 (12 SP). Referência: GEST-AASPGOV01_Planilha-de-Gestao-do-Projeto.xlsx (abas Backlog, Tarefas e Acompanhamento).

## 5. Análise de variâncias

| Variância | Magnitude | Causa-raiz | Ação corretiva |
|---|---|---|---|
| Esforço da Fase 2 acima do estimado (+10%) | Baixa | O mapeamento da API Jira v3 exigiu mais investigação que o previsto, em especial para compreender os requisitos do Atlassian Document Format (ADF) e os comportamentos da API de transições — aspectos não cobertos pelas estimativas iniciais | AC-01 — Adotar estimativa mais conservadora para mapeamento de APIs externas com formatos proprietários em projetos futuros |
| Esforço da Fase 4 acima do estimado (+20%) | Média | A identificação de 5 defeitos (BUG-01 a BUG-05) durante a homologação — relacionados a HTML, comparação de status, sanitização de labels e paginação — exigiu ciclos de correção e reteste não previstos na estimativa inicial da fase | AC-02 — Incluir cenário de teste obrigatório para tratamento de HTML e labels em projetos de integração/migração já nas fases anteriores à homologação |

## 6. Ações corretivas registradas

- **AC-01:** Adoção de fator de estimativa mais conservador (+30% sobre baseline) para a fase de mapeamento de APIs externas com formatos proprietários (ex.: ADF da Atlassian) em projetos futuros. Ação incorporada ao PLA-GPR-001 (Plano de Gerência de Projetos organizacional) como ajuste de template de estimativa para projetos de integração com APIs Atlassian.

- **AC-02:** Inclusão de cenário de teste obrigatório para tratamento de HTML e sanitização de campos em projetos de migração ou integração com sistemas que armazenam conteúdo em HTML. Ação incorporada ao TPL-VV-001 §6 como cenário Gherkin de referência (modelo baseado em CT-05 e CT-10 do AASP_GOV).

## 7. Comunicação dos resultados

Conforme PLA-MED-001 §7, os resultados das medidas M1–M7 e os indicadores específicos do projeto foram comunicados pelos seguintes canais:

- **Internamente (time Timeware):** nas atas de marcos do projeto (ATA-AASPGOV01-001, ATA-AASPGOV01-002 e ATA-AASPGOV01-003), com acompanhamento dos indicadores de prazo, esforço e qualidade em cada reunião de revisão.

- **Ao cliente (Sponsor AASP):** na reunião de Validação de Homologação de 29/05/2026 (ATA-AASPGOV01-003), com apresentação dos resultados dos critérios de aceite CA01–CA07 e dos defeitos identificados e corrigidos; e no Termo de Aceite e Encerramento TAE-AASPGOV01-001 (02/06/2026), assinado por Marcos Correa Fernandez Turnes.

- **À organização Timeware:** os indicadores M1–M7 do projeto AASP_GOV foram consolidados no REG-MED-001 (Repositório Organizacional de Medidas), alimentando a base de dados histórica de projetos para calibração de estimativas futuras.

- **Ao Auditor GQA:** os resultados foram disponibilizados para verificação independente pelo Auditor Jonathan Alves, registrados em GQA-AASPGOV01-001. A auditoria confirmou conformidade com o processo MED do MR-MPS-SW:2024 Nível C.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 02/06/2026 | Time de Melhoria Contínua | Registro de medição consolidado a partir do Registro de Projeto AASP_GOV v2.0 e alinhado ao PLA-MED-001 v1.3 (05/06/2026). |
