# Matriz de Rastreabilidade — Trainer Connect

> **Modelo de preenchimento** com base no projeto real *Trainer Connect* — plataforma web para personal trainers gerenciarem alunos e prescreverem treinos. Os IDs de requisitos (OWN-01, DA-12, DA-35, EXER-04) são reais do repositório. Os IDs de casos de teste e itens de design são plausíveis e compatíveis com a estrutura do projeto — marcados com *(exemplo)* onde não havia dado direto disponível. O objetivo é mostrar como a cadeia de rastreabilidade fica preenchida na prática.

---

## Identificação

| Campo | Valor |
|---|---|
| Documento | MR-TCON-001 |
| Projeto | Trainer Connect — plataforma de gestão para personal trainers |
| Versão | v2 |
| Data | 30/04/2025 |
| Responsável | *(exemplo: Gestor Timeware)* |

---

## Matriz

| Necessidade (ID) | Requisito (ID) | Descrição do requisito | Item de design | Item no backlog / Jira | Caso de teste (ID) | Situação |
|---|---|---|---|---|---|---|
| N-01 | OWN-01 | Como trainer, quero cadastrar e gerenciar meus alunos para organizar minha base | Componente React `StudentList` + serviço `studentsService` + tabela `students` (banco) | TCON-12 *(exemplo)* | CT-OWN-01 — cadastro de aluno com dados válidos retorna 200 e cria registro | Verificado |
| N-02 | DA-12 | Como trainer, quero montar um treino a partir da biblioteca de exercícios para prescrever ao aluno | Componente React `WorkoutBuilder` + serviço `workoutsService` + tabela `workouts` e `workout_exercises` | TCON-28 *(exemplo)* | CT-DA-12 — montagem de treino com 3 exercícios persiste corretamente e aparece na lista do aluno | Verificado |
| N-03 | DA-35 | Como aluno, quero ver e executar o treino que recebi para seguir minha rotina de exercícios | Componente React `WorkoutExecution` + serviço `executionService` + tabela `workout_logs` | TCON-45 *(exemplo)* | CT-DA-35 — aluno executa treino prescrito e o progresso é registrado corretamente | Verificado |
| N-02 | EXER-04 | Como trainer, quero exercícios públicos disponíveis na biblioteca para reaproveitar conteúdo entre trainers | Componente React `ExerciseLibrary` (filtro público) + campo `is_public` na tabela `exercises` + RLS policy | TCON-37 *(exemplo)* | CT-EXER-04 — exercícios públicos aparecem na biblioteca de todos os trainers; exercícios privados só para o trainer dono | Atendido |

---

## Cobertura

### Requisitos sem cobertura de teste

| Requisito (ID) | Motivo da ausência de cobertura | Ação prevista |
|---|---|---|
| Nenhum | Todos os requisitos do escopo v1.8 possuem ao menos um caso de teste associado | — |

### Itens desenvolvidos sem requisito associado (órfãos de construção)

| Item no backlog / Jira | Descrição | Ação prevista |
|---|---|---|
| Nenhum | A auditoria de milestone detectou e tratou órfãos ao longo do desenvolvimento — todos os itens implementados têm requisito rastreável ao fim da v1.8 | — |
