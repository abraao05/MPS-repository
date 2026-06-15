# Ata de Reunião — Alinhamento técnico do fluxo de captura API CNJ

| Campo | Valor |
|---|---|
| **Reunião** | Alinhamento e entendimento do fluxo da API CNJ |
| **Projeto / contexto** | AASP_CNJ — WorkerAndamentos |
| **Data** | 07/04/2026 |
| **Local / meio** | Videoconferência |
| **Responsável pela ata** | Cezar Hiraki Velazquez |

---

## 1. Participantes

| Nome | Papel | Organização |
|---|---|---|
| Cezar Hiraki Velazquez | Gerente de Projeto / Tech Lead | Timeware |
| Raony Chagas | Desenvolvedor Sênior (Principal) | Timeware |
| Renan Kiyoshi | Desenvolvedor (Suporte) | Timeware |
| — | Time de Desenvolvimento | Timeware |

## 2. Pauta

- Apresentação do novo fluxo de captura via API DataJud/CNJ.
- Definição de responsabilidades para a Fase 4.
- Integração do desenvolvedor de suporte incorporado ao time.

## 3. Discussões e definições

O Gerente de Projeto apresentou o fluxo completo da nova arquitetura: funcionamento da API DataJud, lógica de roteamento por `CodigoFonteAPI`, mecanismos de fallback (CNJ → EPROC/ESAJ → parceiras) e modelo de dados de gravação no Elasticsearch (`IModelElastic`). Foi alinhado o enfileiramento unificado no RabbitMQ e a gestão compartilhada do token Bearer.

## 4. Decisões e aceites

| Decisão / aceite | Responsável | Data |
|---|---|---|
| Adotar a DataJud/CNJ como fonte primária universal (D02) | Cezar Hiraki Velazquez / time | 07/04/2026 |
| Unificar a fila RabbitMQ (D03) | Cezar Hiraki Velazquez / time | 07/04/2026 |
| Token Bearer compartilhado em `PonteAPI` (D04) | Raony Chagas | 07/04/2026 |
| Normalização do JSON CNJ no worker (D05) | Raony Chagas | 07/04/2026 |

(Decisões detalhadas em GDE-AASPCNJ01-001.)

## 5. Ações (follow-up)

| Ação | Responsável | Prazo |
|---|---|---|
| Desenvolver o worker de requisição CNJ | Raony Chagas | Abr/2026 |
| Implementar enfileiramento unificado com verificação de `CodigoFonteAPI` | Time de Desenvolvimento | Abr/2026 |
| Onboarding do desenvolvedor de suporte no fluxo | Cezar Hiraki Velazquez | Abr/2026 |

## 6. Próximos passos

Início da Fase 4 (Desenvolvimento CNJ): captura via DataJud, fluxo de gravação via webhook e lógica de fallback.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Ata do alinhamento de 07/04/2026 reconstituída a partir do Registro de Projeto AASP_CNJ v1.0 (08/06/2026). |
