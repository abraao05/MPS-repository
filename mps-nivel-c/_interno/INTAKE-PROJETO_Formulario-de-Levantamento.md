# Formulário de Levantamento de Projeto — MPS-SW Nível C

| Campo | Valor |
|---|---|
| **Documento** | INTAKE-PROJETO (interno) |
| **Versão** | 1.1 |
| **Data** | 15/06/2026 |
| **Uso** | Preencher antes de solicitar a geração dos documentos MPS do projeto |
| **Projeto** | Cadastro de Clientes — Rede D1000 |

> **Como usar:** preencha todos os blocos abaixo e entregue ao responsável pela geração dos documentos. Campos marcados com **\*** são obrigatórios para gerar o conjunto mínimo. Os demais enriquecem documentos específicos. Deixe em branco o que genuinamente não se aplica — não invente dados.

---

## BLOCO 1 — Identificação do projeto

*Alimenta: TAP, PLA, cabeçalhos de todos os documentos*

| Campo | Sua resposta |
|---|---|
| **\* Nome do projeto** | Cadastro de Clientes — Rede D1000 |
| **\* Código do projeto** | PROFARMA01 |
| **\* Cliente / organização** | Profarma S.A. / Rede D1000 |
| **\* Produto ou sistema** | API RESTful de Cadastro de Clientes — cloud-native, .NET 8, PostgreSQL (Azure), deploy em AKS |
| **\* Objetivo principal** | Substituir a gestão de cadastro dispersa no sistema legado ITEC por uma solução cloud-native com CPF como chave primária única, eliminando duplicidades históricas entre bandeiras e expondo API RESTful para todos os canais da Rede D1000 (PDV, Balcão, Call Center, OMNI/VTEX). O sistema integra-se aos sistemas satélites (ITEC, VTEX, Propz CRM, PBM/Interplayers, BlueSoft, CloseUp) e opera a partir de piloto na loja 9. |
| **\* Data de início** | 17/03/2025 (primeiras reuniões de design) / 28/04/2025 (início formal das sprints) |
| **\* Data de encerramento** | 29/01/2026 |
| **O projeto tem pacotes / fases distintas?** | Sim. 6 fases: (1) Discovery e arquitetura — 17/03–27/04/2025; (2) Desenvolvimento sprints 1–6 — 28/04–04/07/2025; (3) Consolidação e apresentação — 07/07–01/08/2025; (4) Preparação para testes — 04/08–26/09/2025; (5) Testes e correções — 29/09–30/11/2025; (6) Reta final — 01/12/2025–29/01/2026. |
| **Código do pacote 1** | PROFARMA01 (contrato único — squad mensalizado) |
| **Código do pacote 2 (se houver)** | — |

---

## BLOCO 2 — Equipe

*Alimenta: TAP, PLA §6, GQA, VV, ATAs*

### Equipe Timeware

| Papel | Nome |
|---|---|
| **\* Gerente de Projeto** | Abraão Oliveira |
| **\* Tech Lead / Arquiteto** | Tiago Nascimento (Tech Lead) / Erick Coelho (Dev Principal / Arquiteto da solução — sprints 1–11) |
| **Desenvolvedor(es)** | Gustavo Mathias (sprints 1–19, integral) |
| | Renan Kiyoshi (sprints 1–19, integral) |
| | Cézar Hiraki (sprints 8–19, integral) |
| | João Cruz (sprints 13–19, parcial 50%) |
| | David Buena (sprint 14 — Infra/DevOps) |
| **QA / Testes** | Lucas Batista (sprints 15–19, parcial 40%) |
| **Designer UX/UI** | Não aplicável (produto API — sem interface gráfica) |
| **\* Auditor GQA** | COO (Operações Timeware) — independente da equipe de projeto |

### Stakeholders do cliente

| Papel | Nome | Responsabilidade |
|---|---|---|
| **\* Sponsor / responsável pelo aceite** | Pedro Alves da Costa Junior | Patrocinador — Rede D1000; decisões de go/no-go; aceite final (e-mail 23/01/2026) |
| **Responsável pelo aceite formal** | Humberto Erler | Gerente de TI D1000; aceite formal em ATA-PROFARMA01-002 (29/01/2026); aprovação GMUD 2624117 |
| **Diretor de TI** | Marcus Falcão | Aprovação do plano de projeto (17/07/2025 — Profarma) |
| **PO / contato técnico** | Armando Pereira Reis Junior | Tech Lead / Gestor de TI D1000; aprovação arquitetural; revisão de PRs; daily 11h30 |
| **Revisor de código (se fizer code review)** | Armando Pereira Reis Junior | Aprovação de mudanças arquiteturais no loja-backend |
| **Outros** | Helena Moreira | Coordenadora de projeto D1000; aceites parciais por e-mail (sprints 1–17) |
| | Ethierre Leite | Especialista de negócio D1000; fluxos PBM e validações de negócio |
| | Julielle Santos | QA/Testes D1000; execução UAT; aprovação dos roteiros de teste |
| | Fagner Pereira | Operações/Deploy D1000; execução de deploys em ambientes; GMUD |
| | Rafael Nader | Técnico D1000; regras de sanitização, testes |
| | Alexandre Henrique | Arquiteto/Dev D1000; integrações ITEC e arquitetura legada |
| | Marcus Ribeiro | DBA Profarma; scripts de carga, base d1000_producao |
| | Diego Lacerda | Arquitetura de infraestrutura Profarma |
| | Marcelo Rezende | Representante técnico Profarma |

---

## BLOCO 3 — Escopo e requisitos

*Alimenta: TAP, PLA §2, REQ, RASTR*

### Escopo

| Campo | Sua resposta |
|---|---|
| **\* O que está incluído** | API de Cadastro de Clientes em .NET 8 com Clean Architecture e PostgreSQL (Azure); 16 endpoints REST (cadastro, consulta, atualização, inativação, reativação, busca, perfil completo, health, métricas, endpoints compatíveis VTEX/Call Center); integração com ITEC (trigger/outbox pattern + worker); integração VTEX (canal OMNI); integração Call Center; integração Propz CRM (Azure Service Bus); integração PBM/Interplayers; integração BlueSoft; integração CloseUp; worker de expurgo LGPD; carga inicial de ~7 milhões de CPFs saneados; deploy em Azure AKS; pipelines CI/CD no Azure DevOps; monitoramento via Datadog; 273 testes unitários; piloto na loja 9 cobrindo PDV, Balcão e OMNI. |
| **\* O que está fora do escopo** | Modernização dos aplicativos D1000 Express e Connect D1000; desenvolvimento de novos módulos do ITEC legado; sustentação pós-piloto; rollout geral para toda a rede (demais lojas). |
| **Produto de entrada** | Acessos aos ambientes Azure (DevOps, homologação, produção) liberados pela Rede D1000; base de dados legada ITEC (~20 milhões de registros) saneada com apoio do DBA Marcus Ribeiro; contratos de API dos sistemas satélites (VTEX, Propz, PBM, BlueSoft, CloseUp, ITEC). |

### Requisitos funcionais

| Código | Nome | Descrição |
|---|---|---|
| RF-01 | Cadastro de cliente | Permite cadastro de novo cliente com CPF como chave primária única; campos obrigatórios: CPF, nome completo, data de nascimento, telefone e e-mail. |
| RF-02 | Rejeição de CPF duplicado | Rejeita cadastro de CPF já existente na base, retornando erro HTTP 409 com mensagem descritiva. |
| RF-03 | Consulta por CPF | Permite consulta de cliente por CPF via GET, retornando todos os dados cadastrais ativos. |
| RF-04 | Atualização parcial | Permite atualização parcial (PATCH) dos dados cadastrais: nome, endereço, telefone, e-mail, dados complementares. |
| RF-05 | Inativação lógica (LGPD) | Permite inativação lógica de cliente preservando integridade referencial, com registro de motivo, data e auditoria. |
| RF-06 | Busca por nome parcial | Permite consulta de cliente por nome parcial (search) com paginação de resultados. |
| RF-07 | Log de auditoria | Registra log de auditoria para toda operação de criação, atualização e inativação, com operador, canal de origem e timestamp. |
| RF-08 | Carga inicial da base | Suporta carga inicial de ~7 milhões de CPFs saneados da base legada ITEC via worker batch. |
| RF-09 | Verificação de existência de CPF | Expõe endpoint HEAD /clientes/{cpf} para verificação sem retorno de dados pessoais. |
| RF-10 | Reativação de cliente | Permite reativação de cliente previamente inativado, mediante registro de motivo. |
| RF-11 | Integração ITEC (outbox) | Publica eventos de criação/atualização/inativação no outbox do PostgreSQL, consumidos por worker de integração com ITEC. |
| RF-12 | Integração VTEX | Expõe endpoints compatíveis com o contrato de API da plataforma VTEX (canal OMNI). |
| RF-13 | Integração Call Center | Expõe endpoints para o Call Center consultar e cadastrar clientes em tempo real (SLA 95% em até 500ms). |
| RF-14 | Integração Propz CRM | Notifica o Propz CRM de eventos via Azure Service Bus seguindo schema Propz. |
| RF-15 | Integração BlueSoft | Integração com BlueSoft para sincronização de dados de endereço e score de crédito. |
| RF-16 | Integração CloseUp | Integração com CloseUp para consulta de histórico de compras, retornando dados agregados no perfil completo. |
| RF-17 | Worker de expurgo LGPD | Worker de anonimização de dados pessoais de clientes inativados há mais de 5 anos, com log de auditoria. |
| RF-18 | Health check | Expõe GET /health com status dos componentes: banco de dados, filas e dependências externas. |
| RF-19 | Métricas Prometheus | Expõe métricas no formato Prometheus para coleta pelo Datadog. |

### Requisitos não funcionais

| Código | Categoria | Descrição |
|---|---|---|
| RNF-01 | Arquitetura | API em .NET 8 com Clean Architecture (camadas Domain, Application, Infrastructure, API). |
| RNF-02 | Infraestrutura | Banco de dados PostgreSQL no Azure (Azure Database for PostgreSQL — Flexible Server). |
| RNF-03 | Infraestrutura | Deploy em contêineres Docker orquestrados pelo Azure Kubernetes Service (AKS). |
| RNF-04 | Segurança | URLs, strings de conexão e segredos armazenados no banco de dados ou Azure Key Vault — nunca hardcoded. |
| RNF-05 | Segurança | Autenticação via API Key para PDV e Balcão; OAuth 2.0 para integrações sistema-a-sistema (VTEX, Propz). |
| RNF-06 | Performance | Suporte a pico de 500 requisições/segundo no endpoint GET /clientes/{cpf} sem degradação de SLA. |
| RNF-07 | Performance | Tempo de resposta GET /clientes/{cpf} ≤ 200ms (percentil 95) em condições normais. |
| RNF-08 | Disponibilidade | Disponibilidade ≥ 99,5% mensal, excluindo janelas de manutenção programadas via GMUD. |
| RNF-09 | Resiliência | Backup automático com retenção de 7 dias e capacidade de point-in-time recovery. |
| RNF-10 | Conformidade (LGPD) | Tratamento de dados pessoais seguindo os princípios da LGPD (Lei 13.709/2018). |
| RNF-11 | Qualidade | Cobertura de testes unitários ≥ 80% nas camadas Application e Domain; mínimo 273 cenários. |
| RNF-12 | DevOps | Pipeline CI/CD no Azure DevOps com gates de qualidade: build, testes unitários e análise estática. |
| RNF-13 | Observabilidade | Monitoramento e observabilidade via Datadog (APM, logs e alertas). |
| RNF-14 | Governança | Mudanças arquiteturais requerem aprovação do Tech Lead D1000 (Armando Junior). |

---

## BLOCO 4 — Adaptação do processo-padrão

*Alimenta: ADAP, PLA §3*

| Item | Decisão | Justificativa |
|---|---|---|
| **Design UX/UI** | Não aplicável | O produto é uma API backend sem interface gráfica |
| **Nível de documentação** | Padrão | Projeto em regime de squad mensalizado com cliente envolvido; documentação MPS completa |
| **Combinação de papéis** | Tech Lead acumula Arquiteto; GP acumula Account Manager | Equipe de porte médio; Tiago Nascimento atua como Tech Lead e Erick Coelho como Arquiteto/Dev Principal nos sprints 1–11 |
| **Processo de revisão de código** | PR obrigatório no Azure DevOps; revisão por Tech Lead ou Dev Senior; mudanças arquiteturais requerem aprovação de Armando Junior (D1000) | Equipe distribuída SP/RJ; alto volume de integração; qualidade do código crítica para piloto |
| **Processo de entrega** | Desenvolvimento local/feature branch → homologação (Azure AKS D1000) → produção (Azure AKS) via GMUD; deploy executado por Fagner Pereira (D1000) | Processo de mudança (GMUD) obrigatório pelo cliente para produção |
| **Cadência de entrega** | Sprints de ~2 semanas com dailys às 11h30 via Teams | Equipe distribuída SP/RJ; ritmo de integração contínua com cliente exigiu cerimônias diárias |
| **Controle de versão** | Azure DevOps — repositórios da Profarma (loja-balcao-frontend, loja-backend) | Repositórios do cliente; acesso compartilhado desde o início |
| **Gestão de backlog** | Azure DevOps Boards (sprints 1–3) + Jira (a partir do sprint 4) | Jira introduzido a partir do sprint 4 para maior visibilidade ao cliente e rastreabilidade formal |
| **Rastreabilidade de defeitos** | Planilha de tickets (Gustavo Mathias) + Azure DevOps | Histórico completo exportado em 07/11/2025 |
| **Outras adaptações** | Viagens presenciais previstas para pontos críticos; custo médio R$ 5.000 por deslocamento (4 pessoas) | Equipe distribuída SP/RJ; bloqueios técnicos de ambiente exigiram alinhamento presencial |

---

## BLOCO 5 — Estimativas e cronograma

*Alimenta: PLA §4 e §5, RAC, planilha de gestão*

### Estimativas

| Campo | Valor |
|---|---|
| **\* Tamanho estimado (story points)** | 573 SP planejados / 564 SP realizados (−1,6%) |
| **\* Velocity de referência (pontos/sprint)** | ~30 SP/sprint (média realizada; pico: 42 SP no Sprint 16) |
| **\* Base histórica usada** | Dados históricos de projetos Timeware de porte similar; velocity calibrada no Sprint 1 com base na composição da equipe |
| **Esforço/prazo estimado** | 19 sprints / ~10 meses (abril/2025 a janeiro/2026); 5.789 h totais estimadas |
| **Duração de cada sprint** | ~2 semanas |

### Marcos

| Marco | Data planejada | Data realizada |
|---|---|---|
| Início do projeto (primeiras reuniões de design) | 17/03/2025 | 17/03/2025 |
| Início formal das sprints / dailys | 28/04/2025 | 28/04/2025 |
| Fim Discovery / Requisitos (Fase 1) | Abril/2025 | 27/04/2025 |
| Aprovação do Plano (baseline — Marcus Falcão) | Junho/2025 | 17/07/2025 |
| Fim Sprint 1 | 09/05/2025 | 09/05/2025 |
| Fim Sprint 2 | 23/05/2025 | 23/05/2025 |
| Fim Sprint 3 | 06/06/2025 | 06/06/2025 |
| Fim Sprint 4 | 20/06/2025 | 20/06/2025 |
| Fim Sprint 5 | 04/07/2025 | 04/07/2025 |
| Fim Sprint 6 — 16 endpoints + 273 testes unitários | 18/07/2025 | 18/07/2025 |
| Apresentação formal do plano ao Diretor (Falcão) | Junho/2025 | 17/07/2025 |
| Fim Sprint 7 | 01/08/2025 | 01/08/2025 |
| Fim Sprint 8 | 15/08/2025 | 15/08/2025 |
| Início da homologação / ambiente AKS configurado | Setembro/2025 | Setembro/2025 |
| Fim Sprint 9 | 29/08/2025 | 29/08/2025 |
| Fim Sprint 10 — carga inicial 7M CPFs | 12/09/2025 | 12/09/2025 |
| Início testes de homologação (<5% em 29/09 — aceleração) | Setembro/2025 | 29/09/2025 |
| Integração Propz CRM disponível para testes | Outubro/2025 | 04/12/2025 |
| Proposta de infraestrutura produtiva Azure | Novembro/2025 | 03/11/2025 |
| GMUD 2624117 (deploy produção) | Janeiro/2026 | 21/01/2026 |
| Liberação formal para testes de homologação | Janeiro/2026 | 22/01/2026 |
| Versão 26.1.1.1 disponível no ambiente | Janeiro/2026 | 26/01/2026 |
| Piloto / Encerramento | Setembro/2025 (original) → Janeiro/2026 (revisado) | 29/01/2026 |
| Aceite final / Encerramento formal | Janeiro/2026 | 29/01/2026 (ATA-PROFARMA01-002 — Humberto Erler) |

---

## BLOCO 6 — Ambiente e configuração

*Alimenta: PLA §6, GCO*

| Campo | Valor |
|---|---|
| **\* Repositório de código** | Azure DevOps — cvelazquez.visualstudio.com / Profarma; repositórios: loja-backend, loja-balcao-frontend |
| **\* Branch strategy** | Git Flow: main + develop + feature branches; PR obrigatório para merge em develop; PRs para release e main requerem aprovação de pelo menos 1 revisor (Tech Lead ou Dev Senior). Mudanças arquiteturais exigem aprovação de Armando Junior (D1000). |
| **Ambiente de desenvolvimento** | Local (Docker / .NET 8); feature branches no Azure DevOps |
| **Ambiente de homologação / staging** | Azure AKS — ambiente de homologação D1000 (homologação); PostgreSQL Azure Flexible Server |
| **Ambiente de produção** | Azure AKS — produção Profarma; Azure Database for PostgreSQL — Flexible Server; Azure Key Vault; Azure Service Bus |
| **\* Tecnologias principais** | .NET 8, C#, Clean Architecture, PostgreSQL (Azure), Docker, Azure Kubernetes Service (AKS), Azure DevOps, Azure Service Bus, Azure Key Vault, Datadog, Prometheus + Grafana, xUnit, FluentAssertions, TestContainers |
| **Ferramentas de gestão** | Jira (Timeware — a partir sprint 4), Azure DevOps Boards (sprints 1–3), Microsoft Teams (dailys 11h30), Microsoft Teams (comunicação interna 9h00), Fireflies (transcrições de reuniões) |
| **Baseline de configuração (versão entregue)** | Tag `25.12.1.1` (Sprint 17 — loja-backend); Tag `26.1.1.1` (Sprint 19 — versão final de produção); Tag `v1.0.0` (Release formal — baseline MPS) |

---

## BLOCO 7 — Decisões arquiteturais e de design

*Alimenta: PCP, GDE, ITP*

### Arquitetura

| Campo | Valor |
|---|---|
| **Padrão arquitetural** | Clean Architecture com 4 camadas: Domain, Application, Infrastructure, API. CPF como chave primária única. Outbox pattern para integração assíncrona com ITEC. |
| **Integrações externas** | ITEC (legado D1000) — outbox pattern + worker assíncrono; VTEX (OMNI) — REST síncrono; Call Center — REST síncrono; Propz CRM — Azure Service Bus (assíncrono); PBM/Interplayers — REST bidirecional; BlueSoft — REST síncrono; CloseUp — REST síncrono |
| **Estratégia de build e entrega** | Docker containers → Azure AKS; pipeline CI/CD no Azure DevOps (build + testes unitários + análise estática); deploy em produção via GMUD aprovada por Humberto Erler; execução de deploy por Fagner Pereira (D1000) |

### Decisões formais (GDE) — uma linha por decisão relevante

| Contexto / Problema | Alternativas consideradas | Decisão tomada | Justificativa |
|---|---|---|---|
| Escolha de banco de dados | SQL Server (legado D1000) vs. PostgreSQL Azure | PostgreSQL Azure Flexible Server | Cloud-native, custo-benefício no Azure, suporte a extensões avançadas, portabilidade |
| Integração com ITEC legado | REST síncrono vs. outbox pattern | Outbox pattern + worker assíncrono | ITEC tem SLA de disponibilidade baixo; outbox garante at-least-once delivery com tolerância a falhas transientes |
| Arquitetura da API | Monólito simples vs. Clean Architecture | Clean Architecture (Domain/Application/Infrastructure/API) | Manutenibilidade de longo prazo; separação de responsabilidades; facilita testes unitários (cobertura ≥ 80%) |
| Chave primária do cliente | ID sequencial legado ITEC vs. CPF | CPF como chave primária única | Elimina duplicidades históricas entre bandeiras; CPF é o identificador de negócio universal nos canais |
| Orquestração de containers | App Service (Azure) vs. AKS | Azure Kubernetes Service (AKS) | Escalabilidade horizontal; ambiente já padronizado na Profarma; suporte ao pico de 500 req/s |
| Integração Propz CRM | REST síncrono vs. Azure Service Bus | Azure Service Bus (mensageria assíncrona) | Schema definido pelo Propz; baixo acoplamento; Propz exige integração via bus; alinhado ao padrão de eventos do sistema |
| Autenticação de canais | JWT vs. API Key | API Key para PDV/Balcão; OAuth 2.0 para integrações sistema-a-sistema | PDV/Balcão não suportam OAuth; VTEX e Propz requerem OAuth 2.0 |

---

## BLOCO 8 — Riscos

*Alimenta: PLA §9, planilha de gestão*

> Probabilidade e Impacto: escala 1–3. Exposição = P × I (resultado 1–9).

| Risco | Prob. (1–3) | Impacto (1–3) | Exposição | Resposta | Status final |
|---|---|---|---|---|---|
| R-01 — Demora da Rede D1000 para aplicar merges e atualizar ambientes (blockers de validação) | 3 | 3 | 9 | Mitigar: comunicação formal ao sponsor Pedro Costa; formalização em e-mail (23/01/2026) | Realizado — Timeware entregava em 1 dia, D1000 levava 7–15 dias para aplicar |
| R-02 — Dados legados com CPFs duplicados e FKs complexas impedindo scripts de carga | 3 | 3 | 9 | Mitigar: saneamento manual com Marcus Ribeiro (DBA Profarma) | Realizado — script de 113 GB gerado em 07/11/2025; saneamento exigiu 3 semanas adicionais |
| R-03 — Acesso ao banco de dados de homologação negado | 3 | 3 | 9 | Mitigar: escalação formal interna; e-mail documentando impacto | Realizado — acesso bloqueado de 14 a 21/10/2025 (~7 dias); impacto no sprint 13 |
| R-04 — Conflito de branches em versões simultâneas do loja-backend | 2 | 3 | 6 | Mitigar: disciplina de Git Flow; comunicação prévia entre times | Realizado — PR 10684 descartado em 23/01/2026 por merge já feito na v26.1.1.1; retrabalho exigido |
| R-05 — Configuração de URLs hardcoded em vez de banco de dados | 1 | 2 | 2 | Mitigar: revisão de código; políticas de arquitetura (RNF-04) | Realizado — jan/2026: URL do HttpClient sendo truncada; Humberto ordenou migração para banco (19/01/2026) |
| R-06 — Sequencial de IDs divergente entre API e banco legado | 2 | 3 | 6 | Mitigar: script de correção; alinhamento com DBA | Realizado — id_cliente gravado com sequencial divergente em 06/11/2025; script de correção aplicado |
| R-07 — Dependência de múltiplos sistemas externos (ITEC, VTEX, Propz, PBM) gerando atrasos de integração | 3 | 2 | 6 | Mitigar: roadmap de integrações com folga; alinhamento com responsáveis de cada sistema | Realizado — Propz atrasou para nov/2025; PBM exigiu reuniões com Interplayers |
| R-08 — Divergência de percepção de responsabilidade pelo atraso entre Timeware e D1000 | 3 | 3 | 9 (reputacional) | Mitigar: status reports semanais documentados; e-mail formal registrando posição da Timeware | Realizado — 09/01/2026: Armando discordou integralmente do status report; Abraão registrou discordância formal por e-mail |

---

## BLOCO 9 — Verificação e Validação (V&V / Testes)

*Alimenta: VV, planilha de gestão — aba V&V*

### Ciclos de execução

| Ciclo / Sprint | Módulo | O que foi testado | Defeitos encontrados | Como foi resolvido | Data |
|---|---|---|---|---|---|
| Sprints 1–3 (CI contínuo) | API Core | Endpoints CRUD básico, health check, outbox pattern, pipeline CI | 0 (S1/S2) | — | Abr–Jun/2025 |
| Sprints 4–7 | Integrações principais | ITEC outbox funcional, VTEX, Call Center, início Propz; 273 testes unitários (cobertura 84%) | 0 (S1/S2) | — | Jun–Ago/2025 |
| Sprints 8–10 | Integrações satélites + carga | PBM, BlueSoft, CloseUp, worker LGPD, carga 7M CPFs | 0 (S1/S2) | — | Ago–Set/2025 |
| Sprints 11–13 (homologação início) | Sistema completo | UAT com D1000; inicio roteiros Julielle Santos; diagnóstico <5% testes em 29/09 | 7 (S3) | Resolvidos na sprint seguinte | Set–Out/2025 |
| Sprints 14–17 (homologação formal) | Sistema completo + Propz CRM | UAT D1000 completo; roteiros formais; Propz CRM (04/12); todas as integrações | 2 (S1), 5 (S2), 7 (S3) | S1 resolvidos em <24h; S2 em <3 dias úteis; S3 na sprint seguinte | Out–Dez/2025 |
| Sprints 18–19 (piloto loja 9) | Produção restrita — loja 9 | Operação real PDV, Balcão, OMNI; regressão; GMUD 2624117 | 0 (S1/S2) em produção | — | Jan/2026 |

### Cenários de teste

---

**Cenário T-CAD-01 — Cadastro de cliente com dados válidos**
- **Módulo:** Cadastro e gerenciamento de clientes (RF-01)
- **Tipo:** Happy
- **Dado que:** o cliente não existe na base e todos os campos obrigatórios estão preenchidos com CPF válido
- **Quando:** uma requisição POST /clientes é enviada com os dados do cliente
- **Então:** a API retorna HTTP 201 com os dados do cliente criado
- **E:** o cliente é persistido no banco de dados PostgreSQL
- **E:** um evento ClienteCriado é registrado no outbox_eventos
- **Evidência:** Azure DevOps pipeline CI — 273 testes passando; validado por Lucas Batista (Sprint 15)
- **Resultado:** Aprovado

---

**Cenário T-CAD-02 — Cadastro com CPF duplicado**
- **Módulo:** Cadastro e gerenciamento de clientes (RF-02)
- **Tipo:** Sad
- **Dado que:** já existe um cliente com o mesmo CPF na base
- **Quando:** uma requisição POST /clientes é enviada com o mesmo CPF
- **Então:** a API retorna HTTP 409 com mensagem de erro descritiva
- **E:** nenhum registro novo é criado no banco de dados
- **Evidência:** xUnit test suite — 273 cenários; validado na pipeline CI
- **Resultado:** Aprovado

---

**Cenário T-CAD-07 — Inativação lógica LGPD**
- **Módulo:** Cadastro e gerenciamento de clientes (RF-05)
- **Tipo:** Happy
- **Dado que:** existe um cliente ativo com o CPF informado
- **Quando:** uma requisição DELETE /clientes/{cpf} é enviada com motivo de inativação
- **Então:** a API retorna HTTP 200
- **E:** o campo ativo é marcado como false no banco de dados
- **E:** motivo e data de inativação são registrados
- **E:** um evento ClienteInativado é inserido no outbox_eventos
- **Evidência:** validado em UAT Sprint 14 — Julielle Santos; log de auditoria verificado
- **Resultado:** Aprovado

---

**Cenário T-ITEC-01 — Cadastro gera evento no outbox**
- **Módulo:** Integração ITEC — outbox pattern (RF-11)
- **Tipo:** Happy
- **Dado que:** o sistema está operacional e o banco de dados está acessível
- **Quando:** um novo cliente é cadastrado via POST /clientes
- **Então:** um registro é criado na tabela outbox_eventos com status pendente (processado_em = null)
- **E:** o worker de integração processa o evento e chama o ITEC com sucesso
- **E:** processado_em é preenchido e tentativas = 1
- **Evidência:** teste de integração com TestContainers (PostgreSQL local); validado na pipeline CI Sprint 7
- **Resultado:** Aprovado

---

**Cenário T-PROD-01 — Performance GET /clientes/{cpf} sob carga**
- **Módulo:** Performance (RNF-07)
- **Tipo:** Happy
- **Dado que:** o sistema está em produção com o banco populado com 7M de CPFs
- **Quando:** 500 requisições/segundo são enviadas para GET /clientes/{cpf}
- **Então:** o percentil 95 de latência é ≤ 200ms
- **E:** não há crash ou degradação de disponibilidade
- **Evidência:** Datadog APM — p95 = 142ms (piloto loja 9, jan/2026)
- **Resultado:** Aprovado (29% abaixo do SLA)

---

---

## BLOCO 10 — Reuniões e acompanhamento

*Alimenta: ATAs, RAC, CR*

### Reuniões realizadas

| Tipo | Data | Participantes (nomes/papéis) | Pautas / Decisões principais |
|---|---|---|---|
| Kickoff / Reunião de design | 17/03/2025 | Tiago, Humberto, Armando, Diego, Marcelo, Alexandre | "Evolução do desenho e material" — escolha de arquitetura cloud-native Azure, CPF como PK; gravado no Fireflies |
| Primeira daily formal | 28/04/2025 | Equipe completa | Início oficial das sprints; formalização do rito diário 11h30 via Teams |
| Alinhamento pré-apresentação | 25/06/2025 | Abraão, Armando, Erick, Tiago, Helena | Preparação urgente para apresentação ao Diretor Marcus Falcão |
| Apresentação formal do plano | 17/07/2025 | Marcus Falcão, Helena, Humberto, Fagner, Rafael, Diego, Tiago, Abraão, Marcus Ribeiro, Armando | Aprovação verbal do plano pelo Diretor de TI; alinhamento executivo |
| Alinhamento técnico 2,5h — integridade de dados | 23/07/2025 | Humberto, Diego, Marcus Ribeiro, Tiago, Abraão, Rafael, Ethierre, Helena, Fagner, Armando | Decisão: CPF como PK única; estratégia de saneamento da base legada (20M registros) |
| Daily de diagnóstico de atraso crítico | 29/09/2025 | Armando, Ethierre, Tiago, Marcelo, Erick, Abraão, Helena, Pedro, Humberto | Diagnóstico: <5% dos testes de homologação executados; definição de plano de aceleração |
| Proposta de infraestrutura produtiva Azure | 03/11/2025 | Time Timeware, Fabio Ruiz, Diego Lacerda, Armando, Marcelo | Apresentação da proposta Azure AKS para produção por David Buena |
| Reuniões de planejamento de piloto | 04–05/11/2025 | Armando, Pedro, Helena, Fagner, Rafael, Tiago, Abraão, Renan, Humberto | Definição do plano de piloto na loja 9; critérios de go/no-go |
| Liberação Propz CRM para testes | 04/12/2025 | Abraão, Helena, Julielle, Armando, Fagner, Raony, Renan, Rafael | Integração Propz CRM concluída; marco contratual atingido; início dos testes Propz |
| E-mail divergência de status | 09/01/2026 | Abraão → Armando | Armando discordou integralmente do status report; Abraão registrou discordância formal |
| Liberação formal para testes | 22/01/2026 | Abraão → Armando, Pedro, Helena | Declaração formal de que responsabilidade Timeware está concluída; bola no campo D1000 |
| Deploy em produção | 26/01/2026 | Fagner → Pedro, Abraão, Armando | Fagner confirma versão 26.1.1.1 disponível no ambiente de produção |
| Últimos PRs / Correções finais | 29/01/2026 | Renan → Cézar, equipe completa | PRs finais com correções de testes solicitadas por D1000; encerramento das atividades Timeware |
| Aceite formal (ATA-PROFARMA01-002) | 29/01/2026 | Humberto Erler + Abraão Oliveira | Aceite formal do projeto; zero defeitos S1/S2 em aberto; piloto loja 9 aprovado |

### Change Requests (se houver mudança de escopo)

| Código | Data | Descrição da mudança | Impacto em prazo/escopo | Aprovado por |
|---|---|---|---|---|
| CR-01 a CR-03 | Abr–Jun/2025 | Refinamentos de requisitos nos sprints 1–3 (critérios de aceite, regras de sanitização, logs de auditoria) | Absorvidos sem impacto de prazo | Armando Junior / Helena Moreira |
| CR-04 | Ago/2025 | Inclusão de integração BlueSoft (RF-15) | +0,5 sprint — Sprints 8–9 | Armando Junior |
| CR-05 | Ago/2025 | Inclusão de integração CloseUp (RF-16) | +0,5 sprint — Sprint 9 | Armando Junior |
| CR-06 | Jun/2025 | Inclusão de worker de expurgo LGPD (RF-17) | +0,5 sprint — Sprint 6–7 | Helena Moreira / Pedro Costa |
| CR-07 | Ago/2025 | Inclusão de integração Propz CRM via Azure Service Bus (RF-14) | +2 sprints — Sprints 13–14 | Pedro Costa |
| CR-08 | Ago/2025 | Saneamento adicional da base legada (volume de duplicidades acima do estimado) | +3 semanas no saneamento | Marcus Ribeiro / Abraão |
| CR-09 a CR-12 | Set–Nov/2025 | Ajustes finos de contrato de API (VTEX, Call Center, PBM), campos de fidelidade/opt-in/opt-out | Absorvidos nos sprints 15–17 sem impacto adicional de prazo | Armando Junior / Julielle Santos |

### Acompanhamento de sprints

| Sprint | Planejado (SP) | Realizado (SP) | Desvio | Observação |
|---|---|---|---|---|
| Sprint 1 | 28 | 28 | 0 | Arquitetura definida; DER v1; ambiente Azure inicial |
| Sprint 2 | 30 | 30 | 0 | DER v2; fluxo ITEC (trigger/outbox); endpoints iniciais |
| Sprint 3 | 30 | 30 | 0 | Regras de sanitização; testes automatizados; acesso Jira liberado |
| Sprint 4 | 32 | 32 | 0 | API Gateway; VTEX no fluxo; PostgreSQL sequencial único |
| Sprint 5 | 30 | 30 | 0 | Preparação apresentação Falcão; desenhos UML |
| Sprint 6 | 32 | 32 | 0 | 16 endpoints; 273 testes unitários; apresentação formal do plano |
| Sprint 7 | 32 | 32 | 0 | Integridade dados CPF como PK; sanitização base legada |
| Sprint 8 | 32 | 30 | −2 | Prometheus/Grafana; documentação endpoints; entrada Cézar |
| Sprint 9 | 28 | 28 | 0 | Ambiente homologação; início carga de clientes |
| Sprint 10 | 30 | 30 | 0 | Carga parcial (1M de 20M); worker de expurgo aprovado |
| Sprint 11 | 28 | 28 | 0 | Datadog; mapping cenários de teste |
| Sprint 12 | 28 | 25 | −3 | Início homologação (<5% em 29/09); status reports iniciados |
| Sprint 13 | 28 | 25 | −3 | Bloqueio banco QA 14–21/10; retomada após desbloqueio |
| Sprint 14 | 28 | 28 | 0 | Plano de piloto; proposta infra Azure; bug id_cliente sequencial |
| Sprint 15 | 32 | 32 | 0 | Consolidação tickets; Propz CRM iniciado |
| Sprint 16 | 35 | 42 | +7 | Propz CRM concluído e disponível (04/12); pico de velocity |
| Sprint 17 | 32 | 32 | 0 | Versão 25.12.1.1; campos fidelidade/opt-in/opt-out |
| Sprint 18 | 28 | 28 | 0 | Daily criada por Armando (06/01); ajuste URL HttpClient |
| Sprint 19 | 30 | 28 | −2 | GMUD 2624117 (21/01); PRs finais; aceite formal (29/01) |
| **Total** | **573** | **564** | **−9 (−1,6%)** | Desvio marginal; dentro do tolerável |

---

## BLOCO 11 — GQA (Garantia da Qualidade)

*Alimenta: GQA*

| Marco auditado | Data | Auditor | Itens verificados | Desvios encontrados | % Conformidade |
|---|---|---|---|---|---|
| GQA-P01 — Aderência ao processo (Sprints 1–5) | 20/06/2025 | COO (Operações Timeware) | Plano documentado; requisitos antes da implementação; revisão de código; pipeline CI; rastreabilidade histórias; registro de riscos; Sprint Review com cliente | NC-01 (requisitos retroativos Sprints 1–3) + NC-02 (rastreabilidade Jira ausente Sprints 1–3) | 71% (5/7 itens conformes) — NCs resolvidas até 30/06/2025 |
| GQA-P02 — Processo de V&V e homologação | 10/10/2025 | COO (Operações Timeware) | VV documentado; roteiros de teste aprovados; defeitos registrados e classificados; SLA de correção cumprido; aceites parciais documentados; change requests formalizados; ICs controlados (GCO-1/2/3) | Nenhum | 100% |
| GQA-P03 — Encerramento do projeto | 05/06/2026 | COO (Operações Timeware) | Completude dos artefatos de encerramento; conformidade com processo GPR; TAE, LI, MED, GQA completos | Nenhum | 100% |

---

## BLOCO 12 — Medição (KPIs)

*Alimenta: MED*

> Preencha o que foi medido. Baseline e meta vêm do PLA-MED-001.

| Código | Indicador | Resultado medido |
|---|---|---|
| M1 | % Entregas no prazo | 100% dentro do prazo revisado (após absorção dos 12 CRs); desvio de 4 meses vs. plano original explicado integralmente por CRs aprovados e bloqueios de infra externos |
| M2 | Desvio de esforço (%) | SPI = 0,91; desvio de prazo de +4 meses vs. baseline original; dentro do aceitável dado o aumento de escopo formal |
| M3 | Story points entregues vs. planejados | 564 SP entregues / 573 SP planejados = −9 SP (−1,6%) |
| M4 | Velocity média realizada | ~30 SP/sprint (pico: 42 SP no Sprint 16) |
| M5 | Taxa de defeitos em homologação | 14 defeitos no total (2 S1, 5 S2, 7 S3); 100% resolvidos antes do aceite |
| M6 | Defeitos escapados para produção | 0 incidentes S1 no piloto (loja 9) |
| M7 | % Requisitos com rastreabilidade completa | 100% (RF-01 a RF-19 e RNF-01 a RNF-14 rastreados em RASTR-PROFARMA01-001) |
| M8 | % Conformidade GQA | GQA-P01: 71% (NCs menores, resolvidas); GQA-P02: 100%; GQA-P03: 100% — conformidade crescente ao longo do projeto |
| M9 | NPS do cliente / satisfação | Aceite formal sem ressalvas por Humberto Erler (29/01/2026); 0 incidentes S1 no piloto; latência p95 = 142ms (29% abaixo do SLA) — indicadores indiretos de satisfação |

---

## BLOCO 13 — Encerramento

*Alimenta: TAE, LI*

| Campo | Valor |
|---|---|
| **\* Data do aceite formal** | 29/01/2026 |
| **\* Forma do aceite** | ATA-PROFARMA01-002 — reunião formal e e-mail de confirmação por Humberto Erler (Gerente de TI Rede D1000) |
| **\* Quem concedeu o aceite** | Humberto Erler (Gerente de TI — Rede D1000); confirmação adicional de Pedro Alves da Costa Junior (Patrocinador — e-mail 23/01/2026) |
| **Entregas finais** | API de Cadastro de Clientes (.NET 8 / Clean Architecture) em produção; 16 endpoints REST documentados (Swagger); 273 testes unitários (cobertura 84%); 7 integrações: ITEC (outbox), VTEX, Call Center, Propz CRM, PBM/Interplayers, BlueSoft, CloseUp; worker de expurgo LGPD; carga inicial de ~7M CPFs saneados; deploy AKS configurado; pipelines CI/CD; Datadog configurado; piloto na loja 9 (PDV, Balcão, OMNI) operacional; documentação técnica completa (PCP, ITP, VV, GCO, GDE) |
| **O projeto foi encerrado conforme planejado?** | Sim, conforme o plano revisado. O prazo original (set/2025) foi formalmente revisado para jan/2026 após absorção de 12 change requests aprovados pelo cliente e bloqueios de infraestrutura externos à Timeware. O encerramento em 29/01/2026 foi dentro do prazo revisado e acordado. |

### Lições aprendidas

| Categoria | O que funcionou bem | O que melhorar |
|---|---|---|
| Processo / gestão | Status reports semanais (out–nov/2025) garantiram transparência e registro formal da posição da Timeware; formalização de change requests evitou escopo aberto | Estabelecer SLA formal do cliente para aplicação de merges e atualizações de ambiente desde o início; incluir no contrato cláusula de responsabilidade por atrasos de ambiente |
| Técnico | Arquitetura Clean Architecture + outbox pattern se provou robusta — zero incidentes S1 em produção; Datadog configurado desde sprint 11 permitiu diagnóstico rápido de performance; cobertura 84% dos testes unitários garantiu confiabilidade | Git Flow mais rígido para evitar conflitos de branches (incidente PR 10684, jan/2026); política de "URLs em banco de dados" deveria ser verificada em code review desde o início (RNF-04) |
| Comunicação com o cliente | Dailys às 11h30 via Teams mantiveram cadência de alinhamento; Sprint Reviews com Helena e Armando geraram aceites contínuos; e-mail formal de 22/01/2026 protegeu a Timeware de disputas sobre responsabilidade | Escalação ao sponsor (Pedro Costa) deveria ser acionada mais cedo quando bloqueios de ambiente ultrapassam 5 dias úteis; divergência de 09/01/2026 com Armando indicou que status report precisava ter KPIs numéricos visíveis para o cliente |
| Estimativas | Velocity de ~30 SP/sprint foi consistente e previsível após calibração no Sprint 3; desvio final de −1,6% em SP demonstra maturidade de estimativa | Escopo de integração com sistemas satélites (BlueSoft, CloseUp, Propz) foi subestimado na baseline; incluir reserva de 20% para integrações com sistemas de terceiros em projetos similares |
| Outros | Saneamento da base legada (7M CPFs) concluído com sucesso; zero dados perdidos no outbox; piloto loja 9 encerrado sem incidentes críticos | Plano de saneamento de base legada deve ser detalhado e validado com DBA do cliente antes do início dos sprints; volume de duplicidades foi 30% acima do estimado |

---

## Checklist antes de entregar este formulário

- [x] Todos os campos **\*** preenchidos
- [x] Pelo menos 1 requisito funcional listado (Bloco 3) — 19 RF + 14 RNF listados
- [x] Pelo menos 1 cenário de teste descrito (Bloco 9) — 5 cenários detalhados
- [x] Datas de início e encerramento confirmadas (Bloco 1)
- [x] Auditor GQA identificado e diferente da equipe do projeto (Bloco 2) — COO (Operações Timeware)
- [x] Aceite formal documentado (Bloco 13) — ATA-PROFARMA01-002, 29/01/2026

---

## Documentos gerados a partir deste formulário

| Documento | Blocos usados |
|---|---|
| TAP — Termo de Abertura | 1, 2 |
| PLA — Plano de Projeto | 1, 2, 3, 4, 5, 6, 8 |
| ADAP — Registro de Adaptação | 4 |
| REQ — Documento de Requisitos | 3 |
| PCP — Documento de Design | 6, 7 |
| ITP — Estratégia de Integração | 6, 7 |
| VV — Plano de V&V | 9 |
| GCO — Registro de Configuração | 6 |
| GDE — Registro de Decisão | 7 |
| GQA — Registro de GQA | 11 |
| MED — Registro de Medição | 12 |
| RASTR — Matriz de Rastreabilidade | 3, 9 |
| ATAs | 10 |
| CR — Change Request | 10 |
| RAC — Relatório de Acompanhamento | 5, 10 |
| TAE — Termo de Encerramento | 13 |
| LI — Lições Aprendidas | 13 |
| Planilha de Gestão (Excel) | todos |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Time de Melhoria Contínua | Versão inicial |
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Preenchimento completo com dados do projeto PROFARMA01 — Cadastro de Clientes — Rede D1000; todos os 13 blocos preenchidos com base nos documentos TAP, PLA, REQ, GQA, VV, MED e TAE do projeto |
