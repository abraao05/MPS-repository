# Change Request — Módulo de Comércio: Parqueamento para v2.0

> **Modelo de preenchimento** com base no Change Request real do projeto *Trainer Connect*. O cliente solicitou integração com gateway de pagamento; a análise de impacto mostrou dependência imatura e risco ao cronograma do núcleo; decisão: parquear formalmente para a v2.0. Este é o exemplo mais representativo de CR deste projeto e serve como modelo de como um CR de "parqueamento de escopo" deve ser documentado.

---

## Identificação

| Campo | Valor |
|---|---|
| Documento | CR-TCON-001 |
| Projeto | Trainer Connect — plataforma de gestão para personal trainers |
| Título da mudança | Parqueamento do módulo de comércio (integração com gateway de pagamento) para a v2.0 |
| Solicitante | *(exemplo: cliente / PO Trainer Connect)* |
| Data da solicitação | 10/03/2025 |
| Gerente de Projeto | *(exemplo: Gestor Timeware)* |

---

## 1. Descrição da mudança

O escopo atual do Trainer Connect (conforme Plano do Projeto v2, seção 1 — Escopo incluído) não previa integração com gateway de pagamento na v1.8. O cliente solicitou a inclusão de um módulo de comércio que permita ao trainer cobrar mensalidades diretamente pela plataforma, com integração a um gateway de pagamento externo.

A mudança proposta altera o escopo incluído adicionando: (a) cadastro de planos de assinatura pelo trainer, (b) fluxo de cobrança do aluno via gateway, (c) integração técnica com a API do gateway. O estado atual do produto não contempla nenhum desses componentes.

---

## 2. Justificativa

O cliente identificou que a cobrança de mensalidades é um ponto de atrito relevante na gestão do trainer — hoje feita fora do sistema (WhatsApp, boleto manual). A integração com gateway tornaria a plataforma mais completa e aumentaria a retenção do trainer como usuário.

A solicitação é legítima do ponto de vista de produto. A questão é de viabilidade e momento: a integração com gateway de pagamento envolve dependências técnicas que ainda não estão maduras (certificação, contrato com o gateway, tratamento de PCI-DSS) e impactaria o cronograma de entrega do núcleo do produto (v1.8 — execução pelo aluno), que está em fase final.

---

## 3. Análise de impacto

| Dimensão | Impacto | Detalhamento |
|---|---|---|
| Escopo | Alto | Adiciona três novos componentes ao produto (cadastro de planos, fluxo de cobrança, integração com gateway) — equivale a uma fase completa adicional de desenvolvimento |
| Prazo | Alto | Estimativa de 6–8 semanas adicionais para implementação segura (integração + testes de pagamento + validação de conformidade); inviabiliza a entrega da v1.8 no prazo de abr/2025 se incluído agora |
| Esforço / custo | Médio | ~50–60 h de esforço adicional estimado *(exemplo)*; impacto financeiro a negociar se incluído como aditivo — por isso a proposta é de parqueamento sem custo adicional imediato |
| Riscos introduzidos | Alto | Dependência de contrato e certificação com gateway (fora do controle da equipe); requisitos de conformidade PCI-DSS não levantados; integração complexa com maior probabilidade de regressões no módulo de alunos/treinos |

---

## 4. Tipo de tratamento proposto

- [ ] Aditivo
- [ ] Crédito
- [ ] Troca de prioridade
- [x] **Parqueamento** — o item é formalmente removido do escopo atual e registrado para versão futura (sem impacto financeiro imediato)

O módulo de comércio é parqueado formalmente para a v2.0. A decisão de incluí-lo, com análise de viabilidade técnica e negociação de custo adicional, ocorre quando as dependências (gateway, PCI-DSS) estiverem resolvidas. O escopo e orçamento atuais do projeto (v1.8) permanecem inalterados.

---

## 5. Decisão

| Campo | Valor |
|---|---|
| Decisão | Aprovado |
| Responsável pela decisão | *(exemplo: Gestor Timeware — Gerente de Projeto, com concordância do cliente/PO)* |
| Data da decisão | 17/03/2025 |
| Referência à ata ou registro | ATA-TCON-003 *(exemplo)* |
| Condições | Nenhuma — parqueamento imediato, sem impacto no cronograma ou orçamento atuais |

---

## 6. Reflexo no projeto

- **Backlog / rastreador de tarefas:** histórias do módulo de comércio movidas para o épico v2.0 no Jira *(exemplo)*; não constam no sprint ou milestone atual.
- **Rastreabilidade:** requisitos de comércio atualizados no REQUIREMENTS.md como "fora do escopo v1.8 — parqueado para v2.0 (ref. CR-TCON-001)".
- **Baseline do Plano do Projeto:** Plano do Projeto atualizado para v3 (seção 1 — Escopo excluído: módulo de comércio movido para v2.0 por CR-TCON-001). Orçamento e cronograma da v1.8 mantidos.
- **Outros artefatos afetados:** Termo de Encerramento (TEN-TCON-001) referenciará este CR na seção de entregas realizadas; Registro de Riscos atualizado (R-02 — dependência de gateway: tratado por parqueamento).
