# Registro de Melhorias de Processo — Timeware

| Campo | Valor |
|---|---|
| **Documento** | REG-GPC-001 — Registro de Melhorias de Processo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | Time de Melhoria Contínua |
| **Processo MPS-SW** | GPC (evidência organizacional — GPC 5, GPC 11) |

---

## 1. Objetivo

Consolidar as oportunidades de melhoria (OMs) identificadas nos projetos da Timeware, registrando origem, prioridade, status de implementação e responsável. Este registro alimenta o ciclo de melhoria contínua do processo-padrão organizacional e serve como evidência de GPC 5 (melhorias planejadas e implementadas) e GPC 11 (efetividade avaliada).

---

## 2. Escopo

Abrange as OMs geradas a partir dos projetos avaliados no ciclo MPS-SW Nível C:
- **PROFARMA** — Cadastro de Clientes · Rede D1000 (sprints 1–19, abr/2025–jan/2026)
- **GASMIG** — Fundação Tecnológica · Governança de APIs (OS-001 e OS-002, abr–jun/2026)

---

## 3. Legenda de status

| Status | Descrição |
|---|---|
| **Em análise** | OM identificada; análise de viabilidade e priorização em andamento |
| **Planejada** | OM priorizada; implementação prevista no ciclo de melhoria |
| **Em implementação** | Implementação em curso |
| **Implementada** | Melhoria aplicada ao processo-padrão ou aos templates; efetividade verificável |

---

## 4. Registro consolidado de oportunidades de melhoria

| ID | Projeto de origem | Área de processo | Descrição da oportunidade | Origem | Prioridade | Status | Responsável | Observação | Ref. Jira |
|---|---|---|---|---|---|---|---|---|---|
| OM-01 | PROFARMA | GPR / REQ | Criar checklist padronizado de discovery para projetos com integrações a sistemas legados: mapeamento de satélites, documentação legada, contratos de API, acesso a ambientes | GQA-P01 NC-01 (20/06/2025) + Retrospectiva Sprint 6 | Alta | Planejada | Time de Melhoria Contínua | Insumo para evolução do GUIA-GPC-001 e TPL-GPR-001 | Jira — TMC |
| OM-02 | PROFARMA | GPR | Incluir no template de estimativa de sprint o campo de lead time do processo de change management (GMUD) do cliente | Retrospectiva Sprints 17–19 | Média | Planejada | Time de Melhoria Contínua | Insumo para evolução do TPL-GPR-001 | Jira — TMC |
| OM-03 | PROFARMA | GPR | Registrar formalmente todos os change requests com esforço estimado, mesmo em contratos de squad sem impacto financeiro direto | Retrospectiva (§3.5) + GQA-P02 (10/10/2025) | Média | Planejada | Time de Melhoria Contínua | Evidência: 12 CRs registrados no projeto PROFARMA (CR-PROFARMA01-001) | Jira — TMC |
| OM-04 | PROFARMA | PCP | Criar guia técnico para projetos com carga inicial de base legada: extração, validação, saneamento, carga em lotes e rollback | Retrospectiva Sprint 10 | Média | Planejada | Time de Melhoria Contínua | Novo artefato a ser criado como GUIA-PCP-001 ou similar | Jira — TMC |
| OM-05 | PROFARMA | PCP | Documentar o outbox pattern como padrão arquitetural recomendado da Timeware para integrações com sistemas legados sem garantia de disponibilidade | Boa prática identificada Sprint 3 (§2.2) | Alta | Em implementação | Time de Melhoria Contínua | Padrão a ser incorporado à biblioteca técnica interna (Confluence) | Jira — TMC |
| OM-06 | GASMIG | GPR (Planejamento) | Criar checklist de pré-engajamento para projetos Azure: acesso ao tenant, permissões mínimas, naming convention, ambientes disponíveis | LE-05 — Retrospectiva OS-001 (GQA-GASMIG02-001 §2.1, 07/05/2026) | Alta | Implementada | Time de Melhoria Contínua | Aplicada na OS-002: credenciais e permissões solicitadas com 1 semana de antecedência (LI-GASMIG02-001 §5) | LI-GASMIG02-001 §5 |
| OM-07 | GASMIG | MED / GPR | Incluir métricas de referência para configuração de alertas e monitoramento Azure na base de estimativas organizacional | LE-06 — Retrospectiva OS-001 (GQA-GASMIG02-001 §2.1, 07/05/2026) | Média | Planejada | Time de Melhoria Contínua | Insumo para PLA-MED-001 e base de estimativas | Jira — TMC |
| OM-08 | GASMIG | PCP (Design) | Elaborar template padrão de naming convention para recursos Azure a ser preenchido durante o kickoff com o cliente | LE-07 — Retrospectiva OS-001 | Média | Planejada | Time de Melhoria Contínua | Novo TPL a ser criado (ex.: TPL-PCP-002) | Jira — TMC |
| OM-09 | GASMIG | VV (Verificação) | Incluir no checklist de verificação técnica a validação explícita de Named Values configurados antes de qualquer deploy em produção | LE-03 — Boa prática identificada OS-001 (§2) | Baixa | Planejada | Time de Melhoria Contínua | Insumo para evolução dos checklists VV de projetos Azure | Jira — TMC |
| OM-10 | GASMIG | GPR (Encerramento) | Criar template de ata de aceite pré-preenchido com checklist de entregáveis e campo de DE ACORDO para uso padrão em projetos de configuração | LE-12 — Retrospectiva OS-002 (GQA-GASMIG02-001 §2.3, 10/06/2026) | Alta | Em análise | Time de Melhoria Contínua | Pode ser criado como TPL-GPR-007 ou incorporado ao TPL-GPR-001 | Jira — TMC |
| OM-11 | GASMIG | PCP (Design) | Incluir seção de parâmetros de monitoramento e alertas no template de PCP para projetos Azure, consolidando os thresholds acordados com o cliente antes da sprint | LE-13 — Retrospectiva OS-002 (GQA-GASMIG02-001 §2.3, 10/06/2026) | Média | Em análise | Time de Melhoria Contínua | Insumo para evolução do TPL-PCP-001 | Jira — TMC |

---

## 5. Resumo por status

| Status | Quantidade |
|---|---|
| Implementada | 1 (OM-06) |
| Em implementação | 1 (OM-05) |
| Planejada | 7 (OM-01 a OM-04, OM-07, OM-08, OM-09) |
| Em análise | 2 (OM-10, OM-11) |
| **Total** | **11** |

---

## 6. Rastreabilidade com o modelo MR-MPS-SW:2024

Este documento evidencia:
- **GPC 5** — Melhorias planejadas e implementadas: ver coluna "Status" e a OM-06 (implementada na OS-002)
- **GPC 11** — Efetividade avaliada: o acompanhamento do status das OMs e a verificação de que OM-06 produziu o efeito esperado (zero bloqueio de acesso na OS-002) demonstram o ciclo completo de melhoria

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Versão inicial — consolidação das 11 OMs dos projetos PROFARMA e GASMIG identificadas no ciclo de implantação MPS-SW Nível C |
