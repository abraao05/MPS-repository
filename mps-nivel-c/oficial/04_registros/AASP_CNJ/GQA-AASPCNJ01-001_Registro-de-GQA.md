# Registro de Verificação de GQA — AASP_CNJ · WorkerAndamentos

| Campo | Valor |
|---|---|
| **Projeto** | AASP_CNJ — WorkerAndamentos: Agente de Captura de Andamentos Processuais |
| **Marco / tipo de verificação** | Desenvolvimento / Homologação (execução) |
| **Data** | 11/06/2026 |
| **Auditor (GQA)** | Jonathan Barbosa (Garantia da Qualidade de Processo — auditor independente da equipe do projeto) |
| **Gerente de Projeto** | Cezar Hiraki Velazquez |

---

## 1. Escopo da verificação

Verificação de aderência ao processo-padrão (PRO-GPC-001) e de existência/completude dos produtos de trabalho do projeto na fase de execução, conforme EST-GPC-001. A independência da função de GQA é assegurada pela atuação de Jonathan Barbosa (Garantia da Qualidade de Processo), fora da equipe de engenharia do projeto.

## 2. Verificação de aderência ao processo

| # | Item verificado | Resultado | Referência ao processo |
|---|---|---|---|
| 1 | Requisitos especificados e validados | ✅ Conforme | REQ-AASPCNJ01-001; ATA-AASPCNJ01-001 |
| 2 | Processo-padrão adaptado e registrado | ✅ Conforme | ADAP-AASPCNJ01-001; GUIA-GPC-001 |
| 3 | Design documentado e avaliado antes da construção | ✅ Conforme | PCP-AASPCNJ01-001 §5 |
| 4 | V&V planejada e executada; defeitos tratados | ✅ Conforme | VV / REL-VV-AASPCNJ01-001 |
| 5 | Decisões relevantes registradas (gatilhos GDE) | ✅ Conforme | GDE-AASPCNJ01-001 |
| 6 | Acompanhamento e mudanças formalizados | ✅ Conforme | RAC / CR-AASPCNJ01-001 |
| GCO-1 | ICs identificados e controlados com convenção de versão | ✅ Conforme | GCO-AASPCNJ01-001 §2–3 |
| GCO-2 | Baseline estabelecida no marco (publicação CNJ) | ✅ Conforme | GCO-AASPCNJ01-001 §4 (`v240`) |
| GCO-3 | Auditoria de configuração de encerramento | ⚠ Desvio | Pendente — projeto em execução (registrar no encerramento) |

## 3. Verificação de produtos de trabalho

| # | Produto de trabalho | Existe? | Completo? | Segue padrão? | Observação |
|---|---|---|---|---|---|
| 1 | TAP-AASPCNJ01-001 | Sim | Sim | Sim | — |
| 2 | PLA-AASPCNJ01-001 | Sim | Sim | Sim | Baseline de aprovação a registrar no encerramento |
| 3 | REQ-AASPCNJ01-001 | Sim | Sim | Sim | — |
| 4 | PCP-AASPCNJ01-001 | Sim | Sim | Sim | — |
| 5 | ITP / VV / REL-VV | Sim | Sim | Sim | — |
| 6 | GCO / GDE / MED / RASTR | Sim | Sim | Sim | — |

## 4. Achados

| # | Desvio | Severidade | Recomendação | Responsável | Status |
|---|---|---|---|---|---|
| 1 | Auditoria de configuração e baseline de aprovação do plano pendentes | Baixa | Registrar no encerramento (TAE e baseline final) | Cezar Hiraki Velazquez | Aberto |
| 2 | Verificação de GQA conduzida de forma consolidada na execução | Baixa | Realizar verificação independente nos marcos restantes (homologação/encerramento) | Jonathan Barbosa (GQA) | Aberto |

## 5. Resultado

| Campo | Valor |
|---|---|
| **Resultado geral** | Conforme com ressalvas |
| **% de conformidade** | 8 de 9 itens de processo conformes (88,9%); produtos de trabalho 100% existentes e aderentes ao padrão |
| **Achados abertos** | 2 (severidade baixa, relativos a marcos de encerramento) |
| **Oportunidades de melhoria** | Antecipar a verificação independente de GQA por marco, em vez de consolidada |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Registro de verificação de GQA (execução) consolidado a partir do Registro de Projeto AASP_CNJ v1.0 (08/06/2026). |
