# Registro de Medição — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | MED-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Plano de medição** | PLA-MED-001 v1.3 (05/06/2026) — medidas organizacionais M1–M7 |

---

## 1. Objetivo

Registrar os resultados das 7 medidas organizacionais (M1–M7) do PLA-MED-001 aplicadas ao projeto AASPGOV01. Conforme ADAP-AASPGOV01-001, os indicadores foram apurados ao encerramento, sobre o ciclo completo do projeto.

## 2. Resultados das medidas M1–M7

| Medida | Objetivo de medição | Meta | Resultado AASPGOV01 | Status |
|---|---|---|---|---|
| M1 — Prazo | Previsibilidade de prazo | ≤ 5% desvio | 0% — entregue em 02/06/2026 conforme TAP | ✅ Atingida |
| M2 — Esforço | Previsibilidade de esforço | ≤ 10% desvio | +9,3% — 216 h estimadas → 236 h realizadas | ✅ Atingida |
| M3 — Velocity | Capacidade de entrega | ≥ 12 SP/sprint | 15 SP/sprint (S0=15, S1=16, S2=16, S3=12) | ✅ Atingida |
| M4 — Itens entregues | Eficiência de entrega | ≥ 95%/sprint | 100% — 17 itens planejados e entregues | ✅ Atingida |
| M5 — Defeitos | Qualidade do produto | ≤ 1 def/4 SP | 0,085 def/SP (5 bugs em 59 SP ≈ 1/12 SP) | ✅ Atingida |
| M6 — Contenção | Antecipação de defeitos | 100% em HOM | 5/5 detectados em HOM · 0 escaparam para produção | ✅ Atingida |
| M7 — Retrabalho | Eficiência pós-entrega | ≤ 5% reabertos | 0% — nenhum item reaberto após conclusão | ✅ Atingida |

## 3. Esforço realizado por fase

| Fase | Período | Est. (h) | Real. (h) | Variação |
|---|---|---|---|---|
| Fase 1 — Arquitetura | 14/04 – 16/04/2026 | 16 | 16 | 0% |
| Fase 2 — Mapeamento e Autenticação | 17/04 – 23/04/2026 | 40 | 44 | +10% |
| Fase 3 — Desenvolvimento dos Serviços | 24/04 – 20/05/2026 | 120 | 128 | +6,7% |
| Fase 4 — Homologação e Correções | 21/05 – 02/06/2026 | 40 | 48 | +20% |
| **Total** | 14/04 – 02/06/2026 | **216** | **236** | **+9,3%** |

## 4. Capacidade de entrega (sprints S0–S3)

| Sprint | Story Points | Período | Velocity |
|---|---|---|---|
| S0 | 15 SP | 14/04 – 16/04/2026 | 15 SP/sprint |
| S1 | 16 SP | 17/04 – 23/04/2026 | 16 SP/sprint |
| S2 | 16 SP | 24/04 – 08/05/2026 | 16 SP/sprint |
| S3 | 12 SP | 09/05 – 02/06/2026 | 12 SP/sprint |
| **Total / média** | **59 SP** | 14/04 – 02/06/2026 | ~15 SP/sprint |

## 5. Análise de variâncias

O desvio de esforço (+9,3%) concentrou-se nas Fases 2 e 4: o mapeamento da API Jira (formato ADF proprietário) e o ciclo de correção de 5 defeitos na homologação. O desvio manteve-se dentro da meta (≤ 10%). Não houve retrabalho pós-entrega (M7 = 0%) nem defeitos escapados para produção (M6 = 0).

## 6. Ações corretivas geradas

| ID | Ação corretiva | Incorporação organizacional |
|---|---|---|
| AC-01 | Adotar fator de estimativa conservador (+30%) para mapeamento de APIs externas com formatos proprietários | Incorporado ao PLA-GPR-001 como ajuste de template para projetos de integração com APIs Atlassian |
| AC-02 | Incluir cenário de teste obrigatório para tratamento de HTML e sanitização de campos em projetos de migração/integração | Incorporado ao TPL-VV-001 §6 como cenário Gherkin de referência (baseado em CT-05 e CT-10) |

## 7. Comunicação dos resultados

Conforme PLA-MED-001 §7, os resultados foram comunicados na validação da homologação (ATA-AASPGOV01-003) e no encerramento (ATA-AASPGOV01-004 / TAE-AASPGOV01-001), e registrados no repositório organizacional de medidas (REG-MED-001).

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Registro de medição (M1–M7) consolidado a partir do INTAKE-AASPGOV01 (14/06/2026), Bloco 12. |
