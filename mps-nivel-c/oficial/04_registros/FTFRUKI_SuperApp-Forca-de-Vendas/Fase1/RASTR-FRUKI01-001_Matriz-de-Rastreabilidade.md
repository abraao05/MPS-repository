# Matriz de Rastreabilidade — SuperApp Fruki · Pacote 1 — Módulo Metas e RV

| Campo | Valor |
|---|---|
| **Documento** | RASTR-FRUKI01-001 |
| **Projeto** | SuperApp Fruki — Pacote 1 — Módulo Metas e Remuneração Variável |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |

---

## Matriz

| Necessidade | Requisito (ID) | Item de design | Branch / PR | Cenário de teste | Situação |
|---|---|---|---|---|---|
| Vendedor visualiza atingimento de metas de volume por família | RF-01 | `MetasScreen.tsx` + `MetaCard.tsx` + API `/acompanhamentoMetasFamilias` | `feature/novos-recursos-superapp` → PR revisada por Jardel | CT — Metas por família (happy path) | Verificado e aceito |
| Vendedor visualiza cobertura, drop size e positivação | RF-02 | `RVScreen.tsx` + `PerfilRVSummary.tsx` + API `/acompanhamentoMetasFamilias` | `feature/novos-recursos-superapp` → PR revisada por Jardel | CT — Indicadores multidimensionais (happy path) | Verificado e aceito |
| Vendedor visualiza RV estimada com base nos indicadores | RF-03 | `RVScreen.tsx` + cálculo no `useMetas.ts` | `feature/novos-recursos-superapp` → PR revisada por Jardel | CT — RV por perfil representante (happy path) | Verificado e aceito |
| Tela adapta indicadores conforme perfil do vendedor | RF-04 | Renderização condicional em `MetasScreen.tsx` e `RVScreen.tsx` | `feature/novos-recursos-superapp` → PR revisada por Jardel | CT — RV por perfil supervisor (happy path) | Verificado e aceito |
| Tratamento de latência de API no front-end | RNF-01 | Loading state em todos os componentes de metas; skeleton screens | `feature/novos-recursos-superapp` → PR revisada por Jardel | CT — Latência de API (sad path) | Verificado e aceito |
| Distribuição via APK Android 8.0+ | RNF-02 | Build Expo APK — piloto 05/08/2025 | — | APK testado em dispositivos físicos | Verificado e aceito |
| Código entregue via PR no Azure DevOps | RNF-03 | Branch `feature/novos-recursos-superapp` | PR revisada e mergeada por Jardel | — | Verificado e aceito |
| Autenticação com APIs via client-id/client-secret | RNF-04 | Headers em `metasService.ts` | `feature/novos-recursos-superapp` → PR revisada por Jardel | — | Verificado e aceito |

---

## Cobertura

- Requisitos sem cobertura de teste: nenhum
- Itens desenvolvidos sem requisito associado: nenhum

Todos os RF-01 a RF-04 e RNF-01 a RNF-04 possuem: elemento de design correspondente, entrega via PR no Azure DevOps e cenário de teste ou validação direta com cliente.

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 01/09/2025 | Abraão Oliveira | Versão inicial — registro retroativo (projeto executado jun–set/2025) |
