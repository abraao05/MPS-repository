# Termo de Abertura do Projeto — SuperApp Fruki · Pacote 1 — Módulo Metas e Remuneração Variável

| Campo | Valor |
|---|---|
| **Documento** | TAP-FRUKI01-001 |
| **Projeto** | SuperApp Fruki — Pacote 1 — Módulo Metas e Remuneração Variável |
| **Cliente** | Fruki Bebidas S.A. |
| **Contrato** | Pacote 1 — Metas/RV |
| **Versão** | 1.1 |
| **Data de abertura** | 05/06/2025 |
| **Gerente de Projeto** | Abraão Oliveira |

---

## 1. Objetivo do projeto

Desenvolver o Módulo de Metas e Remuneração Variável (RV) no SuperApp Fruki — aplicativo mobile de força de vendas (React Native / Expo). A Timeware assume o desenvolvimento como novo fornecedor, dando continuidade à evolução do SuperApp já existente. O módulo entrega aos representantes e supervisores comerciais da Fruki visibilidade em tempo real sobre seus indicadores de performance (volume, cobertura, drop size, positivação) e sobre a composição de sua remuneração variável, substituindo a consulta a relatórios manuais.

## 2. Escopo macro

Conforme proposta comercial "Pacote 1 — Metas/RV" acordada em junho de 2025 com Leandro Lottermann.

- **Incluído:**
  - Módulo Metas/RV: telas de indicadores de volume, cobertura, drop size, positivação e acompanhamento de metas por família de produtos e por item (SKU)
  - Integração com APIs de acompanhamento de metas fornecidas pela Fruki (`/acompanhamentoMetasFamilias`, `/acompanhamentoMetasItens`, `/acompanhamentoForaDeRota`, `/acompanhamentoVisitas`)
  - Piloto com vendedores selecionados pela Fruki (APK de teste via Expo)
  - Entrega via Pull Request no repositório Azure DevOps da Fruki

- **Não incluído:**
  - Desenvolvimento de APIs (responsabilidade da equipe Fruki — Jardel e Renan)
  - Demais módulos do SuperApp (Pedidos Não Alocados, PDV, Regra de Ouro — escopo do Pacote Final 24)
  - Versão iOS

## 3. Partes interessadas

| Parte interessada | Papel | Contato |
|---|---|---|
| Leandro Lottermann | Coordenador de Sistemas / Gestor do Contrato — Fruki | leandro_lottermann@fruki.com.br |
| Cecília Ribeiro | Analista Digital / Product Owner do cliente — Fruki | cecilia_ribeiro@fruki.com.br |
| Jardel Dargas Silva | Desenvolvedor Jr / Responsável pelas APIs — Fruki | jardel_silva@fruki.com.br |
| Renan Gustavo da Silva | Desenvolvedor / Suporte às APIs — Fruki | renan_silva@fruki.com.br |

## 4. Equipe do projeto

| Papel | Responsável |
|---|---|
| Gerente de Projeto / Product Owner | Abraão Oliveira |
| COO / Gestão Comercial | Tiago Nascimento |
| UX/UI Designer | Brenda Chrystie |
| Desenvolvedor Front-End (React Native) | Luca Watson |
| Desenvolvedor Front-End (React Native) | Thiago Gomes |
| Responsável por Medição | Abraão Oliveira |

## 5. Macroplanejamento (datas-alvo)

| Marco | Data-alvo |
|---|---|
| Proposta comercial / Kickoff | 05/06/2025 |
| Acesso ao repositório Azure DevOps e APIs Fruki | 26/06/2025 |
| Levantamento demanda Metas (reunião formal) | 25/06/2025 |
| Desenvolvimento e entregas incrementais | Jul/2025 |
| Piloto com vendedores selecionados | 05/08/2025 |
| Aceite e encerramento do Pacote 1 | Ago/Set 2025 |

## 6. Agenda das próximas atividades

- Criação de acesso ao Azure DevOps para equipe Timeware (usuário `timeware`)
- Levantamento formal das regras de negócio de metas e RV com Cecília Ribeiro
- Desenvolvimento do módulo Metas/RV integrado às APIs Fruki
- Geração de APK de teste via Expo para piloto com vendedores
- Reuniões de acompanhamento com Leandro e Jardel conforme necessidade

## 7. Premissas e restrições iniciais

**Premissas:**
- A Fruki disponibiliza acesso ao repositório Azure DevOps e às APIs documentadas com antecedência ao início do desenvolvimento
- Cecília Ribeiro valida as regras de negócio de RV antes do desenvolvimento de cada tela
- Leandro Lottermann é a autoridade de aprovação e aceite formal das entregas

**Restrições:**
- Tecnologia obrigatória: React Native / Expo (arquitetura existente do SuperApp)
- APIs são de responsabilidade exclusiva da Fruki (Jardel/Renan)
- Prazo de entrega: piloto concluído até agosto de 2025

---

## Registro de abertura

| Reunião de kickoff realizada em | Ref. da autorização |
|---|---|
| 05/06/2025 | Reunião "Proposta Comercial - Fruki <> Timeware" — Fireflies ID: IhH8wQEDaiMe4o4b |
| 25/06/2025 | Reunião "Levantamento demanda Metas" — Fireflies ID: mo3xiqhyv46qvkkb |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2025 | Abraão Oliveira | Versão inicial — abertura retroativa |
| 1.1 | 05/06/2026 | Abraão Oliveira | Rescopo para Pacote 1 (Metas/RV apenas); Pacote Final 24 registrado em TAP-FRUKI01-002 |
