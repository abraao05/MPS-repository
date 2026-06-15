# Change Request — Escopo adicional do ciclo de refatoração (homologação EPROC/ESAJ e tratamento de erros/segredo)

| Campo | Valor |
|---|---|
| **Documento** | CR-AASPAP01-001 (consolida CR-AASPAP01-001 e CR-AASPAP01-002) |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto** | Cezar Hiraki Velazquez |
| **Processo MPS-SW** | GPR (controle de mudanças — evidência de projeto) |

---

Este documento consolida as duas solicitações de mudança formalizadas no projeto, ambas aprovadas pelo representante/patrocinador do cliente, Marcos Correa Fernandez Turnes.

## CR-AASPAP01-001 — Escopo adicional de homologação EPROC/ESAJ e devolutiva aos associados

### 1. Descrição da mudança

Incluir um escopo adicional de homologação da captura EPROC/ESAJ por amostragem e a devolutiva aos associados da AASP sobre o resultado da solução em produção, além do previsto na linha de base original.

### 2. Justificativa

Garantir a validação dos critérios de aceite em ambiente compartilhado (sem Elasticsearch dedicado) e dar retorno formal aos associados sobre a operação da solução EPROC/ESAJ, fortalecendo a confiança na transição e antecipando a detecção de problemas.

### 3. Análise de impacto

| Dimensão | Impacto |
|---|---|
| Escopo | Ampliação acordada — homologação por amostragem + devolutiva aos associados |
| Prazo | +~42 h, absorvidas na Fase 2 — sem impacto no prazo final |
| Esforço / custo | Neutro — esforço absorvido pelo time, sem custo extra ao cliente |
| Riscos | Baixo — atividade de validação reduz o risco de regressão (R-01) |

### 4. Tipo de tratamento

- [x] **Aditivo de escopo absorvido** — esforço adicional sem custo extra
- [ ] Troca de prioridade
- [ ] Crédito

### 5. Decisão

| Situação | Responsável | Data | Ref. |
|---|---|---|---|
| Aprovada | Marcos Correa Fernandez Turnes (cliente/PO) | Jan/2026 | GEST-AASPAP01 (aba Change Requests); REG-AASPAP01-001 §3.5 |

---

## CR-AASPAP01-002 — Escopo adicional da Fase 4 (Observacao, Segredo, CodigoFonteAPI e tratamentos de erro)

### 1. Descrição da mudança

Incluir, na Fase 4, o tratamento de erros por instância via campo `Observacao` (`ProcessoCapturaLogin`), o controle de segredo de justiça por instância via campo `Segredo`, e a atualização do campo `CodigoFonteAPI` em múltiplas rotinas — com os tratamentos de erro parcial, NUP inválido e priorização correlatos.

### 2. Justificativa

A operação real exigiu granularidade por instância: um processo pode estar em segredo (ou falhar) em uma instância e não em outra, e a fonte efetiva de captura precisa ser registrada por processo. Esses requisitos (RF07–RF12) não estavam dimensionados na linha de base original e foram acordados com o cliente.

### 3. Análise de impacto

| Dimensão | Impacto |
|---|---|
| Escopo | Ampliação acordada — RF07 a RF12 (erros por instância, segredo, `CodigoFonteAPI`, desmembramento do `RunUpdater`) |
| Prazo | +~8 h; atraso de ~30 dias vs. prazo original da Fase 4, absorvido — deadline final mantido |
| Esforço / custo | Neutro — esforço adicional absorvido pelo time, sem custo extra |
| Riscos | Tratado — comportamento inconsistente das parceiras (R-02) e perda transitória no webhook (R-05) endereçados |

### 4. Tipo de tratamento

- [x] **Aditivo de escopo absorvido** — esforço adicional sem custo extra
- [ ] Troca de prioridade
- [ ] Crédito

### 5. Decisão

| Situação | Responsável | Data | Ref. |
|---|---|---|---|
| Aprovada | Marcos Correa Fernandez Turnes (cliente/PO) | Mai/2026 | GEST-AASPAP01 (aba Change Requests); REG-AASPAP01-001 §3.5; GDE-AASPAP01-001 (D07) |

---

## Impacto consolidado

| Dimensão | Resultado |
|---|---|
| Prazo | Desvio de ~30 dias na Fase 4 absorvido; encerramento previsto (Jun/2026) mantido |
| Custo | Neutro — esforço adicional absorvido pelo time, sem custo extra ao cliente |
| Escopo | Ampliação acordada com o cliente em ambos os casos; ambos os CRs aprovados formalmente |

Reflexo no projeto: as mudanças estão refletidas no cronograma e no acompanhamento por fase (GEST-AASPAP01, aba Acompanhamento) e na matriz de rastreabilidade (RASTR-AASPAP01-001).

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Change requests CR-AASPAP01-001 e CR-AASPAP01-002 consolidados a partir da Planilha de Gestão GEST-AASPAP01 (aba Change Requests) e do INTAKE-PROJETO_AASPAP01 v1.0 (14/06/2026). |
