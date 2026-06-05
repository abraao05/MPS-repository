# Plano de Gerência de Configuração

> **Modelo de preenchimento** com base no Trainer Connect (diagnóstico: GCO foi o ponto mais forte — Git com 1015 commits, tags por milestone como baselines, auditorias reais com detecção de órfãos. A lacuna era o registro formal de IC com todos os campos exigidos — aqui mostramos como consolidá-lo).

---

## 0. Identificação

| Campo | Valor |
|---|---|
| Projeto / organização | Trainer Connect |
| Data | 2026-06-02 |
| Responsável | *(exemplo: dev)* |

---

## 1. Itens de configuração (IC)

| ID único | Tipo | Descrição | Situação | Relação | Nível de controle |
|---|---|---|---|---|---|
| repo-código | Código-fonte | Aplicação web | Ativo | Base de todos os demais | Versionamento + revisão no PR |
| migration-NNNN | Migração de BD | Alteração de esquema (ID por timestamp) | Aplicada | Depende da anterior (ordem) | Versionamento ordenado |
| REQUIREMENTS | Documento | Requisitos do projeto | Ativo | Origem das tarefas | Versionado por milestone |
| artefatos de fase | Documento | CONTEXT/PLAN/REVIEW/etc. | Ativo | Ligados a requisitos por ID | Versionamento |

> *Na Timeware, este é o registro consolidado de IC que faltava no projeto solo: além do controle via Git, uma visão única com identificação, tipo, descrição, situação e relação.*

---

## 2. Sistema de gerência de configuração e controle de mudanças

- **Sistema:** controle de versão Git; branches; tags; padrão de commits convencionais (mensagens citam requisito/decisão).
- **Controle de mudanças:** alteração entra por pull request → revisão humana → aprovação → merge na branch principal.

---

## 3. Baselines

| Baseline | O que contém | Data | Entregável/interno? |
|---|---|---|---|
| v1.0 | Fundação (auth + cadastro) | 2025-01 | Entregável |
| v1.5 | Treinos | 2025-02 | Entregável |
| v1.8 | Execução pelo aluno | 2025-04 | Entregável |

> *(No projeto solo, a tag v1.5 chegou a faltar — uma falha pontual de baseline que uma auditoria de configuração detecta; ver seção 5.)*

---

## 4. Registros de ICs e modificações

- **Onde:** histórico completo do Git (todas as modificações com autor, data e mensagem citando requisito/decisão); resumos de fase registram as mudanças por plano; migrações em sequência ordenada.
- **Uso:** rastrear quando e por que cada item mudou; base para auditoria.

---

## 5. Auditorias de configuração

| Auditoria | O que verificou | Achados | Tratamento | Data |
|---|---|---|---|---|
| Auditoria do milestone v1.7 | Integridade da baseline, cobertura de requisitos (3 fontes), órfãos | Zero requisitos órfãos; uma fase sem registro de validação | Validação executada antes do fechamento | 2025-03 |
| Auditoria do milestone v1.8 | Integridade + integração entre fases | Wiring entre fases confirmado | — | 2025-04 |
