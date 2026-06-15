# Registro de Verificação de GQA — AASP_AndamentosProcessuais

| Campo | Valor |
|---|---|
| **Documento** | GQA-AASPAP01-001 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Marco / tipo de verificação** | Desenvolvimento / Homologação (execução, Fases 1–4) |
| **Auditor (GQA)** | Jonathan Barbosa (Garantia da Qualidade de Processo — auditor independente da equipe do projeto) |
| **Gerente de Projeto** | Cezar Hiraki Velazquez |
| **Processo MPS-SW** | GQA / GPC (evidência de projeto) |

---

## 1. Escopo da verificação

Verificação de aderência ao processo-padrão (PRO-GPC-001) e de existência/completude dos produtos de trabalho do projeto na fase de execução, conforme EST-GPC-001. A independência da função de GQA é assegurada pela atuação de Jonathan Barbosa (Garantia da Qualidade de Processo), fora da equipe de engenharia do projeto. A verificação foi conduzida em três marcos auditados em 08/06/2026: Fases 1–2 (10 itens), Fases 3–4 (11 itens) e consolidado do ciclo (21 itens), com 0 desvios e 100% de conformidade.

## 2. Verificação de aderência ao processo

| # | Item verificado | Resultado | Referência ao processo |
|---|---|---|---|
| 1 | Requisitos especificados e validados | ✅ Conforme | REQ-AASPAP01-001; ATAs de alinhamento |
| 2 | Processo-padrão adaptado e registrado | ✅ Conforme | ADAP-AASPAP01-001; GUIA-GPC-001 |
| 3 | Design documentado e avaliado antes da construção | ✅ Conforme | PCP-AASPAP01-001 |
| 4 | V&V planejada e executada; defeitos tratados | ✅ Conforme | VV / REL-VV-AASPAP01-001 |
| 5 | Decisões relevantes registradas (gatilhos GDE) | ✅ Conforme | GDE-AASPAP01-001 (D01–D07) |
| 6 | Acompanhamento e mudanças formalizados | ✅ Conforme | RAC / CR-AASPAP01-001; CR-AASPAP01-002 |
| 7 | Revisão por pares (PR ≥ 1 revisor além do autor) | ✅ Conforme | REV-AASPAP01-001 |
| GCO-1 | ICs identificados e controlados com convenção de versão | ✅ Conforme | GCO-AASPAP01-001 §2–3 |
| GCO-2 | Baseline estabelecida no marco (refatoração CNJ) | ✅ Conforme | GCO-AASPAP01-001 §4 (`v240`) |
| GCO-3 | Auditoria de configuração de encerramento | ⚠ Desvio | Pendente — projeto em execução (Fase 5 — implantação) |

## 3. Verificação de produtos de trabalho

| # | Produto de trabalho | Existe? | Completo? | Segue padrão? | Observação |
|---|---|---|---|---|---|
| 1 | TAP-AASPAP01-001 | Sim | Sim | Sim | — |
| 2 | PLA-AASPAP01-001 | Sim | Sim | Sim | Baseline de aprovação (REG v1.0, 08/06/2026) |
| 3 | REQ-AASPAP01-001 | Sim | Sim | Sim | 12 RF + 5 RNF |
| 4 | PCP-AASPAP01-001 | Sim | Sim | Sim | — |
| 5 | ITP / VV / REL-VV / REV | Sim | Sim | Sim | — |
| 6 | GCO / GDE / MED / RASTR | Sim | Sim | Sim | — |

## 4. Achados

| # | Desvio | Severidade | Recomendação | Responsável | Status |
|---|---|---|---|---|---|
| 1 | Auditoria de configuração de encerramento pendente (Fase 5 em andamento) | Baixa | Registrar no encerramento (TAE e baseline final) | Cezar Hiraki Velazquez | Aberto |
| 2 | Cobertura de testes automatizados / pipeline de CI limitada | Baixa | Avaliar automação de testes em ciclos futuros (lição aprendida) | Cezar Hiraki Velazquez | Aberto |

## 5. Resultado

| Campo | Valor |
|---|---|
| **Resultado geral** | Conforme com ressalvas |
| **% de conformidade** | Marcos auditados em 08/06/2026: 21/21 itens conformes (100%); item GCO-3 (auditoria de encerramento) pendente por o projeto estar em execução. Produtos de trabalho 100% existentes e aderentes ao padrão |
| **Achados abertos** | 2 (severidade baixa, relativos ao encerramento e à automação de testes) |
| **Oportunidades de melhoria** | Antecipar a verificação de configuração de encerramento; ampliar cobertura de testes automatizados / CI |

> Referência ao processo de origem: EST-GPC-001 (estratégia de Garantia da Qualidade de Processo).

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Registro de verificação de GQA (execução) consolidado a partir do Registro de Projeto AASP_AndamentosProcessuais e do INTAKE-PROJETO_AASPAP01 v1.0. |
