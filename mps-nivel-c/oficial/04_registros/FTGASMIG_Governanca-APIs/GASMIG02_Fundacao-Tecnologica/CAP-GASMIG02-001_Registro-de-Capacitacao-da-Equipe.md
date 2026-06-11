# Registro de Capacitação da Equipe — GASMIG Governança de APIs

| Campo | Valor |
|---|---|
| **Documento** | CAP-GASMIG02-001 — Registro de Capacitação da Equipe |
| **Versão** | 1.1 |
| **Data** | 11/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Fundação Tecnológica GASMIG — Governança de APIs (OS-001 / OS-002) |
| **Aprovação** | Gerente de Projeto |

---

## 1. Objetivo

Registrar a composição, qualificações e preparo da equipe técnica alocada para a configuração da plataforma de governança de APIs da Fundação Tecnológica GASMIG.

## 2. Equipe alocada

| Membro | Papel | Nível |
|---|---|---|
| Cézar Hiraki | Tech Lead / Arquiteto de Soluções | Sênior |
| Fernando Oliveira | Engenheiro de Configuração | Pleno |
| Henry Komatsu | Engenheiro de Configuração | Pleno |

## 3. Qualificações e experiência relevante

### Cézar Hiraki — Tech Lead / Arquiteto

- Experiência em arquitetura de plataformas Azure: API Management, Key Vault, Microsoft Entra ID, Azure Monitor e Application Insights
- Responsável pela definição das diretrizes técnicas, revisão de políticas APIM e aprovação dos critérios de aceite em ambas as OS
- Atuou como ponto de contato técnico com a equipe da Fundação Tecnológica GASMIG ao longo de todo o engajamento

### Fernando Oliveira — Engenheiro de Configuração

- Experiência em configuração de Azure API Management: produtos, subscrições, Named Values e políticas XML
- Participou de engajamentos anteriores envolvendo integração OAuth 2.0 e Microsoft Entra ID
- Na OS-002: responsável pelos RFs 11, 13, 16 e 18 (ambientes de homologação/produção, Named Values, monitoramento e segurança)

### Henry Komatsu — Engenheiro de Configuração

- Experiência em Azure Monitor, Application Insights e pipelines IaC (Bicep/ARM)
- Familiarizado com políticas JWT e rate-limiting em gateways de API
- Na OS-002: responsável pelos RFs 12, 14, 15 e 17 (validação JWT, rate limiting, Application Insights e Workspaces)

## 4. Preparação para o engajamento

### OS-001

Antes do início das atividades de configuração, a equipe realizou:

| Atividade | Responsável | Concluído em |
|---|---|---|
| Leitura e alinhamento do TAP-GASMIG02-001 (escopo, restrições, ambiente) | Todos | 10/04/2026 |
| Revisão do ambiente Azure do cliente (tenant, resource groups, permissões) | Cézar Hiraki | 12/04/2026 |
| Configuração de acesso ao portal Azure da FTGASMIG | Fernando Oliveira | 12/04/2026 |
| Onboarding no padrão de documentação Timeware para o projeto | Henry Komatsu | 14/04/2026 |

### OS-002

| Atividade | Responsável | Concluído em |
|---|---|---|
| Revisão do PCP-GASMIG02-002 (design de ambientes e OAuth 2.0) | Todos | 27/05/2026 |
| Alinhamento de credenciais Entra ID e apps registrados no tenant | Cézar Hiraki | 28/05/2026 |
| Validação das permissões necessárias para deploy em produção | Fernando Oliveira | 28/05/2026 |

## 5. Observações

Toda a equipe já havia atuado em projetos Azure anteriores da Timeware, dispensando treinamento formal específico para as tecnologias core do engajamento. As atividades de preparo foram focadas no contexto e nas particularidades do ambiente da Fundação Tecnológica GASMIG.

O Plano de Capacitação Organizacional aplicável a esta equipe está registrado em `PLA-CAP-001 v1.1`.

## 6. Registros de treinamento MPS

Confirmação de que os membros da equipe alocada para este projeto estão cobertos pelos registros de treinamento organizacional conforme PLA-CAP-001 v1.1:

| Membro | Papel | Registros de treinamento MPS |
|---|---|---|
| Cézar Hiraki | Tech Lead / Arquiteto | REG-CAP-001 (dez/2024); REG-CAP-007 (jan/2026); REG-CAP-008 (fev/2026); REG-CAP-009 (mar/2026) |
| Fernando Oliveira | Engenheiro de Configuração | REG-CAP-001 (dez/2024); REG-CAP-001B (jan/2025); REG-CAP-002 (mar/2025); REG-CAP-005 (mai/2026) |
| Henry Komatsu | Engenheiro de Configuração | REG-CAP-001 (dez/2024); REG-CAP-002 (mar/2025); REG-CAP-005 (mai/2026) |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 30/05/2026 | Gerente de Projeto | Registro inicial de capacitação da equipe |
| 1.1 | 11/06/2026 | Time de Melhoria Contínua | Referência ao PLA-CAP-001 atualizada para v1.1; adicionada seção 6 com mapeamento dos registros de treinamento MPS de cada membro (REG-CAP-001 a REG-CAP-009) |
