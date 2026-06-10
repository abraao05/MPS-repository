# Termo de Encerramento — Fundação Tecnológica GASMIG · OS-PARCELA-002

| Campo | Valor |
|---|---|
| **Documento** | TAE-GASMIG02-002 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-002 |
| **Cliente** | GASMIG — Companhia de Gás de Minas Gerais |
| **Versão** | 1.0 |
| **Data de encerramento** | 09/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |

---

## 1. Resumo do projeto

A OS-PARCELA-002 completou a Fundação Tecnológica de Integração da GASMIG, adicionando gestão segura de secrets (Azure Key Vault), autenticação OAuth 2.0 via Entra ID, controle granular de API Keys, versionamento e ciclo de vida de APIs, monitoramento com Application Insights e Azure Monitor, alertas automatizados, validação de payload e CORS. O projeto foi executado em 14 dias corridos (26/05–09/06/2026), dentro do prazo contratual de 15 dias, pela equipe Timeware, sem change requests.

## 2. Entregas realizadas

| Entrega | Situação | Observação |
|---|---|---|
| Azure Key Vault integrado ao APIM (Managed Identity, sem secrets hard-coded) | ✅ Concluída | Named values como Key Vault references; auditoria sem hard-codes |
| OAuth 2.0 via Entra ID — fluxo completo (App Registration, validate-jwt, smoke checks) | ✅ Concluída | Token válido aceito (200); sem token ou token inválido rejeitado (401) |
| API Keys com controle granular por workspace e por API | ✅ Concluída | Smoke checks de chave válida/inválida executados |
| Políticas de versionamento (APIM Versions e Revisions) | ✅ Concluída | URLs de versão criadas; roteamento correto |
| Políticas de ciclo de vida e deprecation header | ✅ Concluída | Estados de ciclo de vida configurados e aplicados |
| Application Insights integrado — dashboards de volumetria, latência e erros | ✅ Concluída | Telemetria visível; dashboards configurados; retenção ≥ 30 dias |
| Alertas Azure Monitor com Action Group para o time GASMIG | ✅ Concluída | Regras de alerta ativas; teste de disparo confirmado |
| CORS e validação de payload configurados | ✅ Concluída | Smoke checks de origem bloqueada e payload inválido executados |
| Scripts IaC (Bicep/ARM) atualizados no Azure DevOps GASMIG | ✅ Concluída | Commits com histórico rastreável no repositório da GASMIG |

## 3. Escopo: planejado × realizado

| Dimensão | Planejado | Realizado |
|---|---|---|
| Escopo | RF-11 a RF-19 e RNF-06 a RNF-09 conforme REQ-GASMIG02-002 | 100% entregue conforme planejado; sem itens removidos |
| Prazo | 15 dias corridos (até 10/06/2026) | Entregue em 14 dias (09/06/2026) — 1 dia antes do marco |
| Change requests | — | Nenhum change request durante a execução |

## 4. Aceite do cliente

| Cliente / responsável | Aceite | Data | Ref. |
|---|---|---|---|
| Sérgio Guimarães Villaça — GASMIG | ✅ Aprovado | 09/06/2026 | E-mail Sérgio 09/06/2026 11:30 + ATA-GASMIG02-003 |

**Transcrição do aceite formal:**

> **De:** SÉRGIO GUIMARÃES VILLAÇA \<sergio.villaca@gasmig.com.br\>  
> **Para:** abraao.oliveira@timeware.com.br  
> **Data:** 09/06/2026 11:30  
>
> Prezados, bom dia!
>
> @abraao.oliveira, a entrega da fase 2 está aprovada.  
> Favor enviar a NF.
>
> Quaisquer dúvidas, estou à disposição.  
> Atenciosamente,

NF enviada por Abraão Oliveira em resposta no mesmo dia às 11:53.

## 5. Transição / sustentação

Com o encerramento desta OS, a Fundação Tecnológica GASMIG está completamente operacional. O ambiente Azure API Management — com governança, segurança, monitoramento e automação IaC — passa ao controle da GASMIG (TI — Sérgio Villaça) a partir do aceite.

Toda a documentação técnica (design, IaC, planos de V&V, registros de verificação) está disponível no repositório Azure DevOps da GASMIG e no repositório MPS da Timeware. A fundação está pronta para receber as futuras APIs de negócio da GASMIG.

## 6. Lições aprendidas

Registradas em `LI-GASMIG02-001` — seção de lições da OS-002.

---

## Registro de encerramento

| Aceite formal em | Ref. |
|---|---|
| 09/06/2026 | E-mail Sérgio Villaça 09/06/2026 11:30 — "a entrega da fase 2 está aprovada"; NF encaminhada em 09/06/2026 11:53 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 09/06/2026 | Abraão Oliveira | Versão inicial — encerramento formal da OS-PARCELA-002 |
