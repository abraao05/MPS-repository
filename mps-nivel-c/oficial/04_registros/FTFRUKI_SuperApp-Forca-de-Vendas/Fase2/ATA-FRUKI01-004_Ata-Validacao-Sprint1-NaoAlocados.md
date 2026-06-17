# Ata de Validação — Sprint 1 · Pedidos Não Alocados — SuperApp Fruki · Pacote Final 24

| Campo | Valor |
|---|---|
| **Documento** | ATA-FRUKI01-004 |
| **Projeto** | SuperApp Fruki — Pacote Final 24 |
| **Versão** | 1.0 |
| **Data** | 24/10/2025 |
| **Tipo** | Reunião de validação de protótipo e aceite de sprint |
| **Canal** | Microsoft Teams |
| **Fireflies** | Não registrado — validação conduzida via APK + feedback escrito por WhatsApp/e-mail |

---

## 1. Participantes

| Nome | Empresa | Papel |
|---|---|---|
| Abraão Oliveira | Timeware | GP / Product Owner |
| Brenda Chrystie | Timeware | UX / Analista de negócio |
| Luca Watson | Timeware | Desenvolvedor |
| Cecília Ribeiro | Fruki | Responsável pelo produto (cliente) |
| Jardel Dargas Silva | Fruki | Tech lead / revisor de PR |

---

## 2. Pauta

1. Apresentação do APK de homologação — Módulo Pedidos Não Alocados
2. Walkthrough das funcionalidades: RF-05 (listagem), RF-06 (detalhamento), RF-07 (filtros), RF-08 (exportação CSV)
3. Validação dos cenários funcionais com dados reais de campo
4. Confirmação de critérios de aceite para merge da PR #57

---

## 3. Contexto da sprint

O Módulo Pedidos Não Alocados foi desenvolvido na branch `feature/nao-alocados` do repositório Azure DevOps Fruki. A sprint teve duração de 4 semanas (outubro/2025), com entrega de 22 SP (estimativa: 21 SP). O esforço adicional de 1 SP decorreu da normalização de formato não padronizado detectada na resposta da API durante a integração — implementada em `pedidosNaoAlocadosService.ts` sem solicitação de correção ao time Fruki.

O APK de homologação foi gerado via Expo em 23/10/2025 e distribuído para Cecília Ribeiro via link Expo antes desta sessão de validação.

---

## 4. Cenários validados

| # | Cenário | RF | Resultado | Observação |
|---|---|---|---|---|
| C-01 | Listagem de pedidos não alocados do representante logado | RF-05 | Aprovado | Dados reais carregados corretamente; loading state exibido durante chamada à API |
| C-02 | Detalhamento de pedido individual (cliente, produto, volume, valor) | RF-06 | Aprovado | Layout consistente com protótipo Figma aprovado |
| C-03 | Filtro por período (seletor de data) | RF-07 | Aprovado | Filtro funcional; lista atualizada sem reload da tela |
| C-04 | Exportação da lista para CSV | RF-08 | Aprovado | Arquivo gerado e acessível via compartilhamento nativo Android |
| C-05 | Tela vazia quando não há pedidos não alocados no período | RF-05 | Aprovado | Mensagem amigável exibida; sem tela em branco |
| C-06 | Erro de API — exibição de mensagem de erro e botão de recarregar | RF-05 | Aprovado | Tratamento de erro implementado; usuário pode tentar novamente |

---

## 5. Problemas identificados e resoluções

Nenhum problema crítico identificado durante a validação. Cecília Ribeiro solicitou ajuste cosmético no espaçamento do card de pedido — corrigido pelo desenvolvedor Luca Watson antes do merge da PR.

---

## 6. Decisões tomadas

| Decisão | Responsável |
|---|---|
| Aprovação do módulo Pedidos Não Alocados para merge | Cecília Ribeiro (cliente) |
| Autorização de merge da PR #57 | Jardel Dargas Silva (tech lead Fruki) |
| Nenhuma solicitação de correção de API encaminhada ao time Fruki; normalização mantida no front-end | Abraão Oliveira |

---

## 7. Encaminhamentos

| # | Ação | Responsável | Prazo |
|---|---|---|---|
| 1 | Merge da PR #57 após aprovação de Jardel | Jardel Dargas Silva | 25/10/2025 |
| 2 | Início do desenvolvimento do Módulo Regra de Ouro (Sprint 2) | Luca Watson / Thiago | 27/10/2025 |
| 3 | Compartilhar protótipo do Módulo Regra de Ouro com Cecília para validação antes da sprint | Brenda Chrystie | 27/10/2025 |

---

## 8. Resultado da sprint

- **Status:** Concluída e aprovada
- **PR mergeada:** PR #57 — mergeada por Jardel em 25/10/2025
- **Baseline estabelecida:** BL-02 — Módulo Pedidos Não Alocados (ver `GCO-FRUKI01-001`)

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 24/10/2025 | Abraão Oliveira | Versão inicial — registro retroativo (validação realizada em out/2025) |
