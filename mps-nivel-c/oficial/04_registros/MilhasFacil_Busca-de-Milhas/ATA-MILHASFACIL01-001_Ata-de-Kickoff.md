# Ata de Reunião — Kickoff do Projeto · MilhasFacil · Busca de Milhas

| Campo | Valor |
|---|---|
| **Documento** | ATA-MILHASFACIL01-001 |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Código do projeto** | MILHASFACIL01 |
| **Cliente** | Hub de Milhas |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Reunião** | Kickoff — Início formal das dailys e sprints de desenvolvimento |
| **Data** | 09/02/2026 |
| **Horário** | 09h00 – 11h00 |
| **Canal** | Microsoft Teams |
| **Facilitador** | Abraão (Timeware) |
| **Gerente de Projeto** | Abraão |
| **Versão** | 1.1 |

---

## 1. Participantes

| Nome | Empresa | Papel |
|---|---|---|
| Abraão | Timeware | Gerente de Projeto / Facilitador (gestão; não codifica) |
| Cézar Velazquez | Timeware | Tech Lead / Arquiteto / DevOps (revisor de PR) |
| Felipe Santos | Timeware | Dev Backend Principal (API + crawlers) |
| Lucas Batista | Timeware | Full Stack |
| Henry Oliveira | Timeware | Full Stack |
| Jonathan Alves | Timeware | QA (teste manual) |
| Carol (Caroline) | Timeware | GQA independente (auditoria de processo) |
| PO Hub de Milhas | Hub de Milhas | Product Owner |

---

## 2. Pauta

1. Apresentação da equipe Timeware ao Hub de Milhas
2. Revisão do escopo e dos objetivos do produto
3. Definição da arquitetura macro da solução (API · Web · Crawler)
4. Cadência de trabalho: dailys, sprints e cerimônias
5. Gestão de acessos: Azure DevOps, repositórios e ambientes
6. Definição da política de branch, rastreabilidade e gate de CI
7. Próximos passos e ações imediatas

---

## 3. Resumo das discussões

### 3.1 Apresentação da equipe e alinhamento de papéis

A Timeware apresentou a equipe ao Hub de Milhas. Ficou estabelecido que Abraão atuaria como Gerente de Projeto (sem codificar e fora do DevOps), ponto de gestão e aprovador do escopo/change request; Cézar Velazquez como Tech Lead / Arquiteto / DevOps, responsável pela arquitetura, pela infraestrutura/pipeline e pela aprovação de todos os PRs (revisor de PR); Felipe Santos como Dev Backend Principal (API e crawlers); Lucas Batista e Henry Oliveira como desenvolvedores Full Stack; Jonathan Alves como QA, executando os testes de forma manual e gerando as evidências; e Carol (Caroline) como GQA independente, responsável pela auditoria de processo (sem codificar e fora do DevOps). Ficou distinta a função de QA (Jonathan, que executa os testes) da função de GQA (Carol, que audita o processo). O PO do Hub de Milhas seria o ponto de negócio e priorização do backlog.

### 3.2 Revisão do escopo e objetivo do produto

Abraão e Cézar Velazquez apresentaram o objetivo do produto: uma plataforma de busca e alerta de passagens aéreas por milhas que consulta em paralelo os programas Smiles, Azul e Latam, registra o histórico de buscas do usuário e dispara alertas automáticos quando rotas favoritas atingem o preço-alvo em milhas. O Hub de Milhas confirmou a necessidade de eliminar a consulta manual em portais distintos, hoje feita programa a programa, e reforçou a importância do tempo de resposta da busca (meta de até 30 s; média alvo bem inferior) e da notificação proativa por WhatsApp.

### 3.3 Arquitetura macro

A arquitetura proposta, conduzida por Cézar Velazquez (Tech Lead / Arquiteto), foi composta por três aplicações integradas:
- **API REST** em Spring Boot 3.2.5 / Java 21, base `/api/v1`, autenticação JWT HS256 stateless, persistência PostgreSQL com migrations Flyway e blacklist de token em Redis
- **Front-end Web** em Angular 17.3 standalone com Tailwind 3.4 (rotas `/login`, `/register`, `/search`, `/history`, `/preferences`)
- **Crawler** em FastAPI 0.111 / SeleniumBase 4.27.4 com parsers Smiles/Azul/Latam, exposto à API com CORS restrito

A integração de alertas por WhatsApp seria feita via Z-API, com a falha de envio não interrompendo o fluxo principal. A orquestração local de desenvolvimento seria feita com Docker Compose.

### 3.4 Escopo macro (requisitos funcionais)

O escopo macro acordado abrange os requisitos RF01 a RF15:

| RF | Descrição | Sprint prevista |
|---|---|---|
| RF01 | Cadastro de usuário com senha BCrypt | S1 |
| RF02 | Login JWT (access + refresh) | S1 |
| RF03 | Busca paralela Smiles/Azul/Latam | S2–S3 |
| RF04 | SearchPage (skeleton da busca) | S2 |
| RF05 | Histórico de buscas paginado | S3 |
| RF06 | Rotas favoritas e alertas | S3–S4 |
| RF07 | Perfil GET/PATCH `/users/me` | S4 |
| RF08 | Alertas via Spring Scheduler | S4 |
| RF09 | Notificação WhatsApp (Z-API) | S7 |
| RF10 | Assinaturas BASIC/PRO/ENTERPRISE | S5 |
| RF11 | Refresh token rotation | S5 |
| RF12 | Logout com blacklist Redis (jti) | S8 |
| RF13 | Filtros avançados (maxMiles / cabinType) | S9 |
| RF14 | Export CSV UTF-8 BOM | S8–S9 |
| RF15 | Push PWA | S10 |

### 3.5 Cadência de trabalho

Ficou estabelecida a seguinte cadência:
- **Daily:** todos os dias úteis via Microsoft Teams (canal dedicado ao projeto)
- **Sprint:** 2 semanas; o primeiro sprint (S1) iniciaria em 09/02/2026, com término previsto do projeto em 26/07/2026 (12 sprints)
- **Sprint Planning / Review / Retrospectiva:** ao início e ao fechamento de cada sprint
- **Relatório de status:** periódico, de Abraão (GP) para o PO do Hub de Milhas

### 3.6 Gestão de acessos, política de branch e CI

Cézar Velazquez (Tech Lead / DevOps) ficou responsável por provisionar os acessos no Azure DevOps e configurar os três repositórios (`MilhasFacil_api`, `MilhasFacil_web`, `MilhasFacil_crawler`, branch padrão `main`) e as pipelines (PowerShell@2, agente Windows, triggers `develop`/`homolog`/`main`). Acordou-se a política de branch com PR obrigatório para `develop`, aprovação do PR pelo Tech Lead (Cézar Velazquez), gate de CI e nomes de branch no padrão `feat/fix + MF-XX`. As mudanças de escopo (CR) seriam aprovadas pelo GP (Abraão). A meta de cobertura de testes foi fixada em ≥ 80% (JaCoCo/Karma/pytest), com gate de cobertura no CI a partir da S4.

---

## 4. Decisões tomadas

| # | Decisão | Responsável | Data-limite |
|---|---|---|---|
| D-01 | Arquitetura em três aplicações: API Spring Boot, Web Angular e Crawler FastAPI/SeleniumBase | Cézar Velazquez (Timeware) | Confirmado no kickoff |
| D-02 | Autenticação JWT HS256 stateless (access 30 min / refresh 7 dias) com blacklist Redis | Felipe Santos (Timeware) | S1 |
| D-03 | Busca paralela das três companhias (Smiles/Azul/Latam) via crawler, meta ≤ 30 s | Felipe Santos (Timeware) | S2–S3 |
| D-04 | Sprints de 2 semanas, com S1 iniciando em 09/02/2026 e término previsto em 26/07/2026 | Abraão (Timeware) | Imediato (09/02/2026) |
| D-05 | Política de branch: PR obrigatório para `develop`, aprovação do PR pelo Tech Lead (Cézar) e gate de CI | Cézar Velazquez (Timeware) | Vigente durante todo o projeto |
| D-06 | Meta de cobertura ≥ 80% com gate de cobertura no CI a partir da S4 | Cézar Velazquez (Timeware) | S4 |
| D-07 | Notificação por WhatsApp via Z-API, com falha de envio não interrompendo o fluxo | Felipe Santos (Timeware) | S7 |
| D-08 | Mudanças de escopo formalizadas via change request com aprovação do GP (Abraão) antes da implementação | Abraão (Timeware) | Vigente durante todo o projeto |

---

## 5. Ações imediatas

| Ação | Responsável | Prazo |
|---|---|---|
| Provisionar acessos e criar os três repositórios no Azure DevOps | Cézar Velazquez (Timeware) | 11/02/2026 |
| Configurar pipelines API/Web/Crawler (PowerShell@2, agente Windows) | Cézar Velazquez (Timeware) | 13/02/2026 |
| Criar canal Microsoft Teams dedicado e rotina de daily | Abraão (Timeware) | 09/02/2026 (neste dia) |
| Detalhar o backlog inicial (RF01–RF15) no Jira (board 614) | Abraão + PO Hub de Milhas | 11/02/2026 |
| Definir ambiente de desenvolvimento local (Docker Compose) | Cézar Velazquez (Timeware) | 11/02/2026 |
| Apresentar o primeiro Sprint Planning (S1) | Abraão | 09/02/2026 |

---

## 6. Próximos passos

- Sprint 1 (S1) iniciado em 09/02/2026: cadastro com BCrypt (RF01) e login JWT access+refresh (RF02)
- Próxima cerimônia formal: Sprint Review do S1 ao fim do período de 09–22/02/2026
- Daily diária via Microsoft Teams a partir de 10/02/2026

### Evidências referenciadas

| Código | O que capturar | Fonte/URL |
|---|---|---|
| IMG-JIRA-01 | Board 614 com backlog inicial RF01–RF15 e sprint S1 | Jira — board 614 |
| IMG-DEVOPS-01 | Criação dos repositórios MilhasFacil_api/web/crawler | Azure DevOps — Repos |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Emissão inicial — evidência do ciclo S1–S9 (MR-MPS-SW:2024 Nível C). |
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Correção do nome do plano de assinatura no RF10 (PREMIUM → PRO), alinhando ao enum real do código e ao REQ/PCP. |
