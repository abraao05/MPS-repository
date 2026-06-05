# Registro de Decisão

> **Modelo de preenchimento** com base no Trainer Connect (diagnóstico: decisões registradas com racional e resultado em tabelas de Key Decisions; a lacuna era a *diretriz* dizendo quando uma decisão exige processo formal — aqui mostramos preenchida).

---

## 0. Identificação

| Campo | Valor |
|---|---|
| ID da decisão | D-07 |
| Projeto / contexto | Trainer Connect — módulo de comércio (v2.0) |
| Data | 2025-03 |
| Decisor (papel) | Gestor do produto |

### 0.1 Por que esta decisão exige processo formal
- **Diretriz organizacional:** exigem decisão formal as escolhas que (a) são caras de reverter, (b) afetam arquitetura ou dependências externas, ou (c) impactam o cronograma de entrega. O decisor é o gestor do produto para escopo, o líder técnico para arquitetura.
- **Por que se enquadra:** decidir sobre o módulo de pagamentos afeta dependência externa (gateway) e o cronograma de entrega do núcleo — critérios (b) e (c).

---

## 1. Problema ou questão
Incluir o módulo de comércio (pagamentos) no escopo atual da entrega, ou adiá-lo?

---

## 2. Alternativas de solução

| ID | Alternativa | Descrição |
|---|---|---|
| A | Incluir agora | Implementar pagamentos integrando o gateway nesta entrega |
| B | Parquear para v2.0 | Adiar o módulo até os pré-requisitos do gateway estarem prontos |

---

## 3. Critérios de avaliação

| Critério | Peso | Por que importa |
|---|---|---|
| Risco de atraso do núcleo | Alto | A entrega do núcleo (trainer/aluno) é a prioridade |
| Maturidade da dependência (gateway) | Alto | Sem pré-requisitos prontos, a integração é arriscada |
| Valor imediato ao usuário | Médio | Pagamento não é necessário para o fluxo principal |

---

## 4. Método de avaliação
- **Método:** análise de tradeoff (prós e contras ponderados pelos critérios).
- **Por que:** decisão binária com poucos critérios claros; matriz ponderada seria excesso de formalismo.

---

## 5. Avaliação e decisão

| Alternativa | Avaliação | Resultado |
|---|---|---|
| A (incluir) | Alto risco de atrasar o núcleo; gateway imaturo | Desfavorável |
| B (parquear) | Protege a entrega do núcleo; adia valor não-essencial | Favorável |

- **Decisão:** parquear o módulo de comércio para a v2.0 (alternativa B).
- **Justificativa:** preserva o cronograma do núcleo e evita integração arriscada com dependência imatura; o valor adiado não é essencial ao fluxo principal.
- **Resultado observado:** núcleo entregue no prazo (milestone v1.8); módulo de comércio segue parqueado aguardando pré-requisitos.
