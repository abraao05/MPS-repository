# Registro de Medição — Cadastro de Clientes · Rede D1000

| Campo | Valor |
|---|---|
| **Documento** | MED-PROFARMA01-001 |
| **Projeto** | Cadastro de Clientes — Rede D1000 |
| **Cliente** | Profarma S.A. / Rede D1000 |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | MED (evidência de projeto) |

---

## 1. Objetivo

Registrar as medidas coletadas ao longo do projeto Cadastro de Clientes — Rede D1000, conforme o PLA-MED-001 (Plano de Medição Organizacional), de modo a apoiar a análise de aderência ao prazo, qualidade das entregas e capacidade de processo. As medidas documentadas neste registro abrangem o ciclo completo do projeto: do kickoff em março/2025 ao encerramento formal em janeiro/2026.

---

## 2. Medidas de prazo e progresso

### 2.1 Marcos do projeto — planejado vs. realizado

| Fase / Marco | Período planejado | Período realizado | Variação | Observação |
|---|---|---|---|---|
| Kickoff / início do projeto | 17/03/2025 | 28/04/2025 | +42 dias | Atraso na liberação de acessos ao ambiente Azure da Rede D1000 |
| Fase 1 — Design e API core (Sprints 1–3) | Jun/2025 | Jun/2025 | Dentro do prazo | Arquitetura, modelo de dados, endpoints core entregues |
| Fase 2 — Integrações satélites (Sprints 4–7) | Jul/2025 | Ago/2025 | +1 sprint | BlueSoft e CloseUp adicionados ao escopo (CR-04 e CR-05) |
| Fase 3 — Carga inicial e worker LGPD (Sprints 8–10) | Ago/2025 | Set/2025 | Dentro do prazo | Saneamento e carga dos 7M CPFs concluídos |
| Fase 4 — Integração Propz CRM (Sprints 11–13) | Set/2025 | Out/2025 | +1 sprint | Propz incluído via CR-07 (ago/2025); escopo e esforço ampliados |
| Fase 5 — Homologação e piloto (Sprints 14–17) | Set–Out/2025 | Out/2025–Jan/2026 | +3 sprints | Ambiente AKS disponibilizado 2,5 meses após o planejado; GMUD adicionou ciclos extras |
| Encerramento formal | Set/2025 (original) → Jan/2026 (revisado após CRs) | 29/01/2026 | Dentro do prazo revisado | Marco revisado formalmente após absorção dos 12 CRs |

### 2.2 Sprints realizados vs. planejados

| Métrica | Planejado | Realizado |
|---|---|---|
| Total de sprints | ~14 sprints | 19 sprints |
| Duração média por sprint | ~2 semanas | ~2 semanas |
| Sprints adicionais (expansão de escopo) | — | +5 sprints (CRs e bloqueios de ambiente) |

---

## 3. Medidas de qualidade de produto

### 3.1 Testes unitários e cobertura

| Medida | Meta | Realizado | Status |
|---|---|---|---|
| Quantidade de testes unitários | ≥ 273 | 273 | Atingido (100%) |
| Cobertura de código (Domain + Application) | ≥ 80% | 84% | Atingido |

### 3.2 Performance e escalabilidade

| Medida | Meta / SLA | Realizado | Status |
|---|---|---|---|
| Latência p95 — GET /clientes/{cpf} | ≤ 200ms | 142ms | Atingido (29% abaixo do limite) |
| Latência p95 — endpoint Call Center | ≤ 500ms | Dentro do SLA | Atingido |
| Spike test 1.000 req/s — comportamento sob carga extrema | Degradação graciosa, sem crash | Degradação graciosa confirmada, sem crash | Atingido |

### 3.3 Defeitos por ciclo

| Ciclo | Severidade | Quantidade | Resolução |
|---|---|---|---|
| Piloto (loja 9) | S1 (crítico) | 0 | — |
| Homologação | S1 (crítico) | 2 | Resolvidos em < 24h |
| Homologação | S2 (alto) | 5 | Resolvidos em < 3 dias úteis |
| Homologação | S3 (médio) | 7 | Resolvidos na sprint seguinte |
| **Total homologação** | — | **14** | 100% resolvidos antes do aceite |
| Produção (piloto loja 9) | S1 (crítico) | 0 | — |

---

## 4. Medidas de processo

### 4.1 Entregas de escopo

| Medida | Planejado | Realizado | Status |
|---|---|---|---|
| Endpoints de API entregues | 16 | 16 | Atingido (100%) |
| Integrações entregues | 5 (ITEC, VTEX, Call Center, PBM, Propz) | 7 (+ BlueSoft e CloseUp via CRs) | Superado — escopo expandido via CRs formais |
| Incidentes S1 no piloto de produção | 0 | 0 | Atingido |

### 4.2 Gestão de mudanças e desvio de prazo

| Medida | Valor |
|---|---|
| Change Requests formais absorvidos | 12 |
| Desvio de prazo total vs. plano original | +4 meses |
| Justificativa do desvio | 12 CRs formais aprovados que ampliaram o escopo de 5 para 7 integrações e acrescentaram o worker LGPD e o worker Propz; bloqueios de infraestrutura (Azure AKS, GMUD) |
| SPI — Schedule Performance Index (considerando escopo expandido) | 0,91 |
| Avaliação do SPI | Desvio dentro do aceitável dado o aumento de escopo formal; não caracteriza atraso de execução |

---

## 5. Análise de variâncias e causas-raiz

### 5.1 Variâncias identificadas

| Variância | Magnitude | Causa-raiz |
|---|---|---|
| Início do projeto atrasado em 42 dias | Alta | Liberação de acessos ao ambiente Azure da Rede D1000 dependeu de aprovação de segurança interna; fora do controle da Timeware |
| Fase 2 com +1 sprint | Média | BlueSoft e CloseUp incorporados ao escopo via CR-04 e CR-05; aumento de escopo não previsto na baseline original |
| Fase 4 com +1 sprint | Média | Integração Propz CRM adicionada via CR-07; protocolo de integração com o Propz exigiu alinhamento técnico adicional |
| Fase 5 (Homologação) com +3 sprints | Alta | Duas causas independentes: (a) ambiente AKS disponibilizado 2,5 meses após o planejado, impedindo o início da homologação no AKS; (b) GMUD (Gestão de Mudanças) da Rede D1000 adicionou de 2 a 5 dias úteis por ciclo de release nas fases finais |
| Saneamento da base legada acima do estimado | Média | Base de 7M CPFs com grau de duplicidade e inconsistência superior ao levantado inicialmente; saneamento levou 3 semanas além do estimado |

### 5.2 Avaliação consolidada

O desvio acumulado de 4 meses em relação ao plano original é explicado integralmente por dois fatores formalmente reconhecidos e aprovados pelo cliente:

1. **Aumento de escopo via CRs formais (12 CRs):** a inclusão de BlueSoft, CloseUp, worker LGPD e Propz CRM ampliou o escopo de integração de 5 para 7 sistemas satélites, além de acrescentar dois workers novos. Nenhum dos CRs foi rejeitado pelo cliente — todos foram absorvidos com ajuste de prazo acordado.

2. **Bloqueios de infraestrutura externos à Timeware:** o ambiente AKS foi disponibilizado 2,5 meses após o planejado pela equipe de infraestrutura da Rede D1000, e o processo de GMUD adicionou latência nos ciclos finais de release.

Não foram identificados desvios de produtividade ou qualidade de execução que expliquem os atrasos. A equipe entregou 16/16 endpoints planejados (100%) e 7 integrações (acima das 5 originais), com 0 incidentes S1 no piloto e 142ms de latência p95 no endpoint principal (29% abaixo do SLA).

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Time de Melhoria Contínua | Versão inicial — registro de medição consolidado do projeto Cadastro de Clientes — Rede D1000 |
