# Documento de Design — SuperApp Fruki · Pacote Final 24

| Campo | Valor |
|---|---|
| **Documento** | PCP-FRUKI01-002 |
| **Projeto** | SuperApp Fruki — Pacote Final 24 |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Responsáveis** | Abraão Oliveira (Tech Lead / PO) / Brenda Chrystie (UX/UI) |

---

## 1. Visão geral da solução

O Pacote Final 24 adiciona três novos módulos ao SuperApp Fruki (React Native / Expo): (1) Pedidos Não Alocados — rastreabilidade de pedidos sem entrega para o vendedor em campo; (2) Regra de Ouro — visualização detalhada da composição da remuneração variável (anteriormente chamada "caixa preta"); e (3) PDV / Rota PDV — formulário digital de pesquisa de execução de ponto de venda com geolocalização e integração à API de Rota PDV.

Os módulos são entregues de forma incremental (um por sprint mensal) e integrados às APIs REST fornecidas pelo time de TI da Fruki, com entrega via Pull Request no Azure DevOps e build AAB para publicação na Play Store (versão 2.0).

---

## 2. Design técnico (arquitetura)

### 2.1 Arquitetura

A arquitetura segue o padrão React Native / Expo estabelecido no Pacote 1. Os três novos módulos são implementados como novas screens e serviços na estrutura existente.

```
SuperApp Fruki (React Native / Expo) — versão 2.0
│
├── src/
│   ├── screens/
│   │   ├── PedidosNaoAlocadosScreen.tsx     ← RF-05, RF-06, RF-07
│   │   ├── RegraDeOuroScreen.tsx            ← RF-09, RF-10, RF-11
│   │   └── PDVScreen.tsx                   ← RF-12, RF-13, RF-14
│   ├── services/
│   │   ├── pedidosNaoAlocadosService.ts     ← integração API Pedidos Não Alocados + normalização front-end
│   │   ├── regraDeOuroService.ts            ← integração API Regra de Ouro
│   │   └── pdvService.ts                   ← integração API Rota PDV + captura de geolocalização
│   ├── hooks/
│   │   ├── usePedidosNaoAlocados.ts
│   │   ├── useRegraDeOuro.ts
│   │   └── usePDV.ts
│   └── components/
│       ├── PedidoCard.tsx                   ← card de pedido não alocado
│       ├── IndicadorCircular.tsx            ← gráfico circular para Regra de Ouro
│       └── FormularioPDV.tsx               ← formulário dinâmico de PDV
│
└── App.tsx (novas rotas adicionadas ao navegador existente)
```

**Versionamento:** `app.json` / `package.json` incrementado para versão 2.0; AAB gerado para publicação na Play Store.

### 2.2 Modelo de dados

Todos os dados consumidos via APIs REST da Fruki — sem banco de dados local persistente.

**Pedidos Não Alocados:**
```json
{
  "numeroPedido": "string",
  "nomeFantasia": "string",
  "localizacao": "string",
  "motivoNaoAlocacao": "string",
  "data": "string"
}
```
Normalização front-end em `pedidosNaoAlocadosService.ts`: a API pode retornar formato não padronizado; o serviço normaliza antes de repassar para a tela.

**Regra de Ouro:**
```json
{
  "indicador": "string",
  "realizado": number,
  "meta": number,
  "percentual": number,
  "tipo": "string",
  "skuFamilia": "string"
}
```

**Rota PDV:**
```json
{
  "pdvId": "string",
  "nomeEstabelecimento": "string",
  "endereco": "string",
  "status": "pendente | visitado"
}
```

### 2.3 Integrações

| API | Endpoint base | Módulo |
|---|---|---|
| Pedidos Não Alocados | `GET /comercial/v1/pedidosNaoAlocados/{rep}` | Módulo Pedidos Não Alocados |
| Regra de Ouro | `GET /comercial/v1/regraDeOuro/{rep}/{periodo}` | Módulo Regra de Ouro |
| Rota PDV | `GET /comercial/v1/rotaPDV/{rep}/{data}` | Módulo PDV — lista de PDVs da rota |
| Submit PDV | `POST /comercial/v1/rotaPDV/pesquisa` | Módulo PDV — envio de formulário de pesquisa |

**Base URL:** `https://api.fruki.com.br/comercial/v1/`
**Autenticação:** Headers `client-id` e `client-secret` (mesmo padrão do Pacote 1)
**API Rota PDV recebida de Jardel em 08/01/2026** (durante a Sprint 3)

### 2.4 Decisões de design

| Decisão | Alternativas consideradas | Escolha e justificativa | RAD |
|---|---|---|---|
| Normalização de dados de Pedidos Não Alocados no front-end | A) Solicitar padronização da API à Fruki; B) Normalizar no front-end | B — sprint em andamento; API fornecida pela Fruki em formato não padronizado; normalização implementada em `pedidosNaoAlocadosService.ts` | GDE-FRUKI01-001 |
| Renomeação de "Caixa Preta" para "Regra de Ouro" | A) Manter "Caixa Preta" conforme denominação interna; B) Renomear para "Regra de Ouro" | B — decisão tomada durante revisão de protótipos com Cecília em 22/10/2025; nomenclatura mais positiva e compreensível para os vendedores | — |
| Geolocalização capturada antes do envio do formulário PDV | A) Geolocalização opcional; B) Geolocalização obrigatória antes do submit | B — RNF-02 — validação de presença do vendedor no PDV exigida pela Fruki; submit bloqueado até GPS disponível | — |
| Versionamento para 2.0 com AAB para Play Store | A) Versão incremental (1.9.x); B) Versão 2.0 + AAB | B — conclusão do roadmap 2025 justifica major version; formato AAB exigido pela Play Store atual | — |

---

## 3. Design de produto (UX/UI)

### 3.1 Wireframes / protótipos

Protótipos elaborados em Figma por Brenda Chrystie antes de cada sprint, validados por Cecília Ribeiro (regras de RV e Não Alocados) e Alexsandro de Vargas Braga (formulário de PDV).

| Tela / fluxo | Referência | Status |
|---|---|---|
| Painel de Pedidos Não Alocados (cards + filtros) | Figma — SuperApp Fruki · Não Alocados v1 | Validado |
| Tela Regra de Ouro (gráficos circulares + indicadores por SKU) | Figma — SuperApp Fruki · Regra de Ouro v1 | Validado |
| Formulário de PDV (perguntas dinâmicas + geolocalização) | Figma — SuperApp Fruki · PDV v1 | Validado |
| Rota PDV (lista de PDVs com status visitado/pendente) | Figma — SuperApp Fruki · PDV v1 | Validado |

### 3.2 Validação com o cliente

| Tela / fluxo | Validado com | Data | Resultado |
|---|---|---|---|
| Painel Pedidos Não Alocados (cards: nome fantasia, localização, número, motivo) | Cecília Ribeiro | 26/09/2025 e out/2025 | Aprovado — campos e filtros confirmados |
| Tela Regra de Ouro — indicadores e gráficos circulares | Cecília Ribeiro | 22/10/2025 e 13/11/2025 | Aprovado — nomenclatura "Regra de Ouro" adotada; composição de RV por SKU/família confirmada |
| Formulário de PDV — lista de perguntas | Alexsandro de Vargas Braga | 04/12/2025 | Aprovado — formulário completo de perguntas confirmado |
| Rota PDV — lista e status dos PDVs | Cecília Ribeiro | Jan/2026 | Aprovado após integração com API de Jardel (recebida 08/01/2026) |

---

## 4. Rastreabilidade requisito → design

| Requisito (ID) | Elemento de design |
|---|---|
| RF-05 — Painel de pedidos não alocados com cards | `PedidosNaoAlocadosScreen.tsx` + `PedidoCard.tsx` + API pedidos não alocados |
| RF-06 — Filtros por data e cliente | Filtros em `PedidosNaoAlocadosScreen.tsx` + lógica em `usePedidosNaoAlocados.ts` |
| RF-07 — Mensagem quando lista vazia | Componente de estado vazio em `PedidosNaoAlocadosScreen.tsx` |
| RF-08 — Normalização de dados de pedidos não alocados | `pedidosNaoAlocadosService.ts` — normalização e deduplicação no front-end |
| RF-09 — Tela Regra de Ouro com indicadores e progresso | `RegraDeOuroScreen.tsx` + `IndicadorCircular.tsx` + API Regra de Ouro |
| RF-10 — Gráficos de progresso por indicador | `IndicadorCircular.tsx` — gráficos circulares com distinção visual acima/abaixo da meta |
| RF-11 — Pesquisa de SKUs na Regra de Ouro | Campo de pesquisa em `RegraDeOuroScreen.tsx` com filtro em tempo real |
| RF-12 — Formulário digital de PDV com geolocalização | `PDVScreen.tsx` + `FormularioPDV.tsx` + captura GPS em `pdvService.ts` |
| RF-13 — Integração com API de Rota PDV | `pdvService.ts` — POST para `/comercial/v1/rotaPDV/pesquisa` |
| RF-14 — Visualização da rota do PDV | Lista de PDVs em `PDVScreen.tsx` com status visitado/pendente via API |
| RNF-01 — Versão 2.0 com AAB | `app.json` / `package.json` atualizados; build AAB gerado via Expo |
| RNF-02 — Geolocalização obrigatória | Permissão de GPS solicitada em `pdvService.ts`; submit bloqueado sem GPS |
| RNF-03 — Android first | Build Expo APK (teste) e AAB (produção); compatível com Android 8.0+ |
| RNF-04 — Entrega via PR Azure DevOps | Branches por módulo → PRs revisadas e mergeadas pelo Jardel |
| RNF-05 — Loading state durante chamadas à API | Indicadores de loading em todos os componentes dos três módulos |

---

## 5. Avaliação do design (PCP 2)

| Item avaliado | Avaliador | Problema encontrado | Tratamento |
|---|---|---|---|
| Protótipos Pedidos Não Alocados | Cecília Ribeiro | Nenhum — aprovado conforme proposto | — |
| Protótipos Regra de Ouro | Cecília Ribeiro | Nomenclatura "Caixa Preta" substituída por "Regra de Ouro" | Renomeado em toda a interface e documentação |
| Protótipos formulário PDV | Alexsandro de Vargas Braga | Lista de perguntas incompleta na versão inicial | Perguntas completas fornecidas em 04/12/2025 |
| API Rota PDV — atraso de disponibilização | Jardel Dargas Silva | API disponibilizada apenas em 08/01/2026 (já na Sprint 3) | Desenvolvimento da tela de lista PDV adiantado; integração real feita após recebimento da API |
| PR Módulo Pedidos Não Alocados (PR #57) | Jardel Dargas Silva | Nenhuma — aprovada e mergeada 25/10/2025 | — |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — registro retroativo (projeto executado out/2025–jan/2026) |
