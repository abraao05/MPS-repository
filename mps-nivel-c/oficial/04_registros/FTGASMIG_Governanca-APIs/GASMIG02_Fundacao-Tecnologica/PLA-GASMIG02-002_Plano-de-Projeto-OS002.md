# Plano de Projeto — Fundação Tecnológica GASMIG · OS-PARCELA-002

| Campo | Valor |
|---|---|
| **Documento** | PLA-GASMIG02-002 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-002 |
| **Cliente** | GASMIG — Companhia de Gás de Minas Gerais |
| **Contrato** | Governança de APIs GASMIG |
| **Versão** | 1.2 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Identificação e objetivo do projeto

Completar a Fundação Tecnológica de Integração da GASMIG com gestão de secrets (Azure Key Vault), autenticação OAuth 2.0 e API Keys, versionamento, ciclo de vida de APIs, monitoramento, alertas, ajuste fino de segurança e homologação end-to-end. Ao encerramento desta OS, a fundação estará completamente operacional.

Detalhamento: ver `REQ-GASMIG02-002_Documento-de-Requisitos-OS002.md`.

## 2. Escopo (GPR 1)

- **Incluído:** RF-11 a RF-19 e RNF-06 a RNF-09 conforme REQ-GASMIG02-002
- **Não incluído:** desenvolvimento de APIs de negócio; alterações estruturais nos workspaces da OS-001 (exceto ajustes finos de segurança)

## 3. Adaptação do processo (GPR 2)

Ver `ADAP-GASMIG02-002_Registro-de-Adaptacao-OS002.md`. Mesmas decisões da OS-001 com atenção reforçada em segurança (Key Vault, OAuth 2.0).

## 4. Estimativas e orçamento de horas (GPR 3, 4)

- **Tamanho estimado:** 78 story points

| Requisito | Complexidade | Story Points |
|---|---|---|
| RF-11 — Azure Key Vault + integração APIM | Alta | 13 |
| RF-12 — OAuth 2.0 (Entra ID + JWT validation) | Alta | 13 |
| RF-13 — API Keys com controle granular | Média | 8 |
| RF-14 — Políticas de versionamento | Baixa-Média | 5 |
| RF-15 — Políticas de ciclo de vida | Baixa-Média | 5 |
| RF-16 — Monitoramento (App Insights + dashboards) | Média | 8 |
| RF-17 — Alertas automatizados (Azure Monitor) | Baixa-Média | 5 |
| RF-18 — CORS + validação de payloads | Média | 8 |
| RF-19 — Homologação end-to-end | Média | 8 |
| Documentação, verificação técnica e sessão de aceite | — | 5 |
| **Total** | | **78 SP** |

- **Velocity de referência:** 56 SP/sprint (mesma base da OS-001 — equipe e configuração equivalentes)
- **Esforço/prazo estimado:** ~1,4 sprints / 15 dias corridos
- **Base histórica:** OS-PARCELA-001 (velocity observada: 84 SP em 15 dias com a mesma equipe)

**Orçamento de horas por papel:**

*Referência: 168 h/mês disponíveis por pessoa → ~140 h/mês efetivas (~70 h/sprint) após dedução de cerimônias e reuniões (~15%). Dedicação parcial proporcional.*

| Papel | Pessoas | Dedicação | h efetivas/sprint | Nº sprints | **h estimadas** |
|---|---|---|---|---|---|
| Gerente de Projeto / PO | 1 | 30% | 21 h | 1,4 | 29 h |
| Tech Lead / Arquiteto / GCO | 1 | 50% | 35 h | 1,4 | 49 h |
| Engenheiro Azure (Fernando Oliveira) | 1 | 100% | 70 h | 1,4 | 98 h |
| Engenheiro Azure (Henry Komatsu) | 1 | 100% | 70 h | 1,4 | 98 h |
| **Total** | | | | | **274 h** |

## 5. Cronograma e marcos (GPR 5)

> **Convenção de sprint:** a sprint é encerrada na sexta-feira (freeze de configuração); a entrega formal ao cliente e a verificação técnica ocorrem na segunda-feira seguinte; sessão de homologação e encerramento na terça.

| Marco | Data prevista | Responsável |
|---|---|---|
| Kickoff OS-PARCELA-002 | 26/05/2026 (seg) | Abraão Oliveira |
| Azure Key Vault provisionado e integrado ao APIM | 29/05/2026 (qui) | Fernando Oliveira — revisão: Cézar Hiraki |
| OAuth 2.0 (Entra ID + APIM) funcional | 02/06/2026 (ter) | Henry Komatsu — revisão: Cézar Hiraki |
| API Keys com controle granular configuradas | 03/06/2026 (qua) | Fernando Oliveira |
| Versionamento + ciclo de vida configurados | 04/06/2026 (qui) | Henry Komatsu |
| CORS + validação de payload configurados | 05/06/2026 (qui) | Fernando Oliveira |
| Application Insights integrado + dashboards configurados | 06/06/2026 (sex) | Fernando Oliveira |
| Alertas configurados e validados | 06/06/2026 (sex) | Henry Komatsu |
| **Freeze de configuração — encerramento da sprint** | **06/06/2026 (sex)** | **Time OS-002** |
| Verificação técnica Cézar Hiraki + entrega formal ao cliente | 09/06/2026 (seg) | Cézar Hiraki / Abraão Oliveira |
| Sessão de homologação end-to-end com time técnico GASMIG | 10/06/2026 (ter) | Abraão Oliveira / Cézar Hiraki |
| Encerramento OS-PARCELA-002 | 10/06/2026 (ter) | Abraão Oliveira |

## 6. Recursos (GPR 6, 7)

| Papel | Responsável | Dedicação | Foco principal na OS-002 |
|---|---|---|---|
| Gerente de Projeto / PO | Abraão Oliveira | Parcial | Coordenação, comunicação com GASMIG, encerramento |
| Tech Lead / Arquiteto / GCO | Cézar Hiraki | Parcial | Revisão de Key Vault, OAuth 2.0, alertas; verificação técnica 09/06 |
| Engenheiro Azure | Fernando Oliveira | Integral | RF-11 (Key Vault), RF-13 (API Keys), RF-18 (CORS + payload), RF-16 (dashboards) |
| Engenheiro Azure | Henry Komatsu | Integral | RF-12 (OAuth 2.0), RF-14 (versionamento), RF-15 (ciclo de vida), RF-17 (alertas) |

**Ambiente e ferramentas:** mesmos da OS-001 + Azure Key Vault + Application Insights + Azure Monitor.

## 7. Partes interessadas e comunicação (GPR 9)

Mesmas da OS-001. Reunião semanal recorrente (quarta 14h via Teams) mantida como canal principal com o time GASMIG.

## 8. Transição (GPR 8)

Ao encerramento desta OS, a Fundação Tecnológica GASMIG estará completa. Toda a documentação técnica (design, IaC, checklist, planos) é entregue ao cliente como parte do pacote de aceite. A fundação passa a ser gerida pelo time de TI GASMIG para receber as futuras APIs de negócio.

## 9. Riscos (GPR 10)

| # | Risco | Prob. | Impacto | Resposta |
|---|---|---|---|---|
| R-07 | Permissões insuficientes no Entra ID para registrar aplicações OAuth 2.0 | 2 | 3 | Verificar e solicitar as permissões necessárias na semana 1; escalar via Sérgio Villaça se necessário |
| R-08 | Thresholds de alerta não definidos pelo time GASMIG a tempo, bloqueando a configuração do Azure Monitor | 3 | 2 | Usar valores padrão de mercado como default; solicitar definição formal na semana 1 |
| R-09 | Complexidade do fluxo OAuth 2.0 com o Entra ID da GASMIG excede a estimativa | 2 | 2 | Iniciar pela validação do fluxo básico de token; reservar um dia adicional de buffer se necessário |
| R-10 | Mudança de escopo na homologação end-to-end (cliente identifica necessidade de ajustes não previstos) | 2 | 3 | Delimitar claramente o critério de aceite antes da sessão; formalizar via Change Request se necessário |

## 10. Viabilidade (GPR 11)

Projeto viável. A equipe executa em continuidade à OS-001, com ambiente já configurado e acessos provisionados. O escopo é conhecido e bem delimitado. A velocidade observada na OS-001 (84 SP em ~15 dias) confirma capacidade para 78 SP neste prazo.

## 11. Aprovação do Plano (GPR 13)

| Envolvido | Papel | Aceite | Data | Ref. |
|---|---|---|---|---|
| Sérgio Guimarães Villaça | Gestor do Contrato — GASMIG | Aprovado (escopo acordado desde 29/04/2026; OS-002 iniciada após aceite OS-001) | 26/05/2026 | TAE-GASMIG02-001 / ATA-GASMIG02-002 |
| Abraão Oliveira | Gerente de Projeto — Timeware | Confirmado | 26/05/2026 | — |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão Oliveira | Versão inicial — baseline aprovada no kickoff da OS-002 |
| 1.1 | 04/06/2026 | Abraão Oliveira | Atualização de recursos (Fernando Oliveira e Henry Komatsu como engenheiros executores); cronograma detalhado com responsáveis por marco e convenção de sprint (freeze sexta / entrega segunda) |
| 1.2 | 11/06/2026 | Time de Melhoria Contínua | Acréscimo da tabela de orçamento de horas por papel em §4 (GPR 4) — 274 h totais estimadas; título do §4 atualizado para refletir GPR 3 e GPR 4 |
