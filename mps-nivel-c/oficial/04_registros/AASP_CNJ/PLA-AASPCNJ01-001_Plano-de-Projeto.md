# Plano de Projeto — AASP_CNJ · WorkerAndamentos

| Campo | Valor |
|---|---|
| **Documento** | PLA-AASPCNJ01-001 |
| **Projeto** | AASP_CNJ — WorkerAndamentos: Agente de Captura de Andamentos Processuais |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Identificação e objetivo do projeto

O projeto reconstrói o modelo de captura de andamentos processuais da AASP, que apresentava quatro problemas centrais: instabilidade dos crawlers, cobertura incompleta, custo operacional elevado (~R$ 16.500/mês na API Solucionário) e arquitetura monolítica sem observabilidade. A solução é entregue por dois eixos: um agente de captura nativo para o TJSP (EPROC/ESAJ) e a integração com a API DataJud/CNJ como fonte primária universal, com roteamento por processo e fallback estruturado. Ver REQ-AASPCNJ01-001 para os requisitos detalhados.

## 2. Escopo (GPR 1)

- **Incluído:** agente EPROC/ESAJ para o TJSP; integração DataJud/CNJ como fonte primária; roteamento por `CodigoFonteAPI`; fallback em três níveis; fila RabbitMQ unificada; webhook para a API AndamentosProcessuais; desligamento de APIs parceiras pós-captura; controle de segredo de justiça por instância; gestão centralizada de token Bearer CNJ.
- **Não incluído:** front-end de consulta do associado e índice Elasticsearch já existentes (a solução integra-se a eles); módulos da plataforma AASP fora do fluxo de captura.

Detalhamento em REQ-AASPCNJ01-001.

## 3. Adaptação do processo (GPR 2)

O processo-padrão (PRO-GPC-001) foi adaptado a este projeto conforme o GUIA-GPC-001. Registro completo em ADAP-AASPCNJ01-001. Principais decisões:

| Item de adaptação | Decisão | Justificativa |
|---|---|---|
| Design UX/UI | Não aplicável | Projeto de back-end/worker, sem interface de usuário |
| Nível de documentação | Padrão | Projeto de médio porte, integração crítica de operação |
| Estimativa e cadência | Execução por horas/cards (ClickUp); backlog modelado em sprints e story points (retroativo) para evidência e carga no Jira | Concilia a gestão real por atividades com a rastreabilidade ágil (ver GEST-AASPCNJ01) |
| Combinação de papéis | Dev Sênior acumulou execução de testes nas fases iniciais; GP acumulou responsável por GCO | Equipe enxuta; Analista de Testes dedicado a partir da Fase 5 |

## 4. Estimativas (GPR 3, 4)

O projeto foi estimado e acompanhado por **horas de esforço** registradas no sistema de gestão (ClickUp), somando as atividades dos projetos id 213 (EPROC/ESAJ) e id 256 (CNJ). Para a evidência de gestão ágil e a carga no Jira, o backlog foi **modelado retroativamente** em **20 histórias (155 SP)** derivadas dos requisitos (RF/RNF), distribuídas em **Discovery + 11 sprints** (velocity média ~14 SP/sprint) e conciliadas com as horas reais. Detalhamento em GEST-AASPCNJ01-001 (abas Backlog, Tarefas e Acompanhamento) e em ADAP-AASPCNJ01-001.

**Esforço estimado × realizado por fase**

| Fase | Esforço estimado (h) | Esforço realizado (h) |
|---|---|---|
| Fase 1 — Análise e Arquitetura | 60 | 80 |
| Fase 2 — Desenvolvimento EPROC/ESAJ | 120 | 124 |
| Fase 3 — Estabilização EPROC/ESAJ | 80 | 93 |
| Fase 4 — Desenvolvimento CNJ | 200 | 195 |
| Fase 5 — Testes e Validação | 80 | 109 |
| Fase 6 — Implantação e Complementos | 46 | Em apuração |
| **Total** | **586** | **~601 (parcial)** |

## 5. Cronograma, marcos e orçamento (GPR 5)

**Marcos**

| Marco | Data prevista | Situação |
|---|---|---|
| Abertura (Fase 1) | 01/10/2025 | Concluída |
| Fim EPROC/ESAJ (Fases 2–3) | Abr/2026 | Concluída |
| Fim desenvolvimento CNJ (Fase 4) | Mai/2026 | Concluída |
| Testes e validação (Fase 5) | Jun/2026 | Concluída |
| Implantação e complementos (Fase 6) | Jun/2026 | Em andamento |
| Encerramento | 30/06/2026 | Previsto |

**Estrutura de fases**

| Fase | Período | Status |
|---|---|---|
| Fase 1 — Análise e Arquitetura | Out/2025 – Jan/2026 | Concluída |
| Fase 2 — Desenvolvimento EPROC/ESAJ | Dez/2025 – Mar/2026 | Concluída |
| Fase 3 — Estabilização EPROC/ESAJ | Mar/2026 – Abr/2026 | Concluída |
| Fase 4 — Desenvolvimento CNJ | Abr/2026 – Mai/2026 | Concluída |
| Fase 5 — Testes e Validação | Mai/2026 – Jun/2026 | Concluída |
| Fase 6 — Implantação e Complementos | Jun/2026 | Em andamento |

**Orçamento total**

| Item | Valor |
|---|---|
| Horas totais estimadas | 586 h |
| Horas realizadas (parcial) | ~601 h (Fase 6 em apuração) |
| Período | 01/10/2025 a 30/06/2026 (previsto) |

## 6. Recursos (GPR 6, 7)

- **Equipe:** Abraão Oliveira (Gerente de Projeto / Tech Lead, todas as fases); Cézar (Arquiteto de Software, Fases 1–3); Raony (Desenvolvedor Sênior, Fases 2–6); Levi (Desenvolvedor de Suporte, Fases 4–5); Jonatan (Analista de Testes, Fase 5); David (Infraestrutura/DevOps, Fases 1 e 6).
- **Ambiente e ferramentas:** Azure DevOps (código e CI/CD), AWS (hospedagem dos workers e APIs internas), RabbitMQ, Elasticsearch, ClickUp (gestão de atividades). Ver GCO-AASPCNJ01-001.

## 7. Partes interessadas e comunicação (GPR 9)

| Parte interessada | Interesse | Comunicação |
|---|---|---|
| Carlos Alves (Representante do Cliente — AASP) | Validação, homologação e aceite | Reuniões de alinhamento e devolutivas de resultado |
| Patrocinador interno (Timeware) | Resultado financeiro e operacional | Acompanhamento por marco |
| Time de desenvolvimento | Execução e decisões técnicas | Reuniões de alinhamento periódicas (ver ATA-AASPCNJ01-001) |

## 8. Transição e suporte pós-go-live (GPR 8, GPR 16)

### 8.1 Estratégia de transição para produção

| Item | Descrição |
|---|---|
| Fluxo de deploy | Homologação por amostragem → montagem de pacote GMUD → agendamento com Infraestrutura → produção |
| Responsável pela execução | Equipe de Infraestrutura / DevOps |
| Aprovador do go-live | Gerente de Projeto |
| Processo de mudança | GMUD (Gerência de Mudança) — montagem de pacote, validação e agendamento |
| Plano de rollback | Reversão para a versão anterior do worker; APIs parceiras mantidas como fallback configurável durante a migração |

### 8.2 Critérios de prontidão para go-live

| Critério | Obrigatório? | Verificado por |
|---|---|---|
| Fluxo de captura validado (sucesso, fallback e erro parcial) | Sim | Raony / Jonatan |
| Persistência de movimentações validada | Sim | Jonatan |
| Baseline de configuração registrada (tag de versão) | Sim | David (DevOps) / Abraão Oliveira (GCO) |
| Pacote GMUD montado e agendado | Sim | Abraão Oliveira / David |

### 8.3 Suporte e monitoramento pós-go-live

| Item | Descrição |
|---|---|
| Monitoramento | Monitoramento ativo da fila RabbitMQ e dos logs de captura por instância |
| Responsável | Raony + Abraão Oliveira |
| O que monitorar | Travamentos de fila (meta: zero travamentos manuais/mês); erros por instância nas tabelas de controle |

## 9. Riscos (GPR 10)

Exposição = Probabilidade × Impacto (escala 1–3 por dimensão), conforme EST-GPC-002.

| Risco | Prob. | Impacto | Exposição | Resposta |
|---|---|---|---|---|
| Indisponibilidade/alteração na API DataJud/CNJ | 1 | 3 | 3 | Mitigar — manter APIs parceiras como fallback configurável por `CodigoFonteAPI` |
| Travamento da fila RabbitMQ (ocorreu) | 3 | 3 | 9 | Mitigar — logging aprimorado, tratamento de exceção na publicação e monitoramento ativo |
| Processos em segredo de justiça sem cobertura | 3 | 2 | 6 | Mitigar — controle por instância e fallback para EPROC/ESAJ ou parceiras com credencial |
| Variação de layout dos portais EPROC/ESAJ | 2 | 2 | 4 | Mitigar — CNJ como fonte primária reduz exposição; EPROC como fallback |
| Custo de duplo pagamento durante migração | 2 | 2 | 4 | Mitigar — desligamento automático nas parceiras após 1ª captura via CNJ |
| Erros parciais por instância não tratados (ocorreu) | 2 | 2 | 4 | Mitigar — controle granular de status por instância |

## 10. Viabilidade (GPR 11)

O projeto é viável: a economia projetada (~R$ 180 mil/ano) supera amplamente o esforço estimado (586 h), e a arquitetura de fontes com fallback reduz o risco de indisponibilidade. A principal restrição (segredo de justiça sem cobertura no CNJ) é endereçada pelo fallback por instância.

## 11. Aprovação do Plano (GPR 13)

| Envolvido | Papel | Aceite | Data | Ref. da ata |
|---|---|---|---|---|
| Carlos Alves | AASP | — | — | A registrar no encerramento (Onda 3) |

> A baseline do projeto e o aceite final serão registrados no encerramento (TAE-AASPCNJ01-001), conforme o estágio atual do projeto (em execução).

---

## Controle de atualizações do plano

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Plano consolidado a partir do Registro de Projeto AASP_CNJ v1.0 (08/06/2026). |
