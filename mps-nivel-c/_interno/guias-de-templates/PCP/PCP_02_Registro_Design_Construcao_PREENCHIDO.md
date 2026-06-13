# Registro de Design e Construção do Produto

> **Modelo de preenchimento** com base no Trainer Connect (diagnóstico: design rastreável a requisitos via especificação de UI e pesquisa de arquitetura; análise de reuso registrada).

---

## 0. Identificação

| Campo | Valor |
|---|---|
| Projeto | Trainer Connect |
| Componente / solução | Módulo de montagem de treinos |
| Data | 2026-06-02 |
| Responsável | *(exemplo: dev)* |

---

## 1. Design da solução

- **Requisitos que atende:** DA-12 (montar treino a partir da biblioteca), EXER-04 (exercícios públicos).
- **Estrutura e funcionalidades:** tela de montagem que lista exercícios da biblioteca, permite compor um treino ordenado e prescrevê-lo a um aluno. Componentes: lista de exercícios, editor de treino, vínculo treino↔aluno.
- **Interfaces:** interna com o módulo de alunos (para prescrever) e com a biblioteca de exercícios (para compor); externa com o banco de dados (persistência com regra de acesso por linha).

### 1.1 Critérios de design pré-definidos
Manutenibilidade (reuso de componentes de UI), tempo de implementação (usar a stack padrão sem novas dependências) e desempenho (carregar a biblioteca sob demanda).

### 1.2 Alternativas e decisão construir / comprar / reutilizar

| Componente | Alternativas | Decisão | Justificativa |
|---|---|---|---|
| Editor de treino | Construir do zero vs. reutilizar componentes de UI existentes | Reutilizar | Componentes de lista/formulário já existiam no projeto; menor custo e consistência visual |
| Persistência | Banco gerenciado vs. solução própria | Comprar (serviço gerenciado) | Tempo de implementação e regras de acesso por linha prontas |

---

## 2. Avaliação do design

| Problema | Severidade | Tratamento | Situação |
|---|---|---|---|
| Risco de divergência entre tabela de treinos e tabela de prescrições | Alta | Padrão: atualizar ambas no mesmo commit | Tratado |
| Achados de revisão de design da tela | Média | Revisão → correção registrada | Tratado |

---

## 3. Implementação

- **Conformidade com o design:** verificação de fase conferiu que o construído corresponde à especificação de UI e aos contratos de interface (exports/props esperados).
- **Informações para evolução/sustentação:** design, decisões (com justificativa) e padrões de implementação ficam registrados nos artefatos de fase; convenções reutilizáveis documentadas como padrões do projeto.
