# Registro de Garantia da Qualidade — Milhas3

| Campo | Valor |
|---|---|
| **Documento** | GQA-MILHASFACIL01-001 — Registro de GQA |
| **Versão** | 1.0 |
| **Data** | 16/11/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Milhas3 — Plataforma de Busca e Monitoramento de Milhas |
| **Cliente** | Hub de Milhas (Felipe) |
| **GQA de Processo** | COO (Operações) |
| **Processo MPS-SW** | GQA — Garantia da Qualidade |

---

## 1. Objetivo

Registrar as verificações independentes de aderência ao Processo Padrão Organizacional realizadas ao longo do projeto Milhas3, conforme EST-GPC-001.

## 2. Auditorias realizadas

### 2.1 GQA-P01 — Verificação pós-kickoff

| Campo | Valor |
|---|---|
| Data | 30/05/2025 |
| Fase verificada | Abertura e planejamento (Sprint 0) |
| Auditor | COO (Operações) |

| Item verificado | Resultado | Observação |
|---|---|---|
| TAP gerado e aprovado pelo cliente | Conforme | TAP-MILHASFACIL01-001 v1.0 aprovado em 16/05/2025 |
| Plano de Projeto aprovado e baseline estabelecida (GPR 13) | Conforme | PLA-MILHASFACIL01-001 v1.0 — baseline em 16/05/2025 |
| Adaptação do processo registrada (GPR 2) | Conforme | ADAP-MILHASFACIL01-001 v1.0 |
| Requisitos levantados e confirmados pelo cliente (REQ 1, REQ 3) | Conforme | REQ-MILHASFACIL01-001 v1.0 — confirmação em 16/05/2025 |
| Decisão arquitetural registrada (GDE) | Conforme | GDE-MILHASFACIL01-001 v1.0 — Selenium + bypass Akamai |
| GCO configurado (branches, PR policy, CI/CD) | Conforme | GCO-MILHASFACIL01-001 v1.0; configuração validada no Azure DevOps |
| Equipe com perfil adequado para a stack | Conforme | Java / Angular / Selenium — equipe com experiência comprovada |
| VV plano elaborado | Conforme | VV-MILHASFACIL01-001 v1.0 |

Não conformidades abertas: nenhuma.

### 2.2 GQA-P02 — Verificação meio de projeto

| Campo | Valor |
|---|---|
| Data | 08/08/2025 |
| Fase verificada | Sprints 1–6 (motor de rastreamento, alertas, busca de interface) |
| Auditor | COO (Operações) |

| Item verificado | Resultado | Observação |
|---|---|---|
| Motor de rastreamento testado nos 5 programas | Conforme | Sprints 2–4 concluídas; evidências de teste ao vivo arquivadas no Azure DevOps |
| PR policy ativa e respeitada (GCO) | Conforme | 100% dos merges em `develop` e `main` via PR aprovado |
| Backlog atualizado e priorizado | Conforme | Azure DevOps Boards — itens fechados por sprint |
| Rastreabilidade RF → Sprint → entrega atualizada | Conforme | RASTR-MILHASFACIL01-001 atualizado ao fim de cada sprint |
| Cobertura de testes unitários back-end ≥ 70% | Conforme | Pipeline CI/CD reportando 74% — relatório Jacoco arquivado |
| Sprint Reviews realizadas com cliente | Conforme | Sprints 1–6: reviews com Felipe realizadas quinzenalmente |
| Ausência de secrets no repositório | Conforme | Scan automatizado no pipeline — sem ocorrências |

Não conformidades abertas: nenhuma.

### 2.3 GQA-P03 — Verificação pós-encerramento

| Campo | Valor |
|---|---|
| Data | 16/11/2025 |
| Fase verificada | Encerramento do projeto |
| Auditor | COO (Operações) |

| Item verificado | Resultado | Observação |
|---|---|---|
| Todos os RF de prioridade Alta entregues e aceitos | Conforme | ATA-MILHASFACIL01-002 — aceite formal em 16/11/2025 |
| TAE gerado | Conforme | TAE-MILHASFACIL01-001 v1.0 |
| Lições aprendidas registradas | Conforme | LI-MILHASFACIL01-001 v1.0 |
| Medições registradas | Conforme | MED-MILHASFACIL01-001 v1.0 |
| Tag de release criada no repositório | Conforme | Tag `v1.0.0` criada após aceite |
| Documentação MPS-SW completa | Conforme | Todos os documentos do projeto presentes em `04_registros/MILHASFACIL_Plataforma-Milhas3/` |
| Acesso ao repositório transferido ao cliente | Conforme | Transferência registrada na ATA-MILHASFACIL01-002 |

Não conformidades abertas: nenhuma.

## 3. Resumo geral

| GQA | Data | NC abertas | NC fechadas | Resultado |
|---|---|---|---|---|
| GQA-P01 | 30/05/2025 | 0 | 0 | Aprovado |
| GQA-P02 | 08/08/2025 | 0 | 0 | Aprovado |
| GQA-P03 | 16/11/2025 | 0 | 0 | Aprovado |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 16/11/2025 | Time de Melhoria Contínua | Documento final — projeto encerrado |
