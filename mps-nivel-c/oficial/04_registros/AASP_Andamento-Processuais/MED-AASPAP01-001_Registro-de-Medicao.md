# Registro de Medição — AASP_AndamentosProcessuais · Refatoração da Solução de Captura de Andamentos

| Campo | Valor |
|---|---|
| **Documento** | MED-AASPAP01-001 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto** | Cezar Hiraki Velazquez |
| **Processo MPS-SW** | MED (evidência de projeto) |

---

## 1. Objetivo

Registrar as medidas coletadas ao longo do projeto, conforme o PLA-MED-001, para apoiar a análise de prazo, esforço, qualidade e rastreabilidade da refatoração da solução legada `AndamentosProcessuais` para o modelo DataJud/CNJ + `WorkerAndamentos`. As medidas têm origem na Planilha de Gestão GEST-AASPAP01 (abas Medição, Acompanhamento e Change Requests) e no levantamento INTAKE-PROJETO_AASPAP01.

## 2. Indicadores do projeto

| Código | Indicador | Meta | Resultado consolidado | Status |
|---|---|---|---|---|
| M1 | Aderência ao cronograma (% entregas no prazo) | ≥ 85% | ~91% médio (Fases 1–2: 100%; Fases 3–4: ~85% por escopo acordado) | Atingida |
| M2 | Desvio de esforço (%) | ≤ 20% | +9,7% médio (Fases 1–2: +9%; Fases 3–4: +10%) | Atingida |
| M3 | Defeitos identificados em homologação | — | 5 (0 nas Fases 1–2; 5 nas Fases 3–4) | Contidos |
| M4 | Defeitos escapados para produção | 0 | 0 | Atingida |
| M5 | Taxa de contenção de defeitos | ≥ 95% | 100% (5/5 corrigidos antes da implantação) | Atingida |
| M6 | Retrabalho (% do esforço) | ≤ 5% | 0% | Atingida |
| M7 | % requisitos com rastreabilidade completa | 100% | 100% (RASTR-AASPAP01-001) | Atingida |
| M8 | % conformidade GQA | 100% | 100% (21/21 itens conformes) | Atingida |
| M9 | NCs de GQA abertas ao encerramento | 0 | 0 | Atingida |
| M10 | Escopo realizado vs. planejado | 100% | 100% (12 RF + 5 RNF) | Atingida |
| M11 | Rastreabilidade de status por instância | 100% | 100% dos processos com status por instância | Atingida |

> Nota: o projeto foi gerido por horas/fases no ClickUp, sem story points e sem velocity — por isso os indicadores M3/M4 do template CNJ (SP entregues e velocity) não se aplicam e foram substituídos pelos indicadores de qualidade e rastreabilidade efetivamente coletados.

## 3. Medidas de esforço (prazo/progresso)

| Fase | Período | Esforço estimado (h) | Esforço realizado (h) | Desvio | Defeitos | Responsável principal |
|---|---|---|---|---|---|---|
| Fase 1 — Webhook e CapturaServer (EPROC) | Dez/2025–Fev/2026 | 44 | 48 | +9% | 0 | Raony Chagas |
| Fase 2 — Estabilização e integração RabbitMQ | Fev/2026–Mar/2026 | 66 | 72 | +9% | 0 | Raony Chagas / Cezar Hiraki Velazquez |
| Fase 3 — Refatoração para suporte ao CNJ | Abr/2026–Mai/2026 | 130 | 144 | +11% | 1 | Raony Chagas / Mateus Veloso |
| Fase 4 — Tratamento de erros e validação | Mai/2026–Jun/2026 | 90 | 98 | +9% | 4 | Raony Chagas / Caroline Sousa |
| Fase 5 — Implantação | Jun/2026 | 18 | Em apuração | — | 0 | Cezar Hiraki Velazquez / Lucas Batista |
| **Total** | Dez/2025–Jun/2026 | **~348** | **~362 (parcial)** | **+9,7%** | **5** | |

## 4. Indicadores funcionais da refatoração

| Indicador | Meta | Resultado |
|---|---|---|
| Webhook compatível com múltiplas fontes | 100% das fontes | Operacional para CNJ, EPROC/ESAJ e APIs parceiras |
| Processos desligados nas parceiras após captura via CNJ | 100% dos casos identificados | 100% |
| Histórico de movimentações por instância | Sem perda de dados | 100% preservado (modelo por inativação) |

## 5. Análise de variâncias

| Variância | Magnitude | Causa-raiz |
|---|---|---|
| Atraso de ~30 dias na Fase 4 | Média | Escopo adicional acordado (campos `Observacao`, `Segredo`, `CodigoFonteAPI` em múltiplas rotinas e tratamentos de erro) — ver CR-AASPAP01-002 |
| Desvio de esforço de +9,7% no total | Baixa | Homologação EPROC/ESAJ mais extensa e devolutiva aos associados (CR-AASPAP01-001); estabilização além do previsto |

O atraso e o desvio são explicados por escopo adicional acordado com o cliente, absorvido pelo time sem custo extra, e não por desvio de produtividade. O deadline final (Jun/2026) foi mantido. As metas de prazo, esforço, qualidade e rastreabilidade foram atingidas, com 0 defeitos escapados para produção.

## 6. Comunicação dos resultados

Conforme PLA-MED-001 §7, os resultados foram comunicados nas reuniões de alinhamento e revisão (ver ATA-AASPAP01-001), nas auditorias de GQA (GQA-AASPAP01-001, 100% de conformidade) e na devolutiva aos associados sobre o resultado da solução EPROC/ESAJ em produção. A consolidação de encerramento será registrada no fechamento do projeto, após a conclusão da Fase 5.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Registro de medição consolidado a partir da Planilha de Gestão GEST-AASPAP01 (abas Medição, Acompanhamento e Change Requests) e do INTAKE-PROJETO_AASPAP01 v1.0 (14/06/2026). |
