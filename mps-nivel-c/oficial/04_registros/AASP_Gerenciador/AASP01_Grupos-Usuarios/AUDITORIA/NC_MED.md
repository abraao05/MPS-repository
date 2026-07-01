# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Registro de Medição
**Código:** MED-AASP01-001
**Versão auditada:** 1.2
**Data do documento:** 24/06/2026
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 0 | 0 |
| Conteúdo (CNT) | 1 | 2 | 0 | 0 |
| Datas (DT) | 1 | 0 | 0 | 0 |
| Papéis (PAP) | 0 | 0 | 0 | 0 |
| Coerência (CON) | 0 | 1 | 0 | 0 |
| MPS.BR (MPS) | 0 | 1 | 0 | 0 |
| **TOTAL** | **2** | **4** | **0** | **0** |

**Veredicto:** NÃO-CONFORME CRÍTICO

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-MED-01 — Sprint 2 sem dados de medição coletados (documento de 24/06 sem atualização)
**Severidade:** 🔴 Grave
**RAP impactado:** MED RAP — medições coletadas conforme planejado
**Localização:** Seção 3.2, 4.1, 4.2, 4.3 e 6 — todas as colunas Sprint 2
**Problema:** O documento v1.2 de 24/06/2026 — data em que a Sprint 2 estava em seus últimos dias (encerramento 20/06) — não tem nenhum dado de Sprint 2 coletado. O encerramento previsto da Sprint 2 era 20/06/2026 e o documento foi atualizado em 24/06/2026, 4 dias depois. A ausência de dados da Sprint 2 em um documento datado de 24/06/2026 é inexplicável: se a Sprint 2 encerrou em 20/06, os dados deveriam estar disponíveis para coleta em 24/06. A seção 7 ("próximo ponto de medição: 20/06/2026") não foi executada.
**Evidência:** > "Sprint 2 | 28 | Em andamento | — | — | —"; seção 7 intacta com data passada.
**Referência normativa:** MED RAP — medições coletadas e registradas nos marcos planejados.
**Ação corretiva:** Coletar e registrar urgentemente os dados da Sprint 2: SP realizado vs. planejado, cobertura de testes, achados de code review, taxa de aprovação UAT, tempo de resposta em homologação.

---

### NC-MED-02 — Medição de performance feita via Swagger UI manual em ambiente local — metodologia inadequada
**Severidade:** 🔴 Grave
**RAP impactado:** MED RAP — medições com metodologia documentada e repetível
**Localização:** Seção 5 — Medidas de Performance e Confiabilidade
**Problema:** As medições de performance (≤ 280 ms, ≤ 310 ms, ≤ 260 ms) foram realizadas via "Swagger UI em ambiente dev local durante a Sprint 1". Swagger UI não é ferramenta de medição de performance — exibe o tempo de resposta HTTP mas sem controle de carga, percentil real, ou eliminação de overhead de interface. "Ambiente dev local" com SQL Server Express e sem carga concorrente não representa condições normais de produção. A RNF-01 exige "95% das requisições ≤ 500 ms em condições normais de carga" — Swagger UI em local não mede condições normais de carga.
**Evidência:** > "Medições realizadas via Swagger UI em ambiente dev local durante a Sprint 1."
**Referência normativa:** MED — metodologia de medição deve ser adequada à métrica. RNF-01 especifica condições de carga.
**Ação corretiva:** (a) Qualificar as medições existentes como "indicativas em dev — validação definitiva pendente em homologação"; (b) na Sprint 3, realizar medição formal em ambiente de homologação AASP com ferramenta adequada (ex.: k6, JMeter, ou Postman com iterações) e arquivar relatório de performance.

---

### NC-MED-03 — M3 com mesma inconsistência do RAC (3 achados vs. 5)
**Severidade:** 🟡 Moderada
**RAP impactado:** MED — consistência entre documentos
**Localização:** Seção 6 — Indicadores M3
**Problema:** Mesma inconsistência identificada no RAC: M3 = 0,088 (3 achados P2/34 SP), mas o REV registra 5 achados total.
**Evidência:** > "M3 | Índice de defeitos por SP | 0,088 def/SP (3 achados P2 / 34 SP)"
**Referência normativa:** MED — métricas consistentes com as fontes de dados.
**Ação corretiva:** Corrigir para 5 achados/34 SP = 0,147, ou definir explicitamente que M3 conta apenas achados P2.

---

### NC-MED-04 — "Disponibilidade ambiente dev > 99%" sem metodologia de medição
**Severidade:** 🟡 Moderada
**RAP impactado:** MED — medições com metodologia definida
**Localização:** Seção 5 — Disponibilidade ambiente dev
**Problema:** A métrica "Disponibilidade ambiente dev > 99% no período da Sprint 1" é declarada mas sem metodologia de medição definida. Como a disponibilidade foi medida? Monitoramento automático? Contagem de incidentes relatados? Autodeclaração do desenvolvedor? Esta métrica não tem evidência rastreável.
**Evidência:** > "Disponibilidade ambiente dev | > 99% no período da Sprint 1 | >= 99% | Dev (local) | Meta atingida"
**Referência normativa:** MED — metodologia de coleta deve ser documentada.
**Ação corretiva:** Ou remover esta métrica (não é mensurável de forma rastreável em ambiente dev local) ou definir metodologia: "Nenhum incidente de indisponibilidade reportado pela equipe durante a Sprint 1 = disponibilidade estimada > 99%".

---

### NC-MED-05 — Plano de Medição Organizacional (PLA-MED-001) referenciado mas não disponível no pacote
**Severidade:** 🟡 Moderada
**RAP impactado:** MED — referências a documentos disponíveis
**Localização:** Seção 2 — Plano de Medição Aplicado
**Problema:** O documento referencia "PLA-MED-001 — Plano de Medição Organizacional Timeware" mas este documento não está disponível no pacote documental do projeto AASP01. Durante uma avaliação MPS.BR, o avaliador precisaria acessar o PLA-MED-001 para verificar se as medidas coletadas são consistentes com o plano organizacional.
**Evidência:** > "Plano de referência | PLA-MED-001 — Plano de Medição Organizacional Timeware"
**Referência normativa:** MED — evidências de processo devem referenciar documentos acessíveis ao avaliador.
**Ação corretiva:** Incluir referência ao local onde o PLA-MED-001 pode ser encontrado (repositório MPS Timeware), ou incluir um extrato das medidas relevantes no próprio MED-AASP01-001.
