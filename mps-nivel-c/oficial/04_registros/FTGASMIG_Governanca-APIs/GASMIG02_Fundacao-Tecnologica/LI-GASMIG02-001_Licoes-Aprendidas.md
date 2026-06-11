# Lições Aprendidas e Oportunidades de Melhoria — GASMIG Governança de APIs

| Campo | Valor |
|---|---|
| **Documento** | LI-GASMIG02-001 — Lições Aprendidas e Oportunidades de Melhoria |
| **Versão** | 1.2 |
| **Data** | 11/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Fundação Tecnológica GASMIG — Governança de APIs (OS-001 e OS-002) |
| **Aprovação** | Gerente de Projeto |

---

## 1. Objetivo

Consolidar as lições aprendidas ao longo da OS-001 e identificar oportunidades de melhoria para projetos futuros de configuração de plataformas Azure API Management.

---

## 2. O que funcionou bem

| # | Lição | Impacto |
|---|---|---|
| LE-01 | O documento de design (PCP) elaborado e alinhado com o cliente antes do início da configuração eliminou retrabalho: decisões de arquitetura (gateway tier, networking, políticas base) foram acordadas antecipadamente | Alto — zero refatoração pós-deploy |
| LE-02 | Substituição dos testes de software por checklists de verificação técnica e smoke checks HTTP foi bem aceita pelo cliente; o registro de adaptação (ADAP) formalizou a mudança sem perda de rastreabilidade | Alto — adequação natural ao contexto de configuração |
| LE-03 | Uso de Named Values para todos os segredos e configurações variáveis por ambiente desde o início facilitou a promoção entre ambientes sem exposição de credenciais | Médio — reduziu riscos de segurança e retrabalho |
| LE-04 | Matriz de rastreabilidade (RASTR) conectando requisitos → design → verificação agilizou a revisão de aceite com o cliente | Médio — ata de aceite assinada sem questionamentos sobre cobertura |

---

## 3. O que pode melhorar

| # | Lição | Causa-raiz | Impacto |
|---|---|---|---|
| LE-05 | Acesso ao portal Azure do cliente foi liberado dois dias após o kickoff, atrasando o início das atividades técnicas | Ausência de checklist pré-engajamento com requisitos de acesso | Baixo (absorvido no cronograma) |
| LE-06 | Esforço de configuração de alertas no Azure Monitor foi subestimado em ~20%; ajuste de thresholds exigiu ciclos adicionais com o cliente | Falta de métricas de referência para atividades de monitoramento na base de estimativas da organização | Médio |
| LE-07 | Nomenclatura de recursos Azure (resource groups, APIs, produtos) não foi alinhada com o cliente antes do início; houve renomeações parciais durante a OS-001 | Ausência de artefato de naming convention a ser preenchido no kickoff | Baixo |

---

## 4. Oportunidades de melhoria para processos organizacionais

| # | Oportunidade | Área afetada | Prioridade | Origem |
|---|---|---|---|---|
| OM-01 | Criar checklist de pré-engajamento para projetos Azure cobrindo: acesso ao tenant, permissões mínimas, naming convention de recursos, ambientes disponíveis | Planejamento de projetos | Alta | LE-05 — Retrospectiva OS-001 (GQA-GASMIG02-001 §2.1, 07/05/2026) |
| OM-02 | Incluir métricas de referência para configuração de alertas e monitoramento Azure na base de estimativas organizacional | Estimativas e medição | Média | LE-06 — Retrospectiva OS-001 (GQA-GASMIG02-001 §2.1, 07/05/2026) |
| OM-03 | Elaborar template padrão de naming convention para recursos Azure a ser preenchido durante o kickoff com o cliente | Design / kickoff | Média | LE-07 — Retrospectiva OS-001 |
| OM-04 | Incluir no checklist de verificação a validação explícita de Named Values configurados antes de qualquer deploy para ambiente de produção | Verificação técnica | Baixa | LE-03 — Boa prática identificada OS-001 (§2) |

---

## 5. Aplicação na OS-002

As lições LE-05 e OM-01 foram incorporadas na preparação da OS-002: as credenciais Microsoft Entra ID e as permissões necessárias foram solicitadas com uma semana de antecedência e confirmadas antes do início da sprint (28/05/2026).

As oportunidades OM-01 a OM-04 serão endereçadas no ciclo de melhoria de processos organizacionais.

---

## 6. Lições aprendidas — OS-002

### 6.1 O que funcionou bem

| # | Lição | Impacto |
|---|---|---|
| LE-08 | A aplicação prévia das lições LE-05 e OM-01 (credenciais e permissões Entra ID solicitadas com antecedência) eliminou o atraso de acesso que ocorreu na OS-001 | Alto — sprint iniciada no primeiro dia sem bloqueios de acesso |
| LE-09 | A continuidade da equipe entre OS-001 e OS-002 eliminou a curva de aprendizado sobre o ambiente Azure da GASMIG; o contexto técnico foi transferido sem overhead | Alto — velocity da OS-002 (5,6 SP/dia) reproduziu exatamente a da OS-001 |
| LE-10 | A adoção de valores padrão de mercado para thresholds de alerta (Azure Monitor), sem aguardar definição formal do cliente, permitiu seguir o cronograma e os thresholds foram confirmados durante a execução | Médio — risco R-08 mitigado sem impacto no prazo |
| LE-11 | A antecipação da sessão de apresentação (de 10/06 para 08/06) foi absorvida sem impacto porque a verificação técnica já estava concluída; a flexibilidade de agenda favoreceu o aceite mais rápido | Médio — aceite obtido 1 dia antes do prazo contratual |

### 6.2 O que pode melhorar

| # | Lição | Causa-raiz | Impacto |
|---|---|---|---|
| LE-12 | A homologação end-to-end (RF-19) foi realizada via apresentação em call sem roteiro formal de aceitação; o aceite veio por e-mail sem um protocolo de sign-off estruturado | Ausência de template de ata de aceite formal pré-preenchido para o cliente assinar | Baixo (aceite obtido sem questionamentos) |
| LE-13 | A documentação de thresholds definitivos do Azure Monitor ficou dispersa em e-mails; não há um artefato único consolidando os valores acordados | Falta de seção específica no PCP para parâmetros de monitoramento | Baixo |

### 6.3 Oportunidades de melhoria geradas pela OS-002

| # | Oportunidade | Área afetada | Prioridade | Origem |
|---|---|---|---|---|
| OM-05 | Criar template de ata de aceite pré-preenchido (check-list de entregáveis + campo de assinatura/e-mail de DE ACORDO) para uso padrão em projetos de configuração | Encerramento de projetos | Alta | LE-12 — Retrospectiva OS-002 (GQA-GASMIG02-001 §2.3, 10/06/2026) |
| OM-06 | Incluir seção de parâmetros de monitoramento e alertas no template de PCP para projetos Azure, consolidando os thresholds acordados com o cliente antes da sprint | Design de projeto | Média | LE-13 — Retrospectiva OS-002 (GQA-GASMIG02-001 §2.3, 10/06/2026) |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 07/05/2026 | Gerente de Projeto | Lições aprendidas da OS-001; oportunidades de melhoria identificadas |
| 1.1 | 10/06/2026 | Time de Melhoria Contínua | Adição das lições da OS-002 (§6) após encerramento do projeto |
| 1.2 | 11/06/2026 | Time de Melhoria Contínua | Acréscimo da coluna "Origem" nas tabelas §4 e §6.3, rastreando cada OM à retrospectiva e/ou auditoria GQA que a gerou (CP-vi) |
