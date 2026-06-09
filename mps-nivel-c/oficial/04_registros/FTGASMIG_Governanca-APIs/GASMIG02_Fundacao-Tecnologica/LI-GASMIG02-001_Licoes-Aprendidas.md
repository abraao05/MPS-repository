# Lições Aprendidas e Oportunidades de Melhoria — GASMIG Governança de APIs

| Campo | Valor |
|---|---|
| **Documento** | LI-GASMIG02-001 — Lições Aprendidas e Oportunidades de Melhoria |
| **Versão** | 1.0 |
| **Data** | 07/05/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Fundação Tecnológica GASMIG — Governança de APIs (OS-001) |
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

| # | Oportunidade | Área afetada | Prioridade |
|---|---|---|---|
| OM-01 | Criar checklist de pré-engajamento para projetos Azure cobrindo: acesso ao tenant, permissões mínimas, naming convention de recursos, ambientes disponíveis | Planejamento de projetos | Alta |
| OM-02 | Incluir métricas de referência para configuração de alertas e monitoramento Azure na base de estimativas organizacional | Estimativas e medição | Média |
| OM-03 | Elaborar template padrão de naming convention para recursos Azure a ser preenchido durante o kickoff com o cliente | Design / kickoff | Média |
| OM-04 | Incluir no checklist de verificação a validação explícita de Named Values configurados antes de qualquer deploy para ambiente de produção | Verificação técnica | Baixa |

---

## 5. Aplicação na OS-002

As lições LE-05 e OM-01 foram incorporadas na preparação da OS-002: as credenciais Microsoft Entra ID e as permissões necessárias foram solicitadas com uma semana de antecedência e confirmadas antes do início da sprint (28/05/2026).

As oportunidades OM-01 a OM-04 serão endereçadas no ciclo de melhoria de processos organizacionais.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 07/05/2026 | Gerente de Projeto | Lições aprendidas da OS-001; oportunidades de melhoria identificadas |
