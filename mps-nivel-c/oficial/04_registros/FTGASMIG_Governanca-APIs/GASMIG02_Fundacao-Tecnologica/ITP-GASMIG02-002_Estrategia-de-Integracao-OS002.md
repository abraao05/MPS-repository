# Estratégia de Integração — Fundação Tecnológica GASMIG · OS-PARCELA-002

| Campo | Valor |
|---|---|
| **Documento** | ITP-GASMIG02-002 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-002 |
| **Cliente** | GASMIG — Companhia de Gás de Minas Gerais |
| **Contrato** | Governança de APIs GASMIG |
| **Versão** | 1.0 |
| **Data** | 09/06/2026 |
| **Responsável** | Cézar Hiraki (Tech Lead / Arquiteto) |
| **Processo MPS-SW** | ITP (evidência de projeto) |

---

## 1. Contexto

A OS-PARCELA-001 estabeleceu a fundação base do Azure API Management sem integrações externas além do SSO via Entra ID (catalogado no PCP-GASMIG02-001 e adaptado conforme ADAP-GASMIG02-001). A OS-PARCELA-002 introduz três integrações entre serviços Azure que ampliam a segurança e a observabilidade da plataforma:

| Integração | Serviços envolvidos | Finalidade |
|---|---|---|
| APIM ↔ Azure Key Vault | Azure API Management + Azure Key Vault | Gestão centralizada de secrets e credenciais; eliminação de valores sensíveis hard-coded |
| Entra ID → APIM (OAuth 2.0) | Azure API Management + Microsoft Entra ID | Autenticação moderna via tokens JWT emitidos pelo Entra ID |
| APIM → Application Insights / Azure Monitor | Azure API Management + Application Insights + Azure Monitor | Telemetria de uso, dashboards e alertas de degradação |

A estratégia de integração é 100% dentro do ecossistema Microsoft Azure (tenant GASMIG), sem desenvolvimento de código customizado ou chamadas a serviços externos.

---

## 2. Componentes integrados

### 2.1 Integração APIM ↔ Azure Key Vault (RF-11 / RNF-06)

| Aspecto | Decisão |
|---|---|
| **Tipo de integração** | Azure Managed Identity — o APIM acessa o Key Vault sem credenciais explícitas |
| **Mecanismo** | Named values no APIM configurados como referências ao Key Vault (tipo "Key Vault Reference") |
| **Escopo** | Todos os named values que contêm valores sensíveis (chaves de assinatura, tokens de acesso a backends) |
| **Dependência técnica** | APIM deve ter System-Assigned Managed Identity habilitada; Key Vault deve conceder permissão `get secret` à identity do APIM |
| **Critério de aceite** | Auditoria de named values: 0 valores sensíveis em texto plano; referências Key Vault resolvidas corretamente em ambiente produtivo |

### 2.2 Integração Entra ID → APIM (OAuth 2.0) (RF-12 / RNF-07)

| Aspecto | Decisão |
|---|---|
| **Tipo de integração** | Token-based (JWT Bearer) — cliente obtém token no Entra ID e usa nas chamadas ao APIM |
| **Mecanismo** | Política `validate-jwt` nas operações/produtos configurados; App Registration no Entra ID com audience definido |
| **Escopo** | APIs e produtos selecionados que exigem autenticação moderna; compatibilidade mantida com API Keys para integração machine-to-machine |
| **Dependência técnica** | Entra ID da GASMIG permite App Registration com as permissões necessárias; client secret da App Registration armazenado no Key Vault (integração 2.1 é pré-requisito) |
| **Critério de aceite** | Smoke check: token válido → 200; sem token → 401; token inválido/expirado → 401 |

### 2.3 Integração APIM → Application Insights / Azure Monitor (RF-16, RF-17 / RNF-08, RNF-09)

| Aspecto | Decisão |
|---|---|
| **Tipo de integração** | Logger nativo do APIM integrado ao Application Insights via Connection String |
| **Mecanismo** | Logger do APIM configurado apontando para o Application Insights; dashboards e alertas configurados no Azure Monitor usando as métricas do AI como fonte |
| **Escopo** | Todas as APIs e operações do APIM (telemetria global); dashboards de volumetria/latência/erros; alertas por condição de degradação com Action Group para o time GASMIG |
| **Dependência técnica** | Application Insights criado no mesmo resource group que o APIM; Connection String do AI configurada no Logger do APIM |
| **Critério de aceite** | Dashboards com dados reais populados visíveis no Azure Monitor; teste de disparo de alerta recebido em ≤ 5 minutos (RNF-09); retenção ≥ 30 dias configurada (RNF-08) |

---

## 3. Ordem de integração e dependências

A ordem de execução das integrações foi definida para minimizar retrabalho e dependências em cascata:

| Etapa | Integração / componente | Dependência |
|---|---|---|
| 1 | Key Vault (IC-07) | Nenhuma — base para secrets subsequentes |
| 2 | OAuth 2.0 via Entra ID (RF-12) | Key Vault (client secret da App Registration armazenado no KV) |
| 3 | API Keys granulares (RF-13) | Independente — configuração paralela ao OAuth |
| 4 | Application Insights + Dashboards (RF-16) | Independente dos itens anteriores |
| 5 | Alertas Azure Monitor (RF-17) | Application Insights (usa as métricas do AI como trigger) |
| 6 | CORS + Validação de payload (RF-18) | Independente — ajuste fino de políticas APIM |
| 7 | Homologação end-to-end (RF-19) | Todos os itens anteriores concluídos |

---

## 4. Integração com a fundação OS-001

Os componentes da OS-002 se integram sobre a base já operacional da OS-001 sem alterar sua estrutura:

| Componente OS-001 | Modificação pela OS-002 |
|---|---|
| Named values (credenciais) | Convertidos de texto plano para Key Vault References |
| Produtos e subscriptions | Adição de política `validate-jwt` onde aplicável; demais políticas preservadas |
| Portal do desenvolvedor (catálogo) | Nenhuma alteração — continua com SSO via Entra ID da OS-001 |
| Workspaces ArcelorMittal e Usiminas | Rate limiting e throttling da OS-001 mantidos; OAuth e API Keys adicionados por workspace |
| IaC (Bicep/ARM) no Azure DevOps | Atualizado com os novos recursos; versionamento incremental sobre a baseline OS-001 |

---

## 5. Rastreabilidade

| Requisito | Componente de integração | Verificação |
|---|---|---|
| RF-11 / RNF-06 | Key Vault + Managed Identity | VV-GASMIG02-002 §4 — checklist Key Vault |
| RF-12 / RNF-07 | Entra ID + validate-jwt | VV-GASMIG02-002 §4 — checklist OAuth 2.0 |
| RF-16 / RNF-08 | Application Insights + dashboards | VV-GASMIG02-002 §4 — checklist App Insights |
| RF-17 / RNF-09 | Azure Monitor + Action Group | VV-GASMIG02-002 §4 — checklist alertas |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 09/06/2026 | Cézar Hiraki / Abraão Oliveira | Versão inicial — estratégia de integração OS-002 (Key Vault, OAuth 2.0, Application Insights) |
