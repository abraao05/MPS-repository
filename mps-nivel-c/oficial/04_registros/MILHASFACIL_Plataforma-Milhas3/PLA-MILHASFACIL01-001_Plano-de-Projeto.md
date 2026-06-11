# Plano de Projeto — Milhas3 · Plataforma de Busca e Monitoramento de Milhas

| Campo | Valor |
|---|---|
| **Documento** | PLA-MILHASFACIL01-001 — Plano de Projeto |
| **Versão** | 1.0 |
| **Data** | 16/05/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Milhas3 — Plataforma de Busca e Monitoramento de Milhas |
| **Cliente** | Hub de Milhas (Felipe) |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR — Gerência de Projeto |

---

## 1. Identificação e objetivo (GPR 1)

A plataforma Milhas3 resolve a falta de visibilidade e o esforço manual envolvido na busca de passagens aéreas em programas de milhagem. O produto centraliza o rastreamento automático de disponibilidade em LATAM Pass, Smiles (GOL), TudoAzul (Azul), TAP Miles&Go e Iberia Plus, oferecendo ao usuário final um ponto único de busca, monitoramento de rotas e alertas proativos.

**Referência:** TAP-MILHASFACIL01-001

## 2. Escopo (GPR 1)

### 2.1 Incluído

Requisitos funcionais RF-01 a RF-16 conforme REQ-MILHASFACIL01-001:

- Cadastro e autenticação de usuários (JWT)
- Busca de voos em milhas consolidada (5 programas simultâneos)
- Motor de rastreamento automatizado via Selenium (headless Chrome + bypass Akamai)
- Assinatura de rotas e alertas automáticos
- Histórico de buscas e preferências de rotas
- Sistema de notificações (in-app, e-mail)
- Chat / suporte integrado

### 2.2 Não incluído

- Aplicativos móveis (iOS / Android)
- Compra ou reserva de passagens dentro da plataforma
- Integração com programas além dos cinco definidos
- Programas de pontos de cartões de crédito

## 3. Adaptação do processo (GPR 2)

Referência: ADAP-MILHASFACIL01-001

| Elemento | Decisão |
|---|---|
| Design UX/UI | Aplicável — protótipos Angular validados com cliente antes do desenvolvimento de cada módulo |
| Estratégia de integração | Aplicável — integrações por scraping Selenium com 5 programas de fidelidade (ver ITP-MILHASFACIL01-001) |
| Nível de documentação | Padrão (projeto de médio porte, escopo bem delimitado) |
| Combinação de papéis | Abraão Oliveira (GP + PO); Igor Santana (UX + Analista de Negócio) |
| Cadência de entrega | Incremental — Sprint Reviews quinzenais com cliente |
| Ambiente de staging | VM Linux — branch de homologação isolado por variáveis de ambiente |

## 4. Estimativas (GPR 3, GPR 4)

| Parâmetro | Valor |
|---|---|
| Tamanho estimado | ~650 story points |
| Velocidade de referência | ~50 SP/sprint (4 desenvolvedores, sprints de 2 semanas) |
| Número de sprints | 13 sprints de desenvolvimento + 1 sprint de setup (Sprint 0) |
| Prazo total | 26 semanas (16/05/2025 – 16/11/2025) |
| Base histórica | Projetos Timeware de plataformas web com integração externa (referência interna) |

## 5. Cronograma e marcos (GPR 5)

| Sprint | Período | Foco principal | Marco |
|---|---|---|---|
| Sprint 0 | 16/05 – 30/05/2025 | Kickoff, setup de infra, pipeline CI/CD, repositório Azure DevOps | Infra base operacional |
| Sprint 1 | 02/06 – 13/06/2025 | Autenticação de usuários (JWT), arquitetura base Spring Boot + Angular | Autenticação funcional |
| Sprint 2 | 16/06 – 27/06/2025 | Motor de rastreamento — LATAM Pass (Selenium + bypass Akamai) | LATAM Pass integrado |
| Sprint 3 | 30/06 – 11/07/2025 | Motor de rastreamento — Smiles (GOL) + TudoAzul (Azul) | 3 programas ativos |
| Sprint 4 | 14/07 – 25/07/2025 | Motor de rastreamento — TAP Miles&Go + Iberia Plus | 5 programas ativos |
| Sprint 5 | 28/07 – 08/08/2025 | Interface de busca de voos (Angular) — integração ponta a ponta | Busca funcional end-to-end |
| Sprint 6 | 11/08 – 22/08/2025 | Assinatura de rotas + alertas automáticos | Alertas funcionais |
| Sprint 7 | 25/08 – 05/09/2025 | Histórico de buscas + preferências de rotas | Histórico persistido |
| Sprint 8 | 08/09 – 19/09/2025 | Sistema de notificações (in-app + e-mail) | Notificações funcionais |
| Sprint 9 | 22/09 – 03/10/2025 | Chat / suporte integrado | Canal de suporte ativo |
| Sprint 10 | 06/10 – 17/10/2025 | Integração completa + testes E2E + ajustes de qualidade | Testes E2E aprovados |
| Sprint 11 | 20/10 – 31/10/2025 | Homologação com cliente — fase 1 | Homologação iniciada |
| Sprint 12 | 03/11 – 14/11/2025 | Ajustes de homologação fase 2 + entrega final | Build de produção pronto |
| Aceite | 16/11/2025 | Reunião de aceite formal | Projeto encerrado |

## 6. Recursos (GPR 6, GPR 7)

### 6.1 Equipe

| Papel | Responsável | Dedicação |
|---|---|---|
| Gerente de Projeto | Abraão Oliveira | Parcial |
| UI/UX Designer / Analista de Negócio | Igor Santana | Parcial |
| QA | Caroline Sousa | Parcial |
| Tech Lead / Back-End (Java) | Henry Komatsu | Integral |
| Back-End (Java) | Mateus Veloso | Integral |
| Front-End (Angular) | Beatriz Nunes | Integral |
| Front-End (Angular) | Lucas Batista | Integral |
| GQA de Processo | COO (Operações) | Parcial |

### 6.2 Ambientes e ferramentas

| Recurso | Descrição |
|---|---|
| Repositório de código | Azure DevOps (Git) |
| CI/CD | Azure DevOps Pipelines (YAML versionado) |
| Infraestrutura | VM Linux — provisionada pelo cliente (Hub de Milhas) |
| Banco de dados | PostgreSQL |
| Back-end | Java 17 + Spring Boot 3.x |
| Front-end | Angular 16+ |
| Motor de rastreamento | Java + Selenium WebDriver 4.x (headless Chrome) |
| Gerenciamento de tarefas | Azure DevOps Boards |
| Comunicação | Microsoft Teams / E-mail |

## 7. Partes interessadas e comunicação (GPR 9)

| Parte interessada | Papel | Canal | Frequência |
|---|---|---|---|
| Felipe (Hub de Milhas) | Patrocinador / PO | Sprint Review (Teams) + e-mail | Quinzenal (por sprint) |
| Abraão Oliveira | Gerente de Projeto | Reunião interna | Semanal |
| COO (Timeware) | GQA de Processo | Relatório de GQA | Por marco definido |
| Equipe de desenvolvimento | Execução | Daily + Teams | Diário |

## 8. Transição (GPR 8)

A implantação em produção ocorre na VM Linux provisionada pelo cliente. O repasse operacional inclui:

- Documentação de arquitetura e infraestrutura (PCP-MILHASFACIL01-001)
- Instruções de deploy e variáveis de ambiente
- Guia de operação do motor de rastreamento (pool ChromeDriver, gestão de sessões Selenium)
- Acesso ao repositório Azure DevOps transferido ao cliente após aceite final (ATA-MILHASFACIL01-002)

## 9. Riscos (GPR 10)

| ID | Risco | Prob (1–3) | Impacto (1–3) | Exposição | Tipo | Resposta |
|---|---|---|---|---|---|---|
| R-01 | Sites das companhias aéreas alteram estrutura HTML, quebrando os seletores Selenium | 3 | 3 | 9 | Mitigar | Monitorar continuamente; reajustar seletores na sprint seguinte à detecção; smoke tests diários nos seletores via CI/CD |
| R-02 | Akamai ou outro sistema anti-bot evolui e bloqueia o Selenium headless | 2 | 3 | 6 | Mitigar | Monitorar taxa de falhas; ajustar configurações (user-agent, delays, cookies); GDE-MILHASFACIL01-001 documenta a configuração base |
| R-03 | VM Linux de produção não provisionada no prazo pelo cliente | 2 | 2 | 4 | Mitigar | Solicitar como pré-condição do Sprint 0 (prazo: 30/05/2025); desenvolvimento local não bloqueado |
| R-04 | Credenciais de teste dos programas de fidelidade não fornecidas no prazo | 2 | 3 | 6 | Mitigar | Solicitar no kickoff (prazo: 30/05/2025); usar mock data para desenvolvimento paralelo se necessário |
| R-05 | Mudança de escopo durante o desenvolvimento | 2 | 2 | 4 | Mitigar | Formalizar via Change Request; avaliar impacto no prazo antes de aprovar |
| R-06 | Dificuldade em agendar Sprint Reviews com o cliente | 1 | 2 | 2 | Aceitar | Agendar com antecedência mínima de 5 dias úteis; enviar resumo por e-mail se cliente não puder comparecer |

## 10. Viabilidade (GPR 11)

O projeto é viável. A stack tecnológica (Java Spring Boot, Angular, PostgreSQL, Selenium) é dominada pela equipe. O principal risco técnico — bypass do Akamai via Selenium headless — foi avaliado e validado durante o Sprint 0; a decisão está registrada em GDE-MILHASFACIL01-001. O prazo de 6 meses é compatível com o escopo definido, considerando a velocidade histórica da equipe em projetos similares de plataforma web.

## 11. Aprovação do plano (GPR 13)

| Parte | Papel | Status | Data | Referência |
|---|---|---|---|---|
| Felipe (Hub de Milhas) | Patrocinador | Aprovado | 16/05/2025 | ATA-MILHASFACIL01-001 |
| Abraão Oliveira | Gerente de Projeto | Confirmado | 16/05/2025 | ATA-MILHASFACIL01-001 |

Este documento constitui a linha de base do projeto. Alterações de escopo, prazo ou equipe após esta aprovação seguem o fluxo de Change Request.

## 12. Controle de atualizações do plano

| Versão | Data | Descrição da atualização |
|---|---|---|
| 1.0 | 16/05/2025 | Versão inicial — linha de base aprovada em kickoff |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 16/05/2025 | Time de Melhoria Contínua | Documento inicial |
