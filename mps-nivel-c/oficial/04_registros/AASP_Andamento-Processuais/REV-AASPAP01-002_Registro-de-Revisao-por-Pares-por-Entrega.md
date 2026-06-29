# REGISTRO DE REVISÃO POR PARES POR ENTREGA — AASP_ANDAMENTOSPROCESSUAIS

REV-AASPAP01-002 · Versão 1.2 · 24/06/2026 · Timeware Brasil

| Campo | Valor |
|---|---|
| **Documento** | REV-AASPAP01-002 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Gerente de Projeto** | Abraão Oliveira |
| **Versão** | 1.2 |
| **Data** | 24/06/2026 |
| **Processo MPS-SW** | VV (evidência de projeto) |
| **Ferramenta** | GitLab (Merge Requests) |

## 1. Prática de revisão por pares
O projeto é gerido por fases/entregas (sem sprints/story points). Cada entrega corresponde a um Merge Request (MR) no GitLab, integrado em develop (e em prod via release/hotfix) somente após revisão de ao menos dois membros distintos do autor. O MR é o registro da revisão. Este documento consolida a revisão por entrega; o registro consolidado por marco está em REV-AASPAP01-001.

## 2. Revisões por entrega (Merge Requests)
| Entrega / MR | Fase | Autor | Revisor | Apontamentos / resultado |
|---|---|---|---|---|
| !18 — PR 1402: Integração de endpoint para publicação no RabbitMQ | F2–F3 | Raony Chagas | Cézar Hiraki Velázquez; Abraão Oliveira | Aprovado; fila unificada WorkerAndamentos (RabbitMQ) |
| !19 — PR 1401: Criação de controle por instância (processamento background) | F4 | Renan Kiyoshi | Cézar Hiraki Velázquez; Raony Chagas | Aprovado; base do controle por instância (Observacao/erro) |
| !21 — PR 1427: Correção na definição do Status dos processoCapturas | F4 | Raony Chagas | Cézar Hiraki Velázquez; Abraão Oliveira | Aprovado; status/erro por instância (status 8 / parcial) |
| !22 — PR 1455: Verificação e atualização das movimentações no webhook | F3–F4 | Raony Chagas | Cézar Hiraki Velázquez; Abraão Oliveira | Aprovado; movimentações via webhook (RNF03/RNF04) |
| !26 — PR 1720: Integração da API do CNJ | F5 | Raony Chagas | Cézar Hiraki Velázquez; Abraão Oliveira | Aprovado; captura multi-fonte DataJud/CNJ |
| !23 — PR 1465: Correção CapturaLogin como null (nullabilidade) | F5 | Raony Chagas | Cézar Hiraki Velázquez; Abraão Oliveira | Aprovado; contenção pré-go-live (release v1.5.1) |

## 3. Resultado
Todas as entregas foram integradas após revisão por ao menos dois pares além do autor, conforme a política de GCO-AASPAP01-001. Os apontamentos que geraram correção estão associados aos defeitos BUG-01 a BUG-05 (ver REL-VV-AASPAP01-001), resolvidos antes da implantação.

## Histórico de revisões
| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 09/06/2026 | Equipe Técnica | Registro de revisão por pares por entrega (Merge Requests do GitLab), complementando o registro consolidado REV-AASPAP01-001. |
| 1.1 | 24/06/2026 | Equipe Técnica | Reconciliação com o estado atual do GitLab: 2 revisores por entrega (antes 1); hotfix como release v1.5.1 (antes v2.0.1). |
| 1.2 | 24/06/2026 | Equipe Técnica | Entregas reescritas para os Merge Requests reais do GitLab (Fase 3–5), com autor e dois revisores conforme a ferramenta (vínculo !iid real). |
