# Estratégia de Integração — SuperApp Fruki · Pacote 1 — Módulo Metas e RV

| Campo | Valor |
|---|---|
| **Documento** | ITP-FRUKI01-001 |
| **Projeto** | SuperApp Fruki — Pacote 1 — Módulo Metas e Remuneração Variável |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |

---

## 1. Componentes a integrar

| Componente | Descrição |
|---|---|
| SuperApp Fruki (front-end React Native) | Aplicativo mobile existente; novos módulos de Metas/RV adicionados via branch `feature/novos-recursos-superapp` |
| API `/acompanhamentoMetasFamilias` | API REST Fruki — retorna metas e percentual de atingimento por família de produtos |
| API `/acompanhamentoMetasItens` | API REST Fruki — retorna metas e atingimento por item (SKU) |
| API `/acompanhamentoForaDeRota` | API REST Fruki — retorna representantes fora de rota no dia |
| API `/acompanhamentoVisitas` | API REST Fruki — retorna visitas realizadas no dia por representante |

---

## 2. Interfaces

| Interface | Entre | Tipo / contrato |
|---|---|---|
| Metas por família | `MetasScreen.tsx` ↔ API `/acompanhamentoMetasFamilias/{rep}/{periodo}/{tipo}` | REST GET — resposta JSON; autenticação via headers `client-id` / `client-secret` |
| Metas por item/SKU | `MetasItensScreen.tsx` ↔ API `/acompanhamentoMetasItens/{rep}/{periodo}/{tipo}` | REST GET — mesmo padrão de autenticação |
| Fora de rota | `VisitasScreen.tsx` ↔ API `/acompanhamentoForaDeRota/{rep}/{data}` | REST GET — parâmetro `data` no formato `YYYY-MM-DD` |
| Visitas do dia | `VisitasScreen.tsx` ↔ API `/acompanhamentoVisitas/{rep}/{data}` | REST GET — mesmo padrão |
| Normalização front-end | `metasService.ts` ↔ respostas das APIs | Serviço interno que deduplica famílias e aplica ordenação alfabética antes de repassar ao estado |

**Base URL:** `https://api.fruki.com.br/`
**Autenticação:** headers `client-id` e `client-secret` em todas as requisições; credenciais fornecidas por Jardel em 26/06/2025.

---

## 3. Estratégia e ordem de integração

A integração é incremental, seguindo a ordem de prioridade das telas:

1. **API de metas por família** — integrada primeiro por ser a tela principal do módulo; permite validar o padrão de autenticação e tratamento de loading state com a API de maior volume de dados
2. **API de metas por item (SKU)** — integrada em sequência após a família; reutiliza o mesmo padrão de serviço
3. **APIs de visitas e fora de rota** — integradas em conjunto; dependem do mesmo parâmetro `data` e têm payload mais simples

Todas as integrações são desenvolvidas na branch `feature/novos-recursos-superapp` do repositório Azure DevOps da Fruki, entregues via Pull Request revisada pelo Jardel antes do merge na branch principal.

---

## 4. Ambiente de integração

| Ambiente | Ferramenta | Uso |
|---|---|---|
| Desenvolvimento | Branch `feature/novos-recursos-superapp` no Azure DevOps Fruki | Desenvolvimento e integração local das telas com as APIs reais |
| Homologação / stage | APK gerado via Expo | Build distribuído para vendedores selecionados antes do aceite; validação com dados reais de campo |
| Produção | Merge via PR revisada por Jardel + Play Store (responsabilidade Fruki) | Código promovido após aprovação; APK/AAB publicado pelo time Fruki |

---

## 5. Critérios de prontidão para integração

Para cada módulo ser integrado (merge da PR):

- [x] Tela desenvolvida e testada localmente com dados reais da API
- [x] Tratamento de loading state implementado (skeleton screen enquanto aguarda resposta)
- [x] Normalização e deduplicação de dados implementada em `metasService.ts`
- [x] Cenários sad path implementados (lista vazia, erro de API, latência)
- [x] APK de teste gerado e validado em dispositivo Android físico
- [x] Code review aprovado por Jardel Dargas Silva (Fruki) via Pull Request

---

## 6. Testes do produto integrado

Referência: `VV-FRUKI01-001_Plano-VeV.md`

- **Testes manuais por ciclo de desenvolvimento:** cenários happy path e sad path executados em dispositivo Android físico antes de cada entrega
- **Piloto com vendedores selecionados (05/08/2025):** validação do produto integrado com dados reais de campo; revelou duplicação de famílias e cálculo inconsistente de positivação — corrigidos antes do aceite
- **Revisão de PR:** Jardel Dargas Silva verifica a integração técnica (autenticação, mapeamento de dados, tratamento de erros) antes do merge

---

## 7. Entrega e material de apoio

| Item entregue | Forma |
|---|---|
| Código-fonte do Módulo Metas/RV | Pull Request no repositório Azure DevOps da Fruki — `feature/novos-recursos-superapp` → `main` |
| APK de teste (homologação) | Build Expo distribuído via link para validação com vendedores |
| Documentação de integração | Seção 2.3 do `PCP-FRUKI01-001_Documento-de-Design.md` |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — registro retroativo (projeto executado jun–set/2025) |
