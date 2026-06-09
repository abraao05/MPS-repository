# Registro de Gerência de Configuração — Fundação Tecnológica GASMIG

| Campo | Valor |
|---|---|
| **Documento** | GCO-GASMIG02-001 |
| **Projeto** | Fundação Tecnológica GASMIG — Governança de APIs GASMIG |
| **Cliente** | GASMIG — Companhia de Gás de Minas Gerais |
| **Versão** | 1.0 |
| **Data** | 09/06/2026 |
| **Responsável pela GCO** | Cézar Hiraki (Tech Lead / Arquiteto) |
| **Processo MPS-SW** | GCO (evidência de projeto) |

---

## 1. Objetivo

Identificar e controlar os itens de configuração do projeto, garantindo que as baselines sejam estabelecidas, rastreadas e protegidas contra alterações não autorizadas ao longo das duas OS que compõem a Fundação Tecnológica GASMIG.

---

## 2. Itens de configuração (ICs)

| ID | Item de configuração | Tipo | Local de armazenamento | Responsável |
|---|---|---|---|---|
| IC-01 | Scripts IaC OS-001 — Bicep/ARM (governança APIM, produtos, grupos, políticas globais, workspaces, rate limiting, throttling, SSO) | Código/configuração | Repositório IaC no Azure DevOps GASMIG | Cézar Hiraki |
| IC-02 | Scripts IaC OS-002 — Bicep/ARM (Key Vault, OAuth 2.0, API Keys, versionamento, ciclo de vida, Application Insights, alertas, CORS, payload validation) | Código/configuração | Repositório IaC no Azure DevOps GASMIG | Cézar Hiraki |
| IC-03 | Políticas globais do Azure API Management (XML) | Configuração Azure | Azure API Management — portal + exportado no IaC | Cézar Hiraki |
| IC-04 | Políticas de produtos (interno, externo, sandbox, workspaces ArcelorMittal e Usiminas) | Configuração Azure | Azure API Management — portal + IaC | Cézar Hiraki |
| IC-05 | Named values (referências ao Key Vault — OS-002) | Configuração Azure | Azure API Management — portal + IaC | Cézar Hiraki |
| IC-06 | App Registration OAuth 2.0 no Entra ID GASMIG | Configuração Azure | Microsoft Entra ID — documentado no PCP-GASMIG02-002 | Cézar Hiraki |
| IC-07 | Azure Key Vault — secrets, políticas de acesso e Managed Identity do APIM | Configuração Azure | Azure Key Vault — portal + IaC | Cézar Hiraki |
| IC-08 | Application Insights — logger do APIM, retenção e dashboards | Configuração Azure | Azure Application Insights + IaC | Fernando Oliveira |
| IC-09 | Regras de alerta e Action Group (Azure Monitor) | Configuração Azure | Azure Monitor — portal + IaC | Henry Komatsu |
| IC-10 | Documentação técnica do projeto (artefatos MPS — .md e .docx) | Documentação | Repositório MPS Timeware (GitHub) | Abraão Oliveira |

---

## 3. Baselines estabelecidas

| Baseline | Data | Conteúdo | Aprovação |
|---|---|---|---|
| Baseline OS-001 | 26/05/2026 | IC-01, IC-03, IC-04 (parcial — sem Key Vault e OAuth), IC-10 (documentação OS-001) | Aceite formal de Sérgio Guimarães Villaça — ATA-GASMIG02-002 + e-mail 26/05/2026 |
| Baseline OS-002 | 09/06/2026 | IC-01 a IC-10 completos (fundação integral) | Verificação técnica Cézar Hiraki 09/06/2026; aceite formal pendente — ATA-GASMIG02-003 |

---

## 4. Controle de versão da configuração

O controle de versão dos ICs técnicos (IC-01 a IC-09) é realizado no **repositório IaC no Azure DevOps GASMIG**:

| Aspecto | Decisão adotada |
|---|---|
| Estratégia de branch | `main` (produção) + feature branches por funcionalidade |
| Merge | Pull Request com aprovação obrigatória de Cézar Hiraki |
| Tag de release na baseline OS-001 | `v1.0.0` — estabelecida em 26/05/2026 |
| Tag de release na baseline OS-002 | `v2.0.0` — a ser estabelecida após aceite formal |
| Rastreabilidade de commits | Mensagens de commit referenciam o requisito correspondente (ex.: `RF-11: Key Vault integration`) |

A documentação MPS (IC-10) é controlada pelo repositório GitHub da Timeware.

---

## 5. Controle de mudanças

Mudanças nos itens de configuração após o estabelecimento de uma baseline seguem o fluxo:

1. Identificação da necessidade de mudança (pelo time técnico ou pelo cliente)
2. Avaliação de impacto por Cézar Hiraki (técnico) e Abraão Oliveira (prazo/custo)
3. Aprovação de Sérgio Villaça (GASMIG) para mudanças com impacto no cliente
4. Implementação via Pull Request no Azure DevOps com mensagem de commit rastreável
5. Atualização da documentação afetada e registro da mudança neste documento

---

## 6. Ocorrências de controle de configuração

| Data | Ocorrência | Impacto | Tratamento |
|---|---|---|---|
| 29/04/2026 | Início da configuração OS-001 no Azure GASMIG | — | Acesso provisionado conforme previsto; baseline inicial em construção |
| 14/05/2026 | Entrega técnica OS-001 ao cliente | IC-01, IC-03, IC-04 entregues | Revisão técnica e demonstração ao cliente |
| 26/05/2026 | Baseline OS-001 estabelecida | IC-01, IC-03, IC-04 congelados | Aceite formal + tag `v1.0.0` no Azure DevOps |
| 26/05/2026 | Início da configuração OS-002 sobre a baseline OS-001 | IC-02 e IC-05 a IC-09 em construção | Feature branches no Azure DevOps; IaC incremental sobre v1.0.0 |
| 09/06/2026 | Entrega técnica OS-002 ao cliente | IC-01 a IC-09 completos | Verificação técnica por Cézar Hiraki; apresentação ao cliente |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 09/06/2026 | Cézar Hiraki / Abraão Oliveira | Versão inicial — registro consolidado dos itens de configuração OS-001 e OS-002 |
