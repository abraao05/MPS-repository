# Relatório de Acompanhamento — Milhas3

| Campo | Valor |
|---|---|
| **Documento** | RAC-MILHASFACIL01-001 — Relatório de Acompanhamento |
| **Versão** | 1.0 |
| **Data** | 16/11/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Milhas3 — Plataforma de Busca e Monitoramento de Milhas |
| **Cliente** | Hub de Milhas (Felipe) |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR — Gerência de Projeto |

---

## 1. Resumo executivo

O projeto **Milhas3** foi concluído e aceito formalmente pelo cliente em **16/11/2025**, dentro do prazo contratado. Todos os 16 requisitos funcionais foram entregues — prioridade Alta completamente atendida. O motor de rastreamento via Selenium opera de forma estável nos cinco programas de fidelidade contratados, com taxa de sucesso superior a 90% em todos os programas.

## 2. Status geral ao encerramento

| Dimensão | Status | Observação |
|---|---|---|
| Prazo | No prazo | Aceite em 16/11/2025 conforme planejado |
| Escopo | Completo | RF-01 a RF-16 entregues |
| Qualidade | Aprovado | GQA-P03 sem não conformidades; testes homologados pelo cliente |
| Riscos | Gerenciado | R-01 materializado parcialmente (ajuste de seletores Sprint 7); R-02 não materializado |
| Budget | [A CONFIRMAR] | Sem informação de custo para este documento |

## 3. Progresso por sprint

| Sprint | Período | Foco principal | Status |
|---|---|---|---|
| Sprint 0 | 16/05–30/05/2025 | Setup de infra, repositórios, pipeline CI/CD base | Concluído |
| Sprint 1 | 02/06–13/06/2025 | Autenticação JWT, arquitetura Spring Boot + Angular | Concluído |
| Sprint 2 | 16/06–27/06/2025 | Motor de rastreamento — LATAM Pass | Concluído |
| Sprint 3 | 30/06–11/07/2025 | Motor de rastreamento — Smiles + TudoAzul | Concluído |
| Sprint 4 | 14/07–25/07/2025 | Motor de rastreamento — TAP + Iberia | Concluído |
| Sprint 5 | 28/07–08/08/2025 | Interface de busca Angular — integração ponta a ponta | Concluído |
| Sprint 6 | 11/08–22/08/2025 | Assinatura de rotas + alertas automáticos | Concluído |
| Sprint 7 | 25/08–05/09/2025 | Histórico de buscas + preferências; ajuste seletores Smiles | Concluído |
| Sprint 8 | 08/09–19/09/2025 | Notificações in-app + e-mail | Concluído |
| Sprint 9 | 22/09–03/10/2025 | Chat / suporte integrado | Concluído |
| Sprint 10 | 06/10–17/10/2025 | Testes E2E (Cypress) + testes de carga (JMeter) + ajustes | Concluído |
| Sprint 11 | 20/10–31/10/2025 | Homologação com cliente — fase 1 | Concluído |
| Sprint 12 | 03/11–14/11/2025 | Ajustes de homologação fase 2 + entrega final | Concluído |
| Aceite | 16/11/2025 | Reunião de aceite formal (ATA-MILHASFACIL01-002) | Concluído |

## 4. Indicadores de acompanhamento

| Indicador | Planejado | Realizado |
|---|---|---|
| Story points totais | ~650 SP | [A CONFIRMAR] SP |
| Sprints executadas | 13 + Sprint 0 | 13 + Sprint 0 |
| Defeitos críticos ao encerramento | 0 | 0 |
| Cobertura de testes unitários | ≥ 70% | 74% |
| Taxa de sucesso Selenium (média 5 programas) | ≥ 90% | ≥ 92% |
| Sprint Reviews com cliente realizadas | 13 | 13 |

## 5. Riscos materializados

| Risco | Status | Ação tomada | Impacto no prazo |
|---|---|---|---|
| R-01 — Alteração de HTML nos portais | Materializado parcialmente — portal Smiles alterou estrutura HTML na Sprint 7 | Seletores CSS/XPath reajustados em 1 dia útil | Nenhum |
| R-02 — Evolução do Akamai | Não materializado de forma crítica | Monitoramento contínuo; ajustes preventivos de user-agent realizados nas Sprints 6 e 9 | Nenhum |
| R-03 — VM Linux não provisionada no prazo | Não materializado | VM entregue pelo cliente em 28/05/2025 (2 dias antes do prazo) | Nenhum |
| R-04 — Credenciais de teste não fornecidas | Não materializado | Credenciais recebidas em 27/05/2025 | Nenhum |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 16/11/2025 | Time de Melhoria Contínua | Documento final — relatório de encerramento |
