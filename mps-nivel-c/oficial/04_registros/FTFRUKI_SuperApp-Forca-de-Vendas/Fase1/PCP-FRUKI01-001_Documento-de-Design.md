# Documento de Design — SuperApp Fruki · Pacote 1 — Módulo Metas e Remuneração Variável

| Campo | Valor |
|---|---|
| **Documento** | PCP-FRUKI01-001 |
| **Projeto** | SuperApp Fruki — Pacote 1 — Módulo Metas e Remuneração Variável |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Responsáveis** | Abraão Oliveira (Tech Lead / PO) / Brenda Chrystie (UX/UI) |

---

## 1. Visão geral da solução

O Módulo Metas e Remuneração Variável (RV) adiciona ao SuperApp Fruki (React Native / Expo) um conjunto de telas que exibem, em tempo real, os indicadores de performance e a composição de remuneração variável de cada representante comercial. A solução consome quatro APIs REST fornecidas pela equipe de TI da Fruki, adapta a visualização conforme o perfil do usuário logado e trata internamente problemas de performance e normalização de dados identificados nas APIs.

---

## 2. Design técnico (arquitetura)

### 2.1 Arquitetura

O SuperApp Fruki é um aplicativo React Native gerenciado via Expo, distribuído para Android (Android 8.0+). A arquitetura do Módulo Metas/RV segue o padrão existente no aplicativo:

```
SuperApp Fruki (React Native / Expo)
│
├── src/
│   ├── screens/
│   │   ├── MetasScreen.tsx        ← tela principal de metas por família
│   │   ├── MetasItensScreen.tsx   ← detalhamento por SKU
│   │   ├── RVScreen.tsx           ← composição de RV estimada
│   │   └── VisitasScreen.tsx      ← acompanhamento de visitas / fora de rota
│   ├── services/
│   │   └── metasService.ts        ← chamadas às 4 APIs de metas com tratamento de loading e erro
│   ├── hooks/
│   │   └── useMetas.ts            ← hook de estado e fetch das métricas de metas
│   └── components/
│       ├── MetaCard.tsx           ← card de indicador com barra de progresso
│       └── PerfilRVSummary.tsx    ← resumo de RV por perfil
│
└── App.tsx (navegação existente — novas rotas adicionadas)
```

**Branch de desenvolvimento:** `feature/novos-recursos-superapp` no repositório Azure DevOps da Fruki (`https://dev.azure.com/fruki/superapp/_git/fruki-app.git`).

### 2.2 Modelo de dados

Os dados são consumidos diretamente das APIs REST da Fruki — não há banco de dados local ou cache persistente. O estado de cada tela é gerenciado via hooks React.

Estrutura de resposta principal (API `/acompanhamentoMetasFamilias`):

```json
{
  "familia": "string",
  "meta": number,
  "realizado": number,
  "percentual": number,
  "tipo": "string"
}
```

Anomalia identificada: a API pode retornar famílias duplicadas com chaves de ordenação diferentes. O front-end trata a deduplicação e aplica ordenação alfabética por família.

### 2.3 Integrações

| API | Endpoint | Uso |
|---|---|---|
| Metas por família | `GET /acompanhamentoMetasFamilias/{rep}/{periodo}/{tipo}` | Tela principal de metas |
| Metas por item (SKU) | `GET /acompanhamentoMetasItens/{rep}/{periodo}/{tipo}` | Detalhamento por SKU |
| Fora de rota | `GET /acompanhamentoForaDeRota/{rep}/{data}` | Indicador de visitas fora de rota |
| Visitas | `GET /acompanhamentoVisitas/{rep}/{data}` | Acompanhamento de visitas do dia |

**Autenticação:** Headers `client-id` e `client-secret` enviados em todas as requisições.
**Base URL:** `https://api.fruki.com.br/`

### 2.4 Decisões de design

| Decisão | Alternativas consideradas | Escolha e justificativa | RAD |
|---|---|---|---|
| Tratamento de latência de API no front-end | A) Solicitar otimização da API à Fruki; B) Tratar loading state e exibição incremental no front-end | B — Fruki não tinha capacidade para otimizar as APIs no prazo do projeto; a latência (~3,10s para 5 pedidos) foi tratada com loading state e skeleton screens no front-end | GDE-FRUKI01-001 |
| Normalização de dados duplicados no front-end | A) Solicitar correção da API; B) Deduplicar no front-end | B — mesma justificativa de prazo; lógica de deduplicação e ordenação implementada no `metasService.ts` | GDE-FRUKI01-001 |
| Adaptação de telas por perfil | A) Telas separadas por perfil; B) Tela única com renderização condicional | B — base de código menor; perfil recuperado do token de autenticação existente no app | — |

---

## 3. Design de produto (UX/UI)

### 3.1 Wireframes / protótipos

Protótipos elaborados em Figma por Brenda Chrystie antes de cada sprint de desenvolvimento, compartilhados com Cecília Ribeiro para validação das regras de negócio.

| Tela / fluxo | Arquivo / referência | Status |
|---|---|---|
| Tela principal — Metas por família | Figma — SuperApp Fruki · Metas v1 | Validado |
| Detalhamento por SKU | Figma — SuperApp Fruki · Metas v1 | Validado |
| Composição de RV por perfil | Figma — SuperApp Fruki · Metas v1 | Validado |
| Acompanhamento de visitas / fora de rota | Figma — SuperApp Fruki · Metas v1 | Validado |

### 3.2 Validação com o cliente

| Tela / fluxo | Validado com cliente | Data | Resultado |
|---|---|---|---|
| Tela principal de metas por família + critérios de atingimento | Cecília Ribeiro | 25/06/2025 | Aprovado — indicadores e ordenação confirmados |
| Composição de RV por perfil de vendedor | Cecília Ribeiro | Jul/2025 | Aprovado — regras de cálculo por perfil validadas |
| Tela pós-piloto: ajuste de duplicação de famílias e ordenação | Cecília Ribeiro | Ago/2025 | Aprovado após correção |

---

## 4. Rastreabilidade requisito → design

| Requisito (ID) | Elemento de design |
|---|---|
| RF-01 — Metas de volume por família | `MetasScreen.tsx` + `MetaCard.tsx` + API `/acompanhamentoMetasFamilias` |
| RF-02 — Indicadores de cobertura, drop size e positivação | `RVScreen.tsx` + `PerfilRVSummary.tsx` + API `/acompanhamentoMetasFamilias` |
| RF-03 — RV estimada por perfil | `RVScreen.tsx` + `PerfilRVSummary.tsx` + lógica de cálculo no `useMetas.ts` |
| RF-04 — Adaptação de telas por perfil de vendedor | Renderização condicional em `MetasScreen.tsx` + `RVScreen.tsx` baseada no perfil do usuário autenticado |
| RNF-01 — Tratamento de latência | Loading state em todos os componentes de metas; skeleton screens enquanto aguarda resposta da API |
| RNF-03 — Entrega via PR | Branch `feature/novos-recursos-superapp`; PR revisada pelo Jardel antes do merge |
| RNF-04 — Autenticação | Headers `client-id`/`client-secret` em `metasService.ts` |

---

## 5. Avaliação do design (PCP 2)

| Item avaliado | Avaliador | Problema encontrado | Tratamento |
|---|---|---|---|
| Protótipos de UX — telas de metas por família | Cecília Ribeiro | Nenhum — aprovado conforme proposto | — |
| Integração com APIs durante desenvolvimento | Luca Watson / Thiago Gomes | Latência de ~3,10s identificada; famílias duplicadas na resposta da API de famílias | Tratamento no front-end: loading state + deduplicação e ordenação no `metasService.ts` |
| APK de piloto (05/08/2025) | Vendedores selecionados / Cecília | Duplicação de famílias visível na tela de piloto; cálculo de positivação inconsistente | Corrigido antes do aceite — deduplicação e correção de cálculo implementados |
| Pull Request — revisão técnica | Jardel Dargas Silva (Fruki) | Nenhuma — PR aprovada e mergeada | — |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — registro retroativo (projeto executado jun–set/2025) |
