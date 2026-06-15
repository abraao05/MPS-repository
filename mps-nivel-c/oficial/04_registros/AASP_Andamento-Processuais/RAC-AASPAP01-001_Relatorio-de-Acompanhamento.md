# Relatório de Acompanhamento (Status Report) — AASP_AndamentosProcessuais

| Campo | Valor |
|---|---|
| **Documento** | RAC-AASPAP01-001 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Período de referência** | Junho/2026 — Fase 5 (Implantação) |
| **Data do relatório** | 11/06/2026 |
| **Gerente de Projeto** | Cezar Hiraki Velazquez |
| **Processo MPS-SW** | GPR (evidência de projeto) |
| **Destinatários** | Marcos Correa Fernandez Turnes (Representante / Sponsor / PO — AASP); Patrocinador interno (Timeware) |

---

## 1. Situação geral

Desenvolvimento concluído (Fases 1–4); o projeto está em implantação em produção (Fase 5), com encerramento previsto para 30/06/2026.

| Dimensão | Status | Comentário |
|---|---|---|
| **Prazo** | 🟡 Atenção | Atraso de ~30 dias na Fase 4 por escopo adicional acordado (CR-AASPAP01-002) |
| **Escopo** | 🟡 Em mudança | Escopo adicional de homologação EPROC/ESAJ (CR-001) e de tratamento de erros/segredo na Fase 4 (CR-002), ambos acordados |
| **Risco** | 🟢 Sob controle | Comportamento inconsistente das parceiras (R-02) e falhas transitórias do webhook (R-05) tratados |
| **Qualidade** | 🟢 Dentro do esperado | 5 defeitos identificados e 100% contidos antes da implantação; 0 defeitos escapados |

## 2. Resumo do período

A refatoração para o modelo multi-fonte está concluída e validada: fila unificada WorkerAndamentos, webhook de indexação multi-fonte, histórico de movimentações por instância, verificação e desligamento nas APIs parceiras após captura via CNJ e controle de erros e segredo por instância. Os 12 cenários de teste (CT-01 a CT-12) foram 100% aprovados, incluindo a regressão do fluxo EPROC/ESAJ em produção. No período corrente, o foco é a montagem dos pacotes de GMUD e o deploy em produção.

**Indicadores do período (destaque):**

| Indicador | Valor |
|---|---|
| Esforço total realizado (parcial) | ~362 h |
| Desvio de esforço | +9,7% (meta ≤ 20%) |
| Fases concluídas | 4 de 5 |
| Defeitos contidos antes da implantação | 5 (100% contidos) |

## 3. Entregas realizadas no período

| Entrega | Resultado / valor para o cliente | Situação |
|---|---|---|
| Fila unificada WorkerAndamentos (independente do tribunal) | Pipeline preparado para múltiplas fontes | ✅ Concluído |
| Webhook de indexação multi-fonte | Suporte a novas fontes sem alterar a serialização | ✅ Concluído |
| Histórico de movimentações por instância (inativação) | Histórico preservado integralmente, sem sobrescrita | ✅ Concluído |
| Verificação e desligamento nas APIs parceiras pós-CNJ | Fim do duplo processamento na migração | ✅ Concluído |
| Controle de erro (`Observacao`) e segredo (`Segredo`) por instância | Tratamento correto sem omissões por instância | ✅ Concluído |

## 4. Planejado para o próximo período

| Item / marco | Data prevista | Observação |
|---|---|---|
| Deploy em produção (pacotes GMUD) | Jun/2026 | Agendamento com Infraestrutura |
| Encerramento formal do projeto | 30/06/2026 | TAE e ata de aceite total |

## 5. Indicadores do projeto (acompanhamento)

| Indicador | Meta / referência | Período atual | Tendência |
|---|---|---|---|
| Entregas no prazo (aderência ao cronograma) | ≥ 85% | ~91% | ⬆️ |
| Desvio de esforço (estimado × realizado) | ≤ 20% | +9,7% (~362 h vs. ~348 h) | ➡️ |
| Defeitos escapados para produção | 0 | 0 | ⬆️ |
| Conformidade GQA | 100% | 100% (21/21 itens conformes) | ⬆️ |

## 6. Diário de bordo (eventos e impactos)

| Data | Evento / motivo | Origem | Impacto | Situação |
|---|---|---|---|---|
| Abr/2026 | Incorporação de Mateus Veloso (suporte ao desenvolvimento) | Timeware | Reforço de equipe | Concluído |
| Abr–Mai/2026 | Parametrização dos campos do modelo no webhook multi-fonte | Timeware | Ajuste técnico | Resolvido (BUG-01) |
| Mai/2026 | Comportamento inconsistente das parceiras nos endpoints de exclusão | Externo (parceiras) | Tratamento por parceira | Resolvido (R-02) |
| Mai–Jun/2026 | Escopo adicional Fase 4 (Observacao, Segredo, CodigoFonteAPI) | Acordo c/ cliente | Atraso ~30 dias | Resolvido (CR-002, BUG-02..05) |
| Jun/2026 | Atividades de finalização e implantação | Timeware | Em curso | Em andamento |

## 7. Pontos de atenção, riscos e plano de ação

**Comportamento heterogêneo das APIs parceiras** — 🟡 Médio
- **Ponto:** as parceiras (Solucionário, Botmax) têm estruturas e endpoints de exclusão diferentes.
- **Risco:** retorno inconsistente na verificação/desligamento do NUP.
- **Ação:** controladores específicos por parceira com interface comum e registro do retorno (R-02, decisão D06).

**Cobertura de segredo de justiça por instância** — 🟡 Médio
- **Ponto:** um processo pode estar em segredo em uma instância e não em outra.
- **Risco:** tratamento incorreto se o segredo for controlado por processo.
- **Ação:** campo `Segredo` por instância em `ProcessoCapturaLogin` (decisão D07).

## 8. Mudanças (change requests)

| ID | Descrição | Abertura | Impacto | Status | Aceite final |
|---|---|---|---|---|---|
| CR-AASPAP01-001 | Escopo adicional de homologação EPROC/ESAJ e devolutiva aos associados | Jan/2026 | +~42 h (absorvido na Fase 2) | Aprovada (acordada com o cliente) | — |
| CR-AASPAP01-002 | Escopo adicional Fase 4: campos Observacao, Segredo, CodigoFonteAPI e tratamentos de erro | Mai/2026 | +~8 h · atraso ~30 dias | Aprovada (acordada com o cliente) | — |

## 9. Decisões necessárias

| Decisão necessária | Responsável | Prazo desejado |
|---|---|---|
| Confirmação da data de aceite formal total e do go-live em produção | Marcos Correa Fernandez Turnes (AASP) | Jun/2026 |

---

## Cadência de reporte

| Item | Definição |
|---|---|
| Periodicidade | Por marco/fase, com atividades de alinhamento registradas no ClickUp |
| Canal | Homologação + devolutivas ao cliente por fase |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Relatório de acompanhamento (Fase 5) consolidado a partir do Registro de Projeto AASP_AndamentosProcessuais (REG-AASPAP01-001 v1.0, 08/06/2026) e do levantamento de projeto (INTAKE-PROJETO_AASPAP01 v1.0). |
