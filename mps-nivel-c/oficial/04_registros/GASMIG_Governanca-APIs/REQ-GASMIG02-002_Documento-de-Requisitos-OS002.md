# Documento de Requisitos — Fundação Tecnológica GASMIG · OS-PARCELA-002

| Campo | Valor |
|---|---|
| **Documento** | REQ-GASMIG02-002 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-002 |
| **Cliente** | GASMIG — Companhia de Gás de Minas Gerais |
| **Versão** | 1.0 |
| **Data** | 26/05/2026 |
| **Responsáveis** | Abraão Oliveira (PO) / Cézar Hiraki (Tech Lead) |

---

## 1. Contexto e objetivo

Com a OS-PARCELA-001 entregue e aceita, a fundação base (APIM, workspaces, catálogo, segurança por IP e sandbox) está operacional. Esta OS completa a fundação com os componentes de segurança avançada, observabilidade e governança do ciclo de vida:

- **Segurança avançada:** secrets em Key Vault (eliminando valores sensíveis hard-coded), OAuth 2.0 para autenticação moderna e API Keys para machine-to-machine
- **Governança de ciclo de vida:** políticas de versionamento e lifecycle para que a GASMIG controle a evolução e descontinuação de APIs sem impacto nos consumidores
- **Observabilidade:** dashboards de volumetria/latência/erros e alertas automatizados para visibilidade operacional em tempo real
- **Homologação:** validação end-to-end de toda a fundação antes da entrada em operação plena

## 2. Partes interessadas

| Parte interessada | Necessidade principal |
|---|---|
| GASMIG — TI e Telecomunicação (Sérgio Villaça) | Fundação segura, observável e com ciclo de vida governado |
| GASMIG — Arquitetura de TI (Eduardo Yasuda, José Geraldo) | Implementação correta de OAuth 2.0, Key Vault e monitoramento Azure |
| GASMIG — Gestão (Murilo Morgado) | Dashboards de volumetria e alertas para visibilidade gerencial |
| ArcelorMittal / Usiminas | Autenticação moderna (OAuth 2.0 / API Keys) nos workspaces dedicados |

## 3. Visão geral da solução

Extensão da configuração Azure da OS-PARCELA-001, adicionando:
- **Azure Key Vault** integrado ao APIM para gestão centralizada de secrets
- **OAuth 2.0** via Entra ID registrado no APIM como provedor de identidade para APIs
- **Application Insights** integrado ao APIM para telemetria
- **Azure Monitor** com dashboards e regras de alerta configurados
- Políticas de CORS, validação de payloads e versioning nas APIs

Tudo dentro do tenant Azure GASMIG, sem desenvolvimento de software.

## 4. Requisitos funcionais

| ID | Requisito | Prioridade | Critérios de aceite |
|---|---|---|---|
| RF-11 | Como administrador de TI da GASMIG, quero que todos os secrets e credenciais do APIM sejam gerenciados pelo Azure Key Vault, para eliminar valores sensíveis hard-coded na configuração. | Alta | Azure Key Vault provisionado e integrado ao APIM; named values apontando para referências do Key Vault; nenhum secret hard-coded na configuração. |
| RF-12 | Como gestor de APIs da GASMIG, quero autenticação OAuth 2.0 configurada com controle granular por workspace e por API, para oferecer autenticação moderna e auditável aos consumidores. | Alta | Aplicação OAuth registrada no Entra ID; política de validação de JWT configurada no APIM; fluxo OAuth 2.0 end-to-end funcional (token → chamada API validada). |
| RF-13 | Como gestor de APIs da GASMIG, quero API Keys configuradas com controle granular por workspace e por API, para suportar integrações machine-to-machine sem dependência de fluxo OAuth. | Alta | API Keys configuradas por workspace e por API; acesso com chave válida funcional; acesso com chave inválida bloqueado (401). |
| RF-14 | Como gestor de APIs da GASMIG, quero políticas corporativas de versionamento de APIs configuradas, para que novas versões coexistam com versões anteriores sem quebrar consumidores existentes. | Média | Convenção de versionamento definida e aplicada (ex.: `/v1/`, `/v2/`); políticas de roteamento por versão configuradas no APIM. |
| RF-15 | Como gestor de APIs da GASMIG, quero políticas de ciclo de vida de APIs configuradas, para controlar os estados de cada API (preview, atual, depreciada, descontinuada) e notificar consumidores sobre mudanças. | Média | Estados de ciclo de vida definidos; processo de depreciação documentado; políticas de aviso de depreciação configuradas no portal/APIM. |
| RF-16 | Como time de TI da GASMIG, quero dashboards de monitoramento com volumetria, latência e erros por API e por cliente, para acompanhar a saúde da plataforma em tempo real. | Alta | Application Insights integrado ao APIM; dashboards configurados no Azure Monitor/Portal com métricas de requisições, latência (p50/p95) e erros por API e por workspace. |
| RF-17 | Como time de TI da GASMIG, quero alertas automatizados configurados para degradação de performance e indisponibilidade, para ser notificado proativamente antes de impacto nos consumidores. | Alta | Regras de alerta configuradas no Azure Monitor para: latência acima de threshold, taxa de erro acima de threshold e indisponibilidade do APIM; notificações ativas para destinatários GASMIG. |
| RF-18 | Como arquiteto de TI da GASMIG, quero ajuste fino das políticas de segurança (CORS e validação de payloads), para garantir que apenas origens e payloads autorizados sejam aceitos por cada API. | Média | Políticas CORS configuradas por API (origens permitidas definidas); validação de schema/payload configurada para as APIs existentes. |
| RF-19 | Como gestor do contrato GASMIG, quero que toda a fundação seja homologada end-to-end, para confirmar que todos os componentes (OS-001 + OS-002) funcionam de forma integrada antes da operação plena. | Alta | Sessão de homologação realizada com time técnico GASMIG; fluxo completo validado: autenticação → autorização → chamada API → monitoramento → alerta disparado; aceite formal registrado em ata. |

## 5. Requisitos não funcionais

| ID | Requisito não funcional | Critério |
|---|---|---|
| RNF-06 | Nenhum secret ou credencial sensível deve estar hard-coded na configuração do APIM. | Auditoria de configuração: 100% dos valores sensíveis referenciados via Azure Key Vault. |
| RNF-07 | A implementação OAuth 2.0 deve ser conforme RFC 6749 e utilizar Entra ID como IdP. | Fluxo OAuth 2.0 testado e conforme; JWT emitido pelo Entra ID validado corretamente pelo APIM. |
| RNF-08 | Dados de monitoramento retidos por no mínimo 30 dias. | Política de retenção do Application Insights configurada para ≥ 30 dias. |
| RNF-09 | Alertas disparados em no máximo 5 minutos após detecção de condição de degradação. | Frequência de avaliação das regras de alerta configurada em ≤ 5 minutos. |

## 6. Restrições e premissas

**Restrições:**
- Prazo máximo: 15 dias corridos a partir de 26/05/2026 (até 10/06/2026)
- Plataforma: exclusivamente Microsoft Azure (tenant GASMIG)
- Pagamento condicionado ao aceite formal após sessão de homologação

**Premissas:**
- Fundação base da OS-001 está operacional e acessível
- O Entra ID da GASMIG permite o registro das aplicações OAuth 2.0 necessárias
- Os thresholds de alerta (latência, erro) serão definidos em conjunto com o time GASMIG durante a execução
- Os destinatários das notificações de alerta serão fornecidos pelo time GASMIG

## 7. Validação dos requisitos

| Requisito/conjunto | Forma de validação | Data | Resultado |
|---|---|---|---|
| Escopo OS-002 (RF-11 a RF-19) | Aceite da OS-001 + início formal da OS-002; escopo já acordado em 29/04/2026 | 26/05/2026 | Validado — escopo em continuidade ao acordo original |
| Detalhamento técnico e critérios de aceite | Sessão de homologação end-to-end com time técnico GASMIG | ~10/06/2026 | A realizar |

## 8. Confirmação de entendimento e compromisso

| Envolvido | Papel | Confirmação | Data |
|---|---|---|---|
| Sérgio Guimarães Villaça | Gestor do Contrato — GASMIG | Escopo acordado em 29/04/2026; OS-002 iniciada após aceite da OS-001 | 26/05/2026 |
| Abraão Oliveira | Gerente de Projeto — Timeware | Compromisso da equipe assumido | 26/05/2026 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão Oliveira / Cézar Hiraki | Versão inicial — requisitos da OS-PARCELA-002 |
