# Avaliação de Capacitação — Processo-Padrão Geral

| Campo | Valor |
|---|---|
| **Documento** | AVA-CAP-001 — Avaliação Processo-Padrão Geral |
| **Versão** | 1.2 |
| **Data** | 15/01/2026 |
| **Aplicação** | Todos os papéis — base obrigatória antes das trilhas específicas |
| **Referência** | PLA-CAP-001 §4; GUIA-CAP-001 a 012 |

---

## Instruções

Responda cada questão com suas próprias palavras. Não consulte os materiais durante a avaliação. Ao terminar, entregue ao responsável de capacitação para correção e registro no TPL-CAP-001.

Pontuação de corte: **70%** (mínimo para aprovação por trilha).

---

## Bloco 1 — Visão Geral do Processo-Padrão (todos os papéis)

**1.** Quais são as três faixas do processo-padrão da Timeware? Para cada uma, cite um exemplo de etapa.

> _Resposta esperada: Faixa 1 (entrada/abertura/requisitos), Faixa 2 (concepção/planejamento), Faixa 3 (construção/entrega). Exemplos: Faixa 1 — Abertura; Faixa 2 — Planejamento e aprovação; Faixa 3 — Desenvolvimento ou QA._

---

**2.** O que é o TAP e qual é o seu propósito?

> _Resposta esperada: Termo de Abertura do Projeto. Autoriza formalmente o projeto, define escopo inicial, partes interessadas, restrições e quem o patrocina. É produzido na Faixa 1 pelo GP._

---

**3.** Qual é a diferença entre grooming e planning?

> _Resposta esperada: Grooming é o refinamento do backlog — itens são detalhados, requisitos esclarecidos e critérios de aceite definidos. Planning é o planejamento da sprint — o time seleciona os itens a serem desenvolvidos naquela sprint e estima o esforço._

---

**4.** O que é a Definição de Pronto (DoD) na Timeware?

> _Resposta esperada: O conjunto de critérios que um item precisa satisfazer para ser considerado entregue: critérios de aceite atendidos → code review aprovado → testes QA executados → homologação/staging aprovada._

---

**5.** Cite dois artefatos que devem existir antes do início da construção (Faixa 3).

> _Resposta esperada (qualquer dois): TAP, backlog refinado com critérios de aceite, Plano de Projeto (GPR), Documento de Requisitos (REQ), Documento de Design/Arquitetura (PCP), Plano de V&V (VV), Estratégia de Integração (ITP)._

---

## Bloco 2 — Medição e Indicadores

**6.** Quais são as duas categorias de indicadores do PLA-MED-001? Cite dois indicadores de cada categoria.

> _Resposta esperada: Previsibilidade (aderência ao prazo, esforço estimado × real, velocity, itens entregues × planejados) e Qualidade (densidade de defeitos, defeitos homolog × produção, retrabalho)._

---

**7.** Burndown é um dos 7 indicadores organizacionais? Justifique sua resposta.

> _Resposta esperada: Não. Burndown é uma ferramenta de acompanhamento de sprint — auxilia o time a visualizar o andamento da sprint, mas não é apresentado como indicador organizacional no PLA-MED-001._

---

**8.** Quem calcula os indicadores? Quem registra os dados brutos?

> _Resposta esperada: O Responsável de Medição coleta, verifica e consolida os indicadores. Os demais papéis (GP, Devs, QA, DevOps) registram os dados brutos no Jira/Xray durante a execução do projeto._

---

## Bloco 3 — Qualidade e GQA

**9.** O que é uma auditoria GQA e qual é o seu objetivo?

> _Resposta esperada: É a verificação objetiva (feita por alguém independente do projeto) de que os processos e produtos de trabalho estão em conformidade com o processo-padrão definido. Garante que o que foi definido no nível organizacional está sendo executado nos projetos._

---

**10.** Quem pode conduzir uma auditoria GQA em um projeto? Qual é o requisito de independência?

> _Resposta esperada: Qualquer membro do Time de Melhoria Contínua que não seja parte do projeto auditado. A independência exige que o auditor não tenha conflito de interesse com os artefatos que está auditando._

---

## Bloco 4 — Configuração e Versionamento

**11.** O que é uma baseline? Cite um exemplo no contexto dos projetos Timeware.

> _Resposta esperada: Uma baseline é um ponto de controle formal em que um conjunto de itens de configuração é fixado (não pode ser alterado sem controle de mudança). Exemplo: tag de release de uma versão homologada no Git._

---

**12.** Qual é a convenção de nomenclatura dos documentos na Timeware? Dê um exemplo.

> _Resposta esperada: TIPO-PROCESSO-NÚMERO_Descricao-Curta (sem acentos, sem espaços). Exemplo: TPL-VV-001_Plano-de-VV ou PRO-GPR-001_Processo-de-Gerencia-de-Projeto._

---

## Gabarito e Pontuação

| Questão | Pontos |
|---|---|
| 1 | 10 |
| 2 | 10 |
| 3 | 10 |
| 4 | 10 |
| 5 | 10 |
| 6 | 10 |
| 7 | 5 |
| 8 | 5 |
| 9 | 10 |
| 10 | 5 |
| 11 | 10 |
| 12 | 5 |
| **Total** | **100** |

Corte de aprovação: **70 pontos**.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 10/12/2024 | Time de Melhoria Contínua | Versão inicial — cobrindo processo-padrão e nomenclatura |
| 1.1 | 10/03/2025 | Time de Melhoria Contínua | Inclusão dos blocos de medição e GQA para segunda onda de treinamento |
| 1.2 | 15/01/2026 | Time de Melhoria Contínua | Revisão completa com todos os blocos (processo-padrão, MED, GQA, GCO) |
