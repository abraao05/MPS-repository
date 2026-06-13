# Plano de Projeto — Cadastro de Clientes · Rede D1000

| Campo | Valor |
|---|---|
| **Documento** | PLA-PROFARMA01-001 |
| **Projeto** | Cadastro de Clientes — Rede D1000 |
| **Cliente** | Profarma S.A. / Rede D1000 |
| **Contrato** | Squad D1000 Loja — alocação de 3 Dev Pleno |
| **Versão** | 1.3 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Identificação e objetivo do projeto

Desenvolver o novo sistema de Cadastro de Clientes da Rede D1000, unificando a base legada do ITEC em uma solução cloud-native na Microsoft Azure. O sistema adota CPF como chave primária, elimina duplicidades históricas entre bandeiras, expõe API RESTful para todos os canais (PDV, Balcão, Call Center, OMNI/VTEX) e integra-se ao ecossistema de parceiros da Rede.

Detalhamento de escopo e requisitos: ver `REQ-PROFARMA01-001_Documento-de-Requisitos.md`.

## 2. Escopo (GPR 1)

- **Incluído:** RF-01 a RF-12 conforme `REQ-PROFARMA01-001`. Em síntese: API de cadastro/consulta/atualização/inativação, integração ITEC (trigger/outbox), integração VTEX, Call Center, PBM/Interplayers, BlueSoft, CloseUp, Propz CRM, carga inicial saneada, worker de expurgo, piloto loja 9.
- **Não incluído:** Modernização dos aplicativos D1000 Express e Connect D1000; desenvolvimento no ITEC legado; sustentação pós-piloto.

## 3. Adaptação do processo (GPR 2)

Detalhamento completo em `ADAP-PROFARMA01-001_Registro-de-Adaptacao.md`. Resumo:

| Item de adaptação | Decisão | Justificativa |
|---|---|---|
| Cadência de entrega | Sprints de ~2 semanas com dailys às 11h30 (Teams) | Equipe distribuída SP/RJ, alto volume de integração |
| Controle de versão | Azure DevOps (repositórios da Profarma) | Repositórios do cliente: loja-balcao-frontend, loja-backend |
| Gestão de backlog | Azure DevOps Boards + Jira (a partir de sprint 4) | Jira introduzido para maior visibilidade ao cliente |
| Rastreabilidade de defeitos | Planilha de tickets (Gustavo Mathias) + Azure DevOps | Histórico completo exportado em 07/11/2025 |
| Viagens presenciais | Previstas quando ambiente travado ou pontos críticos | Custo médio R$ 5.000 por deslocamento (4 pessoas) |

## 4. Estimativas e orçamento de horas (GPR 3, 4)

- **Tamanho estimado:** 573 story points (total realizado; ver tabela §5.2)
- **Duração total:** 19 sprints / ~10 meses (março/2025 a janeiro/2026)
- **Modelo de contratação:** alocação mensalizada (squad dedicado)

**Distribuição por entregável:**

| Módulo / entregável | Sprints | Observações |
|---|---|---|
| Design de arquitetura e modelo de dados | 2 | Sprints 1–2 |
| API core (endpoints cadastro/consulta) | 3 | Sprints 2–4; 16 endpoints, 273 testes unitários |
| Integração ITEC (trigger/outbox) | 2 | Sprints 4–5 |
| Integração VTEX e Call Center | 2 | Sprints 5–6 |
| Carga inicial + worker de expurgo | 2 | Sprints 7–8 |
| Integração Propz CRM | 2 | Sprints 13–14 (nov/2025) |
| Testes de homologação e bug fixes | 5+ | Sprints 9–15 (set–jan) |
| Configuração de ambiente produtivo (Azure) | 1 | Sprint 14 |

**Orçamento de horas por papel:**

*Referência: 168 h/mês disponíveis por pessoa → ~140 h/mês efetivas (~70 h/sprint) após dedução de cerimônias e reuniões (~15%). Dedicação parcial proporcional.*

| Papel | Pessoas | Dedicação | h efetivas/sprint | Sprints | **h estimadas** |
|---|---|---|---|---|---|
| Gerente de Projeto | 1 | 30% | 21 h | 19 | 399 h |
| Tech Lead | 1 | 50% | 35 h | 19 | 665 h |
| Dev Principal / Arquiteto | 1 | 100% | 70 h | 11 | 770 h |
| Dev Backend (Gustavo, Renan) | 2 | 100% | 70 h | 19 | 2.660 h |
| Dev Backend (Cézar — a partir Sprint 8) | 1 | 100% | 70 h | 12 | 840 h |
| Dev Backend (João — a partir Sprint 13, 50%) | 1 | 50% | 35 h | 7 | 245 h |
| DevOps (Sprint 14) | 1 | 100% | 70 h | 1 | 70 h |
| QA / Automação (Sprints 15–19, 40%) | 1 | 40% | 28 h | 5 | 140 h |
| **Total** | | | | | **5.789 h** |

## 5. Cronograma e marcos (GPR 5)

### 5.1 Linha do tempo consolidada

| Fase | Período | Marcos e eventos-chave |
|---|---|---|
| **Fase 1 — Discovery e arquitetura** | 17/03/2025 – 27/04/2025 | Reuniões de alinhamento técnico; escolha de PostgreSQL, arquitetura cloud-native Azure, Clean Architecture .NET 8 |
| **Fase 2 — Desenvolvimento (Sprints 1–6)** | 28/04/2025 – 04/07/2025 | Dailys estruturadas; model de dados (DER); 16 endpoints; testes unitários; integração ITEC |
| **Fase 3 — Consolidação e apresentação** | 07/07/2025 – 01/08/2025 | Apresentação formal do plano ao Diretor (17/07); alinhamento de integridade de dados (23/07) |
| **Fase 4 — Preparação para testes** | 04/08/2025 – 26/09/2025 | Sprints 7–9; configuração de ambiente de homologação; carga inicial; worker de expurgo |
| **Fase 5 — Testes e correções** | 29/09/2025 – 30/11/2025 | Testes homologação; status reports semanais; integração Propz; bug fixes intensivos |
| **Fase 6 — Reta final** | 01/12/2025 – 29/01/2026 | Propz CRM disponível para testes (04/12); GMUD 2624117 (21/01); liberação formal para testes (22/01); correções finais (27–29/01) |

### 5.2 Sprints de desenvolvimento

| Sprint | Período (aprox.) | SP Planejado | Principais entregas |
|---|---|---|---|
| Sprint 1 | 28/04–09/05/2025 | 28 | Arquitetura definida; Docker; DER v1; ambiente Azure inicial; dailys iniciadas |
| Sprint 2 | 12/05–23/05/2025 | 30 | DER v2; fluxo ITEC (trigger/outbox); endpoints iniciais; pipelines DevOps |
| Sprint 3 | 26/05–06/06/2025 | 30 | Regras de sanitização da base; testes automatizados (início); acesso JIRA liberado |
| Sprint 4 | 09/06–20/06/2025 | 32 | Arquitetura API Gateway finalizada; VTEX no fluxo de cadastro; PostgreSQL sequencial único |
| Sprint 5 | 23/06–04/07/2025 | 30 | Preparação apresentação Falcão; desenhos UML de arquitetura; checklist técnico pré-piloto |
| Sprint 6 | 07/07–18/07/2025 | 32 | Apresentação formal do plano (17/07); 16 endpoints entregues; 273 testes unitários; piloto loja 9 definido |
| Sprint 7 | 21/07–01/08/2025 | 32 | Alinhamento integridade dados (CPF como PK); modelo push; sanitização base legada |
| Sprint 8 | 04/08–15/08/2025 | 32 | Configuração Prometheus/Grafana (observabilidade); CloudTree loja-backend; documentação endpoints |
| Sprint 9 | 18/08–29/08/2025 | 28 | Ambiente homologação configurado; início carga de clientes |
| Sprint 10 | 01/09–12/09/2025 | 30 | Carga parcial (1 M de 20 M registros); worker de expurgo aprovado |
| Sprint 11 | 15/09–26/09/2025 | 28 | Preparação dailys de teste; Datadog configurado; mapping cenários de teste |
| Sprint 12 | 29/09–10/10/2025 | 28 | Início testes homologação (<5% em 29/09 — aceleração exigida); status reports iniciados |
| Sprint 13 | 13/10–24/10/2025 | 28 | Status reports 08/10, 14/10, 17/10; bloqueio acesso banco QA (14–21/10); retomada após desbloqueio |
| Sprint 14 | 27/10–07/11/2025 | 28 | Plano de piloto (04–05/11); proposta de infra produtiva Azure (03/11); bug id_cliente sequencial (06/11) |
| Sprint 15 | 10/11–21/11/2025 | 32 | Consolidação histórico tickets; daily 10/11 registrada; integração Propz CRM iniciada |
| Sprint 16 | 24/11–05/12/2025 | 35 | Propz CRM concluído e disponível para testes (04/12); documentação Propz enviada |
| Sprint 17 | 08/12–19/12/2025 | 32 | Versão 25.12.1.1 do loja-backend; ajuste campos fidelidade/opt-in/opt-out |
| Sprint 18 | 06/01–17/01/2026 | 28 | Daily Teams criada por Armando (06/01); status conflituoso com cliente (09/01); ajuste loja-backend URL HttpClient |
| Sprint 19 | 20/01–29/01/2026 | 30 | GMUD 2624117 (21/01); PR 10684 loja-backend; liberação para testes (22/01); versão 26.1.1.1; deploy (26/01); PRs finais (27–29/01) |
| **Total** | | **573** | |

### 5.3 Eventos e comunicações formais relevantes

| Data | Evento | Participantes-chave |
|---|---|---|
| 17/03/2025 | Reunião "Evolução do desenho e material" (Fireflies) | Tiago, Humberto, Armando, Diego, Marcelo, Alexandre |
| 28/04/2025 | Primeira daily formal do projeto | Equipe completa |
| 25/06/2025 | Alinhamento urgente pré-apresentação Falcão | Abraão, Armando, Erick, Tiago, Helena |
| 17/07/2025 | Apresentação formal do plano ao Diretor | Marcus Falcão, Helena, Humberto, Fagner, Rafael, Diego, Tiago, Abraão, Marcus Ribeiro, Armando |
| 23/07/2025 | Alinhamento técnico 2,5 h (integridade de dados) | Humberto, Diego, Marcus Ribeiro, Tiago, Abraão, Rafael, Ethierre, Helena, Fagner, Armando |
| 29/09/2025 | Daily com diagnóstico de atraso crítico (<5% testes) | Armando, Ethierre, Tiago, Marcelo, Erick, Abraão, Helena, Pedro, Humberto |
| 03/11/2025 | Proposta de infraestrutura produtiva Azure (David Buena) | Time Timeware, Fabio Ruiz, Diego Lacerda, Armando, Marcelo |
| 04–05/11/2025 | Reuniões de planejamento de piloto | Armando, Pedro, Helena, Fagner, Rafael, Tiago, Abraão, Renan, Humberto |
| 04/12/2025 | Integração Propz CRM concluída — liberação para testes | Abraão, Helena, Julielle, Armando, Fagner, Raony, Renan, Rafael |
| 09/01/2026 | E-mail de status — divergência de percepção com cliente | Abraão → Armando (discordância formal registrada) |
| 22/01/2026 | Liberação formal para testes — responsabilidade Timeware concluída | Abraão → Armando, Pedro, Helena |
| 23/01/2026 | Confirmação de deploy pelo cliente; e-mail de cronograma e impactos | Pedro → equipe; Abraão → Pedro |
| 26/01/2026 | Versão disponibilizada no ambiente (Fagner) | Fagner → Pedro, Abraão, Armando |
| 29/01/2026 | Últimos PRs com correções de testes (Renan) | Renan → Cézar, equipe completa |

## 6. Recursos (GPR 6, 7)

**Equipe Timeware:**

| Papel | Responsável | Dedicação |
|---|---|---|
| Gerente de Projeto / Account Manager | Abraão Oliveira | Parcial (gestão, comunicação, viagens) |
| Tech Lead | Tiago Nascimento | Parcial (decisões técnicas, PRs críticos) |
| Dev Principal / Arquiteto da solução | Erick Coelho | Integral (sprints 1–11) |
| Dev Backend | Gustavo Mathias | Integral (sprints 1–19) |
| Dev Backend | Renan Kiyoshi | Integral (sprints 1–19) |
| Dev Backend | Cézar Hiraki | Integral (sprints 8–19) |
| Dev Backend | João Cruz | Parcial (sprints 13–19) |
| Infra / DevOps | David Buena | Parcial (sprint 14 — proposta infra) |
| QA / Automação | Lucas Batista | Parcial (sprints 15–19) |
| GQA | COO (Operações) | Parcial (auditorias de processo) |

**Equipe Rede D1000/Profarma:**

| Papel | Responsável | Envolvimento |
|---|---|---|
| Patrocinador | Pedro Alves da Costa Junior | Decisões de go/no-go, aprovações finais |
| Diretor de TI | Marcus Falcão | Aprovação do plano (17/07/2025) |
| Tech Lead D1000 | Armando Pereira Reis Junior | Decisões de arquitetura, aprovação PRs |
| Gerente de TI D1000 | Humberto Erler | Gestão de ambientes, aprovação de versões |
| Coordenadora de projeto | Helena Moreira | Coordenação interna, convites, atas |
| Especialista de negócio | Ethierre Leite | Fluxos de negócio, validações PBM |
| Arquiteto/Dev | Alexandre Henrique | Integrações ITEC, arquitetura legada |
| Técnico | Rafael Nader | Regras de sanitização, testes |
| Operações/Deploy | Fagner Pereira | Deploy em ambientes, GMUD |
| QA/Testes | Julielle Santos | Execução de testes homologação |
| DBA | Marcus Ribeiro | Scripts de carga, base d1000_producao |
| Arquitetura | Diego Lacerda | Arquitetura de infraestrutura Profarma |

**Ambiente e ferramentas:**

| Ferramenta / Ambiente | Uso |
|---|---|
| Microsoft Azure (AKS, PostgreSQL, Service Bus, Key Vault) | Plataforma de produção do sistema |
| Azure DevOps (loja-balcao-frontend, loja-backend) | Repositório de código, pipelines CI/CD, PRs |
| Jira (Timeware) | Gestão de backlog e sprints (a partir de sprint 4) |
| Microsoft Teams | Canal diário com cliente (11h30) |
| Datadog | Monitoramento e observabilidade de ambientes |
| Prometheus + Grafana | Observabilidade interna (sprints 8+) |

## 7. Partes interessadas e comunicação (GPR 9)

| Parte interessada | Interesse | Canal / frequência |
|---|---|---|
| Pedro Costa (Rede D1000) | Go/no-go do piloto; cronograma | E-mail formal; escalonamentos críticos |
| Marcus Falcão (Profarma) | Visibilidade executiva | Apresentações pontuais (17/07/2025) |
| Armando Junior (Rede D1000) | Decisões técnicas e de processo | Daily 11h30 via Teams; e-mails |
| Humberto Erler (Rede D1000) | Aprovação de versões, ambientes | E-mails; aprovação de PRs |
| Time técnico D1000 | Execução de testes e deploys | Daily; e-mails de status; PRs |
| Tiago Nascimento (Timeware) | Qualidade técnica, decisões arquiteturais | Daily interna 9h00; alinhamentos ad-hoc |
| Abraão Oliveira (Timeware) | Status, comunicação formal com cliente | Status reports semanais (out–nov/2025) |

## 8. Transição (GPR 8)

Ao final da fase de piloto (loja 9), o sistema é promovido para rollout geral nas demais lojas da Rede D1000.

**Estratégia de promoção para produção:**

- **Fluxo de ambientes:** desenvolvimento (local/feature branch) → homologação (Azure AKS — ambiente D1000) → produção (Azure AKS — produção Profarma)
- **GMUD obrigatória:** qualquer promoção ao ambiente de produção da Rede D1000 requer abertura formal de Gerenciamento de Mudança (GMUD) com janela de mudança definida, rollback plan documentado e aprovação do Gerente de TI D1000 (Humberto Erler)
- **Execução do deploy em produção:** responsabilidade de Fagner Pereira (Operações/Deploy — Rede D1000), após aprovação da GMUD
- **Suporte pós-deploy:** a Timeware mantém canais de suporte ao vivo (Teams) durante o período de estabilização do piloto para atendimento a incidentes

*Evidência: GMUD 2624117 executada em 21/01/2026 — deploy da versão final no ambiente produtivo, após aprovação formal.*

A operação e sustentação pós-piloto são objeto de contrato separado de sustentação. A documentação técnica e de arquitetura (`PCP-PROFARMA01-001`) é entregue à Rede D1000 como parte da base de conhecimento para a equipe interna.

### 8.2 Checklist de go-live (pré-produção)

| Item | Atendido | Responsável |
|---|---|---|
| Homologação aprovada pelo cliente | Sim — aceite Helena Moreira (e-mail, Sprints 1–17) | QA D1000 (Julielle Santos) |
| Documentação de entrega completa (PCP, API docs) | Sim — PCP-PROFARMA01-001 + Swagger | Tech Lead |
| Testes de regressão executados sem falhas S1 | Sim — Sprints 18–19, zero S1 em aberto | QA Timeware (Lucas Batista) |
| Baseline de configuração registrada (tag/release) | Sim — tag `26.1.1.1` (Azure DevOps) | DevOps |
| GMUD aprovada pelo cliente (processo de mudança) | Sim — GMUD 2624117 aprovada por Humberto Erler | Gerente de Projeto |
| Credenciais e permissões de produção confirmadas | Sim — Azure Key Vault configurado; acessos AKS liberados | DevOps |

### 8.3 Suporte e monitoramento pós-go-live

| Item | Descrição |
|---|---|
| **Período de suporte pós-go-live** | 2 semanas a partir do deploy de 21/01/2026 (até 04/02/2026) |
| **Responsável pela sustentação** | Tech Lead + Gerente de Projeto |
| **Canal de atendimento** | Microsoft Teams — canal `#d1000-suporte` |
| **SLA de resposta (S1)** | Resposta em 2h; resolução em 24h |
| **SLA de resposta (S2/S3)** | Resposta em 1 dia útil; resolução em 3 dias úteis |

| Indicador | Fonte | Resultado no período |
|---|---|---|
| Incidentes em produção (S1) | Jira / canal Teams | 0 incidentes S1 no piloto (loja 9) |
| Latência p95 — GET /clientes/{cpf} | Datadog APM | 142ms (meta: ≤ 200ms) ✓ |
| Disponibilidade do serviço | Datadog Monitor / AKS | ≥ 99,5% ✓ |
| Erros de integração outbox | Datadog Logs | 0 eventos perdidos no período |

### 8.4 Critério de encerramento do suporte pós-go-live

O período de suporte intensivo encerrou em 29/01/2026 com o aceite formal de Humberto Erler (ATA-PROFARMA01-002), após:
- Período de 8 dias de operação no piloto (loja 9) sem incidentes S1;
- Todos os canais (PDV, Balcão, OMNI) operando dentro do SLA;
- Zero defeitos S1 ou S2 em aberto.

O projeto passou formalmente ao encerramento. Incidentes subsequentes são tratados via contrato de sustentação separado.

## 9. Riscos (GPR 10)

| # | Risco | Prob. | Impacto | Resposta / O que ocorreu |
|---|---|---|---|---|
| R-01 | Demora da Rede D1000 para aplicar merges e atualizar ambientes (blockers de validação) | Alta | Alto | Padrão recorrente: Timeware entregava em 1 dia, D1000 levava 7–15 dias para aplicar. Formalizado em e-mail para Pedro Costa em 23/01/2026 |
| R-02 | Dados legados com CPFs duplicados e FKs complexas, impedindo scripts de carga | Alta | Alto | Ocorreu em 07/11/2025: script de 113 GB gerado; execução bloqueada por CPFs duplicados (Marcus Ribeiro). Exigiu sanitização manual |
| R-03 | Acesso ao banco de dados de homologação negado | Alta | Alto | Ocorreu em 21/10/2025: acesso bloqueado por ~7 dias; impacto documentado em e-mail interno (21/10/2025) |
| R-04 | Conflito de branches em versões simultâneas do loja-backend | Média | Alto | Ocorreu em 23/01/2026: PR 10684 foi descartado pois merge já havia sido feito na versão 26.1.1.1; retrabalho exigido |
| R-05 | Configuração de URLs hardcoded em vez de banco de dados | Baixa | Médio | Ocorreu em jan/2026: URL do HttpClient sendo truncada; Humberto ordenou migração para parâmetros em banco (19/01/2026) |
| R-06 | Sequencial de IDs divergente entre API e banco legado | Média | Alto | Ocorreu em 06/11/2025: id_cliente gravado com sequencial divergente; script de correção solicitado |
| R-07 | Dependência de múltiplos sistemas externos (ITEC, VTEX, Propz, PBM) gerando atrasos de integração | Alta | Médio | Integração Propz atrasou para novembro/2025; PBM exigiu reuniões com Interplayers |
| R-08 | Divergência de percepção de responsabilidade pelo atraso entre Timeware e D1000 | Alta | Reputacional | Materializado em 09/01/2026: Armando discordou integralmente do status report da Timeware |

## 10. Viabilidade (GPR 11)

O projeto foi viável e concluído em janeiro de 2026, com a entrega das correções finais solicitadas pela equipe de QA da Rede D1000. A viabilidade foi testada por múltiplos blockers de infra, dados e integração, mas o time manteve o ritmo de entregas. O principal fator de extensão do cronograma foi a cadência de aplicação de ambiente pela Rede D1000 (risco R-01 materializado).

## 11. Aprovação do Plano (GPR 13)

| Envolvido | Papel | Aceite | Data | Ref. |
|---|---|---|---|---|
| Marcus Falcão | Diretor de TI — Profarma | Aprovado verbalmente na apresentação | 17/07/2025 | Fireflies transcript — Projeto Cadastro de Cliente - Apresentação do plano |
| Pedro Alves da Costa Junior | Patrocinador — Rede D1000 | Confirmado via e-mail | 23/01/2026 | Re: Status do Projeto Cadastro de Clientes – Liberação para Testes |
| Abraão Oliveira | Gerente de Projeto — Timeware | Confirmado | 28/04/2025 | ATA-PROFARMA01-001 |

---

## Controle de atualizações do plano

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Time de Melhoria Contínua | Versão inicial — reconstituída com base em e-mails e transcrições Fireflies do período 03/2025–01/2026 |
| 1.1 | 10/06/2026 | Time de Melhoria Contínua | Acréscimo da coluna SP Planejado na tabela §5.2 (573 SP totais) para consistência com a planilha de gestão do projeto |
| 1.2 | 11/06/2026 | Time de Melhoria Contínua | Acréscimo da tabela de orçamento de horas por papel em §4 (GPR 4) — 5.789 h totais estimadas; ampliação do §8 (GPR 8) com estratégia de transição para produção, fluxo de GMUD e responsáveis pelo deploy |
| 1.3 | 11/06/2026 | Time de Melhoria Contínua | Adição de §8.2 (checklist go-live), §8.3 (suporte pós-go-live com SLAs e indicadores Datadog) e §8.4 (critério de encerramento do suporte) — conformidade com TPL-GPR-001 v1.2 (GPR 8 / GPR 16) |
