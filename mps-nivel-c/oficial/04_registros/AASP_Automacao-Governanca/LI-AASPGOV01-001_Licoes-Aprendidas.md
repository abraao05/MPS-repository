# Lições Aprendidas — AASP_GOV · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | LI-AASPGOV01-001 |
| **Projeto** | AASP_GOV — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 02/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR (GPR 20) — evidência de projeto |

---

## 1. Objetivo

Consolidar as lições aprendidas durante a execução do projeto AASP_GOV para alimentar a melhoria contínua dos processos organizacionais da Timeware. Esta seção atende ao requisito GPR 20 do MR-MPS-SW:2024 e ao item correspondente do relatório de gaps da avaliação ASR. As lições relevantes são incorporadas aos templates organizacionais (TPL-*), aos processos (PRO-*) e aos guias de adaptação (GUIA-*) conforme aplicável.

## 2. Lições por dimensão

### 2.1 Validação prévia de contratos de API

| Item | Conteúdo |
|---|---|
| **O que ocorreu** | A API Jira v3 exige obrigatoriamente o formato ADF (Atlassian Document Format) para campos de texto rico (descrição, comentários). Essa exigência não era óbvia na documentação inicial e só foi descoberta durante a Fase 2 (Mapeamento de APIs). O time precisou alocar tempo adicional na Sprint 0 para investigar o formato, resultando em +4 h de esforço além do estimado. |
| **Impacto no projeto** | Desvio de +10% na Fase 2; necessidade de implementar `BuildAdfDocument` (não previsto inicialmente como componente separado). |
| **Causa-raiz** | Documentação oficial da Atlassian não destaca claramente a obrigatoriedade do ADF em texto rico; assumimos compatibilidade com texto plano por analogia com a API v2. |
| **Lição** | Em integrações com APIs maduras (Atlassian, Microsoft Graph, Google Workspace), realizar prova de conceito (PoC) específica para campos de texto rico durante o Discovery, **antes** do mapeamento completo de endpoints. |
| **Ação corretiva organizacional** | AC-01 (registrada em MED-AASPGOV01-001 §6): estimativa para mapeamento de APIs Atlassian em projetos futuros recebe acréscimo de 30% sobre baseline; checklist de PoC de ADF incorporado ao GUIA-GPC-001 §X (adaptação para projetos de integração com Atlassian). |

### 2.2 Identificação por prefixo no summary

| Item | Conteúdo |
|---|---|
| **O que ocorreu** | A decisão D03 (identificar cards migrados pelo prefixo `#ID` no summary do Jira) eliminou a necessidade de manter estado externo (banco de dados ou tabela de mapeamento) e simplificou drasticamente a lógica de idempotência (RNF-01). |
| **Impacto no projeto** | Redução estimada de 2 SP no esforço de RNF-01 (idempotência); ausência de novos componentes de persistência; serviço completamente stateless (atende D07). |
| **Lição** | Em cenários de sincronização unidirecional entre sistemas sem campo customizado disponível no destino, considerar identificação por prefixo/marcador no campo de texto público (summary, título, name). Estratégia replicável em integrações similares. |
| **Aplicabilidade** | Recomendado como padrão arquitetural em projetos de migração/sincronização unidirecional — documentado como referência em PCP-AASPGOV01-001 §2.4. |

### 2.3 Testes em ambiente real desde o início da Fase 4

| Item | Conteúdo |
|---|---|
| **O que ocorreu** | Os 5 defeitos identificados na Sprint 3 (BUG-01 a BUG-05) **só apareceram em ambiente real** Sensr/Jira. Nenhum deles seria detectado por mocks ou ambientes simulados — todos dependiam de comportamento específico das APIs externas (HTML real do Sensr, transições disponíveis no workspace Jira, paginação real). |
| **Impacto no projeto** | Validação a tempo (correções na própria Sprint 3); zero defeitos escapados para produção; meta M6 atingida. |
| **Causa-raiz** | Comportamento crítico do serviço depende da compatibilidade real entre Sensr e Jira; mocks não capturam variações reais de payload, transições disponíveis e formato HTML. |
| **Lição** | Em projetos de integração entre sistemas maduros, **homologação em ambiente real (workspace de teste) é mandatória desde o início da fase de validação**. Não substituir por mocks/simuladores em hipótese alguma. |
| **Ação corretiva organizacional** | Registrada na ADAP-AASPGOV01-001 §1 (eixo "Ambiente de stage") como padrão para projetos de integração. Recomendar inclusão de orientação equivalente no GUIA-GPC-001 e no TPL-VV-001 §2 (Métodos e critérios). |

### 2.4 Conversão HTML → texto plano

| Item | Conteúdo |
|---|---|
| **O que ocorreu** | A conversão de HTML do Sensr para texto plano foi inicialmente subestimada — assumida como "limpeza simples de tags". Na prática, exigiu o desenvolvimento de um HtmlHelper completo com dois métodos especializados: `ToPlainText` (para descrição) e `ParseDescriptionHistory` (para histórico estruturado, com múltiplas entradas). |
| **Impacto no projeto** | BUG-01 surgiu por envio direto de HTML ao Jira; correção exigiu desenvolvimento adicional na Sprint 3; +8h sobre estimativa da Fase 4. |
| **Lição** | Em projetos que migram conteúdo entre plataformas com formatos de texto diferentes (HTML, Markdown, ADF, Slack mrkdwn, Discord, etc.), tratar conversão de texto rico como **item de design obrigatório no PCP**, com prova de conceito específica para os tipos de conteúdo mais frequentes. |
| **Ação corretiva organizacional** | AC-02 (registrada em MED-AASPGOV01-001 §6): inclusão de cenário de teste obrigatório para tratamento de HTML/texto rico em TPL-VV-001 §6 (Cenários de teste) para projetos de migração de conteúdo. |

### 2.5 Mapeamento case-insensitive de status

| Item | Conteúdo |
|---|---|
| **O que ocorreu** | BUG-03 surgiu de comparação case-sensitive entre status Sensr e status Jira. Por exemplo, status "In Progress" no Jira foi tratado como diferente de "in progress" retornado por uma API em outra chamada, causando transições desnecessárias e ruído nos logs. |
| **Impacto no projeto** | Defeito de pequena complexidade técnica, mas com impacto operacional (transições redundantes geram ruído em painéis Jira). |
| **Lição** | Padronizar uso de `StringComparison.OrdinalIgnoreCase` para comparações de domínio cross-sistema (status, IDs textuais, nomes de entidades). Não confiar em case consistente entre sistemas independentes. |
| **Aplicabilidade** | Recomendado para inclusão no guia de boas práticas de integração da Timeware (apoio ao TPL-PCP-001 §2.3). |

### 2.6 Modelagem retroativa em sprints para evidência ágil

| Item | Conteúdo |
|---|---|
| **O que ocorreu** | O projeto foi executado em 4 fases waterfall (Arquitetura, Mapeamento, Desenvolvimento, Homologação) com gestão por horas, mas a evidência exigida pela avaliação MPS-SW Nível C demanda modelagem agile (sprints, story points, velocity). A solução foi modelar retroativamente o backlog em 4 sprints (~59 SP), documentar a adaptação em ADAP-AASPGOV01-001 e carregar tudo no Jira via CSV. |
| **Impacto no projeto** | Esforço adicional de ~6h para conciliação retroativa fases ↔ sprints e geração do JIRA-AASPGOV01_Backlog-Import.csv; resultado: evidência ágil completa sem distorcer a realidade da execução. |
| **Lição** | A modelagem retroativa em sprints/SP é uma estratégia válida e auditável quando a execução real é por fases — desde que **documentada explicitamente na ADAP** e refletida na planilha de gestão e no Jira. |
| **Aplicabilidade** | Padrão herdado do projeto AASP_CNJ — confirmado como abordagem replicável para projetos Timeware de pequeno e médio porte executados sem Scrum formal. |

### 2.7 Acúmulo de papéis em equipes enxutas

| Item | Conteúdo |
|---|---|
| **O que ocorreu** | Cezar Hiraki acumulou os papéis de Tech Lead e Arquiteto durante todo o projeto (ADAP §1). Decisão adequada ao porte (~7 semanas, escopo bem delimitado, equipe de 6 pessoas) — não houve sobrecarga nem conflito de responsabilidades. |
| **Lição** | Em projetos de pequeno porte (≤ 300 h, ≤ 8 semanas), o acúmulo de papéis Tech Lead + Arquiteto é viável e recomendável quando o escopo é técnico-uniforme. Para projetos maiores ou multi-tecnologia, manter papéis separados. |
| **Aplicabilidade** | Reforça o critério atual do GUIA-GPC-001 sobre acúmulo de papéis em projetos de pequeno porte. |

## 3. Oportunidades de melhoria para a organização

As lições acima geram as seguintes oportunidades de melhoria a serem avaliadas pelo Time de Melhoria Contínua:

| OM | Origem | Recomendação | Destino |
|---|---|---|---|
| OM-AASPGOV-01 | Lição 2.1 | Incluir checklist de PoC de campos de texto rico em integrações com APIs Atlassian no GUIA-GPC-001 | GUIA-GPC-001 (próxima revisão) |
| OM-AASPGOV-02 | Lição 2.3 | Reforçar no TPL-VV-001 §2 a obrigatoriedade de homologação em ambiente real para projetos de integração | TPL-VV-001 v1.1 |
| OM-AASPGOV-03 | Lição 2.4 | Adicionar cenário Gherkin de teste de tratamento de HTML/texto rico no TPL-VV-001 §6 para projetos de migração | TPL-VV-001 v1.1 |
| OM-AASPGOV-04 | Lição 2.5 | Documentar boas práticas de comparação cross-sistema (case-insensitive, normalização) em apoio ao TPL-PCP-001 | TPL-PCP-001 (próxima revisão) |
| OM-AASPGOV-05 | Lição 2.6 | Confirmar a modelagem retroativa em sprints como padrão da Timeware no GUIA-GPC-001 §X (Adaptação para projetos waterfall) | GUIA-GPC-001 (próxima revisão) |

As oportunidades acima são encaminhadas ao Time de Melhoria Contínua via PLA-GPC-001 (Plano de Gestão e Melhoria de Processos).

## 4. Auditoria e validação independente

As lições aprendidas registradas neste documento serão verificadas pela auditoria de GQA (Jonathan Alves, Auditor independente) e referenciadas em GQA-AASPGOV01-001 como parte da verificação de aderência ao processo MPS-SW (GPR 20).

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 02/06/2026 | Time de Melhoria Contínua | Lições aprendidas do projeto AASP_GOV consolidadas no encerramento (02/06/2026), com 7 lições e 5 oportunidades de melhoria organizacional. |
