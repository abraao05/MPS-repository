# Material de Treinamento — QA (Verificação e Validação)

| Campo | Valor |
|---|---|
| **Documento** | MAT-CAP-020 — Trilha QA |
| **Versão** | 1.2 |
| **Data** | 15/02/2026 |
| **Papel** | QA |
| **Processos cobertos** | VV (Verificação e Validação) |

---

## 1. O fluxo do processo-padrão da Timeware

```
Faixa 1 — entrada, abertura e requisitos
  1. Originação → 2. Escritório de Projetos → 3. Abertura → 4. Discovery + Requisitos

Faixa 2 — concepção e aprovação do plano
  5. Concepção → 6. Planejamento e aprovação

Faixa 3 — construção e entrega
  7. Grooming → Planning → Dev + code review → QA (V&V)  ← você está aqui
  → Homologação → Encerramento
```

---

## 2. Seu papel no geral

Você garante que o produto faz o que deveria fazer (validação) e que foi construído certo (verificação). Atua nas sprints, recebe a demanda já em homologação com critérios de aceite, e formaliza a evidência de teste.

| Processo | Seu envolvimento | Etapa no fluxo |
|---|---|---|
| VV | Protagonista | QA nas sprints (exploratório → Gherkin) |

---

## 3. VV — Verificação e Validação

Processo de referência: **PRO-VV-001**. Templates: **TPL-VV-001** (Plano de V&V), **TPL-VV-002** (Registro de Revisão por Pares). Ferramentas: **Azure Test Plans + Jira/Xray**.

### 3.1 Planejamento de V&V

**Input:** Requisitos e critérios de aceite do item. Produtos a verificar/validar.

**O que você faz:** Seleciona o que será verificado e validado (testes + revisão por pares). Define métodos, critérios e ambientes de V&V.

**Output:** Plano de V&V → template **TPL-VV-001** (inclui métodos, critérios e ambientes).

**Onde fica:** Confluence (nó "V&V" do projeto).

**Atende:** VV 1, 3.

### 3.2 Execução dos testes

**Input:** Demanda já em homologação, com critérios de aceite (o Dev já testou pelos critérios antes; code review via PR).

**O que você faz:** Executa teste **exploratório** guiado pelos requisitos. Documenta os cenários testados com **evidências** (prints, vídeos, logs). Aprova. Formaliza os cenários happy path e sad path em **Gherkin** (Dado/Quando/Então), prontos para regressão e automação quando decidirem.

**Output:** Registros de teste com evidências → Azure Test Plans + Jira/Xray. Cenários em Gherkin.

**Onde fica:** Azure Test Plans / Jira / Xray (testes); evidências anexadas.

**Atende:** VV 4.

> **Mapa de teste:** história simples não exige mapa de teste, mas exige teste. Tela elaborada exige mapa. Mockado não conta como evidência.

### 3.3 Revisão por pares

**Input:** Produto de trabalho a revisar (ex.: código via pull request).

**O que você faz:** Aplica o procedimento de revisão por pares e registra. Pode ser evidenciada via pull request (Git/Azure) + registro de revisão.

**Output:** Registro de Revisão por Pares → template **TPL-VV-002**.

**Onde fica:** Confluence / vinculado ao PR no Git/Azure.

**Atende:** VV 2.

### 3.4 Análise e comunicação dos resultados

**Input:** Resultados de teste e revisão.

**O que você faz:** Analisa, registra e comunica os resultados.

**Output:** Relatório de V&V.

**Onde fica:** Confluence (nó "V&V").

**Atende:** VV 5.

---

## 4. O que é medido no seu trabalho

Você gera os principais dados de **qualidade** do PLA-MED-001. Você registra, não calcula.

| O que você registra (Jira/Xray) | Vira o indicador |
|---|---|
| Defeitos encontrados por item/esforço | Densidade de defeitos |
| Defeitos em homologação vs. em produção | Defeitos homolog × produção |
| Bugs reabertos / subtarefas de bug | Retrabalho |

---

## 5. Referência rápida

| Momento | Você entrega | Template | Onde |
|---|---|---|---|
| Planejamento | Plano de V&V | TPL-VV-001 | Confluence |
| Testes | Registros + evidências + Gherkin | — | Azure Test Plans / Xray |
| Revisão por pares | Registro de Revisão por Pares | TPL-VV-002 | Confluence / PR |
| Fechamento | Relatório de V&V | — | Confluence |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 10/03/2025 | Time de Melhoria Contínua | Versão inicial — baseada no processo VV |
| 1.1 | 22/09/2025 | Time de Melhoria Contínua | Inclusão de Gherkin como prática obrigatória, após dúvidas identificadas no REL-CAP-001 |
| 1.2 | 15/02/2026 | Time de Melhoria Contínua | Atualização conforme PRO-VV-001 v1.2 |
