# Registro de Medição — Milhas3

| Campo | Valor |
|---|---|
| **Documento** | MED-MILHASFACIL01-001 — Registro de Medição |
| **Versão** | 1.0 |
| **Data** | 16/11/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Milhas3 — Plataforma de Busca e Monitoramento de Milhas |
| **Cliente** | Hub de Milhas (Felipe) |
| **Processo MPS-SW** | MED — Medição |

---

## 1. Objetivo

Registrar as medições coletadas ao longo do projeto Milhas3, em alinhamento com o Plano de Medição Organizacional (PLA-MED-001).

## 2. Medições de projeto

### 2.1 Esforço e prazo

| Indicador | Planejado | Realizado |
|---|---|---|
| Duração total | 26 semanas (16/05 – 16/11/2025) | 26 semanas |
| Número de sprints executadas | 13 + Sprint 0 | 13 + Sprint 0 |
| Story points totais entregues | ~650 SP | [A CONFIRMAR] SP |
| Velocidade média por sprint | ~50 SP/sprint | [A CONFIRMAR] SP/sprint |
| Desvio de prazo | 0 dias | 0 dias |

### 2.2 Qualidade de código

| Indicador | Meta | Realizado |
|---|---|---|
| Cobertura de testes unitários — back-end (Service + Domain) | ≥ 70% | 74% |
| Defeitos críticos abertos ao encerramento | 0 | 0 |
| Defeitos totais abertos ao encerramento | ≤ 5 não críticos | [A CONFIRMAR] |
| Builds com pipeline quebrado (total de sprints) | ≤ 2 | [A CONFIRMAR] |
| PRs rejeitados por falha de code review | [A CONFIRMAR] | [A CONFIRMAR] |

### 2.3 Motor de rastreamento (indicadores específicos do produto)

| Indicador | Meta | Realizado |
|---|---|---|
| Taxa de sucesso de scraping — LATAM Pass | ≥ 90% | ≥ 92% |
| Taxa de sucesso de scraping — Smiles (GOL) | ≥ 90% | ≥ 91% |
| Taxa de sucesso de scraping — TudoAzul (Azul) | ≥ 90% | ≥ 93% |
| Taxa de sucesso de scraping — TAP Miles&Go | ≥ 90% | ≥ 90% |
| Taxa de sucesso de scraping — Iberia Plus | ≥ 90% | ≥ 92% |
| Tempo médio de busca consolidada (5 programas, p95) | ≤ 30s | [A CONFIRMAR] |
| Instâncias ChromeDriver simultâneas no pico | ≤ 5 | ≤ 5 |
| Incidentes de bloqueio permanente Akamai em produção | 0 | 0 |

### 2.4 Satisfação do cliente e processo

| Indicador | Resultado |
|---|---|
| Aceite formal no prazo contratado | Sim — 16/11/2025 |
| Não conformidades em GQA ao encerramento | 0 |
| Reclamações formais de cliente | 0 |
| Sprint Reviews realizadas com presença do cliente | 13 de 13 (todas as sprints) |

## 3. Análise

O projeto foi executado dentro dos parâmetros planejados em prazo e qualidade. O principal risco técnico (evolução do Akamai) foi gerenciado com sucesso: a taxa de sucesso do Selenium ficou acima de 90% em todos os cinco programas ao longo de toda a execução, superando a meta estabelecida. O único incidente foi o ajuste de seletores CSS no portal Smiles na Sprint 7 (estrutura HTML alterada pelo próprio site), resolvido em 1 dia sem impacto no prazo geral.

Os campos marcados como `[A CONFIRMAR]` serão preenchidos após compilação definitiva dos dados do Azure DevOps Boards no encerramento do projeto.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 16/11/2025 | Time de Melhoria Contínua | Documento final — projeto encerrado |
