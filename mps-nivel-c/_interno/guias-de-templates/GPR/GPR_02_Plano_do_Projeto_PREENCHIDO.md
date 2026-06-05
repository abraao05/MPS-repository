# Plano do Projeto

> **Nota sobre este exemplo.** Este é um **modelo de preenchimento** — mostra como o template fica preenchido, usando o projeto real *Trainer Connect* como base. Os dados vêm do diagnóstico de maturidade do repositório. Onde um dado não existia no projeto solo original (ex.: orçamento comercial, equipe), usamos um valor plausível de exemplo e o marcamos com *(exemplo)* — porque na Timeware esses campos terão valor real. O objetivo é servir de orientação visual de "como preencher", não ser um registro oficial do Trainer Connect.

---

## 0. Identificação e controle de versão

| Campo | Valor |
|---|---|
| Projeto | Trainer Connect — plataforma de gestão para personal trainers |
| Código / chave no rastreador de tarefas | TCON *(exemplo)* |
| Gestor responsável | *(exemplo: nome do gestor Timeware)* |
| Data de abertura | 2025-01 *(exemplo)* |
| Versão deste plano | v3 |
| Data desta versão | 2026-06-02 |
| O que mudou em relação à versão anterior | Inclusão do milestone v1.8; reestimativa do escopo de comércio (v2.0) movido para fora do escopo atual |

---

## 1. Escopo do trabalho

- **Objetivo de negócio.** Permitir que personal trainers gerenciem alunos, montem e prescrevam treinos e acompanhem a execução, num produto web acessível ao trainer e aos seus alunos.
- **Escopo incluído.** Cadastro e gestão de alunos; biblioteca de exercícios; montagem e prescrição de treinos; acompanhamento de execução pelo aluno; autenticação e perfis (trainer/aluno).
- **Escopo excluído.** Cobrança/pagamentos in-app e funcionalidades de comércio (parqueadas como v2.0, dependentes de integração com gateway de pagamento); confirmação de e-mail (excluída por limite do plano de infraestrutura adotado). *Exclusões registradas para evitar ambiguidade — não são esquecimentos, são decisões.*
- **Critério de pronto do projeto.** Trainer consegue cadastrar alunos, prescrever treinos e o aluno consegue executá-los em produção, com os fluxos validados por usuário real.
- **Controle de mudança de escopo.** Mudanças de escopo são registradas como ação no Relatório de Acompanhamento e, se aprovadas, geram nova versão deste plano. (Exemplo real: o escopo de comércio foi formalmente movido para fora, gerando nova versão.)

---

## 2. Abordagem de condução do projeto

- **Abordagem-padrão da organização.** Ciclo de vida por fases, aplicado a cada incremento: levantamento de contexto → pesquisa de alternativas → planejamento detalhado → execução → revisão → verificação → validação → aceite do usuário. Cada fase produz seus registros próprios. A lista de tarefas de cada fase é explicitada no planejamento da fase.
- **Adaptações para este projeto.** Segue a abordagem-padrão integralmente. Adaptação pontual: como o produto tem forte componente visual, cada fase de interface inclui um registro adicional de especificação de UI antes da execução.

---

## 3. Estimativas

### 3.1 Método de estimativa

- **Dimensão (tamanho do trabalho).** Story Points, estimados por história de usuário via Planning Poker.
- **Esforço e duração.** Derivados da dimensão pela velocidade da equipe (ver 3.4).
- **Custo.** Definido comercialmente (seção 4); não derivado do esforço.

### 3.2 Histórias de usuário e dimensão estimada

| ID da história | História (como… quero… para…) | Pontos (estimado) | Fase alocada | Status |
|---|---|---|---|---|
| OWN-01 | Como trainer, quero cadastrar meus alunos para gerenciar minha base | 5 | Fundação | Concluída |
| DA-12 | Como trainer, quero montar um treino a partir da biblioteca de exercícios para prescrever ao aluno | 8 | Treinos | Concluída |
| DA-35 | Como aluno, quero ver e executar o treino que recebi para seguir minha rotina | 8 | Execução | Concluída |
| EXER-04 | Como trainer, quero exercícios públicos na página de exercícios para reaproveitar conteúdo | 3 | Biblioteca | Concluída |
| *(demais histórias…)* | | | | |

- **Total de pontos estimados do projeto (baseline):** 120 *(exemplo — soma de todas as histórias do escopo)*

### 3.3 Esforço e duração agregados

| Métrica | Valor estimado | Como foi calculado (racional obrigatório) |
|---|---|---|
| Esforço total | ~150 h *(exemplo)* | 120 pontos × 1,25 h/ponto (esforço médio observado) |
| Duração | ~10 semanas *(exemplo)* | esforço ÷ capacidade de ~15 h úteis/semana dedicadas |
| Premissas assumidas | Dedicação parcial; uso intensivo de assistência de IA na implementação | — |

### 3.4 Velocidade e referência de esforço

- **Esforço médio por ponto usado:** 1,25 h/ponto *(exemplo, derivado das durações realizadas registradas nos resumos de fase)*
- **Velocidade da equipe usada:** ~12 pontos/semana *(exemplo)*
- **Origem desta referência:** durações reais das fases já concluídas do próprio projeto (estimado vs. realizado acumulado). *Tratada como premissa revisável: a referência organizacional consolidada ainda está em construção.*

---

## 4. Orçamento, cronograma e marcos  *(baseline)*

- **Orçamento total (comercial, contratado):** R$ 45.000 *(exemplo — valor comercial; o Trainer Connect original foi solo e sem custo formal)*
- **Cronograma macro:** início 2025-01 → término previsto 2025-04 *(exemplo)*

### 4.1 Marcos

| Marco | Data prevista | Critério de conclusão |
|---|---|---|
| v1.0 — Fundação (auth + cadastro) | 2025-01 | Trainer cadastra alunos em produção |
| v1.5 — Treinos | 2025-02 | Trainer monta e prescreve treino |
| v1.8 — Execução pelo aluno | 2025-04 | Aluno executa treino prescrito; fluxos validados por usuário real |

### 4.2 Fases e alocação  *(tabela viva)*

| Fase | Histórias incluídas | Esforço estimado | Início | Fim | Parcela do orçamento alocada |
|---|---|---|---|---|---|
| Fundação | OWN-01..06 | ~30 h | 2025-01 | 2025-01 | R$ 9.000 |
| Treinos | DA-01..36 | ~55 h | 2025-02 | 2025-02 | R$ 16.500 |
| Execução | DA-35, EXER-04… | ~45 h | 2025-03 | 2025-04 | R$ 13.500 |
| Biblioteca | EXER-04… | ~20 h | 2025-03 | 2025-03 | R$ 6.000 |

*(Soma das parcelas = R$ 45.000 = orçamento total. Valores de exemplo.)*

---

## 5. Recursos humanos

| Papel | Pessoa | Habilidades necessárias | Lacuna (a contratar / a treinar) |
|---|---|---|---|
| Desenvolvedor full-stack | *(exemplo: dev Timeware)* | React, banco de dados, integração de APIs | Nenhuma |
| Gestor do projeto | *(exemplo)* | Gestão de produto, priorização | Nenhuma |

---

## 6. Recursos materiais e ambiente de trabalho

- **Ambientes.** Desenvolvimento (local), homologação (preview automático a cada alteração), produção (domínio público).
- **Ferramentas e infraestrutura.** Stack web (React/Vite), banco de dados gerenciado com regras de acesso por linha, hospedagem com publicação automática, controle de versão Git.
- **Padrão organizacional de referência.** ‹na Timeware: ambiente-padrão de trabalho da organização — a definir no processo OSW›

---

## 7. Estratégia de transição para operação e suporte

- **Como o produto entra em operação.** Publicação automática a cada alteração aprovada na branch principal; migrações de banco aplicadas de forma versionada e ordenada.
- **Quem opera e dá suporte após a entrega.** *(exemplo: equipe de sustentação Timeware)*
- **Tarefas e cronograma de transição.** Validação em produção com usuário real antes do encerramento do milestone; monitoramento dos primeiros acessos.

---

## 8. Partes interessadas

| Parte interessada | Papel / interesse | Como e quando é envolvida |
|---|---|---|
| Personal trainer (usuário primário) | Usa o produto para gerenciar alunos | Validação de aceite ao fim de cada milestone |
| Alunos do trainer | Usuários finais do acompanhamento | Teste dos fluxos de execução |
| Patrocinador / cliente | Define escopo e aprova orçamento | Aprovação do plano e dos marcos |

---

## 9. Riscos e oportunidades

| ID | Risco / Oportunidade | Probabilidade × Impacto | Tratamento | Responsável | Situação |
|---|---|---|---|---|---|
| R-01 | Limite do plano de infraestrutura impede confirmação de e-mail | Média × Baixa | Excluir confirmação de e-mail do escopo atual; reavaliar com upgrade de plano | Gestor | Tratado (escopo ajustado) |
| R-02 | Dependência de integração de pagamento (gateway) para o módulo de comércio | Alta × Alto | Parquear módulo de comércio (v2.0) até prereqs do gateway estarem prontos | Gestor | Em acompanhamento |
| O-01 | Reuso da biblioteca de exercícios entre trainers como diferencial | — | Avaliar exercícios públicos como funcionalidade de valor | Gestor | Oportunidade aberta |

---

## 10. Viabilidade, integração e compromisso

### 10.1 Viabilidade
- O projeto é viável com a equipe e infraestrutura previstas. Restrições (limite de infra, dependência de gateway) foram tratadas por ajuste de escopo.
- Ajuste realizado: módulo de comércio movido para fora do escopo atual, viabilizando a entrega do núcleo no prazo.

### 10.2 Consistência do plano
- Escopo, estimativas, marcos e recursos são consistentes: o esforço estimado (~150 h) cabe na duração prevista (~10 semanas) com a capacidade da equipe.

### 10.3 Revisão e compromisso
- Plano revisado com os interessados em 2025-01 *(exemplo)*.
- Dependências críticas: integração de pagamento (isolada no v2.0); ordem de construção das fases (Fundação antes de Treinos antes de Execução).
- Compromisso obtido de: patrocinador (aprovação de escopo/orçamento) e equipe de desenvolvimento (execução). *(exemplo)*
