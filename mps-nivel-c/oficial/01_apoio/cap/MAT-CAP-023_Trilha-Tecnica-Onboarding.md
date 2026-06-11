# Material de Treinamento — Trilha Técnica de Onboarding

| Campo | Valor |
|---|---|
| **Documento** | MAT-CAP-023 — Trilha Técnica de Onboarding |
| **Versão** | 1.0 |
| **Data** | 09/01/2026 |
| **Papel** | Tech Lead, Arquiteto, Desenvolvedores, QA, DevOps |
| **Tipo** | Competência técnica (complementar às trilhas de processo MAT-CAP-016 a 022) |

---

## 1. Objetivo

Esta trilha cobre a **competência técnica de base** necessária para atuar nos projetos da Timeware — o "como fazer" técnico, complementar às trilhas de processo (que cobrem o "como seguir o processo"). É aplicada no onboarding de novos integrantes técnicos e como base para os workshops de aprofundamento.

Enquanto as trilhas MAT-CAP-016 a 022 ensinam o processo (GPR, REQ, PCP, VV, etc.), esta trilha garante que o profissional domina o ambiente técnico, o stack e os padrões da casa.

---

## 2. Módulo 1 — Stack e ferramentas

| Tema | Conteúdo |
|---|---|
| Controle de versão | Git, Azure DevOps; fluxo de branches conforme CONV-ORG-001 |
| Gestão de trabalho | Jira — backlog, sprints, registro de esforço e defeitos |
| Stack de desenvolvimento | Linguagens e frameworks do stack; estrutura de projeto padrão |
| Pipelines | Build e deploy automatizados; execução de testes no pipeline |

---

## 3. Módulo 2 — Ambientes e fluxo de promoção

Topologia padrão de ambientes (conforme PRO-GPC-001):

```
Dev → QA → Homologação → Stage → Produção
```

| Ambiente | Propósito |
|---|---|
| Dev | Desenvolvimento e testes locais |
| QA | Verificação e validação pelo time de QA |
| Homologação | Validação com o cliente |
| Stage | Réplica de produção (quando aplicável) |
| Produção | Ambiente final, após aprovação do cliente |

Regras de promoção: cada ambiente só recebe o que passou pelo anterior; promoção para produção exige aprovação formal do cliente (ponto de controle obrigatório).

---

## 4. Módulo 3 — Padrões de código e configuração

| Tema | Conteúdo |
|---|---|
| Convenções | CONV-ORG-001 — nomenclatura de branches, commits, tags |
| Code review | Pull request obrigatório; revisão por pares antes do merge (evidência VV 2) |
| Definição de Pronto | Critérios de aceite → code review → testes QA → homologação |
| Configuração | GUIA-GCO-001 — itens de configuração, baselines, controle de mudanças |

---

## 5. Módulos de aprofundamento (workshops)

Esta trilha é a base. Os aprofundamentos técnicos são registrados como workshops específicos:

| Módulo | Tema | Workshop / Registro |
|---|---|---|
| §3 (este material — Azure) | Azure API Management, Key Vault, OAuth, monitoramento | REG-CAP-011 |
| §4 (este material — testes) | Automação de testes, Gherkin avançado, evidências | REG-CAP-012 |

---

## 6. Referência rápida

| Momento | O que dominar | Referência |
|---|---|---|
| Setup inicial | Acesso, repositórios, ambiente local | Módulo 1 |
| Trabalho diário | Branching, PR, code review | CONV-ORG-001 / Módulo 3 |
| Entrega | Fluxo de promoção entre ambientes | PRO-GPC-001 / Módulo 2 |
| Aprofundamento | Workshops técnicos por domínio | REG-CAP-011, 012 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 09/01/2026 | Time de Melhoria Contínua | Versão inicial — trilha técnica de onboarding (competência técnica de base) |
