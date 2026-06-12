# Relatório de Acompanhamento (Status Report) — Cadastro de Clientes · Rede D1000

> **EXEMPLO DE PREENCHIMENTO (acompanha TPL-GPR-005 v2.1).** Modelo de referência que demonstra como preencher o template de status report no padrão executivo. Os indicadores (SPI, velocity, latência, defeitos, nº de CRs) refletem dados reais do projeto PROFARMA registrados em MED-PROFARMA01-001; as datas finas de sprint e os itens de decisão são ilustrativos, para fins de demonstração do formato. O §2.1 (dailys internas) é seção interna — não é enviada ao cliente. Não é evidência de projeto — é material de apoio à adoção do template.

| Campo | Valor |
|---|---|
| **Projeto** | Modernização do Cadastro de Clientes |
| **Cliente** | Profarma S.A. / Rede D1000 |
| **Período de referência** | Sprint 16 · 13/10–24/10/2025 |
| **Data do relatório** | 24/10/2025 |
| **Gerente de Projeto** | Gerente de Projeto |
| **Destinatários** | Patrocinador e pontos focais do cliente |

---

## 1. Situação geral

O projeto avançou bem na construção (melhor velocity do projeto na sprint), mas a homologação segue condicionada à disponibilização do ambiente AKS e ao ciclo de GMUD da Rede D1000 — fatores externos que pressionam o prazo final.

| Dimensão | Status | Comentário |
|---|---|---|
| **Prazo** | 🟡 Atenção | Homologação depende de ambiente AKS e janela de GMUD do cliente |
| **Escopo** | 🟡 Em mudança | 12 CRs absorvidos; escopo passou de 5 para 7 integrações |
| **Risco** | 🟡 Atenção | Risco de ambiente e de janela de release sob acompanhamento |
| **Qualidade** | 🟢 Dentro do esperado | 0 defeitos S1; latência p95 142ms (29% abaixo do SLA) |

## 2. Resumo do período

Na Sprint 16 a equipe atingiu o pico de produtividade do projeto (42 SP), concluindo os ajustes finais da consolidação de vendas e a preparação do worker LGPD para homologação. O ambiente AKS foi parcialmente disponibilizado, permitindo iniciar os testes técnicos. O principal fator de atenção continua sendo a janela de GMUD, que adiciona de 2 a 5 dias úteis por ciclo de release.

| Indicador | Valor |
|---|---|
| Horas trabalhadas no período | 280 h |
| Entregas concluídas | 3 |
| Avanço do projeto (acumulado) | ~88% |
| Story Points na sprint | 42 SP (pico do projeto) |

### 2.1 Registro de dailys internas

> *Seção interna — presença da equipe Timeware e temas tratados nas dailys da sprint. Não inclusa na versão enviada ao cliente.*

**Presenças por daily:**

| Data | Equipe presente | Ausência / motivo |
|---|---|---|
| 13/10 (seg) | Gerente de Projeto, Tech Lead, Dev 1, Dev 2, QA | — |
| 14/10 (ter) | Gerente de Projeto, Tech Lead, Dev 1, Dev 2, QA | — |
| 15/10 (qua) | Tech Lead, Dev 1, Dev 2, QA | GP em reunião com cliente (AKS) |
| 16/10 (qui) | Gerente de Projeto, Tech Lead, Dev 1, Dev 2, QA | — |
| 17/10 (sex) | Gerente de Projeto, Tech Lead, Dev 1, QA | Dev 2 ausente — justificado |
| 20/10 (seg) | Gerente de Projeto, Tech Lead, Dev 1, Dev 2, QA | — |
| 21/10 (ter) | Gerente de Projeto, Tech Lead, Dev 1, Dev 2, QA | — |
| 22/10 (qua) | Gerente de Projeto, Tech Lead, Dev 1, Dev 2, QA | — |
| 23/10 (qui) | Tech Lead, Dev 1, Dev 2, QA | GP em reunião interna de portfólio |
| 24/10 (sex) | Gerente de Projeto, Tech Lead, Dev 1, Dev 2, QA | — |

**Resumo semanal:**

| Semana | Principais tópicos e decisões internas |
|---|---|
| 13/10 – 17/10 | Ajustes finais da consolidação de vendas (ID legado ITEC + CPF); alinhamento sobre o ambiente AKS disponibilizado parcialmente em 15/10; decisão de iniciar testes técnicos no AKS sem aguardar ambiente completo; worker LGPD em finalização pelo Dev 2 |
| 20/10 – 24/10 | Identificação de volume maior de duplicidades na base legada (saneamento +5 dias); abertura do CR-08; ciclo de GMUD confirmado para 11/11 — alinhamento interno sobre impacto de +3 dias úteis; sprint fechada com 42 SP (pico do projeto); revisão do planejamento para Sprint 17 com foco em homologação funcional |

---

## 3. Entregas realizadas no período

| Entrega | Resultado / valor para o cliente | Situação |
|---|---|---|
| Consolidação de vendas com ID legado ITEC + CPF | Convivência segura entre sistema antigo e novo durante o piloto | ✅ Concluído |
| Worker LGPD pronto para homologação | Saneamento e conformidade da base de 7M CPFs | ✅ Concluído |
| Início dos testes técnicos no AKS | Validação da aplicação no ambiente-alvo de produção | ✅ Concluído |

## 4. Planejado para o próximo período

| Item / marco | Data prevista | Observação |
|---|---|---|
| Homologação funcional completa (piloto loja 9) | 07/11/2025 | Condicionada à janela de GMUD |
| Execução da GMUD para deploy de homologação | 11/11/2025 | Aprovação do patrocinador do cliente |
| Início do rollout assistido | 18/11/2025 | Após aceite do piloto |

## 5. Indicadores do projeto (acompanhamento)

| Indicador | Meta / referência | Período atual | Tendência |
|---|---|---|---|
| Aderência ao prazo (SPI) | ≥ 0,90 | 0,91 | ➡️ |
| Esforço estimado × realizado | ≤ 10% desvio | dentro (escopo ampliado via CR) | ➡️ |
| Velocity | ~30 SP/sprint | 42 SP | ⬆️ |
| Defeitos S1 em produção | 0 | 0 | ➡️ |

## 6. Diário de bordo (eventos e impactos)

| Data | Evento / motivo | Origem | Impacto (dias) | Situação |
|---|---|---|---|---|
| 15/10 | Ambiente AKS disponibilizado parcialmente (2,5 meses após o planejado) | Cliente (Infra) | +cumulativo | Em curso |
| 20/10 | Ciclo de GMUD adicionou 3 dias úteis ao release de homologação | Cliente (processo de mudança) | +3 | Em curso |
| 22/10 | Saneamento da base legada acima do estimado (duplicidades) | Timeware / dado legado | +5 | Resolvido |

## 7. Pontos de atenção, riscos e plano de ação

**Disponibilidade do ambiente AKS** — 🔴 Crítico
- **Ponto:** A homologação só avança no AKS, disponibilizado com 2,5 meses de atraso.
- **Risco:** Compressão da janela de homologação e do piloto, empurrando o go-live.
- **Ação:** Acompanhamento diário com a Infra do cliente; testes técnicos iniciados assim que o ambiente subiu parcialmente. Responsável: Gerente de Projeto. Prazo: contínuo até 07/11.

**Janela de GMUD do cliente** — 🟡 Médio
- **Ponto:** Cada deploy em homologação/produção depende da GMUD da Rede D1000.
- **Risco:** 2 a 5 dias úteis adicionais por ciclo de release.
- **Ação:** Antecipar a abertura da GMUD para 11/11 com aprovação do patrocinador; consolidar entregas para reduzir o número de ciclos.

## 8. Mudanças (change requests)

| ID | Descrição | Abertura | Dias em aberto | Status | Aceite final |
|---|---|---|---|---|---|
| CR-07 | Integração Propz CRM | 18/08 | 6 | Aprovada | 24/08 |
| CR-08 | Saneamento adicional da base legada | 22/10 | 2 | Aprovada | 24/10 |

> *Total acumulado no projeto: 12 CRs formais aprovados.*

## 9. Decisões necessárias

| Decisão necessária | Responsável pela decisão | Prazo desejado |
|---|---|---|
| Aprovação da janela de GMUD para deploy de homologação | Patrocinador do cliente | 07/11/2025 |
| Confirmação da loja-piloto para o rollout | Ponto focal do cliente | 12/11/2025 |

---

## Cadência de reporte

| Item | Definição |
|---|---|
| **Periodicidade** | Quinzenal (a cada sprint) |
| **Participantes obrigatórios** | Pontos focais do cliente |
| **Participantes opcionais** | Patrocinador |
| **Canal** | Sprint Review + envio do report em PDF |
