# Lições Aprendidas — Rede D1000 · Cadastro de Clientes

| Campo | Valor |
|---|---|
| **Documento** | LI-PROFARMA01-001 |
| **Projeto** | Cadastro de Clientes — Rede D1000 |
| **Cliente** | Profarma S.A. / Rede D1000 |
| **Versão** | 1.2 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR (evidência de projeto — lições aprendidas) |

---

## 1. Objetivo

Registrar as principais lições aprendidas ao longo do projeto Cadastro de Clientes — Rede D1000 (abril/2025 a janeiro/2026), para aplicação em projetos futuros da Timeware de perfil semelhante: APIs críticas de negócio com integração a sistemas legados e múltiplos canais de consumo.

---

## 2. O que funcionou bem

### 2.1 Arquitetura robusta desde o início

A decisão de adotar Clean Architecture com separação rigorosa de camadas provou seu valor ao longo das 19 sprints. Mudanças frequentes nos contratos de integração (VTEX, Propz, BlueSoft) foram absorvidas sem retrabalho nas camadas de domínio e aplicação — apenas a camada de infraestrutura foi impactada. Isso foi especialmente importante dado o volume de change requests do projeto.

### 2.2 Outbox pattern como decisão estratégica

A implementação do outbox pattern para integração com o ITEC mostrou-se correta. O ITEC ficou indisponível em múltiplas ocasiões durante o desenvolvimento e em produção; o outbox garantiu que nenhum evento foi perdido e que a API de cadastro nunca ficou dependente da disponibilidade do legado. O investimento em implementar o padrão no Sprint 3 (maior complexidade inicial) pagou dividendos em confiabilidade ao longo de todo o projeto.

### 2.3 Piloto na loja 9

A estratégia de piloto restrito à loja 9 antes do rollout geral foi acertada. Identificaram-se e corrigiram-se problemas que só apareciam em condições reais de operação (volume de transações PDV no horário de pico, edge cases de CPF com caracteres especiais em terminais legados) sem impactar a rede como um todo.

### 2.4 Qualidade dos testes unitários

Os 273 cenários de teste unitário entregues forneceram segurança para o time ao longo das mudanças de requisitos. Em mais de uma ocasião, alterações de escopo que pareciam simples quebraram testes unitários existentes, revelando efeitos colaterais que não eram imediatamente óbvios. A cultura de TDD adotada pelo time a partir do Sprint 3 foi determinante para isso.

### 2.5 Dailys consistentes e rastreabilidade com Jira

A cadência de daily diária manteve a equipe alinhada em um projeto de alta complexidade com múltiplas integrações em paralelo. A introdução do Jira no Sprint 4 melhorou significativamente a rastreabilidade de requisitos para tarefas e o planejamento das sprints subsequentes.

### 2.6 Engajamento do time técnico D1000

O envolvimento ativo de Armando Junior (Tech Lead D1000) nas decisões arquiteturais e revisões de PRs de mudanças significativas garantiu alinhamento contínuo com as restrições e o contexto do ambiente D1000. A presença de Julielle Santos (QA D1000) nos testes de homologação acelerou o aceite formal das entregas.

---

## 3. O que pode melhorar

### 3.1 Requisitos de integração com sistemas satélites

**O que aconteceu:** Os contratos de API das integrações com BlueSoft, CloseUp e PBM só foram disponibilizados pela D1000 a partir do Sprint 6 (agosto/2025), causando replanejamento e adição de escopo não previsto originalmente.

**Causa raiz:** As equipes responsáveis pelos sistemas satélites não foram envolvidas nas reuniões de discovery no início do projeto. O levantamento inicial de requisitos focou no comportamento do sistema principal sem mapear todas as dependências externas.

**Melhoria proposta:** Em projetos com múltiplas integrações, mapear todos os sistemas satélites e seus proprietários técnicos na fase de discovery (antes do kickoff). Solicitar contratos de API e ambientes de sandbox de todos os sistemas integrados como pré-requisito do Sprint 1.

### 3.2 Acesso ao ambiente de homologação

**O que aconteceu:** O ambiente AKS de homologação só ficou disponível em julho/2025 (~2,5 meses após o início do desenvolvimento). Durante esse período, o time trabalhou em ambiente Docker local, o que atrasou a identificação de problemas específicos do ambiente Azure (configurações de rede, limites de recursos do AKS, comportamento do Azure Service Bus em produção).

**Causa raiz:** A liberação dos acessos ao Azure pela D1000 dependia do processo de aprovação do time de Infraestrutura interno, que não foi mapeado como dependência crítica no planejamento inicial.

**Melhoria proposta:** Mapear como dependência bloqueante no plano do projeto a disponibilidade do ambiente de homologação antes do início do desenvolvimento. Incluir como critério de aceite do Sprint 1 a confirmação do acesso ao ambiente cloud de destino.

### 3.3 Processo GMUD — lead time de deploys em produção

**O que aconteceu:** O processo GMUD da D1000 adicionou 2–5 dias úteis de lead time a cada ciclo de release em produção. Nas sprints finais (Sprint 17–19), esse lead time comprimiu o tempo disponível para identificar e corrigir bugs de produção antes dos prazos.

**Causa raiz:** O processo GMUD não foi mapeado como fator de planejamento durante o kickoff. O tempo de aprovação de GMUD não foi incluído nas estimativas de sprint que envolviam entregas em produção.

**Melhoria proposta:** Em projetos com clientes que têm processo formal de GMUD, incluir o lead time de aprovação nas estimativas de sprint desde o início. Planejar releases em produção com pelo menos 5 dias úteis de antecedência do prazo final.

### 3.4 Conhecimento do legado ITEC

**O que aconteceu:** A documentação do ITEC era inexistente ou desatualizada. O time Timeware precisou reverse-engineer o comportamento do sistema legado analisando código-fonte Delphi e dados de produção, o que consumiu tempo não planejado nos sprints 2–4.

**Causa raiz:** A premissa do projeto de que a D1000 forneceria documentação técnica do ITEC não se confirmou. O ITEC tem ~15 anos de desenvolvimento sem documentação formal.

**Melhoria proposta:** Em projetos de substituição/integração de sistemas legados sem documentação, incluir explicitamente um marco de "discovery técnico do legado" no planejamento inicial, com alocação de tempo e entregável específico (mapeamento de comportamento do legado). Não assumir que documentação existente é suficiente.

### 3.5 Volume de change requests e gestão do escopo

**O que aconteceu:** O projeto acumulou 12 change requests formais ao longo das 19 sprints, adicionando integrações (BlueSoft, CloseUp), funcionalidades (RF-10 reativação, RF-17 worker LGPD) e alterando contratos de API. A maioria foi absorvida sem aditivo contratual, por decisão comercial da Timeware.

**Causa raiz:** O contrato de squad mensalizado (3 Dev Pleno) cria incentivo para absorver mudanças sem formalização de escopo, pois o modelo de cobrança não é por funcionalidade entregue. Isso facilita o relacionamento com o cliente mas aumenta o risco de scope creep não gerenciado.

**Melhoria proposta:** Mesmo em contratos de squad mensalizado, manter o registro formal de change requests com estimativa de esforço adicional, mesmo que não gerem cobrança adicional. Isso aumenta a visibilidade do esforço real entregue e serve como insumo para renegociações futuras.

### 3.6 Coordenação da carga inicial da base (~7 milhões de CPFs)

**O que aconteceu:** A carga inicial da base (migration batch de ~7 milhões de registros saneados) precisou ser executada em múltiplas rodadas, pois a primeira execução revelou problemas de qualidade no arquivo de extração do ITEC (CPFs inválidos, campos com encoding errado). O processo levou 3 semanas a mais do que o planejado.

**Causa raiz:** O processo de saneamento da base legada foi subestimado. A expectativa era de que o DBA da Profarma entregaria um arquivo limpo; na prática, o saneamento foi iterativo com múltiplos ciclos de extração → validação → correção.

**Melhoria proposta:** Para projetos de migração de base legada, planejar o processo de saneamento como um subprojeto com suas próprias etapas, critérios de aceite e prazo. Incluir um ciclo de validação do arquivo de extração antes de incluí-lo no cronograma da API.

---

## 4. Oportunidades de melhoria para a organização

| # | Oportunidade | Área de processo | Ação proposta | Origem |
|---|---|---|---|---|
| OM-01 | Checklist de discovery para projetos de integração com legados | GPR / REQ | Criar checklist padronizado com itens: mapeamento de sistemas satélites, disponibilidade de documentação legada, contratos de API de integrações, acesso a ambientes | GQA-P01 NC-01 (20/06/2025) + Retrospectiva Sprint 6 (§3.1) |
| OM-02 | Template de estimativa incluindo lead time GMUD | GPR | Adicionar ao template de planejamento de sprint um campo para "lead time de aprovação do processo de change management do cliente" | Retrospectiva Sprints 17–19 (§3.3) |
| OM-03 | Registro de change requests mesmo em contratos de squad | GPR | Incluir na rotina de gestão o registro de CRs com esforço estimado, mesmo quando não há impacto financeiro direto | Retrospectiva (§3.5) + GQA-P02 (10/10/2025) |
| OM-04 | Protocolo de migration de base legada | PCP | Criar guia técnico para projetos com carga inicial de dados legados: extração, validação, saneamento, carga em lotes, rollback | Retrospectiva Sprint 10 (§3.6) |
| OM-05 | Replicar outbox pattern como padrão Timeware | PCP | Documentar o outbox pattern implementado neste projeto como padrão arquitetural recomendado para integrações com sistemas legados sem garantia de disponibilidade | Boa prática identificada Sprint 3 (§2.2) |

---

## 5. Aplicação no próximo ciclo e publicação

Todas as lições identificadas com ação proposta (seções 3 e 4) devem ser consideradas no planejamento dos próximos projetos Timeware de perfil semelhante (API crítica + legado + múltiplas integrações). Itens OM-01, OM-02 e OM-03 são candidatos a atualização dos templates e processos de GPR da organização.

As lições aprendidas e oportunidades de melhoria deste projeto foram encaminhadas ao COO e publicadas na base de conhecimento organizacional da Timeware:

- **Confluence:** `Timeware / Base de Conhecimento / Projetos Encerrados / Cadastro de Clientes — Rede D1000 / Lições Aprendidas`
- **Google Drive:** `Projetos / PROFARMA01 — Cadastro de Clientes / Encerramento / Lições Aprendidas`

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Time de Melhoria Contínua | Versão inicial — reconstituída com base em retrospectivas, dailys e transcrições Fireflies do período 04/2025–01/2026 |
| 1.1 | 11/06/2026 | Time de Melhoria Contínua | Acréscimo da coluna "Origem" na tabela §4, rastreando cada OM à retrospectiva e/ou auditoria GQA que a gerou (CP-vi) |
| 1.2 | 11/06/2026 | Time de Melhoria Contínua | Adição em §5 do registro de publicação das lições aprendidas no Confluence e Google Drive (conformidade com GPC 12 — PRO-GPC-001 v2.3) |
