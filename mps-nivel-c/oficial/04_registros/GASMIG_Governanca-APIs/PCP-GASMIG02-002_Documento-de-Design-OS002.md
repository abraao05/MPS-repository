# Documento de Design — Fundação Tecnológica GASMIG · OS-PARCELA-002

| Campo | Valor |
|---|---|
| **Documento** | PCP-GASMIG02-002 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-002 |
| **Versão** | 1.0 |
| **Data** | 26/05/2026 |
| **Responsáveis** | Cézar Hiraki (Tech Lead / Arquiteto) / Abraão Oliveira (GP/PO) |

---

## 1. Visão geral da solução

Esta OS estende a arquitetura entregue na OS-PARCELA-001. Os novos componentes se integram à instância APIM existente sem alteração estrutural dos workspaces ou produtos já configurados. O resultado final é a fundação completa: segura, observável e com ciclo de vida governado.

## 2. Design técnico (arquitetura)

### 2.1. Arquitetura estendida

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Microsoft Azure (Tenant GASMIG)                  │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │              Azure API Management (APIM) — OS-001 + OS-002   │  │
│  │                                                              │  │
│  │  ┌──────────────────────────────────────────────────────┐   │  │
│  │  │           Camada de Políticas Globais (OS-001)        │   │  │
│  │  │  + OAuth 2.0 JWT validation  + CORS  + Payload Validation│  │  │
│  │  └──────────────────────────────────────────────────────┘   │  │
│  │                                                              │  │
│  │  ┌──────────────────┐  ┌──────────────────────────────┐    │  │
│  │  │  Named Values     │  │  Policy Fragments             │    │  │
│  │  │  → Key Vault refs │  │  pf-oauth, pf-cors,           │    │  │
│  │  │  (sem hard-code)  │  │  pf-payload-validation        │    │  │
│  │  └──────────────────┘  └──────────────────────────────┘    │  │
│  │                                                              │  │
│  │  Workspaces ws-arcelormittal / ws-usiminas (OS-001)          │  │
│  │  + OAuth 2.0 e API Keys granulares por workspace             │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  ┌─────────────────────┐   ┌──────────────────────────────────┐   │
│  │  Azure Key Vault     │   │  Microsoft Entra ID              │   │
│  │  (secrets, API Keys, │   │  App Registration (OAuth 2.0)    │   │
│  │   connection strings)│   │  → JWT tokens para APIM          │   │
│  └─────────────────────┘   └──────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  Observabilidade                                             │  │
│  │  Application Insights ──► APIM (telemetria nativa)          │  │
│  │  Azure Monitor ──► Dashboards + Regras de Alerta            │  │
│  └─────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2. Novos componentes e integrações

**Azure Key Vault (RF-11):**
- Key Vault provisionado no mesmo resource group do APIM
- Named values do APIM migrados para referências do Key Vault (tipo `Key Vault reference`)
- Managed Identity do APIM com acesso de leitura ao Key Vault
- Secrets: connection strings, chaves de integração, valores sensíveis que antes eram named values diretos

**OAuth 2.0 via Entra ID (RF-12):**
- App Registration criada no Entra ID GASMIG (escopo: APIM)
- Política `validate-jwt` configurada no APIM referenciando o Entra ID como IdP
- Fluxo: consumidor obtém token no Entra ID → envia no header `Authorization: Bearer <token>` → APIM valida e autoriza
- Controle granular: política aplicada por workspace e por API conforme necessidade

**API Keys (RF-13):**
- Subscription keys do APIM já existiam na OS-001; esta OS adiciona controle granular por API (além de por produto/workspace)
- Política de verificação de chave aplicável em nível de operação específica quando necessário
- Coexistência com OAuth 2.0: cada API pode exigir OAuth, API Key, ou ambos (defense in depth)

**Versionamento (RF-14):**
- Convenção de versionamento adotada: path-based (`/v1/`, `/v2/`)
- Revisões de API (minor changes) via APIM Revisions — sem impacto na URL de consumo
- Versões (breaking changes) via APIM Versions — URLs distintas, coexistência controlada
- Política de deprecation header configurada para versões em fim de vida

**Ciclo de vida (RF-15):**
- Estados definidos: **Preview → Current → Deprecated → Retired**
- Processo documentado: mudança de estado comunicada via portal do desenvolvedor + email aos subscritores afetados
- Política de aviso (`set-header`) adicionada às APIs em estado Deprecated

**Application Insights + Dashboards (RF-16):**
- Application Insights provisionado e integrado ao APIM (logger nativo)
- Telemetria coletada: todas as requisições — método, URL, status, latência, workspace de origem
- Dashboards no Azure Portal configurados:
  - Volumetria por API e por workspace (últimas 24h, 7d, 30d)
  - Latência p50 e p95 por API
  - Taxa de erros (4xx, 5xx) por API e por cliente
  - Top 10 APIs por volume

**Alertas automatizados (RF-17):**
- Regras de alerta no Azure Monitor:
  - Latência p95 > threshold definido com GASMIG → alerta crítico
  - Taxa de erro 5xx > threshold → alerta crítico
  - Taxa de erro 4xx > threshold → alerta de atenção
  - Indisponibilidade do APIM (health check falha) → alerta crítico
- Action Group configurado com destinatários GASMIG (e-mail / Teams webhook)
- Frequência de avaliação: 5 minutos (atende RNF-09)

**CORS e validação de payloads (RF-18):**
- Política CORS configurada por API: origens permitidas definidas por ambiente (interno/externo)
- Política `validate-content` para validação de schema JSON/XML em APIs que recebem payload
- Rejeição de payloads malformados com resposta 400 antes de atingir o backend

### 2.3. Decisões de design

| Decisão | Alternativas consideradas | Escolha e justificativa | RAD |
|---|---|---|---|
| Key Vault: Managed Identity vs. Service Principal | (A) Managed Identity do APIM; (B) Service Principal com certificado | **A — Managed Identity.** Sem rotação manual de credenciais; nativa do Azure; alinhada às boas práticas de segurança Microsoft. | — |
| OAuth 2.0: validate-jwt policy vs. API Management OAuth server built-in | (A) Política `validate-jwt` referenciando Entra ID; (B) Servidor OAuth built-in do APIM | **A — validate-jwt.** Mais flexível, suporta múltiplos IdPs futuros, Entra ID como IdP corporativo já existente. | — |
| Versionamento: path-based vs. header-based vs. query-based | (A) Path (`/v1/`); (B) Header (`api-version`); (C) Query param | **A — Path-based.** Mais explícito para consumidores, mais fácil de documentar no catálogo, padrão adotado pela maioria dos grandes fornecedores de API. | — |
| Monitoramento: Application Insights nativo vs. stack externa (Datadog, Grafana) | (A) Application Insights + Azure Monitor; (B) Stack externa | **A — Application Insights/Azure Monitor.** Integração nativa com APIM, sem custo adicional de licenciamento, dentro do ecossistema Azure já adotado pela GASMIG. | — |

## 3. Design de produto (UX/UI)

**Não aplicável.** Projeto de configuração de ferramenta, sem desenvolvimento de interface. Ver ADAP-GASMIG02-002.

## 4. Rastreabilidade requisito → design

| Requisito (ID) | Elemento de design |
|---|---|
| RF-11 — Azure Key Vault | Key Vault + Managed Identity APIM; named values como Key Vault references |
| RF-12 — OAuth 2.0 | App Registration Entra ID; política `validate-jwt` por workspace/API |
| RF-13 — API Keys granulares | Política de subscription key por operação; coexistência com OAuth |
| RF-14 — Versionamento | APIM Versions (path-based `/v1/`, `/v2/`); APIM Revisions para minor changes |
| RF-15 — Ciclo de vida | Estados de API no APIM; política de deprecation header; comunicação via portal |
| RF-16 — Monitoramento / dashboards | Application Insights logger; dashboards Azure Monitor (volumetria, latência, erros) |
| RF-17 — Alertas automatizados | Regras de alerta Azure Monitor; Action Group com destinatários GASMIG |
| RF-18 — CORS + payload validation | Política CORS por API; política `validate-content` para payloads |
| RF-19 — Homologação end-to-end | Sessão de homologação cobrindo RF-11 a RF-18 + toda a OS-001 |
| RNF-06 — Sem secrets hard-coded | 100% named values como Key Vault references |
| RNF-07 — OAuth 2.0 conforme RFC 6749 | validate-jwt com Entra ID como IdP conforme padrão |
| RNF-08 — Retenção 30 dias | Política de retenção Application Insights ≥ 30 dias |
| RNF-09 — Alertas em ≤ 5 min | Frequência de avaliação das regras: 5 minutos |

## 5. Verificação técnica do design (PCP 2)

Cézar Hiraki realizará a verificação técnica em 09/06/2026, com foco em:
- Key Vault: Managed Identity configurada corretamente; nenhum secret hard-coded
- OAuth 2.0: fluxo end-to-end funcional; validate-jwt configurada
- Dashboards e alertas: métricas corretas, thresholds acordados com GASMIG
- CORS e payload validation: políticas aplicadas e testadas

| Item verificado | Verificador | Resultado | Data |
|---|---|---|---|
| Azure Key Vault + Managed Identity APIM | Cézar Hiraki | A verificar | 09/06/2026 |
| OAuth 2.0 end-to-end (token → API validada) | Cézar Hiraki | A verificar | 09/06/2026 |
| Dashboards e regras de alerta | Cézar Hiraki | A verificar | 09/06/2026 |
| CORS e validação de payload | Cézar Hiraki | A verificar | 09/06/2026 |
| Scripts IaC atualizados no Azure DevOps | Cézar Hiraki | A verificar | 09/06/2026 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 26/05/2026 | Cézar Hiraki / Abraão Oliveira | Versão inicial — design da OS-PARCELA-002 |
