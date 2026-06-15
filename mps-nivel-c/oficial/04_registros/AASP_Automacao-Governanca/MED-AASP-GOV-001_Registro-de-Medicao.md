# Registro de Medição — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | MED-AASP-GOV-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 15/06/2026 |
| **Gerente de Projeto** | Cezar Hiraki Velazquez |
| **Processo MPS-SW** | MED (evidência de projeto) · Catálogo organizacional: PLA-MED-001 |

---

## 1. Objetivo

Registrar as medidas apuradas ao encerramento do projeto, conforme o PLA-MED-001, para apoiar a análise de prazo, esforço, qualidade e valor entregue. Conforme ADAP-AASP-GOV-001, os indicadores foram apurados sobre o ciclo completo (projeto sem sprints formais).

## 2. Indicadores do projeto

| Indicador | Valor real | Meta organizacional | Status |
|---|---|---|---|
| Eliminação de trabalho manual de migração | 100% dos cards migrados automaticamente | 100% sem intervenção manual | ✅ Atingida |
| Idempotência — zero duplicatas | 0 duplicatas em todos os ciclos de teste | 0 duplicatas | ✅ Atingida |
| Fidelidade dos dados migrados | 100% dos campos verificados com correspondência | 100% conformidade | ✅ Atingida |
| Taxa de contenção de defeitos | 100% (5 bugs corrigidos antes da entrega) | ≥ 95% | ✅ Atingida |
| Defeitos escapados para produção | 0 | 0 | ✅ Atingida |
| Retrabalho (% do esforço total) | 0% | ≤ 5% | ✅ Atingida |
| Aderência ao prazo de entrega | Entregue em 02/06/2026 | Entrega até 02/06/2026 | ✅ Atingida |
| Desvio de esforço | +9% (+20 h sobre estimativa) | ≤ 10% | ✅ Atingida |
| NCs de GQA abertas ao encerramento | 0 | 0 | ✅ Atingida |

## 3. Esforço realizado por fase

| Fase | Esforço estimado (h) | Esforço realizado (h) | Principal responsável |
|---|---|---|---|
| Fase 1 — Arquitetura | 16 | 16 | Gerente de Projeto / Desenvolvedor Sênior |
| Fase 2 — Mapeamento e Autenticação | 40 | 44 | Desenvolvedor Sênior / Desenvolvedor |
| Fase 3 — Desenvolvimento dos Serviços | 120 | 128 | Desenvolvedor Sênior / Desenvolvedor |
| Fase 4 — Homologação e Correções | 40 | 48 | Desenvolvedor Sênior / Desenvolvedor |
| **Total** | **216** | **236** | |

## 4. Análise de variâncias

| Variância | Magnitude | Causa-raiz |
|---|---|---|
| Esforço realizado acima do estimado nas Fases 2, 3 e 4 | +20 h (+9%) | Ajustes na camada de transformação (HTML/ADF, status) e ciclo de correção de defeitos na homologação |

O desvio de esforço de +9% manteve-se dentro da meta organizacional (≤ 10%). Não houve retrabalho fora do ciclo de correção de defeitos previsto na homologação, e nenhum defeito escapou para produção.

## 5. Comunicação dos resultados

Conforme PLA-MED-001, os resultados foram comunicados na homologação e consolidados no encerramento do projeto (ver TAE-AASP-GOV-001). Os indicadores de qualidade derivam da execução de testes registrada em REL-VV-AASP-GOV-001 e da auditoria GQA-AASP-GOV-001.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Registro de medição consolidado a partir do Registro de Projeto AASP_Automacao-Governanca v2.0 (08/06/2026). |
