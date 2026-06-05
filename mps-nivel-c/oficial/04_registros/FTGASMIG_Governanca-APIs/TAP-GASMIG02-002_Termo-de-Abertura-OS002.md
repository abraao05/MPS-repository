# Termo de Abertura do Projeto — Fundação Tecnológica GASMIG · OS-PARCELA-002

| Campo | Valor |
|---|---|
| **Documento** | TAP-GASMIG02-002 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-002 |
| **Cliente** | GASMIG — Companhia de Gás de Minas Gerais |
| **Contrato** | Governança de APIs GASMIG |
| **Versão** | 1.0 |
| **Data de abertura** | 26/05/2026 |
| **Gerente de Projeto** | Abraão Oliveira |

---

## 1. Objetivo do projeto

Completar a Fundação Tecnológica de Integração da GASMIG com os componentes de segurança avançada, automação e observabilidade: gestão de secrets via Azure Key Vault, autenticação OAuth 2.0 e API Keys, versionamento e ciclo de vida de APIs, monitoramento com dashboards, alertas automatizados, ajuste fino de políticas de segurança (CORS e validação de payloads) e homologação end-to-end de toda a plataforma. Ao final desta OS, a fundação estará completa e operacional para suportar qualquer API futura da GASMIG.

## 2. Escopo macro

Conforme OS-PARCELA-002 do contrato Governança de APIs GASMIG, iniciada após aceite formal da OS-PARCELA-001 em 26/05/2026.

- **Incluído:**
  - Configuração de gestão de secrets e credenciais integrada ao Azure Key Vault
  - Implementação de autenticação OAuth 2.0 com controle granular por workspace e por API
  - Configuração de API Keys com controle granular por workspace e por API
  - Configuração de políticas corporativas de versionamento de APIs
  - Configuração de políticas de ciclo de vida de APIs
  - Configuração de monitoramento nativo com dashboards de volumetria, latência e erros por API e por cliente
  - Configuração de alertas automatizados para degradação de performance e indisponibilidade
  - Ajuste fino de políticas de segurança: CORS e validação de payloads
  - Homologação completa end-to-end de todas as configurações da fundação

- **Não incluído:**
  - Desenvolvimento de APIs de negócio (projetos futuros que utilizarão a fundação)
  - Alterações nos workspaces ou produtos configurados na OS-PARCELA-001 (exceto ajustes finos de segurança previstos no escopo)

## 3. Partes interessadas

| Parte interessada | Papel | Contato |
|---|---|---|
| Sérgio Guimarães Villaça | Gestor do Contrato — TI e Telecomunicação / GASMIG | sergio.villaca@gasmig.com.br |
| Eduardo Andrade Yasuda | Arquiteto / Tech Lead Técnico — GASMIG | eduardo.yasuda@gasmig.com.br |
| José Geraldo Veloso Moreira | Arquiteto / Tech Lead Técnico — GASMIG | jose.moreira@gasmig.com.br |
| Murilo Barboza Morgado | Stakeholder — GASMIG | murilo.morgado@gasmig.com.br |
| Elizabeth Luiza Maynarte de Oliveira | Representante GASMIG | elizabeth.oliveira@gasmig.com.br |

## 4. Equipe do projeto

| Papel | Responsável |
|---|---|
| Gerente de Projeto / Product Owner | Abraão Oliveira |
| Tech Lead / Arquiteto | Cézar Hiraki |
| Engenheiro Azure (configuração) | Fernando Oliveira |
| Engenheiro Azure (configuração) | João Victor Cruz Silva |
| Gerência de Configuração (GCO) | Cézar Hiraki |
| Responsável por Medição | Abraão Oliveira |
| Responsável por GQA | A definir |

## 5. Macroplanejamento (datas-alvo)

| Marco | Data-alvo |
|---|---|
| Kickoff — início OS-PARCELA-002 | 26/05/2026 |
| Azure Key Vault + OAuth 2.0 + API Keys | 01/06/2026 |
| Versionamento, ciclo de vida, CORS, payload validation | 06/06/2026 |
| Monitoramento (Application Insights + dashboards) + alertas | 09/06/2026 |
| Homologação end-to-end | 10/06/2026 |
| Sessão de aceite com time técnico GASMIG | ~10/06/2026 |
| Encerramento OS-PARCELA-002 | 10/06/2026 |

## 6. Agenda das próximas atividades

- Configuração do Azure Key Vault e integração com named values do APIM
- Implementação de OAuth 2.0 (registro de aplicações no Entra ID, políticas JWT no APIM)
- Configuração de API Keys com controle granular
- Definição e implementação das políticas de versionamento e ciclo de vida
- Integração com Application Insights para monitoramento
- Configuração de dashboards e alertas no Azure Monitor
- Ajuste fino de políticas CORS e validação de schemas/payloads
- Homologação end-to-end de toda a fundação
- Sessão de aceite com o time técnico GASMIG

## 7. Premissas e restrições iniciais

**Premissas:**
- A OS-PARCELA-001 foi entregue e aceita — fundação base operacional disponível
- A subscription Azure GASMIG mantém os acessos já provisionados na OS-001
- O Entra ID da GASMIG suporta o registro das aplicações OAuth 2.0 necessárias
- Os thresholds de monitoramento e os critérios de alerta serão definidos em conjunto com o time GASMIG durante a execução

**Restrições:**
- Prazo máximo: 15 dias corridos a partir de 26/05/2026 (entrega até 10/06/2026)
- Todo o trabalho é realizado exclusivamente dentro da plataforma Microsoft Azure
- Pagamento condicionado ao aceite formal da sessão de homologação end-to-end

---

## Registro de abertura

| Kickoff iniciado em | Ref. |
|---|---|
| 26/05/2026 | TAE-GASMIG02-001 — encerramento OS-001 / aceite e-mail Sérgio 26/05/2026; ATA-GASMIG02-002 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão Oliveira | Versão inicial — abertura da OS-PARCELA-002 |
