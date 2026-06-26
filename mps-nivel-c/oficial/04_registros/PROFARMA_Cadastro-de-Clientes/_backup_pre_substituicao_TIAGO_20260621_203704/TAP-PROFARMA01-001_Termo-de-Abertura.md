# Termo de Abertura do Projeto — Rede D1000 · Cadastro de Clientes

| Campo | Valor |
|---|---|
| **Documento** | TAP-PROFARMA01-001 |
| **Projeto** | Cadastro de Clientes — Rede D1000 |
| **Cliente** | Profarma S.A. / Rede D1000 |
| **Contrato** | Squad D1000 Loja — alocação de 3 Dev Pleno |
| **Versão** | 1.0 |
| **Data de abertura** | 17/03/2025 |
| **Gerente de Projeto** | Abraão Oliveira |

---

## 1. Objetivo do projeto

Desenvolver o novo sistema de Cadastro de Clientes da Rede D1000, substituindo a base legada do ITEC por uma solução cloud-native na Microsoft Azure. O sistema unifica o cadastro em uma base única e confiável, com CPF como chave primária, eliminando duplicidades históricas entre as bandeiras da rede e garantindo integridade para todos os canais de atendimento: PDV, Balcão, Call Center e OMNI (VTEX). A solução expõe 16 endpoints de API RESTful com cobertura de 273 testes unitários e integra-se aos sistemas satélites da Rede (ITEC, BlueSoft, CloseUp, Propz CRM, PBM/Interplayers).

## 2. Escopo macro

- **Incluído:**
  - API de Cadastro de Clientes em .NET com Clean Architecture e PostgreSQL (Azure)
  - Integração com ITEC (trigger/outbox), VTEX, Call Center, PBM, BlueSoft, CloseUp e Propz CRM
  - Endpoints de cadastro, consulta, atualização e inativação (LGPD)
  - Carga inicial de base (~7 milhões de CPFs saneados) e worker de expurgo de dados
  - Deploy em ambiente Azure (AKS), monitoramento via Datadog, pipelines CI/CD no Azure DevOps
  - Testes unitários (273 cenários) e suporte à execução de testes de homologação
  - Piloto na loja 9 cobrindo PDV, Balcão e OMNI

- **Não incluído:**
  - Modernização dos aplicativos D1000 Express e Connect D1000 (escopo separado)
  - Desenvolvimento de novos módulos do ITEC legado
  - Sustentação pós-piloto (objeto de contrato futuro)

## 3. Partes interessadas

| Parte interessada | Papel | Contato |
|---|---|---|
| Pedro Alves da Costa Junior | Patrocinador do projeto — Rede D1000 | pedro.costa@reded1000.com.br |
| Marcus Falcão | Diretor de TI — Profarma | marcus.falcao@profarma.com.br |
| Armando Pereira Reis Junior | Tech Lead / Gestor de TI — Rede D1000 | armando.junior@reded1000.com.br |
| Humberto Erler | Gerente de TI — Rede D1000 | humberto.erler@reded1000.com.br |
| Marcelo Rezende | Representante técnico — Profarma | marcelo.rezende@profarma.com.br |
| Helena Moreira | Coordenadora de projeto — Rede D1000 | helena.moreira@reded1000.com.br |
| Ethierre Leite | Especialista de negócio — Rede D1000 | ethierre.leite@reded1000.com.br |
| Alexandre Henrique | Arquiteto/Dev — Rede D1000 | alexandre.henrique@reded1000.com.br |
| Rafael Nader | Técnico — Rede D1000 | rafael.nader@reded1000.com.br |
| Fagner Pereira | Operações/Deploy — Rede D1000 | Fagner.Pereira@reded1000.com.br |
| Julielle Santos | QA/Testes — Rede D1000 | julielle.santos@reded1000.com.br |
| Marcus Ribeiro | DBA — Profarma | marcus.ribeiro@profarma.com.br |
| Diego Lacerda | Arquitetura — Profarma | diego.lacerda@profarma.com.br |

## 4. Equipe do projeto (Timeware)

| Papel | Responsável |
|---|---|
| Gerente de Projeto / Account Manager | Abraão Oliveira |
| Tech Lead | Tiago Barbosa Nascimento |
| Dev Principal / Arquiteto da solução | Erick Coelho |
| Dev Backend | Gustavo Mathias |
| Dev Backend | Renan Kiyoshi |
| Dev Backend | Cézar Hiraki Velázquez |
| Dev Backend | João Cruz |
| Infra / DevOps | David Buena |
| QA / Testes automatizados | Lucas Batista |

## 5. Macroplanejamento (datas-alvo)

| Marco | Data |
|---|---|
| Início do projeto / primeiras reuniões de design | 17/03/2025 |
| Início das dailys e sprints de desenvolvimento | 28/04/2025 |
| Apresentação do plano ao Diretor (Marcus Falcão) | 25/06/2025 |
| Apresentação formal do plano de projeto | 17/07/2025 |
| Início da fase de testes de homologação | Setembro/2025 |
| Proposta de infraestrutura produtiva | 03/11/2025 |
| Integração Propz CRM concluída e disponível para testes | 04/12/2025 |
| Liberação formal para testes de homologação | 22/01/2026 |
| Correções finais e última rodada de PRs | 27–29/01/2026 |

## 6. Premissas e restrições iniciais

**Premissas:**
- A Rede D1000 disponibiliza acessos aos ambientes Azure (DevOps, homologação, produção) para a equipe Timeware
- Os sistemas legados (ITEC, DemoSuite, loja-backend) permitem integração via trigger/outbox
- A base de dados legada (~20 milhões de registros) será saneada com apoio do DBA da Profarma
- O Datadog será licenciado e configurado para monitoramento do ambiente

**Restrições:**
- Escopo contratado: 3 recursos Dev Pleno (alocação mensalizada)
- URLs e configurações de ambiente devem ser armazenadas em banco de dados (não hardcoded)
- Mudanças arquiteturais significativas requerem aprovação do Tech Lead D1000 (Armando Junior)
- Piloto restrito à loja 9 antes do rollout geral

---

## Registro de abertura

| Kickoff realizado em | Ref. de autorização |
|---|---|
| 17/03/2025 | Reunião "Cadastro de Clientes - Evolução do desenho e material" — 17/03/2025 — Fireflies transcript |
| 28/04/2025 | Início formal das dailys do projeto (Daily - Projeto cadastro de clientes — Teams) |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Time de Melhoria Contínua | Versão inicial — reconstituída com base em e-mails e transcrições Fireflies do período 03/2025–01/2026 |
