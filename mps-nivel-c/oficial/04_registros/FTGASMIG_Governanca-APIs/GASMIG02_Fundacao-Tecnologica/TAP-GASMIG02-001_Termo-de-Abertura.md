# Termo de Abertura do Projeto — Fundação Tecnológica GASMIG · OS-PARCELA-001

| Campo | Valor |
|---|---|
| **Documento** | TAP-GASMIG02-001 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-001 |
| **Cliente** | GASMIG — Companhia de Gás de Minas Gerais |
| **Contrato** | Governança de APIs GASMIG |
| **Versão** | 1.0 |
| **Data de abertura** | 29/04/2026 |
| **Gerente de Projeto** | Abraão Oliveira |

---

## 1. Objetivo do projeto

Configurar a fundação tecnológica de integração da GASMIG sobre a plataforma Microsoft Azure API Management (APIM), estabelecendo governança corporativa de APIs, controle de acesso por usuário, barreiras de segurança para tráfego interno e externo, ambiente de sandbox, catálogo corporativo e workspaces dedicados por cliente (ArcelorMittal e Usiminas). A entrega cria a base reutilizável que suportará todas as futuras integrações da GASMIG sem necessidade de reconfiguração da infraestrutura.

## 2. Escopo macro

Conforme OS-PARCELA-001 do contrato Governança de APIs GASMIG, autorizada formalmente em 29/04/2026.

- **Incluído:**
  - Configuração de governança corporativa de APIs no Azure API Management conforme padrão Microsoft e boas práticas internacionais
  - Gestão de controle de acesso por usuário com políticas de expiração e renovação de credenciais
  - Configuração de barreiras de segurança para acesso interno (rede corporativa GASMIG) e externo (parceiros e grandes clientes)
  - Preparação e configuração de ambiente de sandbox para testes e validações pré-produção
  - Configuração de catálogo corporativo de APIs com exibição padronizada para consumidores internos e externos
  - Criação e configuração de workspaces dedicados por cliente: ArcelorMittal e Usiminas
  - Configuração de políticas de rate limiting e throttling por workspace

- **Não incluído:**
  - Gestão de secrets e integração com Azure Key Vault (escopo OS-PARCELA-002)
  - Autenticação OAuth 2.0 e API Keys (escopo OS-PARCELA-002)
  - Versionamento e ciclo de vida de APIs (escopo OS-PARCELA-002)
  - Monitoramento, dashboards e alertas automatizados (escopo OS-PARCELA-002)
  - Desenvolvimento de APIs de negócio (escopo de projetos futuros)

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
| Kickoff — autorização formal (DE ACORDO) | 29/04/2026 |
| Discovery / Requisitos | Concluído durante pré-venda (jan–abr/2026) |
| Aprovação do Plano (baseline) | 30/04/2026 |
| Entrega OS-PARCELA-001 | 14/05/2026 |
| Sessão de aceite com time técnico GASMIG | ~14/05/2026 |
| Início OS-PARCELA-002 | Após aceite da OS-PARCELA-001 |

## 6. Agenda das próximas atividades

- Emissão formal das OS pela GASMIG (prevista até 30/04/2026)
- Configuração do ambiente Azure API Management — governança e estrutura base
- Configuração de workspaces ArcelorMittal e Usiminas
- Configuração de sandbox e catálogo corporativo
- Configuração de controle de acesso, barreiras de segurança, rate limiting e throttling
- Sessão de apresentação e validação com o time técnico GASMIG

## 7. Premissas e restrições iniciais

**Premissas:**
- A GASMIG dispõe de subscription Azure ativa e concede acesso ao time Timeware para configuração
- O tenant Entra ID da GASMIG suporta SSO/SAML para o portal do Azure API Management
- As definições técnicas de nomenclatura, ambientes e padrões Azure serão alinhadas no início da execução
- Os workspaces ArcelorMittal e Usiminas são os únicos clientes no escopo desta OS

**Restrições:**
- Prazo máximo: 15 dias corridos a partir de 29/04/2026 (entrega até 14/05/2026)
- Todo o trabalho é realizado exclusivamente dentro da plataforma Microsoft Azure
- Pagamento condicionado ao aceite formal da GASMIG após sessão de validação

---

## Registro de abertura

| Reunião de kickoff realizada em | Ref. da autorização |
|---|---|
| 29/04/2026 | E-mail de Sérgio Guimarães Villaça, 29/04/2026 às 15:45 — DE ACORDO formal para OS-PARCELA-001 e OS-PARCELA-002 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 29/04/2026 | Abraão Oliveira | Versão inicial — abertura do projeto |
