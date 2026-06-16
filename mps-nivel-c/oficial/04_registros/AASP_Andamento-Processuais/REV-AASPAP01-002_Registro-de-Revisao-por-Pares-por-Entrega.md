# REGISTRO DE REVISÃO POR PARES POR ENTREGA — AASP_ANDAMENTOSPROCESSUAIS

REV-AASPAP01-002 · Versão 1.0 · 11/06/2026 · Timeware Brasil

| Campo | Valor |
|---|---|
| **Documento** | REV-AASPAP01-002 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Gerente de Projeto** | Abraão Oliveira |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Processo MPS-SW** | VV (evidência de projeto) |
| **Ferramenta** | GitLab (Merge Requests) |

## 1. Prática de revisão por pares
O projeto é gerido por fases/entregas (sem sprints/story points). Cada entrega corresponde a um Merge Request (MR) no GitLab, integrado em develop (e em prod via release/hotfix) somente após revisão de ao menos um membro distinto do autor. O MR é o registro da revisão. Este documento consolida a revisão por entrega; o registro consolidado por marco está em REV-AASPAP01-001.

## 2. Revisões por entrega (Merge Requests)
| Entrega / MR | Fase | Autor | Revisor | Apontamentos / resultado |
|---|---|---|---|---|
| ERRO-1 — campo Observacao por instância | F3–F4 | Raony Chagas | Cézar Hiraki Velázquez | Aprovado; trata erro por instância (RF07/RF08) |
| NUP-1 — NUP inválido (status 8 / resposta 10) | F4 | Mateus Veloso | Cézar Hiraki Velázquez | Aprovado; BUG-04 tratado na revisão |
| RETRY-1 — retry no envio do webhook | F4 | Raony Chagas | Cézar Hiraki Velázquez | Aprovado; não-perda de dados (RNF04) |
| REGR-1 — regressão EPROC/ESAJ | F4 | Raony Chagas | Cézar Hiraki Velázquez | Aprovado; sem regressão (CT-12) |
| hotfix — nullabilidade em CapturaLogin (produção) | F5 | Raony Chagas | Cézar Hiraki Velázquez | Aprovado; contenção pré-go-live (release v2.0.1) |

## 3. Resultado
Todas as entregas foram integradas após revisão por ao menos um par além do autor, conforme a política de GCO-AASPAP01-001. Os apontamentos que geraram correção estão associados aos defeitos BUG-01 a BUG-05 (ver REL-VV-AASPAP01-001), resolvidos antes da implantação.

## Histórico de revisões
| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Registro de revisão por pares por entrega (Merge Requests do GitLab), complementando o registro consolidado REV-AASPAP01-001. |
