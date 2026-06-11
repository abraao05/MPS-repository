# Plano de Verificação e Validação — Milhas3 · Plataforma de Busca e Monitoramento de Milhas

| Campo | Valor |
|---|---|
| **Documento** | VV-MILHASFACIL01-001 — Plano de Verificação e Validação |
| **Versão** | 1.0 |
| **Data** | 16/05/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Milhas3 — Plataforma de Busca e Monitoramento de Milhas |
| **Cliente** | Hub de Milhas (Felipe) |
| **QA** | Caroline Sousa |
| **Processo MPS-SW** | VV — Verificação e Validação |

---

## 1. Itens a verificar e validar (VV 1)

| ID | Produto de trabalho | Método de verificação | Critério de validação com cliente |
|---|---|---|---|
| VV-01 | Autenticação (RF-01, RF-02, RF-03) | Testes unitários + testes de integração da API | Funcional sem erros em sessão de homologação |
| VV-02 | Motor de rastreamento — LATAM Pass (RF-05) | Teste de integração com Selenium ao vivo | Retorna dados válidos para ao menos 3 rotas de teste |
| VV-03 | Motor de rastreamento — Smiles / GOL (RF-06) | Teste de integração com Selenium ao vivo | Idem VV-02 |
| VV-04 | Motor de rastreamento — TudoAzul / Azul (RF-07) | Teste de integração com Selenium ao vivo | Idem VV-02 |
| VV-05 | Motor de rastreamento — TAP Miles&Go (RF-08) | Teste de integração com Selenium ao vivo | Idem VV-02 |
| VV-06 | Motor de rastreamento — Iberia Plus (RF-09) | Teste de integração com Selenium ao vivo | Idem VV-02 |
| VV-07 | Busca consolidada — interface Angular (RF-04) | Teste funcional E2E (Cypress) | Busca retorna resultados dos 5 programas em ≤ 30s em homologação |
| VV-08 | Assinatura de rotas + alertas automáticos (RF-10, RF-11) | Teste funcional + inspeção de banco + captura de notificação | Alerta disparado em ≤ 5 min após detecção em cenário de teste controlado |
| VV-09 | Histórico de buscas (RF-12) | Teste funcional | Histórico exibe buscas em ordem cronológica; paginação funcional |
| VV-10 | Preferências de rotas favoritas (RF-13) | Teste funcional | Favoritos salvos e exibidos corretamente; remoção funcional |
| VV-11 | Notificações in-app (RF-14) | Teste funcional | Badge atualizado em tempo real; status lido/não lido persistido |
| VV-12 | Notificações por e-mail (RF-15) | Teste de integração SMTP | E-mail recebido em ≤ 5 min com template e conteúdo corretos |
| VV-13 | Chat / suporte (RF-16) | Teste funcional | Widget funcional; mensagem enviada e persistida |
| VV-14 | Requisitos não funcionais (RNF-01 a RNF-12) | Testes de carga (JMeter) + análise estática + inspeção de configuração | Critérios conforme REQ-MILHASFACIL01-001 §5 |

## 2. Revisão por pares (VV 2)

| Elemento | Prática |
|---|---|
| Code review | Pull requests obrigatórios no Azure DevOps; aprovação de ao menos 1 revisor (Tech Lead para mudanças em motor de rastreamento; outro desenvolvedor para demais mudanças) antes do merge |
| Revisores de back-end | Henry Komatsu (Tech Lead) para código do motor Selenium; Mateus Veloso para demais módulos |
| Revisores de front-end | Beatriz Nunes ou Lucas Batista (rodízio por sprint) |
| Documentação técnica | PCP e ITP revisados pelo Tech Lead após entrega de cada módulo |
| Critério de aprovação de PR | Zero comentários críticos (tipo `blocking`) em aberto; pipeline CI/CD verde |

## 3. Métodos e critérios (VV 3)

| Tipo de teste | Ferramenta | Cobertura / meta | Ambiente |
|---|---|---|---|
| Unitários — back-end | JUnit 5 + Mockito | ≥ 70% (camadas Service e Domain) | CI/CD — Azure DevOps |
| Integração — API | Spring Boot Test + Testcontainers (PostgreSQL) | Endpoints críticos: auth, busca, alertas | CI/CD |
| Integração — Selenium | Selenium WebDriver ao vivo | 5 programas × 3 rotas de teste cada | Ambiente local / staging |
| E2E — front-end | Cypress | Fluxos principais: busca, assinatura de rota, histórico | Staging (VM Linux) |
| Performance | JMeter | GET /buscas: 100 req/s sem degradação de SLA | Staging |
| Homologação (UAT) | Execução manual pelo cliente | Todos os RF de prioridade Alta e Média | VM de produção do cliente |

## 4. Execução e registro (VV 4)

| Artefato | Localização |
|---|---|
| Casos de teste | Azure DevOps — Test Plans |
| Registro de defeitos | Azure DevOps — Boards (tipo: Bug) |
| Resultados de execução | Azure DevOps — Test Runs |
| Evidências do motor de rastreamento | Screenshots do ChromeDriver salvos por sessão de teste em `artifacts/selenium-evidences/` |
| Relatório de cobertura | Jacoco — gerado no pipeline CI/CD; publicado como artefato de build |

## 5. Análise e comunicação (VV 5)

| Métrica | Meta |
|---|---|
| Defeitos críticos abertos ao aceite | 0 |
| Cobertura de testes unitários — back-end | ≥ 70% |
| Testes E2E (fluxos principais) aprovados | 100% |
| Taxa de falha do motor de rastreamento por sessão | ≤ 10% por programa |
| Tempo de busca consolidada (5 programas) | ≤ 30s (p95) |

Resultados comunicados ao cliente nas Sprint Reviews e consolidados no RAC-MILHASFACIL01-001.

## 6. Cenários de teste — Motor de Rastreamento (Gherkin)

### Cenário 1 — Busca com sucesso (LATAM Pass)

```gherkin
Dado que o motor de rastreamento está ativo
  E o portal LATAM Pass está acessível
Quando uma busca é solicitada para origem "GRU", destino "GIG" e data "2025-09-01"
Então o sistema retorna ao menos 1 voo disponível em milhas
  E o resultado contém campo "milhas" com valor numérico positivo
  E o resultado é persistido na tabela resultados_busca com status "disponivel = true"
```

### Cenário 2 — Bloqueio temporário pelo Akamai

```gherkin
Dado que o portal Smiles detecta comportamento automatizado
  E retorna página de desafio (challenge page) do Akamai
Quando o motor de rastreamento recebe a resposta de bloqueio
Então o sistema aguarda o intervalo de backoff configurado
  E realiza nova tentativa com perfil de browser ajustado
  E registra a tentativa de bloqueio em sessoes_scraping com status "retry"
  E após 3 tentativas malsucedidas, registra status "falha" e emite log de erro
```

### Cenário 3 — Alerta disparado para rota cadastrada

```gherkin
Dado que o usuário cadastrou a rota "GRU → LIS" no programa TAP Miles&Go
  E uma disponibilidade de 45.000 milhas para essa rota é detectada pelo motor
Quando o resultado é persistido na tabela resultados_busca
Então o sistema dispara um alerta para o usuário em ≤ 5 minutos
  E o alerta é exibido como badge na interface web (RF-14)
  E um e-mail de notificação é enviado para o endereço cadastrado (RF-15)
```

### Cenário 4 — Busca sem disponibilidade

```gherkin
Dado que o usuário realiza uma busca para origem "POA" e destino "MIA" para a data "2025-12-25"
Quando nenhum dos 5 programas retorna disponibilidade em milhas para essa rota e data
Então a interface exibe a mensagem "Nenhuma disponibilidade encontrada para os critérios informados"
  E a busca é registrada no histórico com resultado vazio
  E nenhum alerta é disparado
```

### Cenário 5 — Falha total do motor (VM sobrecarregada)

```gherkin
Dado que todas as 5 instâncias do pool ChromeDriver estão ocupadas
Quando uma nova solicitação de busca é recebida
Então o sistema enfileira a solicitação
  E processa assim que uma instância do pool é liberada
  E o tempo total de resposta não excede 60 segundos
```

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 16/05/2025 | Time de Melhoria Contínua | Documento inicial |
