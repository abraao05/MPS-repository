# Documento de Requisitos — SuperApp Fruki · Pacote 1 — Módulo Metas e Remuneração Variável

| Campo | Valor |
|---|---|
| **Documento** | REQ-FRUKI01-001 |
| **Projeto** | SuperApp Fruki — Pacote 1 — Módulo Metas e Remuneração Variável |
| **Cliente** | Fruki Bebidas S.A. |
| **Versão** | 1.1 |
| **Data** | 05/06/2026 |
| **Responsáveis (Discovery)** | Abraão Oliveira (PO) / Brenda Chrystie (UX/Analista) |

---

## 1. Contexto e objetivo

A Fruki Bebidas opera uma extensa rede de representantes e supervisores comerciais em campo. Esses profissionais utilizam o SuperApp Fruki (React Native / Expo) para acompanhar sua jornada de vendas. O problema central é a falta de visibilidade em tempo real sobre indicadores de performance e composição de remuneração variável (RV): os dados existiam apenas em relatórios de planejamento diário inacessíveis pelo celular em campo.

O Pacote 1 entrega o Módulo de Metas e Remuneração Variável, integrando o SuperApp às APIs de acompanhamento de metas da Fruki e exibindo os indicadores diretamente na tela do aplicativo.

## 2. Partes interessadas

| Parte interessada | Necessidade principal |
|---|---|
| Vendedores (representantes) | Visualizar metas, indicadores de RV e performance em tempo real no celular, em campo |
| Supervisores de vendas | Acompanhar a performance da equipe por família de produtos e indicadores de RV |
| Cecília Ribeiro (Analista Digital — Fruki) | Garantir que as regras de negócio de RV e metas estejam corretamente implementadas |
| Leandro Lottermann (Coordenador de Sistemas — Fruki) | Evolução do SuperApp dentro do prazo e escopo acordados |
| Jardel / Renan (Devs — Fruki) | Integração correta entre APIs Fruki e front-end Timeware |

## 3. Visão geral da solução

Novas telas no SuperApp Fruki (React Native / Expo) com indicadores de metas e RV, integradas às quatro APIs REST fornecidas pela Fruki:

- `GET /acompanhamentoMetasFamilias/{representante}/{periodo}/{tipo}` — metas por família de produtos
- `GET /acompanhamentoMetasItens/{representante}/{periodo}/{tipo}` — metas por item (SKU)
- `GET /acompanhamentoForaDeRota/{representante}/{data}` — acompanhamento fora de rota
- `GET /acompanhamentoVisitas/{representante}/{data}` — acompanhamento de visitas

A solução envolve: UX/UI com protótipos validados por Cecília antes do desenvolvimento; integração REST com autenticação via `client-id` / `client-secret`; entregas via PR no Azure DevOps Fruki.

## 4. Requisitos funcionais

| ID | Requisito (história) | Prioridade | Critérios de aceite |
|---|---|---|---|
| RF-01 | Como vendedor, quero visualizar meu percentual de atingimento de meta de volume por família de produtos no SuperApp, para acompanhar minha performance em campo | Alta | Tela exibe volume real, meta e percentual de atingimento por família; dados atualizados conforme API; famílias ordenadas alfabeticamente |
| RF-02 | Como vendedor, quero visualizar indicadores de cobertura, drop size e positivação, para entender minha performance multidimensional | Alta | Todos os indicadores exibidos; valores calculados conforme regras de negócio confirmadas por Cecília Ribeiro |
| RF-03 | Como vendedor, quero visualizar minha remuneração variável (RV) estimada com base nos indicadores atingidos, para projetar meu ganho mensal | Alta | Cálculo de RV exibido conforme composição de metas por perfil de vendedor; composição validada por Cecília |
| RF-04 | Como sistema, devo adaptar a visualização de indicadores e composição de RV conforme o perfil do vendedor logado | Alta | Tela de metas adapta indicadores exibidos ao perfil (vendedor, supervisor, representante); regras de composição por perfil confirmadas por Cecília Ribeiro |

## 5. Requisitos não funcionais

| ID | Requisito não funcional | Critério |
|---|---|---|
| RNF-01 | Desempenho da integração com as APIs | Tratamento de latência no front-end (API identificada com ~3,10s de resposta inicialmente); exibição de loading state enquanto aguarda resposta |
| RNF-02 | Compatibilidade | Android first (piloto); React Native / Expo; Android 8.0+ |
| RNF-03 | Integração com repositório Fruki | Código entregue via Pull Request no Azure DevOps; revisão e merge pelo Jardel |
| RNF-04 | Autenticação com APIs | Headers `client-id` e `client-secret` conforme especificação Fruki |

## 6. Restrições e premissas

**Restrições:**
- Tecnologia: React Native / Expo (arquitetura existente do SuperApp)
- APIs são de responsabilidade da Fruki; Timeware não altera a camada de backend
- Todo o código em branches separadas; merge somente após revisão do Jardel

**Premissas:**
- APIs disponibilizadas pelo time Fruki antes do início do desenvolvimento
- Cecília Ribeiro valida protótipos antes do início de cada sprint
- Leandro Lottermann tem autoridade para o aceite formal das entregas

## 7. Validação dos requisitos

| Requisito / conjunto | Forma de validação | Data | Resultado |
|---|---|---|---|
| RF-01 a RF-04 — Metas/RV | Reunião "Levantamento demanda Metas" com Leandro e Cecília | 25/06/2024 | Validado — regras de negócio levantadas; APIs e acesso ao repositório fornecidos |
| RF-01 a RF-04 — Metas/RV | Piloto com vendedores selecionados (APK de teste via Expo) | 05/08/2024 | Validado com ajustes — identificado problema de duplicação de famílias e cálculos; corrigido antes do aceite |
| RF-04 — Perfis de vendedor | Validação com Cecília Ribeiro via reuniões de alinhamento | Ago/2024 | Validado — composição de RV por perfil confirmada |

## 8. Confirmação de entendimento e compromisso

| Envolvido | Papel | Confirmação | Data |
|---|---|---|---|
| Leandro Lottermann | Coordenador de Sistemas / Gestor — Fruki | Entendimento confirmado — acesso ao repositório e APIs fornecidos | 26/06/2024 |
| Cecília Ribeiro | Analista Digital / PO cliente — Fruki | Entendimento confirmado — regras de negócio levantadas e validadas | 25/06/2024 |
| Abraão Oliveira | Gerente de Projeto — Timeware | Compromisso assumido | 26/06/2024 |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — registro retroativo |
| 1.1 | 05/06/2026 | Abraão Oliveira | Rescopo para Pacote 1 (Metas/RV apenas); RF-05 a RF-14 movidos para REQ-FRUKI01-002 |
