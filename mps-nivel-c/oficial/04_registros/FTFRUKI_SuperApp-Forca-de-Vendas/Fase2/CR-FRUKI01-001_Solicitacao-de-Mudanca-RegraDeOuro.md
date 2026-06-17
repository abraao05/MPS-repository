# Solicitação de Mudança de Escopo — SuperApp Fruki · Pacote Final 24

| Campo | Valor |
|---|---|
| **Documento** | CR-FRUKI01-001 |
| **Projeto** | SuperApp Fruki — Pacote Final 24 |
| **Versão** | 1.0 |
| **Data da solicitação** | 09/10/2025 |
| **Data de aprovação** | 09/10/2025 |
| **Status** | Aprovada e implementada |
| **Solicitante** | Leandro Lottermann (Coordenador de Sistemas — Fruki) |
| **Aprovado por (Timeware)** | Abraão Oliveira (GP) / Tiago Nascimento (COO) |
| **Referência no GCO** | CM-03 — `GCO-FRUKI01-001_Registro-de-Configuracao.md` |

---

## 1. Contexto da solicitação

A proposta comercial "Pacote Final 24", apresentada em 26/09/2025, contemplava originalmente dois módulos: **Pedidos Não Alocados** e **PDV / Rota PDV**. O módulo de Regra de Ouro (à época denominado internamente pela Fruki como "Caixa Preta") não fazia parte do escopo proposto.

Na reunião de kickoff do Pacote Final 24 em 09/10/2025 e na reunião de "Entendimento Demanda Caixa Preta" realizada no mesmo dia, Leandro Lottermann solicitou a inclusão do módulo de composição detalhada da remuneração variável ("Caixa Preta") no escopo do Pacote Final 24, sem custo adicional, como parte do fechamento do roadmap 2025 da Fruki.

---

## 2. Descrição da mudança

| Campo | Detalhe |
|---|---|
| **Tipo de mudança** | Ampliação de escopo |
| **Módulo impactado** | Módulo Regra de Ouro (anteriormente denominado "Caixa Preta") — RF-09, RF-10, RF-11 |
| **Escopo anterior** | Pedidos Não Alocados (RF-05 a RF-08) + PDV / Rota PDV (RF-12 a RF-14) |
| **Escopo após mudança** | Pedidos Não Alocados + **Regra de Ouro** (RF-09 a RF-11) + PDV / Rota PDV |

### Funcionalidades incluídas pela mudança

| RF | Descrição |
|---|---|
| RF-09 | Painel de indicadores de Regra de Ouro — progresso atual vs. meta por indicador de RV |
| RF-10 | Visualização do progresso de atingimento por SKU e por família de produtos |
| RF-11 | Pesquisa de SKU em tempo real com filtro reativo na lista de indicadores |

---

## 3. Análise de impacto

| Dimensão | Impacto | Detalhamento |
|---|---|---|
| Custo | Nenhum | Módulo incluído sem custo adicional conforme alinhamento entre Leandro Lottermann e Tiago Nascimento |
| Prazo | Absorvido | Sprint 2 (novembro/2025) alocada para o módulo Regra de Ouro; prazo final de 15/01/2026 mantido |
| Esforço | +21 SP estimados | Sprint 2 adicionada ao planejamento — refletido em PLA-FRUKI01-002 |
| Riscos | Baixo | Arquitetura React Native já estabelecida; APIs de indicadores de RV disponíveis pela Fruki |
| Requisitos | Adição de 3 RF (RF-09 a RF-11) | Registrado em REQ-FRUKI01-002 |
| Design | Adição de protótipos para o módulo | Brenda Chrystie produziu protótipos validados por Cecília antes da Sprint 2 |

---

## 4. Justificativa da aprovação

A inclusão foi aprovada por ambas as partes pelos seguintes motivos:

1. O módulo Regra de Ouro era uma demanda latente da Fruki — o sistema interno de RV era opaco para os vendedores e havia pressão interna para dar visibilidade à composição do bônus
2. A inclusão sem custo adicional foi viável porque o esforço de desenvolvimento do módulo era compatível com a capacidade disponível no planejamento de 3 sprints mensais
3. A entrega em sprint dedicado (Sprint 2 — novembro/2025) não afetou as sprints de Pedidos Não Alocados (outubro) e PDV (dezembro/janeiro)
4. A arquitetura existente (React Native / Expo + autenticação via `client-id`/`client-secret`) permitia integração com a nova API sem overhead técnico

---

## 5. Rastreabilidade

| Artefato impactado | Tipo de impacto | Referência |
|---|---|---|
| TAP-FRUKI01-002 | Escopo atualizado para incluir o módulo | §2 Escopo macro; §7 Premissas |
| PLA-FRUKI01-002 | Sprint 2 adicionada ao planejamento; +21 SP | §3 Cronograma; §4 Estimativas |
| REQ-FRUKI01-002 | RF-09 a RF-11 incluídos | Seção "Módulo Regra de Ouro" |
| PCP-FRUKI01-002 | Arquitetura do módulo documentada | Seção 2.2 e 3.2 |
| ITP-FRUKI01-002 | Estratégia de integração da API Regra de Ouro | Sprint 2 |
| VV-FRUKI01-002 | Plano de V&V do módulo | Seção Sprint 2 |
| RASTR-FRUKI01-002 | RF-09 a RF-11 rastreados | Matriz de rastreabilidade |
| GCO-FRUKI01-001 | Mudança registrada como CM-03 | §4 Controle de mudanças |
| ATA-FRUKI01-005 | Ata de validação do módulo | Validação Sprint 2 — nov/2025 |

---

## 6. Reuniões de referência

| Data | Reunião | Fireflies ID |
|---|---|---|
| 09/10/2025 | Parceria Fruki ↔ Timeware — kickoff Pacote Final 24 | HWwWGbMe3glWfXgl |
| 09/10/2025 | Entendimento Demanda Caixa Preta — levantamento do módulo | gOI5CeLpUr7VPiyf |

---

## 7. Resultado da mudança

A mudança foi implementada conforme planejado. O Módulo Regra de Ouro foi entregue em novembro/2025 via Pull Request revisada e mergeada por Jardel Dargas Silva. A nomenclatura "Caixa Preta" foi substituída por "Regra de Ouro" durante a revisão de protótipos com Cecília Ribeiro em 22/10/2025 (ver `GDE-FRUKI01-001` — Decisão 2). O módulo integra o build AAB v2.0 entregue em janeiro/2026.

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — registro retroativo (mudança aprovada e implementada em out–nov/2025) |
