# Plano de Implementação de Melhorias de Processo — Timeware

| Campo | Valor |
|---|---|
| **Documento** | REG-GPC-002 — Plano de Implementação de Melhorias de Processo |
| **Versão** | 1.0 |
| **Data** | 13/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | Time de Melhoria Contínua |
| **Processo MPS-SW** | GPC (evidência organizacional — GPC 5, GPC 6, GPC 11) |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Objetivo

Detalhar, por tarefa de implementação, as oportunidades de melhoria (OMs) registradas em REG-GPC-001 e as ações de melhoria documental executadas no ciclo MPS-SW Nível C, evidenciando que as melhorias selecionadas foram efetivamente planejadas e implementadas (GPC 5) e que o ciclo de melhoria foi gerenciado (GPC 6).

O rastreamento operacional das tarefas é realizado no Jira (quadro do Time de Melhoria Contínua). Este documento é a consolidação formal para fins de evidência MPS.

---

## 2. Critérios de priorização

| Critério | Peso |
|---|---|
| Impacto direto em futuros projetos (previne retrabalho ou bloqueio) | Alto |
| Evidência de boa prática já testada em projeto real | Alto |
| Esforço de implementação vs. ganho operacional | Médio |
| Dependência de outros artefatos ou decisões | Baixo |

---

## 3. Tarefas de implementação — Oportunidades de Melhoria (OMs)

Cada OM de REG-GPC-001 é desdobrada em uma ou mais tarefas de implementação. Tarefas com status **Implementada** têm o resultado verificável; as demais estão planejadas para o próximo ciclo de melhoria.

| ID Tarefa | OM Ref. | Área | Descrição da tarefa | Responsável | Prazo previsto | Status | Artefato gerado / impactado |
|---|---|---|---|---|---|---|---|
| IMPL-OM01-A | OM-01 | GPR / REQ | Elaborar checklist padronizado de discovery para projetos com integrações a sistemas legados (mapeamento de satélites, documentação legada, contratos de API, acesso a ambientes) | Time de Melhoria Contínua | Ago/2026 | Planejada | GUIA-GPC-001 (nova seção) / TPL-GPR-001 (novo campo) |
| IMPL-OM02-A | OM-02 | GPR | Incluir no template de estimativa de sprint o campo de lead time de change management (GMUD) do cliente | Time de Melhoria Contínua | Ago/2026 | Planejada | TPL-GPR-001 |
| IMPL-OM03-A | OM-03 | GPR | Formalizar no processo-padrão a obrigatoriedade de registrar CRs com esforço estimado em contratos de squad, mesmo sem impacto financeiro direto | Time de Melhoria Contínua | Jul/2026 | Planejada | PRO-GPC-001 (seção de change request) |
| IMPL-OM04-A | OM-04 | PCP | Criar guia técnico para projetos com carga inicial de base legada: extração, validação, saneamento, carga em lotes e rollback | Time de Melhoria Contínua | Set/2026 | Planejada | GUIA-PCP-001 (novo documento) |
| IMPL-OM05-A | OM-05 | PCP | Documentar o outbox pattern como padrão arquitetural recomendado para integrações com sistemas legados sem garantia de disponibilidade | Time de Melhoria Contínua | Jul/2026 | Em implementação | Confluence — biblioteca técnica interna |
| IMPL-OM06-A | OM-06 | GPR (Pré-engajamento) | Criar checklist de pré-engajamento para projetos Azure: acesso ao tenant, permissões mínimas, naming convention, ambientes disponíveis | Time de Melhoria Contínua | Jun/2026 | **Implementada** | LI-GASMIG02-001 §5 — aplicado na OS-002 com antecedência de 1 semana |
| IMPL-OM07-A | OM-07 | MED / GPR | Incluir métricas de referência para configuração de alertas e monitoramento Azure na base de estimativas organizacional | Time de Melhoria Contínua | Set/2026 | Planejada | PLA-MED-001 / base de estimativas (Confluence) |
| IMPL-OM08-A | OM-08 | PCP (Design) | Elaborar template de naming convention para recursos Azure a ser preenchido no kickoff com o cliente | Time de Melhoria Contínua | Ago/2026 | Planejada | TPL-PCP-002 (novo documento) |
| IMPL-OM09-A | OM-09 | VV (Verificação) | Incluir no checklist de verificação técnica a validação explícita de Named Values configurados antes de qualquer deploy | Time de Melhoria Contínua | Jul/2026 | Planejada | Checklists VV de projetos Azure |
| IMPL-OM10-A | OM-10 | GPR (Encerramento) | Criar template de ata de aceite pré-preenchido com checklist de entregáveis e campo DE ACORDO, para uso padrão em projetos de configuração | Time de Melhoria Contínua | Jul/2026 | Em análise | TPL-GPR-007 (novo documento) |
| IMPL-OM11-A | OM-11 | PCP (Design) | Incluir seção de parâmetros de monitoramento e alertas no template de PCP para projetos Azure | Time de Melhoria Contínua | Ago/2026 | Em análise | TPL-PCP-001 (nova seção) |

---

## 4. Ações de melhoria documental — ciclo MPS-SW Nível C

Além das OMs de projeto, o ciclo de preparação MPS-SW gerou melhorias diretas nos ativos de processo organizacional. As tarefas abaixo foram executadas em Jun/2026 como parte da implantação e conformidade do modelo.

| ID Tarefa | Categoria | Descrição da ação | Responsável | Data | Status | Documentos impactados |
|---|---|---|---|---|---|---|
| IMPL-DOC-01 | Conformidade AQU | Registrar explicitamente a não aplicabilidade do processo de Aquisição (AQU) em todos os Registros de Adaptação, com referência ao PRO-AQU-001 §2 | Time de Melhoria Contínua | 13/06/2026 | **Implementada** | ADAP-GASMIG02-001 v1.4, ADAP-GASMIG02-002 v1.2, ADAP-FRUKI01-001 v1.2, ADAP-FRUKI01-002 v1.2, ADAP-PROFARMA01-001 v1.1 |
| IMPL-DOC-02 | Governança OSW | Criar Painel de Portfólio (REG-OSW-001) consolidando evidências de OSW 8, OSW 9 e OSW 10 | Time de Melhoria Contínua | 13/06/2026 | **Implementada** | REG-OSW-001 v1.0 (novo) |
| IMPL-DOC-03 | GQA Organizacional | Estender GQA-ORG-001 para cobrir os processos AQU (§3.6) e OSW (§3.7), alcançando cobertura completa dos 7 processos organizacionais | Time de Melhoria Contínua | 13/06/2026 | **Implementada** | GQA-ORG-001 v1.1 |
| IMPL-DOC-04 | Governança OSW | Atualizar PRO-OSW-002 para referenciar REG-OSW-001 como evidência operacional do portfólio | Time de Melhoria Contínua | 13/06/2026 | **Implementada** | PRO-OSW-002 v1.3 |
| IMPL-DOC-05 | Capacitação / OSW 2 | Incluir orçamento detalhado do ciclo MPS-SW Nível C em PLA-CAP-001 §6.1 | Time de Melhoria Contínua | 13/06/2026 | **Implementada** | PLA-CAP-001 v1.2 |
| IMPL-DOC-06 | Governança OSW 3 | Produzir ATA da reunião de análise crítica de processos do TMC, evidenciando comunicação de melhorias aos grupos relevantes | Time de Melhoria Contínua | 13/06/2026 | **Implementada** | ATA-GPC-001 v1.0 (novo) |
| IMPL-DOC-07 | Governança OSW 7 | Produzir REG-OSW-002 registrando a comunicação formal da política organizacional pela alta gestão | Time de Melhoria Contínua | 13/06/2026 | **Implementada** | REG-OSW-002 v1.0 (novo) |
| IMPL-DOC-08 | GPC 5 / GPC 6 | Produzir REG-GPC-002 (este documento) com plano de implementação das OMs e rastreabilidade das tarefas | Time de Melhoria Contínua | 13/06/2026 | **Implementada** | REG-GPC-002 v1.0 (este documento) |

---

## 5. Resumo consolidado

| Categoria | Implementada | Em implementação | Planejada | Em análise | Total |
|---|---|---|---|---|---|
| OMs de projeto (§3) | 1 (IMPL-OM06) | 1 (IMPL-OM05) | 6 | 2 | 11 |
| Melhorias documentais (§4) | 8 | — | — | — | 8 |
| **Total** | **9** | **1** | **6** | **2** | **19** |

---

## 6. Rastreabilidade com o modelo MR-MPS-SW:2024

| Resultado | Como este documento atende |
|---|---|
| GPC 5 — Melhorias selecionadas implementadas | §3 (tarefas de implementação por OM) e §4 (melhorias documentais implementadas) |
| GPC 6 — Processo de melhoria gerenciado pelo SEPG/TMC | §2 (critérios de priorização), §3–§4 (rastreabilidade de tarefas), §5 (resumo de situação) |
| GPC 11 — Efetividade avaliada | OM-06 e IMPL-DOC-01 a IMPL-DOC-08: todas as melhorias com resultado verificável nos artefatos referenciados |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 13/06/2026 | Time de Melhoria Contínua | Versão inicial — plano de implementação das 11 OMs de REG-GPC-001 e 8 tarefas documentais do ciclo MPS-SW Nível C |
