# Registro de Revisão por Pares — AASP_CNJ · WorkerAndamentos

| Campo | Valor |
|---|---|
| **Documento/Referência** | REV-AASPCNJ01-001 |
| **Projeto** | AASP_CNJ — WorkerAndamentos: Agente de Captura de Andamentos Processuais |
| **Item revisado** | Código dos workers, CapturaServer e API AndamentosProcessuais |
| **Data** | 11/06/2026 |

---

## 1. Prática de revisão por pares

A revisão por pares é conduzida via Pull Request no Azure DevOps. O merge de branches `feature/*` e `bugfix/*` para `develop` requer revisão de ao menos um membro da equipe além do autor (ver GCO-AASPCNJ01-001 §2). O Pull Request correspondente é o registro da revisão.

## 2. Participantes

| Papel | Identificação |
|---|---|
| Autor | Desenvolvedor Sênior / Desenvolvedor (Suporte) |
| Revisor(es) | Membro da equipe distinto do autor (mínimo 1) |

## 3. Itens revisados (representativos)

| Item | Contexto |
|---|---|
| Worker de requisição CNJ e roteamento por `CodigoFonteAPI` | Fase 4 |
| Lógica de atualização e injeção do token Bearer | Fase 4 |
| Merge na solução AndamentosProcessuais | Fase 5 |

## 4. Apontamentos tratados (exemplos)

| # | Apontamento | Severidade | Tratamento | Situação |
|---|---|---|---|---|
| 1 | Campos do modelo CNJ com dados do TJSP hardcoded | Média | Parametrização por tribunal | Resolvido (BUG-07) |
| 2 | Referências de projeto quebradas após merge | Média | Correção das referências e recompilação | Resolvido (BUG-08) |

## 5. Resultado

| Resultado | Data | Responsável |
|---|---|---|
| Aprovado (merges integrados em `develop` após revisão) | Abr–Mai/2026 | Revisor(es) da equipe |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Registro da prática de revisão por pares, consolidado a partir do Registro de Projeto AASP_CNJ v1.0 (08/06/2026). |
