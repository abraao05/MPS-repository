# Matriz de Papéis e Responsabilidades — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | MAPA-ORG-001 — Matriz de Papéis e Responsabilidades |
| **Versão** | 1.3 |
| **Data** | 15/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | COO (Operações) |
| **Modelo de referência** | MR-MPS-SW:2024 — Nível C |
| **Classificação** | Ativo de processo organizacional (capacidade) |

---

## 1. Propósito

Esta matriz consolida, em um único documento, a definição de **responsáveis pelos processos** e a **evidência de competência** de quem ocupa cada papel. Conecta três camadas que o modelo exige (atributos de capacidade CP-ii e CP-iii):

1. **Processo → papel responsável** (quem responde por cada processo) — Seção 3
2. **Papel → competências exigidas** (o que o papel precisa dominar) — Seção 4
3. **Papel → titular → evidência de competência** (quem ocupa e a prova) — Seção 5

A matriz aplica-se aos 12 processos do escopo MPS-SW Nível C e cobre tanto os papéis de projeto quanto os organizacionais.

---

## 2. Convenção RACI

| Sigla | Significado |
|---|---|
| **R** | Responsável pela execução (executa a atividade) |
| **A** | Autoridade / presta contas (responde pelo processo; aprova) |
| **C** | Consultado (fornece insumo) |
| **I** | Informado (recebe o resultado) |

---

## 3. Processos × Papéis (RACI)

| Processo | A (responde) | R (executa) | C / I |
|---|---|---|---|
| **GPR** — Gerência de Projetos | Time de Melhoria Contínua | Gerente de Projeto | GQA (C); COO (I) |
| **REQ** — Engenharia de Requisitos | Time de Melhoria Contínua | PO + Gerente de Projeto + Tech Lead | GQA (C); Cliente (C) |
| **PCP** — Projeto e Construção | Time de Melhoria Contínua | Tech Lead + Desenvolvedores | GQA (C); QA (C) |
| **ITP** — Integração do Produto | Time de Melhoria Contínua | Tech Lead + DevOps | QA (C); GQA (C) |
| **VV** — Verificação e Validação | Time de Melhoria Contínua | QA + Gerente de Projeto (validação) | GQA (C); Cliente (C) |
| **GCO** — Gerência de Configuração | Time de Melhoria Contínua | GCO Baseline + DevOps + Tech Lead | GQA (C) |
| **CAP** — Capacitação | COO | RH / Capacitação + Time de Melhoria Contínua | COO (A) |
| **MED** — Medição | Time de Melhoria Contínua | Responsável de Medição (consolida) + Gerente de Projeto (coleta) | COO (I) |
| **AQU** — Aquisição | COO | RH / Capacitação + Gerente de Projeto | COO (A) |
| **GDE** — Gerência de Decisões | Time de Melhoria Contínua | Tech Lead ou Gerente de Projeto (conforme contexto) | COO (C); GQA (C) |
| **GPC** — Gerência de Processos | COO | Time de Melhoria Contínua | GQA (C); COO (A) |
| **OSW** — Gerência Organizacional de Software | CEO | COO + Time de Melhoria Contínua | CEO (A) |

> A independência da **GQA** em relação à equipe de projeto é assegurada: a GQA verifica os processos, mas não os executa (consultada/informada, nunca responsável pela execução do produto auditado).

---

## 4. Papéis × Competências exigidas

| Papel | Processos que executa | Competências exigidas |
|---|---|---|
| **Gerente de Projeto** | GPR, REQ, VV (validação), MED (coleta) | Gestão ágil (Scrum); planejamento e estimativas; gestão de riscos; comunicação com cliente; Jira / Azure DevOps |
| **Product Owner (PO)** | REQ | Elicitação de requisitos; escrita de histórias e critérios de aceite; priorização de backlog; validação com cliente |
| **Tech Lead / Arquiteto** | PCP, ITP, GCO, GDE | Arquitetura de software; design patterns; estratégias de integração; cloud (Azure); Git / branching; code review |
| **Desenvolvedores** | PCP, ITP, GCO | Linguagens e frameworks do stack; testes; Git; Definição de Pronto; registro de dados de medição |
| **QA** | VV, ITP (apoio) | Técnicas de teste funcional e exploratório; automação de testes; Gherkin; gestão de defeitos; evidências |
| **DevOps** | ITP, GCO (operação) | CI/CD; ambientes e fluxo de promoção; IaC (Bicep/ARM); baselines e releases |
| **GCO Baseline / Auditoria** | GCO (governança) | Gestão de configuração; itens de configuração; auditoria de baseline; controle de mudanças |
| **GQA** | VV (verificação independente), GPC (auditoria) | Auditoria de processos; independência; conhecimento do MR-MPS-SW e do processo-padrão |
| **Time de Melhoria Contínua / SEPG** | GPC, CAP (apoio), MED (consolidação) | Definição e melhoria de processos; MR-MPS-SW; modelagem de processos; análise de métricas; facilitação |
| **Responsável de Medição** | MED (operação) | Coleta e consolidação de medidas; análise de indicadores; repositório de medição |
| **RH / Capacitação** | CAP, AQU (apoio) | Identificação de necessidades de competência; planejamento de capacitação; avaliação de eficácia |
| **Consultora de Processos (PJ)** | GPC (apoio à definição) | Lean Six Sigma; modelagem e melhoria de processos; mapeamento de fluxo de valor |
| **COO** | OSW, GPC (autoridade), portfólio | Gestão de portfólio; governança organizacional; análise crítica de desempenho |

---

## 5. Papel × Titular × Equipe × Evidência de competência

Esta seção nomina os titulares de cada papel e os demais membros da equipe que atuam sob aquele papel nos projetos. A evidência de competência é **currículo** (em `cap/curriculos/`) e/ou **registro de capacitação** (`REG-CAP-*`). Detalhe em REG-CAP-CV-001.

| Papel | Titular | Equipe | Evidência de competência |
|---|---|---|---|
| **Gerente de Projeto** | Abraão Oliveira | — | REG-CAP-001/003/004/005/009 (Abraão); AVA-CAP-002 |
| **Product Owner (PO)** | Abraão Oliveira | Silvio Baroni | REG-CAP-001/003/004/005/009 (Abraão); REG-CAP-003/006/009 (Baroni) |
| **Tech Lead / Arquiteto** | Cézar Velázquez | — | CV (Fatec BS); REG-CAP-011 (Azure); REG-CAP-001/002/005/009 |
| **Desenvolvedores** | — | Renan Kioshi, Raony Chagas, Mateus Veloso, Lucas Batista, Henry Komatsu, Allan Patrocínio, Felipe Siqueira | REG-CAP-010 (onboarding técnico); REG-CAP-011 (Azure); REG-CAP-012 (testes) |
| **QA** | Caroline Jenifer (Carol) | Jonatan Silva, Letícia Moraes | CV Carol (FIAP, 7+ anos QA); REG-CAP-012 (automação de testes); REG-CAP-002/007/008/009 |
| **DevOps / GCO (pipeline/release)** | Cézar Velázquez | Flávio Fernandes | REG-CAP-011 (Azure/IaC); REG-CAP-001/002/005/009 (Cézar); REG-CAP-002/009 (Flávio) |
| **GCO Baseline / Auditoria** | Cézar Velázquez | Flávio Fernandes | REG-CAP-011 (Azure); REG-CAP-001/002/005/009 (Cézar); REG-CAP-002/009 (Flávio) |
| **GQA / Qualidade do Processo** | Caroline Jenifer (Carol) | — | CV Carol (FIAP, 7+ anos QA); REG-CAP-012 (automação de testes); REG-CAP-007/008/009 |
| **Time de Melhoria Contínua / SEPG** | Silvio Baroni (coordenador), Abraão Oliveira, Flávio Fernandes | Patricia Lima, Mariana Teixeira | CV Silvio (PM Sênior); REG-CAP-013 (desenho de processos); REG-CAP-003/006/009 |
| **Responsável de Medição** | Silvio Baroni | Abraão Oliveira | CV Silvio (PM Sênior); REG-CAP-013; REG-CAP-003/006/009 |
| **RH / Capacitação** | Guilherme Gomes | Klayton Roberto | REG-CAP-004/006/009; AVA-CAP-005 |
| **Portfólio / OSW** | Wilson Yamada | Abraão Oliveira, Silvio Baroni | CV Wilson (FIAP, ITIL, 20+ anos gestão de TI); REG-CAP-006/009 |
| **COO** | Wilson Yamada | — | REG-CAP-006; AVA-CAP-005 (trilha OSW) |
| **CEO / Founder** | Tiago Barbosa Nascimento | — | Patrocínio formal (POL-ORG-001) |

---

## 6. Rastreabilidade e instrução para auditoria

*Esta seção relaciona o documento ao modelo de referência MR-MPS-SW:2024.*

| Exigência de capacidade | Onde é atendida nesta matriz |
|---|---|
| CP-ii / CP-iii — responsáveis pelos processos definidos | Seção 3 (RACI processo × papel) |
| CP-ii / CP-iii — competências definidas por papel | Seção 4 (papel × competências) |
| CP — pessoas preparadas (evidência de competência) | Seção 5 (titular × evidência) + REG-CAP-CV-001 + `cap/curriculos/` |

A matriz aplica-se a projetos (GPR, REQ, PCP, ITP, VV) e à organização (GCO, CAP, OSW, GPC, MED, AQU, GDE). A comprovação de competência é detalhada no índice REG-CAP-CV-001 e nos currículos arquivados.

---

## 7. Documentos relacionados

- REG-CAP-CV-001 — Índice de Currículos e Evidências de Competência
- MAPA-CAP-001 — Mapa de Capacidade dos Processos (atributos CP-E/D/C)
- PRO-OSW-001 — Governança Organizacional de Processos (autoridade e RACI de governança)
- PRO-GPC-001 — Processo-Padrão Organizacional (papéis de projeto)
- PLA-CAP-001 — Plano de Capacitação
- POL-ORG-001 — Política Organizacional de Processos

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.3 | 15/06/2026 | Time de Melhoria Contínua | Seção 5 atualizada: titulares e equipes revistos conforme distribuição de papéis para entrevistas MPS-SW — GQA passa para Caroline Jenifer; Medição passa para Silvio Baroni; GP fica só com Abraão Oliveira; PO adiciona Baroni como equipe; Devs expandidos (Mateus Veloso, Lucas Batista, Allan Patrocínio, Felipe Siqueira); RH equipe atualizado (Klayton Roberto); Portfólio/OSW adiciona Abraão e Baroni como equipe; Baroni identificado como coordenador do SEPG; DevOps e GCO Baseline passam para Cézar Velázquez (titular) e Flávio Fernandes (equipe) |
| 1.2 | 15/06/2026 | Time de Melhoria Contínua | Papel "Consultora de Processos (PJ)" removido apenas da seção 5 (titulares/equipe); mantido na seção 4 (competências) |
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Seção 5 reestruturada: coluna "Equipe" adicionada; titulares corrigidos (Wilson Yamada = COO/Medição/Portfólio; Baroni = GP/PO; Flávio = MC/GQA; Guilherme = RH); equipe de projeto separada dos titulares |
| 1.0 | 10/06/2026 | Time de Melhoria Contínua | Versão inicial — matriz consolidando RACI processo × papel, competências por papel e titulares com evidência de competência |
