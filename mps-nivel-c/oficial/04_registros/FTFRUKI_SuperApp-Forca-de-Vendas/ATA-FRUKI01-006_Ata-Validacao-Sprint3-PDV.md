# Ata de Validação — Sprint 3 · PDV / Rota PDV — SuperApp Fruki · Pacote Final 24

| Campo | Valor |
|---|---|
| **Documento** | ATA-FRUKI01-006 |
| **Projeto** | SuperApp Fruki — Pacote Final 24 |
| **Versão** | 1.0 |
| **Data** | 14/01/2026 |
| **Tipo** | Reunião de validação final + aceite de sprint |
| **Canal** | Microsoft Teams |
| **Fireflies** | Não registrado — validação conduzida via APK + feedback escrito por WhatsApp/e-mail |

---

## 1. Participantes

| Nome | Empresa | Papel |
|---|---|---|
| Abraão Oliveira | Timeware | GP / Product Owner |
| Brenda Chrystie | Timeware | UX / Analista de negócio |
| Luca Watson | Timeware | Desenvolvedor |
| Thiago Gomes | Timeware | Desenvolvedor |
| Cecília Ribeiro | Fruki | Responsável pelo produto (cliente) |
| Leandro Lottermann | Fruki | Sponsor / responsável comercial |
| Jardel Dargas Silva | Fruki | Tech lead / revisor de PR |
| Alexsandro de Vargas Braga | Fruki | Responsável pelo formulário PDV |

---

## 2. Pauta

1. Apresentação do APK de homologação — Módulo PDV / Rota PDV
2. Walkthrough das funcionalidades: RF-12 (lista de PDVs da rota), RF-13 (formulário de pesquisa de execução), RF-14 (geolocalização obrigatória)
3. Validação em campo com dados reais da API Rota PDV
4. Confirmação de critérios de aceite para merge da PR PDV e geração do AAB v2.0

---

## 3. Contexto da sprint

O Módulo PDV / Rota PDV foi desenvolvido na branch `feature/pdv-rota` do repositório Azure DevOps Fruki. A sprint teve duração estendida (dezembro/2025–janeiro/2026), com entrega de ~10 SP na fase de interface (dezembro/2025) e integração completa após recebimento da API Rota PDV por Jardel em 08/01/2026. O formulário PDV com 20 perguntas foi recebido de Alexsandro de Vargas Braga em 04/12/2025.

O atraso de ~3 semanas na API Rota PDV foi absorvido pela estratégia de desenvolvimento com mock de dados — a interface foi desenvolvida e validada estruturalmente antes da integração real. Integração completa com API real concluída na semana de 08/01/2026 a 14/01/2026.

O APK de homologação final foi gerado via Expo em 13/01/2026 e distribuído para Cecília Ribeiro e Alexsandro de Vargas Braga via link Expo antes desta sessão de validação. Versionamento do app incrementado para 2.0 (`app.json` / `package.json`).

---

## 4. Cenários validados

| # | Cenário | RF | Resultado | Observação |
|---|---|---|---|---|
| C-01 | Lista de PDVs da rota do representante com status (visitado/pendente) | RF-12 | Aprovado | Dados reais da API Rota PDV GET carregados corretamente |
| C-02 | Abertura do formulário de pesquisa de execução a partir de um PDV | RF-13 | Aprovado | Formulário com 20 perguntas conforme lista de Alexsandro |
| C-03 | Preenchimento e envio do formulário PDV com geolocalização | RF-13 / RF-14 | Aprovado | Payload enviado via POST com lat/long do dispositivo; resposta 200 OK da API |
| C-04 | Bloqueio de envio quando GPS indisponível | RF-14 | Aprovado | Mensagem de alerta exibida; botão de submit desabilitado sem permissão GPS |
| C-05 | Solicitação de permissão de geolocalização antes do primeiro submit | RF-14 | Aprovado | Dialog nativo Android exibido na primeira tentativa de envio |
| C-06 | Atualização de status do PDV para "visitado" após submit do formulário | RF-12 | Aprovado | Status atualizado na lista após envio bem-sucedido |
| C-07 | Loading state durante carregamento da lista de PDVs | RF-12 | Aprovado | Skeleton screen consistente com demais módulos |
| C-08 | Tela de erro quando GPS negado permanentemente | RF-14 | Aprovado | Mensagem orientando usuário a habilitar GPS nas configurações |
| C-09 | Tela vazia quando rota não possui PDVs no dia | RF-12 | Aprovado | Mensagem amigável; sem crash |

---

## 5. Problemas identificados e resoluções

Nenhum problema crítico identificado. Alexsandro de Vargas Braga solicitou reordenação de duas perguntas do formulário para alinhar com o fluxo de visita presencial — ajustado por Luca Watson antes do merge final.

---

## 6. Decisões tomadas

| Decisão | Responsável |
|---|---|
| Aprovação do módulo PDV / Rota PDV para merge | Cecília Ribeiro / Alexsandro de Vargas Braga (cliente) |
| Autorização de merge da PR PDV e geração do AAB v2.0 | Jardel Dargas Silva (tech lead Fruki) |
| Versão do app incrementada para 2.0 — build final para Play Store | Abraão Oliveira / Jardel Dargas Silva |
| Aceite formal do Pacote Final 24 confirmado para 15/01/2026 | Leandro Lottermann |

---

## 7. Encaminhamentos

| # | Ação | Responsável | Prazo |
|---|---|---|---|
| 1 | Merge da PR PDV após aprovação de Jardel | Jardel Dargas Silva | Jan/2026 |
| 2 | Geração do AAB v2.0 para publicação na Play Store | Luca Watson | Jan/2026 |
| 3 | Entrega do AAB v2.0 ao time Fruki para publicação | Abraão Oliveira | Jan/2026 |
| 4 | Reunião de aceite formal do Pacote Final 24 via Microsoft Teams | Abraão Oliveira / Leandro Lottermann | 15/01/2026 |

---

## 8. Resultado da sprint

- **Status:** Concluída e aprovada
- **PR mergeada:** PR PDV — mergeada por Jardel em Jan/2026
- **Build gerado:** AAB v2.0 — entregue ao time Fruki para publicação na Play Store
- **Baselines estabelecidas:** BL-04 (Módulo PDV / Rota PDV) e BL-05 (Release v2.0) — ver `GCO-FRUKI01-001`

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — registro retroativo (validação realizada em jan/2026) |
