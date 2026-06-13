# Avaliação de Capacitação — Trilha Técnica (Tech Lead / Devs / QA)

| Campo | Valor |
|---|---|
| **Documento** | AVA-CAP-003 — Avaliação Trilha Técnica |
| **Versão** | 1.1 |
| **Data** | 10/03/2025 |
| **Aplicação** | Tech Lead, Desenvolvedores, QA |
| **Pré-requisito** | AVA-CAP-001 aprovado |
| **Referência** | PLA-CAP-001 §4; MAT-CAP-016, MAT-CAP-017, MAT-CAP-018, MAT-CAP-020; GUIA-CAP-002, 003, 004 |

---

## Instruções

Responda com suas próprias palavras. Questões marcadas com **(TL)** são obrigatórias apenas para Tech Lead; questões **(DEV)** apenas para Desenvolvedores; questões **(QA)** apenas para QA. As demais são comuns a todos. Pontuação de corte: **70%**.

---

## Bloco 1 — REQ (Requisitos — visão técnica)

**1.** O que o Tech Lead faz com os requisitos antes do grooming?

> _Resposta esperada: Analisa a viabilidade técnica dos requisitos, questiona ambiguidades, sugere alternativas de implementação e contribui para a definição dos critérios de aceite com granularidade técnica._

**2.** Como um desenvolvedor deve agir se, durante a implementação, perceber que um requisito é ambíguo ou conflitante?

> _Resposta esperada: Não assumir nenhuma interpretação silenciosamente. Levantar a questão no Jira (comentário no item) ou na daily, registrar a dúvida e aguardar alinhamento com GP/PO antes de implementar._

---

## Bloco 2 — PCP (Projeto e Construção do Produto)

**3.** O que é o Documento de Design/Arquitetura (TPL-PCP-001) e quem o produz?

> _Resposta esperada: É o documento que define a arquitetura da solução, componentes, interfaces, tecnologias e decisões de design. É produzido pelo Tech Lead antes do início da construção e serve de referência para os desenvolvedores._

**4. (DEV)** Quais são as duas responsabilidades do desenvolvedor antes de entregar um item para o QA?

> _Resposta esperada: (1) Testar pelos critérios de aceite definidos no item — o Dev confirma que o item atende o que foi especificado. (2) Submeter pull request e ter o code review aprovado._

**5. (DEV)** Quais dados o desenvolvedor deve registrar no Jira para alimentar os indicadores de medição?

> _Resposta esperada: Esforço estimado (planning poker) e esforço real (horas lançadas). Pontos entregues por sprint (velocity). Subtarefas de bug ou retrabalho abertos/resolvidos. Defeitos encontrados no seu código._

**6. (TL)** Como o Tech Lead contribui para o processo de GDE (Gerência de Decisões)?

> _Resposta esperada: Conduz a análise de alternativas técnicas formalmente quando a decisão tem impacto arquitetural ou de alto risco. Registra o critério de avaliação, as alternativas consideradas e a decisão tomada no GDE-PROJETO-001._

---

## Bloco 3 — VV (Verificação e Validação)

**7. (QA)** Qual é a diferença entre verificação e validação?

> _Resposta esperada: Verificação confirma que o produto foi construído corretamente (conforme especificado/design). Validação confirma que o produto certo foi construído (satisfaz a necessidade do usuário). Verificação = "fiz certo?"; Validação = "fiz a coisa certa?"._

**8. (QA)** O que é um teste exploratório e quando ele é aplicado na Timeware?

> _Resposta esperada: Teste sem roteiro fixo — o QA navega pelo produto guiado pelos requisitos e critérios de aceite buscando falhas não previstas. É aplicado na etapa de QA das sprints, antes da formalização em Gherkin._

**9. (QA)** O que é Gherkin? Para que serve na Timeware?

> _Resposta esperada: Linguagem de escrita de cenários de teste no formato "Dado / Quando / Então". Na Timeware, o QA formaliza os cenários happy path e sad path em Gherkin após o teste exploratório, como base para regressão e automação futura._

**10. (QA)** O que é uma revisão por pares e qual template é usado?

> _Resposta esperada: É a verificação formal de um produto de trabalho por outra pessoa além do autor — busca inconsistências, omissões e conformidade com padrões. Na Timeware usa o template TPL-VV-002. Pode ser evidenciada pelo pull request + registro de revisão._

**11.** O que é obrigatório como evidência de teste? Por que "mockado não conta"?

> _Resposta esperada: São necessários prints, vídeos ou logs mostrando o comportamento real do sistema (não simulado). Mock/stub de dados substitui a realidade — não comprova que o produto funciona no ambiente correto, por isso não é aceito como evidência._

---

## Bloco 4 — Integração e Configuração (Tech Lead)

**12. (TL)** O que é a Estratégia de Integração (TPL-ITP-001) e quem a produz?

> _Resposta esperada: Define como os componentes serão integrados: ordem de integração, interfaces, ambientes, responsáveis. É produzida pelo Tech Lead com apoio do DevOps e usada como guia para a promoção dos builds entre ambientes._

---

## Gabarito e Pontuação

| Questão | Papel | Pontos |
|---|---|---|
| 1 | Todos | 8 |
| 2 | Todos | 8 |
| 3 | Todos | 8 |
| 4 | DEV (obrigatória) | 10 |
| 5 | DEV (obrigatória) | 8 |
| 6 | TL (obrigatória) | 10 |
| 7 | QA (obrigatória) | 8 |
| 8 | QA (obrigatória) | 8 |
| 9 | QA (obrigatória) | 8 |
| 10 | QA (obrigatória) | 8 |
| 11 | Todos | 8 |
| 12 | TL (obrigatória) | 10 |

**Pontuação por papel:**
- **Tech Lead:** questões 1, 2, 3, 6, 11, 12 = 52 pts base + questões comuns restantes até 100.
- **Desenvolvedores:** questões 1, 2, 3, 4, 5, 11 = 50 pts base + questões comuns.
- **QA:** questões 1, 2, 3, 7, 8, 9, 10, 11 = 64 pts base + questões comuns.

A pontuação final é normalizada para 100 com base nas questões aplicáveis ao papel. Corte de aprovação: **70 pontos**.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 10/12/2024 | Time de Melhoria Contínua | Versão inicial — cobrindo REQ e PCP |
| 1.1 | 10/03/2025 | Time de Melhoria Contínua | Inclusão das questões de VV para a segunda onda de treinamento |
