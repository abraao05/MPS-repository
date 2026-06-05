# Termo de Abertura do Projeto — SuperApp Fruki · Pacote Final 24

| Campo | Valor |
|---|---|
| **Documento** | TAP-FRUKI01-002 |
| **Projeto** | SuperApp Fruki — Pacote Final 24 |
| **Cliente** | Fruki Bebidas S.A. |
| **Contrato** | Pacote Final 24 |
| **Versão** | 1.0 |
| **Data de abertura** | 09/10/2024 |
| **Gerente de Projeto** | Abraão Oliveira |

---

## 1. Objetivo do projeto

Desenvolver novas funcionalidades no SuperApp Fruki como continuação do Pacote 1 (Módulo Metas/RV), entregando ao time comercial de campo: rastreabilidade de pedidos não alocados, visualização detalhada da Regra de Ouro (composição da RV), e execução digital de PDV com geolocalização e integração à API de Rota PDV. O Pacote Final 24 encerra o roadmap acordado pela Fruki para o ano de 2024, com entregas incrementais mensais.

## 2. Escopo macro

Conforme proposta "Pacote Final 24" apresentada em 26/09/2024 e aprovada por Leandro Lottermann em 09/10/2024.

- **Incluído:**
  - Módulo Pedidos Não Alocados: painel com cards por cliente, filtros por data, geolocalização e mensageria; integração com API de pedidos não alocados
  - Módulo Regra de Ouro (Caixa Preta): visualização detalhada da composição de meta de RV, com gráficos e indicadores por família/SKU por perfil de vendedor
  - Módulo PDV (Ponto de Venda): formulário digital de pesquisa de execução de PDV com geolocalização; integração com API Rota PDV (`https://api.fruki.com.br/comercial/v1/`)
  - Ajustes no módulo Metas/RV (normalização de dados no front-end, correções pós-piloto)
  - Entrega de APK e AAB (Play Store) — versão 2.0 do aplicativo

- **Não incluído:**
  - Desenvolvimento de APIs (responsabilidade da equipe Fruki — Jardel e Renan)
  - Módulos adicionais fora do roadmap acordado (gamificação, supervisores, etc.)
  - Versão iOS

## 3. Partes interessadas

| Parte interessada | Papel | Contato |
|---|---|---|
| Leandro Lottermann | Coordenador de Sistemas / Gestor do Contrato — Fruki | leandro_lottermann@fruki.com.br |
| Cecília Ribeiro | Analista Digital / Product Owner do cliente — Fruki | cecilia_ribeiro@fruki.com.br |
| Jardel Dargas Silva | Desenvolvedor Jr / Responsável pelas APIs — Fruki | jardel_silva@fruki.com.br |
| Renan Gustavo da Silva | Desenvolvedor / Suporte às APIs — Fruki | renan_silva@fruki.com.br |
| Alexsandro de Vargas Braga | Responsável comercial pelo módulo PDV — Fruki | alexsandro_braga@fruki.com.br |

## 4. Equipe do projeto

| Papel | Responsável |
|---|---|
| Gerente de Projeto / Product Owner | Abraão Oliveira |
| COO / Gestão Comercial | Tiago Nascimento |
| UX/UI Designer / Analista de Negócio | Brenda Chrystie |
| Desenvolvedor Front-End (React Native) | Luca Watson |
| Desenvolvedor Front-End (React Native) | Thiago Gomes |
| Responsável por Medição | Abraão Oliveira |

## 5. Macroplanejamento (datas-alvo)

| Marco | Data-alvo |
|---|---|
| Apresentação da proposta ao cliente | 26/09/2024 |
| Kickoff formal / aprovação da proposta | 09/10/2024 |
| Entendimento Demanda Caixa Preta | 09/10/2024 |
| Entrega Módulo Pedidos Não Alocados (PR #57) | 25/10/2024 |
| Alinhamento de protótipos Regra de Ouro e PDV | Nov/2024 |
| Desenvolvimento e entrega Regra de Ouro e PDV | Dez/2024 |
| Entrega final — aceite via Teams | 15/01/2025 |

## 6. Agenda das próximas atividades

- Reuniões quinzenais recorrentes de Alinhamento de Negócio e Backlog (toda quarta 15h — Timeware e Fruki)
- Reuniões técnicas com Jardel para integração das novas APIs
- Entregas mensais: Pedidos Não Alocados (out/2024) → Regra de Ouro (nov/2024) → PDV (dez/2024)
- Validação de protótipos de UX com Cecília antes de cada sprint de desenvolvimento
- Emissão de Nota Fiscal por parcela de entrega
- Sessão de aceite final via Microsoft Teams — 15/01/2025

## 7. Premissas e restrições iniciais

**Premissas:**
- A Fruki disponibiliza as APIs de cada módulo com antecedência mínima de 1 semana antes do início de cada sprint
- Cecília Ribeiro valida protótipos de UX antes do desenvolvimento de cada módulo
- Leandro Lottermann é a autoridade de aprovação e aceite formal das entregas
- A Regra de Ouro (Caixa Preta) foi incluída no escopo sem custo adicional, conforme alinhamento de 09/10/2024

**Restrições:**
- Prazo máximo para entrega: 15/01/2025 (aceite via Teams)
- Tecnologia: React Native / Expo (arquitetura existente)
- APIs são de responsabilidade exclusiva da Fruki
- Mudanças de escopo fora do Pacote Final 24 requerem nova proposta comercial

---

## Registro de abertura

| Reunião de kickoff realizada em | Ref. da autorização |
|---|---|
| 26/09/2024 | Reunião "Apresentação Proposta - Não Alocados - Fruki" — Fireflies ID: ZXGua1cMVMBiRQ5s |
| 09/10/2024 | Reunião "Parceria Fruki <> Timeware" — Fireflies ID: HWwWGbMe3glWfXgl |
| 09/10/2024 | Reunião "Entendimento Demanda Caixa Preta" — Fireflies ID: gOI5CeLpUr7VPiyf |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — abertura retroativa (projeto executado out/2024–jan/2025) |
