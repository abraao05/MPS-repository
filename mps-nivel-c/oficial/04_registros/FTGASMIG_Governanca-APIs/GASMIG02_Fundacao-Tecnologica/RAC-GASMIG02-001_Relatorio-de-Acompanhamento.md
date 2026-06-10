# Relatório de Acompanhamento — Fundação Tecnológica GASMIG · OS-PARCELA-002

| Campo | Valor |
|---|---|
| **Documento** | RAC-GASMIG02-001 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-002 |
| **Cliente** | GASMIG — Companhia de Gás de Minas Gerais |
| **Período** | 26/05/2026 – 09/06/2026 |
| **Versão** | 1.1 |
| **Data** | 10/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Resumo executivo

A OS-PARCELA-002 foi executada em **14 dias corridos** (26/05–09/06/2026), dentro do prazo contratual de 15 dias. Todos os 78 story points planejados foram entregues. A entrega foi apresentada ao cliente em call no dia 08/06/2026 e aceite formal recebido em 09/06/2026 via e-mail de Sérgio Guimarães Villaça. NF emitida em 09/06/2026.

---

## 2. Evolução do cronograma

| Marco | Data Prevista | Data Realizada | Status |
|---|---|---|---|
| Kickoff OS-002 | 26/05/2026 | 26/05/2026 | ✅ |
| Azure Key Vault provisionado e integrado ao APIM | 29/05/2026 | 29/05/2026 | ✅ |
| OAuth 2.0 (Entra ID + APIM) funcional | 02/06/2026 | 02/06/2026 | ✅ |
| API Keys com controle granular configuradas | 03/06/2026 | 03/06/2026 | ✅ |
| Versionamento + ciclo de vida configurados | 04/06/2026 | 04/06/2026 | ✅ |
| CORS + validação de payload configurados | 05/06/2026 | 05/06/2026 | ✅ |
| Application Insights + dashboards configurados | 06/06/2026 | 06/06/2026 | ✅ |
| Alertas Azure Monitor configurados e validados | 06/06/2026 | 06/06/2026 | ✅ |
| Freeze de configuração (encerramento da sprint) | 06/06/2026 | 06/06/2026 | ✅ |
| Verificação técnica (Cézar Hiraki) + entrega formal ao cliente | 09/06/2026 | 09/06/2026 | ✅ |
| Apresentação de entrega ao cliente (call) | 08/06/2026 | 08/06/2026 | ✅ |
| Aceite formal do cliente (e-mail) | 09/06/2026 | 09/06/2026 | ✅ |

---

## 3. Status dos requisitos

| ID | Requisito | SP | Situação |
|---|---|---|---|
| RF-11 | Azure Key Vault integrado ao APIM | 13 | ✅ Entregue |
| RF-12 | OAuth 2.0 via Entra ID | 13 | ✅ Entregue |
| RF-13 | API Keys com controle granular | 8 | ✅ Entregue |
| RF-14 | Políticas de versionamento | 5 | ✅ Entregue |
| RF-15 | Políticas de ciclo de vida | 5 | ✅ Entregue |
| RF-16 | Monitoramento (App Insights + dashboards) | 8 | ✅ Entregue |
| RF-17 | Alertas automatizados (Azure Monitor) | 5 | ✅ Entregue |
| RF-18 | CORS + validação de payloads | 8 | ✅ Entregue |
| RF-19 | Homologação end-to-end | 8 | ✅ Entregue — apresentação 08/06; aceite 09/06 |
| Documentação, verificação e sessão de aceite | — | 5 | ✅ Concluído |
| **Total** | | **78** | **78 SP entregues / aceite formal recebido** |

---

## 4. Desvios e ocorrências

| # | Ocorrência | Data | Impacto | Tratamento |
|---|---|---|---|---|
| O-01 | Thresholds de alerta não fornecidos pelo cliente no início (risco R-08) | 26/05/2026 | Baixo | Valores padrão de mercado adotados como default; thresholds confirmados durante a execução |
| O-02 | Sessão de apresentação ao cliente realizada em 08/06/2026 (antecipada de 10/06) | 08/06/2026 | Nenhum | Verificação técnica concluída em 09/06; entrega realizada antes do prazo |

---

## 5. Situação dos riscos

| # | Risco | Status | Ocorreu? |
|---|---|---|---|
| R-07 | Permissões insuficientes no Entra ID para registrar App OAuth | ✅ Mitigado | Não — App Registration criada sem restrições |
| R-08 | Thresholds de alerta não fornecidos a tempo | ✅ Mitigado | Parcialmente — resolvido com valores padrão (O-01) |
| R-09 | Complexidade OAuth 2.0 excede estimativa | ✅ Mitigado | Não — executado dentro do prazo planejado |
| R-10 | Mudança de escopo na homologação end-to-end | ✅ Mitigado | Não ocorreu — aceite formal recebido sem solicitação de mudança de escopo |

---

## 6. Indicadores de desempenho

| Indicador | Resultado | Meta Org. |
|---|---|---|
| SP entregues vs. planejados | 78/78 = 100% | ≥ 90% |
| Desvio de prazo | 0 dias (entregue em 14 de 15 dias) | ≤ 10% |
| Change Requests | 0 | Referência |
| Defeitos identificados na verificação técnica | 0 | ≤ 5% dos itens verificados |
| % Conformidade GQA (auditoria parcial 04/06) | 100% | ≥ 90% |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 09/06/2026 | Abraão Oliveira | Versão inicial — relatório de acompanhamento da OS-002 até a entrega técnica |
| 1.1 | 10/06/2026 | Time de Melhoria Contínua | Fechamento: aceite formal registrado (09/06); todos os ⏳ atualizados para ✅; R-10 mitigado |
