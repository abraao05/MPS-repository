# Registro de Revisão por Pares — AASP_AndamentosProcessuais

| Campo | Valor |
|---|---|
| **Documento** | REV-AASPAP01-001 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Item revisado** | Código da API AndamentosProcessuais e do CapturaServer |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto** | Cezar Hiraki Velazquez |
| **Processo MPS-SW** | VV (revisão por pares — evidência de projeto) |

---

## 1. Prática de revisão por pares

A revisão por pares é conduzida via Pull Request no Azure DevOps. O merge de branches `feature/*` e `bugfix/*` para `develop` (e de `release` para `main`) requer revisão de ao menos um membro da equipe além do autor (ver GCO-AASPAP01-001 §2). O Pull Request correspondente é o registro da revisão. A estratégia de branching segue GitFlow: `main` (default) + `develop` + `feature/<ÉPICO>-NNN`.

## 2. Participantes

| Papel | Identificação |
|---|---|
| Autor | Raony Chagas (Dev Sênior) / Mateus Veloso (Dev Suporte, a partir de Abr/2026) |
| Revisor(es) | Cezar Hiraki Velazquez (revisor de código; mínimo 1 membro distinto do autor) |

## 3. Itens revisados (representativos)

| Item | Contexto |
|---|---|
| Migração do CapturaServer da fila EprocTjsp para a fila unificada WorkerAndamentos | Fase 2 (D02) |
| Parametrização do webhook para suporte multi-fonte | Fase 3 (D03) |
| Histórico de movimentações por inativação de registro | Fase 3 (D04) |
| Controladores específicos por parceira (Solucionário, Botmax) na camada da API | Fase 4 (D05, D06) |
| Tratamento de erro e campo `Segredo` por instância | Fase 4 (D07) |
| Merge na solução AndamentosProcessuais | Fase 4 |

## 4. Apontamentos tratados (exemplos)

| # | Apontamento | Severidade | Tratamento | Situação |
|---|---|---|---|---|
| 1 | Campos do modelo com dados de tribunal fixos no webhook multi-fonte | Média | Parametrização dos campos do modelo | Resolvido (BUG-01) |
| 2 | Referências de projeto quebradas após merge | Média | Correção das referências e recompilação | Resolvido (BUG-02) |
| 3 | Ordem incorreta no fluxo de desligamento das parceiras | Média | Correção da ordem das operações | Resolvido (BUG-04) |

## 5. Resultado

| Resultado | Data | Responsável |
|---|---|---|
| Aprovado (merges integrados em `develop` após revisão) | Abr–Jun/2026 | Cezar Hiraki Velazquez (revisor) |

---


## Evidências

- `devops_andamentos_prs.png` — Pull Requests concluídos (code review)
- `devops_andamentos_pr_detail_1.png` — Detalhe de PR aprovado (1)
- `devops_andamentos_pr_detail_2.png` — Detalhe de PR aprovado (2)

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Registro da prática de revisão por pares, consolidado a partir do Registro de Projeto AASP_AndamentosProcessuais e do INTAKE-PROJETO_AASPAP01 v1.0. |
