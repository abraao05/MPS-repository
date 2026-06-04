# Plano de Projeto — Fundação Tecnológica GASMIG · OS-PARCELA-002

| Campo | Valor |
|---|---|
| **Documento** | PLA-GASMIG02-002 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-002 |
| **Cliente** | GASMIG — Companhia de Gás de Minas Gerais |
| **Contrato** | Governança de APIs GASMIG |
| **Versão** | 1.0 |
| **Data** | 26/05/2026 |
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

## 4. Estimativas (GPR 3, 4)

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

## 5. Cronograma e marcos (GPR 5)

| Marco | Data prevista |
|---|---|
| Kickoff OS-PARCELA-002 | 26/05/2026 |
| Azure Key Vault provisionado e integrado ao APIM | 29/05/2026 |
| OAuth 2.0 (Entra ID + APIM) funcional | 02/06/2026 |
| API Keys com controle granular configuradas | 03/06/2026 |
| Versionamento + ciclo de vida + CORS + payload validation | 06/06/2026 |
| Application Insights integrado + dashboards configurados | 09/06/2026 |
| Alertas configurados e validados | 09/06/2026 |
| Verificação técnica Cézar Hiraki | 09/06/2026 |
| Sessão de homologação end-to-end com time técnico GASMIG | ~10/06/2026 |
| Encerramento OS-PARCELA-002 | 10/06/2026 |

## 6. Recursos (GPR 6, 7)

| Papel | Responsável | Dedicação |
|---|---|---|
| Gerente de Projeto / PO | Abraão Oliveira | Parcial |
| Tech Lead / Arquiteto / GCO | Cézar Hiraki | Parcial (foco reforçado em Key Vault e OAuth 2.0) |
| Engenheiro Azure | Fernando Oliveira | Integral |
| Engenheiro Azure | João Victor Cruz Silva | Integral |

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
