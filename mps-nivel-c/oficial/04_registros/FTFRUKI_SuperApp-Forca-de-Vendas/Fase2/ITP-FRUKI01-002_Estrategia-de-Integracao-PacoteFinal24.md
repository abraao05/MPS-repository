# Estratégia de Integração — SuperApp Fruki · Pacote Final 24

| Campo | Valor |
|---|---|
| **Documento** | ITP-FRUKI01-002 |
| **Projeto** | SuperApp Fruki — Pacote Final 24 |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |

---

## 1. Componentes a integrar

| Componente | Descrição |
|---|---|
| SuperApp Fruki v2.0 (front-end React Native) | Base de código existente (Pacote 1 integrado); três novos módulos adicionados |
| Módulo Pedidos Não Alocados | Novas telas: `PedidosNaoAlocadosScreen.tsx`, `PedidoCard.tsx`; serviço `pedidosNaoAlocadosService.ts` |
| Módulo Regra de Ouro | Novas telas: `RegraDeOuroScreen.tsx`, `IndicadorCircular.tsx`; serviço `regraDeOuroService.ts` |
| Módulo PDV / Rota PDV | Novas telas: `PDVScreen.tsx`, `FormularioPDV.tsx`; serviço `pdvService.ts` |
| API Pedidos Não Alocados | API REST Fruki — lista de pedidos sem entrega por representante |
| API Regra de Ouro | API REST Fruki — composição dos indicadores de RV do representante |
| API Rota PDV (GET) | API REST Fruki — lista de PDVs da rota do representante com status |
| API Rota PDV (POST) | API REST Fruki — recebe dados do formulário de pesquisa de execução de PDV |

---

## 2. Interfaces

| Interface | Entre | Tipo / contrato |
|---|---|---|
| Pedidos não alocados | `PedidosNaoAlocadosScreen.tsx` ↔ API GET `/comercial/v1/pedidosNaoAlocados/{rep}` | REST GET — resposta JSON; normalização de formato não padronizado em `pedidosNaoAlocadosService.ts` |
| Regra de Ouro | `RegraDeOuroScreen.tsx` ↔ API GET `/comercial/v1/regraDeOuro/{rep}/{periodo}` | REST GET — indicadores com progresso real vs. meta por SKU/família |
| Rota PDV — lista | `PDVScreen.tsx` ↔ API GET `/comercial/v1/rotaPDV/{rep}/{data}` | REST GET — lista de PDVs com status (visitado/pendente); API fornecida por Jardel em 08/01/2026 |
| Submit formulário PDV | `pdvService.ts` ↔ API POST `/comercial/v1/rotaPDV/pesquisa` | REST POST — payload: respostas do formulário + geolocalização (lat/long) do dispositivo |
| Geolocalização | `pdvService.ts` ↔ GPS do dispositivo Android | React Native Geolocation API; permissão solicitada antes do submit; submit bloqueado sem GPS |

**Base URL:** `https://api.fruki.com.br/comercial/v1/`
**Autenticação:** headers `client-id` e `client-secret` — mesmo padrão do Pacote 1.

---

## 3. Estratégia e ordem de integração

A integração segue a cadência de sprints mensais, com cada módulo integrado e entregue de forma independente:

**Sprint 1 (Out/2025) — Pedidos Não Alocados:**
- Integração com API de pedidos não alocados
- Normalização de formato não padronizado implementada no `pedidosNaoAlocadosService.ts` antes da integração na tela
- Entrega via PR #57 mergeada por Jardel em 25/10/2025

**Sprint 2 (Nov/2025) — Regra de Ouro:**
- Integração com API de Regra de Ouro
- Renderização de gráficos circulares (`IndicadorCircular.tsx`) com dados reais
- Funcionalidade de pesquisa de SKU em tempo real integrada ao estado local
- Entrega via PR revisada e mergeada por Jardel em Nov/2025

**Sprint 3 (Dez/2025–Jan/2026) — PDV / Rota PDV:**
- Interface da tela de PDV e formulário desenvolvidos com mock de dados (API Rota PDV recebida de Jardel apenas em 08/01/2026)
- Integração com API Rota PDV (GET e POST) realizada após recebimento em 08/01/2026
- Integração com GPS do dispositivo via React Native Geolocation
- Versionamento do app incrementado para 2.0 (`app.json` / `package.json`)
- Entrega via PR revisada e mergeada por Jardel em Jan/2026

---

## 4. Ambiente de integração

| Ambiente | Ferramenta | Uso |
|---|---|---|
| Desenvolvimento | Branch por módulo no Azure DevOps Fruki | Integração local com APIs reais; branches: `feature/nao-alocados`, `feature/regra-de-ouro`, `feature/pdv-rota` |
| Homologação / stage | APK gerado via Expo por módulo | Build distribuído para Cecília antes de cada merge; validação com dados reais da API antes do aceite |
| Produção | PR mergeada por Jardel + AAB v2.0 para Play Store | Código promovido após aprovação; publicação na Play Store pelo time Fruki |

---

## 5. Critérios de prontidão para integração

Para cada módulo ser integrado (merge da PR):

- [x] Interface desenvolvida e testada com mock antes da API real estar disponível (onde aplicável)
- [x] Integração com API real testada em dispositivo Android físico
- [x] Loading state implementado em todos os componentes dos três módulos
- [x] Normalização e tratamento de erro de API implementados nos serviços
- [x] Geolocalização obrigatória implementada e testada (módulo PDV)
- [x] Cenários sad path implementados (lista vazia, erro de API, GPS indisponível)
- [x] APK de teste gerado via Expo e validado com Cecília Ribeiro antes da entrega
- [x] Code review aprovado por Jardel Dargas Silva via Pull Request

---

## 6. Testes do produto integrado

Referência: `VV-FRUKI01-002_Plano-VeV-PacoteFinal24.md`

- **Testes manuais por sprint:** cenários Gherkin executados em dispositivo Android físico antes de cada PR
- **APK de homologação:** distribuído para Cecília Ribeiro e, no caso do PDV, para validação em campo antes do aceite final
- **Aceite final integrado (15/01/2026):** validação dos três módulos em conjunto na reunião via Microsoft Teams com Leandro e Cecília
- **Revisão de PR por Jardel:** verificação técnica de cada módulo antes do merge — garante compatibilidade com o codebase existente

---

## 7. Entrega e material de apoio

| Item entregue | Forma |
|---|---|
| Código-fonte dos três novos módulos | PRs individuais por módulo no Azure DevOps Fruki |
| APK de homologação por módulo | Build Expo distribuído via link para validação com cliente |
| Build AAB v2.0 para Play Store | Entregue em Jan/2026 para publicação pelo time Fruki |
| Documentação de integração | Seção 2.3 do `PCP-FRUKI01-002_Documento-de-Design-PacoteFinal24.md` |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 09/10/2025 | Abraão Oliveira | Versão inicial — registro retroativo (projeto executado out/2025–jan/2026) |
