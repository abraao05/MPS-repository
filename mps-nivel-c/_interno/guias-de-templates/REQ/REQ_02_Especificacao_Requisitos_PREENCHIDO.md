# Especificação de Requisitos

> **Modelo de preenchimento** com base no Trainer Connect (evidência do diagnóstico: rastreabilidade bidirecional real com detecção de órfãos foi um dos pontos mais fortes do projeto). Dados de equipe/cliente marcados *(exemplo)*.

---

## 0. Identificação e versão

| Campo | Valor |
|---|---|
| Projeto | Trainer Connect |
| Versão | v3 |
| Data | 2026-06-02 |
| Responsável | *(exemplo: gestor)* |
| O que mudou na versão | Requisitos de comércio (v2.0) movidos para fora do escopo; inclusão dos requisitos de execução de treino |

---

## 1. Partes interessadas e critérios de envolvimento

- **Critério para definir parte interessada:** quem usa o produto (trainer, aluno), quem patrocina (cliente) e quem o opera.
- **Critério para envolver:** usuário primário valida ao fim de cada milestone; cliente aprova escopo e marcos.

| Parte interessada | Tipo | Como é envolvida |
|---|---|---|
| Personal trainer | Usuário primário | Validação de aceite por milestone |
| Aluno | Usuário final | Teste dos fluxos de execução |
| Cliente/patrocinador | Cliente | Aprovação de escopo e marcos |

---

## 2. Necessidades, expectativas e restrições levantadas

| ID | Necessidade | Origem | Produto ou interface? |
|---|---|---|---|
| N-01 | Trainer precisa organizar sua base de alunos | Trainer | Produto |
| N-02 | Trainer precisa prescrever treinos a partir de exercícios | Trainer | Produto |
| N-03 | Aluno precisa acessar e executar o treino recebido | Aluno | Produto |
| N-04 | Restrição: confirmação de e-mail inviável no plano de infra atual | Equipe | Interface externa |

- **Como o entendimento foi confirmado:** clarificações registradas em conversa com o usuário ao longo das fases; entendimento aprovado pelo critério de aceite de cada história.

---

## 3. Requisitos especificados

| ID req | Descrição | Origem | Prioridade | Alocado para | Status |
|---|---|---|---|---|---|
| OWN-01 | Cadastrar e gerenciar alunos | N-01 | Alta | Fase Fundação | Concluído |
| DA-12 | Montar treino a partir da biblioteca | N-02 | Alta | Fase Treinos | Concluído |
| DA-35 | Aluno visualiza e executa treino prescrito | N-03 | Alta | Fase Execução | Concluído |
| EXER-04 | Exercícios públicos na biblioteca | N-02 | Média | Fase Biblioteca | Concluído |

### 3.1 Conceitos operacionais, cenários e interfaces
- **Cenários:** trainer cadastra aluno → monta treino → prescreve; aluno faz login → vê treino → executa e marca progresso.
- **Interfaces internas:** módulo de alunos ↔ módulo de treinos ↔ módulo de execução.
- **Interfaces externas:** autenticação; banco de dados gerenciado com regras de acesso por linha.

---

## 4. Compromisso da equipe técnica
- Compromisso obtido no início de cada fase, ao planejar a fase com a lista de requisitos a implementar.
- Registrado pela alocação requisito→fase→tarefa, com cada requisito planejado, executado e verificado.

---

## 5. Rastreabilidade bidirecional

| ID req | Implementado em | Verificado/validado em | Órfão? |
|---|---|---|---|
| OWN-01 | Tarefas da fase Fundação (commits citam o ID) | Verificação da fase + aceite do usuário | Não |
| DA-12 | Tarefas da fase Treinos | Verificação + UAT | Não |
| DA-35 | Tarefas da fase Execução | Verificação + UAT em produção | Não |

- **Verificação de órfãos:** auditoria de milestone cruzou três fontes (requisitos, planos, implementação) e reportou **zero requisitos órfãos**. Nenhuma implementação sem requisito correspondente.

---

## 6. Análise de suficiência
- Requisitos do núcleo são necessários e suficientes para o objetivo (trainer prescreve, aluno executa). A restrição de infraestrutura (N-04) foi balanceada excluindo confirmação de e-mail do escopo, sem comprometer o fluxo principal.

---

## 7. Validação dos requisitos
- Validados por aceite do usuário real (trainer) ao fim de cada milestone, com sign-off, e por execução dos fluxos ponta-a-ponta em produção.
- Resultado: fluxos principais validados; produto em uso real.
