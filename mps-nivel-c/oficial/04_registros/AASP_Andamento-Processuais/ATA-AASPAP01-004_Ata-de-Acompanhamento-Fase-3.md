# ATA DE ACOMPANHAMENTO — Fase 3 — Refatoração para suporte ao CNJ

ATA-AASPAP01-004 · Versão 1.0 · 29/05/2026 · Timeware Brasil

| Campo | Valor |
|---|---|
| **Documento** | ATA-AASPAP01-004 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Gerente de Projeto** | Abraão Oliveira |
| **Versão** | 1.0 |
| **Data** | 29/05/2026 |
| **Tipo** | Reunião de acompanhamento de projeto (cadência por fase/marco) |
| **Local / meio** | Videoconferência |
| **Responsável pela ata** | Abraão Oliveira |

## 1. Participantes
| Nome | Papel |
|---|---|
| Abraão Oliveira | Gerente de Projeto |
| Cézar Hiraki Velázquez | Tech Lead / DevOps / Arquiteto |
| Raony Chagas | Desenvolvedor Sênior |
| Mateus Veloso | Desenvolvedor (Suporte) |
| Marcos Correa Fernandez Turnes | Sponsor / PO (AASP) |

## 2. Pauta
- Webhook multi-fonte e roteamento por CodigoFonteAPI
- Histórico por instância e desligamento das parceiras
- Defeito BUG-01

## 3. Discussões e definições
Concluída a Fase 3: webhook parametrizado para múltiplas fontes, roteamento por CodigoFonteAPI, histórico de movimentações por inativação de registro e verificação/desligamento nas APIs parceiras (Solucionário, Botmax) após captura via CNJ. BUG-01 (parametrização dos campos) identificado e corrigido. Esforço ~144 h ante 130 h (+11%).

## 4. Decisões e aceites
| Decisão / aceite | Responsável | Data |
|---|---|---|
| Aceite da Fase 3 (refatoração multi-fonte CNJ) | Marcos Correa Fernandez Turnes | 29/05/2026 |

## 5. Ações (follow-up)
| Ação | Responsável | Prazo |
|---|---|---|
| Implementar tratamento de erros e segredo por instância e concluir a validação (Fase 4) | Raony Chagas / Caroline Sousa | Jun/2026 |

## 6. Próximos passos
Fase 4 — Tratamento de erros e validação.

## Histórico de revisões
| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 29/05/2026 | Gerente de Projeto | Ata de acompanhamento da Fase 3, consolidada a partir de MED-AASPAP01-001 §3-4 e de REL-VV-AASPAP01-001. |
