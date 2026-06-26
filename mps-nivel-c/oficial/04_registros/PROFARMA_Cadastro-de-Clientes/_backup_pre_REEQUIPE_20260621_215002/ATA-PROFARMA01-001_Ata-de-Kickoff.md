# Ata de Reunião — Kickoff do Projeto · Rede D1000 · Cadastro de Clientes

| Campo | Valor |
|---|---|
| **Documento** | ATA-PROFARMA01-001 |
| **Projeto** | Cadastro de Clientes — Rede D1000 |
| **Reunião** | Kickoff — Início formal das dailys e sprints de desenvolvimento |
| **Data** | 28/04/2025 |
| **Horário** | 09h00 – 11h00 |
| **Canal** | Microsoft Teams |
| **Facilitador** | Abraão Oliveira (Timeware) |
| **Versão** | 1.0 |

---

## 1. Participantes

| Nome | Empresa | Papel |
|---|---|---|
| Abraão Oliveira | Timeware | Gerente de Projeto / Facilitador |
| Cézar Hiraki Velázquez | Timeware | Tech Lead |
| Erick Coelho | Timeware | Dev Principal / Arquiteto |
| Gustavo Mathias | Timeware | Dev Backend |
| Renan Kiyoshi | Timeware | Dev Backend |
| João Cruz | Timeware | Dev Backend |
| David Buena | Timeware | Infra / DevOps |
| Lucas Batista | Timeware | QA / Testes automatizados |
| Armando Pereira Reis Junior | Rede D1000 | Tech Lead / Gestor de TI |
| Humberto Erler | Rede D1000 | Gerente de TI |
| Helena Moreira | Rede D1000 | Coordenadora de Projeto |
| Ethierre Leite | Rede D1000 | Especialista de Negócio |
| Julielle Santos | Rede D1000 | QA / Testes |
| Alexandre Henrique | Rede D1000 | Arquiteto / Dev |
| Rafael Nader | Rede D1000 | Técnico |
| Fagner Pereira | Rede D1000 | Operações / Deploy |

---

## 2. Pauta

1. Apresentação da equipe Timeware ao time D1000
2. Revisão do escopo e objetivos do projeto
3. Definição da arquitetura macro da solução
4. Cadência de trabalho: dailys, sprints e cerimônias
5. Gestão de acessos: Azure DevOps, ambientes, repositórios
6. Alinhamentos sobre o legado ITEC e o processo de saneamento da base
7. Próximos passos e ações imediatas

---

## 3. Resumo das discussões

### 3.1 Apresentação da equipe e alinhamento de papéis

A Timeware apresentou a equipe completa ao time D1000. Ficou estabelecido que Cézar Hiraki Velázquez (Timeware) e Armando Junior (D1000) seriam os pontos técnicos primários de cada lado, com Abraão Oliveira como ponto de gestão e Helena Moreira como coordenadora D1000. Humberto Erler participaria das reuniões executivas de status.

### 3.2 Revisão do escopo e objetivo

Abraão Oliveira apresentou o escopo acordado: API de Cadastro de Clientes em .NET com Clean Architecture, banco PostgreSQL no Azure, substituindo a base legada do ITEC. A equipe D1000 confirmou os objetivos e reforçou a criticidade de eliminar duplicatas históricas de CPF — problema sistêmico identificado como causa raiz de inconsistências nos canais PDV, Balcão e OMNI.

Ethierre Leite (especialista de negócio D1000) apresentou as regras de negócio críticas: o CPF deve ser a chave primária única e todo cadastro deve ser validado pela Receita Federal antes da persistência.

### 3.3 Arquitetura macro

Erick Coelho apresentou a proposta de arquitetura:
- Clean Architecture em .NET 8
- PostgreSQL (Azure Database for PostgreSQL) como banco principal
- AKS para orquestração de containers
- Outbox pattern para integração assíncrona com o ITEC
- API Gateway como ponto de entrada único

Armando Junior validou a arquitetura e levantou a necessidade de acesso à VNet do AKS. Ficou acordado que os acessos seriam providenciados por Fagner Pereira em até 3 dias úteis.

### 3.4 Cadência de trabalho

Ficou estabelecida a seguinte cadência:
- **Daily:** todos os dias úteis às 09h30 via Microsoft Teams (canal dedicado ao projeto)
- **Sprint:** 2 semanas; primeiro sprint iniciaria em 28/04/2025
- **Sprint Review/Retrospectiva:** sexta-feira da semana de fechamento de sprint, 14h00–16h00
- **Sprint Planning:** segunda-feira de abertura de sprint, 09h00–11h00
- **Relatório de status:** toda sexta-feira, Abraão Oliveira para Helena Moreira e Humberto Erler

### 3.5 Gestão de acessos

Rafael Nader ficou responsável pela criação dos acessos no Azure DevOps para a equipe Timeware (repositórios `loja-balcao-frontend` e `loja-backend` em `profarma.visualstudio.com/rede-d1000/`). David Buena (Infra/DevOps Timeware) ficou responsável por receber e validar os acessos.

### 3.6 Legado ITEC e saneamento da base

Alexandre Henrique apresentou a estrutura atual do ITEC: sistema Delphi com banco SQL Server, ~20 milhões de registros históricos com duplicatas por CPF estimadas em ~15% da base. O DBA Marcus Ribeiro (Profarma) conduziria o saneamento com apoio do time Timeware para geração de scripts. A carga inicial planejada é de ~7 milhões de CPFs saneados.

Ficou acordado que o time Timeware não teria acesso direto ao banco de dados de produção do ITEC — toda extração seria realizada pelo time D1000 e entregue em formato CSV para importação.

---

## 4. Decisões tomadas

| # | Decisão | Responsável | Data-limite |
|---|---|---|---|
| D-01 | CPF como chave primária única no novo sistema (sem campo ID interno alternativo como PK exposta) | Erick Coelho (Timeware) + Armando Junior (D1000) | Implementado no Sprint 1 |
| D-02 | Banco de dados PostgreSQL no Azure (não SQL Server) | Cézar Hiraki Velázquez (Timeware) | Confirmado no kickoff |
| D-03 | Outbox pattern para integração com ITEC (não chamada síncrona) | Erick Coelho | Sprint 3 |
| D-04 | Sprint de 2 semanas com dailys às 09h30 via Teams | Abraão Oliveira | Imediato (28/04/2025) |
| D-05 | Acesso ao Azure DevOps concedido em até 3 dias úteis | Fagner Pereira (D1000) | 01/05/2025 |
| D-06 | Time Timeware não terá acesso direto ao banco ITEC produtivo | Armando Junior / Humberto Erler (D1000) | Vigente durante todo o projeto |
| D-07 | Validação de CPF na Receita Federal como pré-requisito de cadastro | Ethierre Leite (D1000) | Sprint 2 |
| D-08 | Mudanças arquiteturais precisam da aprovação de Armando Junior (D1000) antes da implementação | Cézar Hiraki Velázquez (Timeware) | Vigente durante todo o projeto |

---

## 5. Ações imediatas

| Ação | Responsável | Prazo |
|---|---|---|
| Providenciar acessos ao Azure DevOps para a equipe Timeware | Fagner Pereira / Rafael Nader (D1000) | 01/05/2025 |
| Criar canal Microsoft Teams dedicado para o projeto | Helena Moreira (D1000) | 29/04/2025 |
| Compartilhar documentação do ITEC (schema do banco, endpoints existentes) | Alexandre Henrique (D1000) | 02/05/2025 |
| Iniciar levantamento detalhado dos campos de cadastro obrigatórios vs. opcionais | Ethierre Leite (D1000) + Erick Coelho (Timeware) | 05/05/2025 |
| Definir ambiente de desenvolvimento local (Docker Compose) para o time Timeware | David Buena (Timeware) | 30/04/2025 |
| Estabelecer rotina de daily no Teams | Abraão Oliveira | 28/04/2025 (neste dia) |
| Apresentar primeiro Sprint Planning em 28/04/2025 | Cézar Hiraki Velázquez / Erick Coelho | 28/04/2025 |
| Confirmar disponibilidade do DBA Marcus Ribeiro para apoio no saneamento | Abraão Oliveira → Marcelo Rezende (Profarma) | 02/05/2025 |

---

## 6. Próximos passos

- Sprint 1 iniciado em 28/04/2025: implementação dos endpoints básicos de cadastro e consulta de cliente (RF-01 a RF-03, RF-18)
- Próxima reunião formal: Sprint Review do Sprint 1 — 09/05/2025 às 14h00 via Teams
- Daily diária: a partir de 29/04/2025 às 09h30

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Time de Melhoria Contínua | Versão inicial — reconstituída com base em transcrições Fireflies e registros do período 04/2025 |
