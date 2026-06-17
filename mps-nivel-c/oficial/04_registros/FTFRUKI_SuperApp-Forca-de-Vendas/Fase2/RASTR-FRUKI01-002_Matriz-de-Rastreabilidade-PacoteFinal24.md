# Matriz de Rastreabilidade — SuperApp Fruki · Pacote Final 24

| Campo | Valor |
|---|---|
| **Documento** | RASTR-FRUKI01-002 |
| **Projeto** | SuperApp Fruki — Pacote Final 24 |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |

---

## Matriz

| Necessidade | Requisito (ID) | Item de design | Branch / PR | Cenário de teste | Situação |
|---|---|---|---|---|---|
| Vendedor visualiza pedidos não alocados com dados completos | RF-05 | `PedidosNaoAlocadosScreen.tsx` + `PedidoCard.tsx` + API pedidos não alocados | PR #57 (Azure DevOps Fruki) — 25/10/2025 | CT — Lista pedidos não alocados (happy path) | Verificado e aceito |
| Vendedor filtra pedidos não alocados por data e cliente | RF-06 | Filtros em `PedidosNaoAlocadosScreen.tsx` + `usePedidosNaoAlocados.ts` | PR #57 | CT — Filtros por data e cliente | Verificado e aceito |
| Mensagem quando lista de pedidos está vazia | RF-07 | Componente de estado vazio em `PedidosNaoAlocadosScreen.tsx` | PR #57 | CT — Lista vazia (sad path) | Verificado e aceito |
| Normalização de dados de pedidos no front-end | RF-08 | `pedidosNaoAlocadosService.ts` — normalização de formato não padronizado | PR #57 | CT — Normalização de formato (sad path) | Verificado e aceito |
| Vendedor visualiza composição da Regra de Ouro | RF-09 | `RegraDeOuroScreen.tsx` + `IndicadorCircular.tsx` + API Regra de Ouro | PR Regra de Ouro (Azure DevOps Fruki) — Nov/2025 | CT — Regra de Ouro indicadores e gráficos | Verificado e aceito |
| Gráficos circulares de progresso por indicador | RF-10 | `IndicadorCircular.tsx` — gráficos circulares com distinção visual | PR Regra de Ouro | CT — Gráficos de progresso | Verificado e aceito |
| Pesquisa de SKUs na Regra de Ouro | RF-11 | Campo de pesquisa em `RegraDeOuroScreen.tsx` com filtro em tempo real | PR Regra de Ouro | CT — Pesquisa de SKU em tempo real | Verificado e aceito |
| Formulário digital de pesquisa de PDV com geolocalização | RF-12 | `PDVScreen.tsx` + `FormularioPDV.tsx` + captura GPS em `pdvService.ts` | PR PDV (Azure DevOps Fruki) — Jan/2026 | CT — Formulário PDV com geolocalização | Verificado e aceito |
| Integração com API de Rota PDV para envio de dados | RF-13 | `pdvService.ts` — POST para `/comercial/v1/rotaPDV/pesquisa` | PR PDV | CT — Submit formulário PDV | Verificado e aceito |
| Visualização da rota do PDV com status | RF-14 | Lista de PDVs em `PDVScreen.tsx` via API Rota PDV | PR PDV | CT — Rota PDV lista de PDVs | Verificado e aceito |
| Versão 2.0 com AAB para Play Store | RNF-01 | `app.json` v2.0; build AAB via Expo | Build AAB entregue Jan/2026 | Smoke test do AAB | Verificado e aceito |
| Geolocalização obrigatória no PDV | RNF-02 | Permissão GPS + bloqueio de submit sem GPS em `pdvService.ts` | PR PDV | CT — Formulário PDV sem GPS (sad path) | Verificado e aceito |
| Android 8.0+ (React Native / Expo) | RNF-03 | Build Expo APK e AAB | APK de homologação; AAB de produção | Testado em dispositivos Android 8.0+ | Verificado e aceito |
| Código entregue via PR no Azure DevOps | RNF-04 | Branches por módulo; PRs revisadas pelo Jardel | PR #57 + PR Regra de Ouro + PR PDV | — | Verificado e aceito |
| Loading state durante chamadas às APIs | RNF-05 | Indicadores de loading em `PedidosNaoAlocadosScreen`, `RegraDeOuroScreen` e `PDVScreen` | Incluído nas PRs respectivas | CT — Latência de API (loading state) | Verificado e aceito |

---

## Cobertura

- Requisitos sem cobertura de teste: nenhum
- Itens desenvolvidos sem requisito associado: nenhum

Todos os RF-05 a RF-14 e RNF-01 a RNF-05 possuem: elemento de design correspondente, entrega via PR revisada no Azure DevOps e cenário de teste ou validação direta com cliente. A aceite final dos três módulos foi registrada via Microsoft Teams em 15/01/2026 (TAE-FRUKI01-002).

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — registro retroativo (projeto executado out/2025–jan/2026) |
