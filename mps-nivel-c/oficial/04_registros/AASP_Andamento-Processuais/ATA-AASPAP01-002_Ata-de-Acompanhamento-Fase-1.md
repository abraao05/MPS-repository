# ATA DE ACOMPANHAMENTO — Fase 1 — Webhook e CapturaServer (EPROC)

ATA-AASPAP01-002 · Versão 1.0 · 27/02/2026 · Timeware Brasil

| Campo | Valor |
|---|---|
| **Documento** | ATA-AASPAP01-002 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Gerente de Projeto** | Abraão Oliveira |
| **Versão** | 1.0 |
| **Data** | 27/02/2026 |
| **Tipo** | Reunião de acompanhamento de projeto (cadência por fase/marco) |
| **Local / meio** | Videoconferência |
| **Responsável pela ata** | Abraão Oliveira |

## 1. Participantes
| Nome | Papel |
|---|---|
| Abraão Oliveira | Gerente de Projeto |
| Cézar Hiraki Velázquez | Tech Lead / DevOps / Arquiteto |
| Raony Chagas | Desenvolvedor Sênior |
| Marcos Correa Fernandez Turnes | Sponsor / PO (AASP) |

## 2. Pauta
- Entregas da Fase 1 (webhook EPROC e publicação do CapturaServer na fila)
- Esforço estimado × realizado
- Riscos e próximos passos

## 3. Discussões e definições
Concluída a Fase 1: o CapturaServer passou a publicar na fila WorkerAndamentos (RabbitMQ) com SegmentoTribunal e o webhook de indexação foi preparado para o fluxo EPROC. Esforço realizado ~48 h ante 44 h estimadas (+9%), sem defeitos no período. Sem regressão no fluxo em produção.

## 4. Decisões e aceites
| Decisão / aceite | Responsável | Data |
|---|---|---|
| Aceite da Fase 1 (fluxo EPROC) | Marcos Correa Fernandez Turnes | 27/02/2026 |

## 5. Ações (follow-up)
| Ação | Responsável | Prazo |
|---|---|---|
| Iniciar estabilização e integração unificada via RabbitMQ (Fase 2) | Raony Chagas / Cézar Hiraki Velázquez | Mar/2026 |

## 6. Próximos passos
Fase 2 — Estabilização e integração RabbitMQ.

## Histórico de revisões
| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 27/02/2026 | Gerente de Projeto | Ata de acompanhamento da Fase 1, consolidada a partir de MED-AASPAP01-001 §3 e do acompanhamento no GitLab. |
