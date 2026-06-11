# Documento de Requisitos — Milhas3 · Plataforma de Busca e Monitoramento de Milhas

| Campo | Valor |
|---|---|
| **Documento** | REQ-MILHASFACIL01-001 — Documento de Requisitos |
| **Versão** | 1.0 |
| **Data** | 16/05/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Milhas3 — Plataforma de Busca e Monitoramento de Milhas |
| **Cliente** | Hub de Milhas (Felipe) |
| **Tech Lead** | Henry Komatsu |
| **Processo MPS-SW** | REQ — Engenharia de Requisitos |

---

## 1. Contexto e objetivo

Programas de fidelidade aéreos (milhagem) oferecem disponibilidade de assentos de forma imprevisível e fragmentada: cada companhia opera seu próprio portal, sem integração entre si, e as janelas de disponibilidade costumam ser curtas. O usuário que deseja resgatar milhas precisa acessar manualmente cada site, repetidamente, sem garantia de encontrar o que procura.

O Hub de Milhas contratou a Timeware para desenvolver a plataforma **Milhas3**, cujo objetivo é centralizar e automatizar esse processo:

- **Busca unificada:** o usuário informa origem, destino e data; a plataforma consulta os cinco programas simultaneamente e retorna os resultados consolidados
- **Monitoramento contínuo:** o motor de rastreamento opera em background, identificando disponibilidades novas nas rotas de interesse cadastradas pelo usuário
- **Alertas proativos:** o usuário é notificado assim que uma oportunidade é detectada na sua rota cadastrada

## 2. Partes interessadas

| Papel | Organização | Necessidades principais |
|---|---|---|
| Felipe (Patrocinador) | Hub de Milhas | Plataforma operacional, rastreamento confiável dos 5 programas, alertas funcionais |
| Usuários finais da plataforma | Hub de Milhas (clientes) | Busca fácil, alertas precisos, histórico de disponibilidades |
| Henry Komatsu (Tech Lead) | Timeware | Clareza de interfaces e integrações para desenvolvimento |
| Igor Santana (UX) | Timeware | Requisitos de usabilidade e fluxo de navegação |

## 3. Visão geral da solução

A plataforma é composta por três camadas que operam em conjunto:

| Camada | Tecnologia | Responsabilidade |
|---|---|---|
| Interface Web | Angular 16+ | Busca, preferências, histórico, notificações, chat |
| Servidor Central | Java 17 / Spring Boot 3.x + PostgreSQL | Autenticação, lógica de negócio, persistência, orquestração de alertas |
| Motor de Rastreamento | Java 17 / Spring Boot + Selenium WebDriver (headless Chrome) | Acesso automatizado aos sites dos programas de fidelidade para coleta de disponibilidade e preços em milhas |

## 4. Requisitos funcionais

### 4.1 Autenticação e gestão de usuários

| ID | Requisito | Formato | Prioridade | Critérios de aceite |
|---|---|---|---|---|
| RF-01 | Cadastro de usuário | Como usuário, quero me cadastrar com e-mail e senha para acessar a plataforma | Alta | Usuário cadastrado com sucesso; e-mail duplicado retorna erro 409; senha armazenada com hash bcrypt |
| RF-02 | Autenticação via e-mail e senha | Como usuário, quero fazer login para receber um token JWT e acessar as funcionalidades | Alta | Token JWT válido retornado no login; token expirado rejeitado com 401; sessão persistida no front-end |
| RF-03 | Logout | Como usuário, quero encerrar minha sessão para proteger minha conta | Alta | Token invalidado; usuário redirecionado para tela de login |

### 4.2 Busca de voos em milhas

| ID | Requisito | Formato | Prioridade | Critérios de aceite |
|---|---|---|---|---|
| RF-04 | Busca consolidada de voos | Como usuário, quero informar origem, destino e data e receber resultados dos 5 programas de milhas em uma única tela | Alta | Resultados retornados em ≤ 30 segundos; exibidos por programa com custo em milhas, escalas e disponibilidade; busca sem resultado exibe mensagem informativa |
| RF-05 | Rastreamento LATAM Pass | Como sistema, devo acessar o portal LATAM Pass via Selenium para coletar disponibilidade de voos em milhas | Alta | Coleta retorna dados válidos em ao menos 3 rotas de teste; sessão Selenium gerenciada sem vazamento de recursos; bypass Akamai funcional |
| RF-06 | Rastreamento Smiles — GOL | Como sistema, devo acessar o portal Smiles via Selenium para coletar disponibilidade | Alta | Idem RF-05, para o portal Smiles |
| RF-07 | Rastreamento TudoAzul — Azul | Como sistema, devo acessar o portal TudoAzul via Selenium para coletar disponibilidade | Alta | Idem RF-05, para o portal TudoAzul |
| RF-08 | Rastreamento TAP Miles&Go | Como sistema, devo acessar o portal TAP Miles&Go via Selenium para coletar disponibilidade | Alta | Idem RF-05, para o portal TAP |
| RF-09 | Rastreamento Iberia Plus | Como sistema, devo acessar o portal Iberia Plus via Selenium para coletar disponibilidade | Alta | Idem RF-05, para o portal Iberia |

### 4.3 Assinaturas e alertas

| ID | Requisito | Formato | Prioridade | Critérios de aceite |
|---|---|---|---|---|
| RF-10 | Cadastro de rota de interesse | Como usuário, quero cadastrar rotas de interesse (origem, destino, programa, faixa de datas) para ser notificado quando houver disponibilidade | Alta | Rota salva; usuário pode visualizar, editar e excluir suas rotas cadastradas |
| RF-11 | Alerta automático de disponibilidade | Como usuário, quero ser notificado automaticamente quando o sistema detectar disponibilidade em uma rota que eu cadastrei | Alta | Notificação disparada em ≤ 5 minutos após detecção; alerta contém rota, programa, custo em milhas e link |

### 4.4 Histórico e preferências

| ID | Requisito | Formato | Prioridade | Critérios de aceite |
|---|---|---|---|---|
| RF-12 | Histórico de buscas | Como usuário, quero visualizar todas as buscas que realizei, com datas e resultados, para acompanhar a evolução de disponibilidade | Média | Histórico exibido em ordem cronológica decrescente; paginação funcional |
| RF-13 | Preferências de rotas favoritas | Como usuário, quero salvar rotas favoritas para acessá-las rapidamente na próxima busca | Média | Rotas favoritas exibidas na tela inicial; adição e remoção funcionais |

### 4.5 Notificações

| ID | Requisito | Formato | Prioridade | Critérios de aceite |
|---|---|---|---|---|
| RF-14 | Notificações in-app | Como usuário, quero ver um badge de notificação e uma lista de alertas dentro da plataforma | Alta | Badge atualizado em tempo real; lista de alertas com status lido / não lido persistido |
| RF-15 | Notificações por e-mail | Como usuário, quero receber um e-mail quando um alerta de rota for disparado | Média | E-mail enviado em ≤ 5 minutos após disparo; template com informações do voo formatadas |

### 4.6 Suporte

| ID | Requisito | Formato | Prioridade | Critérios de aceite |
|---|---|---|---|---|
| RF-16 | Chat / suporte integrado | Como usuário, quero acessar um canal de chat dentro da plataforma para tirar dúvidas e obter suporte | Baixa | Widget de chat funcional; mensagens persistidas; histórico de atendimento acessível |

## 5. Requisitos não funcionais

| ID | Categoria | Requisito |
|---|---|---|
| RNF-01 | Arquitetura | Back-end em Java 17 + Spring Boot 3.x, arquitetura em camadas (Controller → Service → Repository) |
| RNF-02 | Arquitetura | Front-end em Angular 16+, com separação de módulos por funcionalidade |
| RNF-03 | Infraestrutura | PostgreSQL como banco de dados relacional principal; migrações gerenciadas via Flyway |
| RNF-04 | Infraestrutura | Implantação em VM Linux provisionada pelo cliente (Hub de Milhas) |
| RNF-05 | DevOps | Pipeline CI/CD no Azure DevOps com gates de qualidade obrigatórios (build + testes unitários) |
| RNF-06 | Performance | Resposta da busca consolidada (5 programas) em ≤ 30 segundos em condições normais |
| RNF-07 | Performance | Endpoints REST do servidor central (exceto busca): p95 ≤ 500ms |
| RNF-08 | Segurança | Autenticação via JWT; senhas armazenadas com bcrypt; secrets em variáveis de ambiente (nunca versionados no repositório) |
| RNF-09 | Conformidade | Coleta e armazenamento de dados pessoais em conformidade com LGPD (finalidade, minimização, segurança) |
| RNF-10 | Rastreamento | Motor de rastreamento utiliza Selenium WebDriver com headless Chrome para contornar proteção Akamai Bot Manager dos portais das companhias aéreas; decisão registrada em GDE-MILHASFACIL01-001 |
| RNF-11 | Qualidade | Cobertura de testes unitários ≥ 70% nas camadas de serviço e domínio do back-end |
| RNF-12 | Disponibilidade | Uptime ≥ 99% mensal (excluindo janelas de manutenção programada acordadas com cliente) |

## 6. Restrições e premissas

### 6.1 Restrições

- Prazo fixo: aceite em 16/11/2025
- Infraestrutura exclusivamente em VM Linux (sem PaaS ou Kubernetes neste projeto)
- Plataforma não realiza transações financeiras; sem integração com meios de pagamento
- Rastreamento limitado aos 5 programas definidos no escopo

### 6.2 Premissas

- Cliente fornece credenciais de contas de teste nos 5 programas de fidelidade até 30/05/2025
- Estrutura dos portais das companhias aéreas permanece suficientemente estável durante o ciclo de desenvolvimento; alterações estruturais são tratadas como manutenção pós-entrega
- Protótipos de UI submetidos ao cliente têm retorno em até 3 dias úteis

## 7. Validação dos requisitos

| Etapa | Forma | Data |
|---|---|---|
| Levantamento inicial | Reunião de kickoff + visão de produto fornecida pelo cliente | 16/05/2025 |
| Validação de protótipos de UI | Revisões por sprint com Igor Santana e Felipe | Sprints 1–5 |
| Validação técnica do motor de rastreamento | Sprint Reviews com demonstração ao vivo por programa | Sprints 2–4 |
| Aprovação final | Reunião de aceite (ATA-MILHASFACIL01-002) | 16/11/2025 |

## 8. Confirmação de entendimento e compromisso (REQ 1, REQ 3)

| Papel | Nome | Confirmação | Data |
|---|---|---|---|
| Patrocinador / PO (cliente) | Felipe (Hub de Milhas) | Escopo e requisitos entendidos e aprovados | 16/05/2025 |
| Gerente de Projeto (Timeware) | Abraão Oliveira | Equipe comprometida com a execução conforme este documento | 16/05/2025 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 16/05/2025 | Time de Melhoria Contínua | Versão inicial — aprovada no kickoff |
