# Registro de Revisão por Pares

> **Modelo de preenchimento** com base no projeto *Trainer Connect*. Revisão do módulo de execução de treinos (história DA-35 — "Como aluno, quero ver e executar o treino que recebi"). Dados marcados com *(exemplo)* não existiam no projeto solo original mas são representativos de uma equipe Timeware.

---

## 0. Identificação

| Campo | Valor |
|---|---|
| ID / referência | REV-TCON-008 *(exemplo)* |
| Projeto | Trainer Connect |
| Item revisado | Módulo de execução de treinos — história DA-35 |
| Tipo de revisão | Revisão de código (Pull Request) |
| Data | 2025-04 *(exemplo)* |

---

## 1. Participantes

| Papel | Nome / identificação |
|---|---|
| Autor | Dev full-stack *(exemplo)* |
| Revisor(es) | Tech Lead *(exemplo)* |

---

## 2. Itens revisados

`src/modules/workout/workout-execution.service.ts`, `src/modules/workout/workout-execution.controller.ts`, `src/modules/workout/dto/log-set.dto.ts` *(exemplo — arquivos representativos do módulo)*

---

## 3. Apontamentos

| # | Apontamento | Severidade | Tratamento | Situação |
|---|---|---|---|---|
| 1 | Ausência de validação de autorização: qualquer aluno autenticado consegue registrar execução em treinos de outros alunos — falta verificar que o treino pertence ao aluno da sessão antes de persistir | alta | Adicionada verificação `workout.studentId === session.userId` no service antes do `save()` | resolvido |
| 2 | Variável `d` no loop de séries não descreve sua intenção — renomear para `setIndex` | baixa | Renomeada | resolvido |
| 3 | Query N+1 no carregamento das séries de cada exercício: para cada exercício é feito um `SELECT` separado — substituir por `leftJoinAndSelect` na query principal | média | Refatorada query para usar join eager; testado com 10 exercícios, tempo de resposta caiu de ~400ms para ~40ms | resolvido |

---

## 4. Resultado

| Campo | Valor |
|---|---|
| Resultado | Aprovado com ressalvas (apontamentos resolvidos antes do merge) |
| Decisão de merge / avanço | Aprovado para merge após verificação das correções pelo revisor |
| Data da decisão | 2025-04 *(exemplo)* |
| Responsável pela decisão | Tech Lead *(exemplo)* |
