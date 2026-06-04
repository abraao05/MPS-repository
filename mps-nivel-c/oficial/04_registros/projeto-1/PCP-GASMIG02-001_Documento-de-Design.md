# Documento de Design — Fundação Tecnológica GASMIG · OS-PARCELA-001

| Campo | Valor |
|---|---|
| **Documento** | PCP-GASMIG02-001 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-001 |
| **Versão** | 1.0 |
| **Data** | 29/04/2026 |
| **Responsáveis** | Cézar Hiraki (Tech Lead / Arquiteto) / Abraão Oliveira (GP/PO) |

---

## 1. Visão geral da solução

A solução configura uma instância Azure API Management (APIM) como plataforma central de governança de APIs da GASMIG. A arquitetura estabelece uma fundação corporativa escalável: todos os requisitos de segurança, acesso, catalogação e isolamento por cliente são implementados como políticas e workspaces nativos do APIM, sem desenvolvimento de software customizado.

O design prioriza **reutilização** — políticas são definidas em fragmentos reutilizáveis; workspaces são isolados e parametrizáveis; a adição de novos clientes ou APIs não requer reconfiguração da base.

## 2. Design técnico (arquitetura)

### 2.1. Arquitetura

**Componentes principais:**

```
┌─────────────────────────────────────────────────────────────────┐
│                    Microsoft Azure (Tenant GASMIG)              │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Azure API Management (APIM)                 │  │
│  │                                                          │  │
│  │  ┌─────────────────┐    ┌──────────────────────────┐    │  │
│  │  │  Gateway Externo │    │    Portal do             │    │  │
│  │  │  (modo público)  │    │  Desenvolvedor (Catálogo) │    │  │
│  │  └────────┬────────┘    └──────────────────────────┘    │  │
│  │           │                                              │  │
│  │  ┌────────▼────────────────────────────────────────┐    │  │
│  │  │              Camada de Políticas Globais         │    │  │
│  │  │  (segurança, CORS, HTTPS enforced, rate base)    │    │  │
│  │  └────────────────────────────────────────────────-┘    │  │
│  │                                                          │  │
│  │  ┌──────────────────────────────────────────────────┐   │  │
│  │  │                   Produtos                        │   │  │
│  │  │  prod-interno │ prod-externo │ prod-sandbox       │   │  │
│  │  └──────────────────────────────────────────────────┘   │  │
│  │                                                          │  │
│  │  ┌─────────────────────┐  ┌─────────────────────────┐  │  │
│  │  │  Workspace           │  │  Workspace              │  │  │
│  │  │  ArcelorMittal       │  │  Usiminas               │  │  │
│  │  │  (APIs + políticas   │  │  (APIs + políticas      │  │  │
│  │  │   isoladas)          │  │   isoladas)             │  │  │
│  │  └─────────────────────┘  └─────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌──────────────────────┐   ┌──────────────────────────────┐  │
│  │  Microsoft Entra ID  │   │  Azure DevOps GASMIG         │  │
│  │  (SSO / SAML para    │   │  (repositório IaC —          │  │
│  │   portal do dev.)    │   │   scripts Bicep/ARM)         │  │
│  └──────────────────────┘   └──────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘

Consumidores externos:                     Consumidores internos:
  ArcelorMittal ──► ws-arcelormittal         Equipe GASMIG ──► prod-interno
  Usiminas      ──► ws-usiminas              (rede corporativa GASMIG)
  Sandbox       ──► prod-sandbox
```

**Camadas da arquitetura:**

| Camada | Componente | Responsabilidade |
|---|---|---|
| Gateway | APIM Gateway (modo externo) | Recebe e roteia todas as requisições; aplica políticas globais |
| Governança | Políticas globais APIM | HTTPS enforced, headers de segurança, base de autenticação |
| Catálogo | Portal do Desenvolvedor | Exibição padronizada de APIs para consumidores internos e externos |
| Segregação | Produtos e grupos | Isolamento lógico por perfil de acesso (interno, externo, sandbox) |
| Isolamento por cliente | Workspaces (ArcelorMittal, Usiminas) | Segregação de APIs, credenciais e políticas por cliente |
| Segurança | Políticas de IP + subscription keys | Controle de acesso por origem (interno/externo) e por credencial |
| Controle de carga | Rate limiting + throttling (named values) | Proteção dos backends e SLA por cliente |
| Identidade | Entra ID (SAML) | SSO corporativo para o portal do desenvolvedor |
| Rastreabilidade | Azure DevOps — IaC scripts | Versionamento de toda a configuração em Bicep/ARM |

### 2.2. Modelo de dados

Este projeto não envolve banco de dados. Os principais objetos de configuração do APIM e suas relações são:

```
APIM Service
├── Named Values (variáveis globais — thresholds de rate, IPs internos, etc.)
├── Policy Fragments (fragmentos reutilizáveis de políticas)
├── Produtos
│   ├── prod-gasmig-interno       ──► APIs internas, acesso por rede GASMIG
│   ├── prod-gasmig-externo       ──► APIs externas gerais
│   └── prod-gasmig-sandbox       ──► APIs de exemplo para teste
├── Grupos
│   ├── grp-gasmig-interno        ──► Usuários rede corporativa GASMIG
│   ├── grp-gasmig-externo        ──► Parceiros e grandes clientes
│   └── grp-gasmig-administradores
├── Workspaces
│   ├── ws-arcelormittal
│   │   ├── APIs                  ──► (publicadas neste workspace)
│   │   ├── Produtos              ──► prod-ws-arcelormittal
│   │   └── Assinaturas           ──► subscription keys ArcelorMittal
│   └── ws-usiminas
│       ├── APIs                  ──► (publicadas neste workspace)
│       ├── Produtos              ──► prod-ws-usiminas
│       └── Assinaturas           ──► subscription keys Usiminas
└── Portal do Desenvolvedor
    ├── Layout e branding GASMIG
    ├── Visibilidade por grupo (interno/externo)
    └── SSO — Entra ID GASMIG (SAML 2.0)
```

### 2.3. Integrações

| Sistema | Tipo | Descrição |
|---|---|---|
| Microsoft Entra ID (tenant GASMIG) | SSO / Identidade | Autenticação de usuários no portal do desenvolvedor via SAML 2.0 delegada ao Entra ID corporativo da GASMIG |
| Rede corporativa GASMIG | Controle de acesso | IPs da rede interna GASMIG utilizados nas políticas de restrição de IP do produto `prod-gasmig-interno` |
| Azure DevOps GASMIG | Repositório IaC | Scripts Bicep/ARM gerados durante o projeto armazenados no Azure DevOps da GASMIG para rastreabilidade e reuso |
| APIs de backend (futuros projetos) | Gateway | O APIM atua como gateway reverso para APIs que serão publicadas em projetos subsequentes — a configuração desta OS provê a plataforma, não os backends |

### 2.4. Decisões de design

| Decisão | Alternativas consideradas | Escolha e justificativa | RAD |
|---|---|---|---|
| Instância APIM única vs. múltiplas instâncias | (A) APIM único centralizado; (B) APIM separado por cliente | **A — APIM único.** Reduz custo operacional, centraliza a governança e é o padrão Microsoft recomendado para o caso de uso. O isolamento por cliente é obtido nativamente via workspaces. | — |
| Isolamento por cliente: workspaces vs. produtos separados | (A) Workspaces dedicados; (B) Produtos com políticas diferenciadas | **A — Workspaces.** Workspaces oferecem isolamento de ciclo de vida (APIs, políticas, assinaturas independentes por cliente). Produtos compartilham o escopo global, sem isolamento real. | — |
| Sandbox: produto separado vs. instância APIM separada | (A) Produto `prod-sandbox` na mesma instância; (B) Instância APIM dedicada para sandbox | **A — Produto separado.** Custo-benefício superior; segregação suficiente para o objetivo de testes e validações pré-produção. Uma instância APIM separada seria justificada apenas para compliance ou SLA diferenciado, que não é o caso. | — |
| IaC: Bicep vs. ARM templates | (A) Bicep; (B) ARM JSON | **A — Bicep.** Sintaxe mais legível, suporte nativo da Microsoft, facilita manutenção futura pela equipe GASMIG. | — |
| Controle de carga: named values vs. valores hard-coded nas políticas | (A) Named values parametrizáveis; (B) Hard-coded nas políticas | **A — Named values.** Permite alterar thresholds de rate limiting e throttling sem editar as políticas diretamente. Alinhado ao requisito de escalabilidade (RNF-04). | — |

## 3. Design de produto (UX/UI)

**Não aplicável.** Conforme Registro de Adaptação (ADAP-GASMIG02-001), este é um projeto de infraestrutura e configuração cloud sem desenvolvimento de interface de usuário pela Timeware. O portal do desenvolvedor é um componente nativo do Azure API Management que será configurado (não desenvolvido).

## 4. Rastreabilidade requisito → design

| Requisito (ID) | Elemento de design |
|---|---|
| RF-01 — Governança corporativa APIM | Named values, policy fragments, políticas globais, estrutura de produtos e grupos |
| RF-02 — Controle de acesso / ciclo de vida | Configuração de TTL de subscription keys; políticas de renovação; grupos de usuários |
| RF-03 — Segurança acesso interno | Política de restrição de IP no `prod-gasmig-interno` — IPs da rede corporativa GASMIG |
| RF-04 — Segurança acesso externo | Política de validação de credenciais no `prod-gasmig-externo`; IP restrictions para parceiros |
| RF-05 — Sandbox | Produto `prod-gasmig-sandbox` com APIs de exemplo; isolamento lógico do ambiente produtivo |
| RF-06 — Catálogo corporativo | Portal do desenvolvedor configurado: layout GASMIG, visibilidade por grupo (interno/externo) |
| RF-07 — Workspace ArcelorMittal | `ws-arcelormittal`: produtos, assinaturas e políticas dedicadas |
| RF-08 — Workspace Usiminas | `ws-usiminas`: produtos, assinaturas e políticas dedicadas |
| RF-09 — Rate limiting por workspace | Named values `nv-ratelimit-arcelormittal`, `nv-ratelimit-usiminas`; policy fragment `pf-ratelimit` |
| RF-10 — Throttling por workspace | Named values `nv-throttle-arcelormittal`, `nv-throttle-usiminas`; policy fragment `pf-throttle` |
| RNF-01 — Boas práticas Microsoft | Arquitetura auditável vs. Azure Well-Architected Framework — Security e Operational Excellence pilars |
| RNF-02 — 100% Azure | Todos os recursos provisionados no Azure (tenant GASMIG) |
| RNF-03 — SSO SAML / Entra ID | Configuração do portal do desenvolvedor com provedor de identidade Entra ID (SAML 2.0) |
| RNF-04 — Escalabilidade | Named values parametrizáveis; workspaces independentes; políticas modulares por fragmento |
| RNF-05 — IaC / versionamento | Scripts Bicep/ARM exportados e armazenados no Azure DevOps GASMIG |

Matriz completa com casos de teste: ver `RASTR-GASMIG02-001_Matriz-de-Rastreabilidade.md`.

## 5. Avaliação do design (PCP 2)

Revisão por pares a ser realizada por Cézar Hiraki antes da sessão de aceite (~13/05/2026). O registro de revisão seguirá o template TPL-VV-002 e será arquivado nesta pasta.

| Item avaliado | Avaliador | Problema encontrado | Tratamento |
|---|---|---|---|
| Topologia APIM e estrutura de workspaces | Cézar Hiraki | — | A realizar em 13/05/2026 |
| Políticas de segurança (IP, credenciais) | Cézar Hiraki | — | A realizar em 13/05/2026 |
| Configuração SSO Entra ID | Cézar Hiraki | — | A realizar em 13/05/2026 |
| Scripts IaC (Bicep/ARM) | Cézar Hiraki | — | A realizar em 13/05/2026 |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 29/04/2026 | Cézar Hiraki / Abraão Oliveira | Versão inicial — design arquitetural da OS-PARCELA-001 |
