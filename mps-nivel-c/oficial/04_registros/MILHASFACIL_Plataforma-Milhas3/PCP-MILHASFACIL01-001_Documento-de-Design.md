# Documento de Design — Milhas3 · Plataforma de Busca e Monitoramento de Milhas

| Campo | Valor |
|---|---|
| **Documento** | PCP-MILHASFACIL01-001 — Documento de Design |
| **Versão** | 1.0 |
| **Data** | 02/06/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Milhas3 — Plataforma de Busca e Monitoramento de Milhas |
| **Cliente** | Hub de Milhas (Felipe) |
| **Tech Lead** | Henry Komatsu |
| **Processo MPS-SW** | PCP — Projeto e Construção do Produto |

---

## 1. Objetivo

Descrever a arquitetura técnica e as decisões de design da plataforma Milhas3, fornecendo referência para desenvolvimento, revisão técnica, integração e operação.

## 2. Visão arquitetural

A plataforma é composta por três componentes principais que operam de forma integrada via HTTP REST:

```
[Usuário]
    ↕ HTTPS (porta 443)
[Nginx — VM Linux]
    ├── serve build estático Angular (porta 80/443)
    └── proxy_pass → Spring Boot (porta 8080)
[Servidor Central — Spring Boot]
    ├── API REST (Controller → Service → Repository)
    ├── Spring Scheduler → invoca Motor de Rastreamento
    └── JDBC/JPA → PostgreSQL (porta 5432)
[Motor de Rastreamento — Spring Scheduler + Selenium]
    ↕ HTTPS (scraping headless Chrome)
[Portais externos: LATAM Pass / Smiles / TudoAzul / TAP / Iberia]
```

O Motor de Rastreamento é um serviço Spring Scheduler integrado ao mesmo JAR do Servidor Central (monolito modular), simplificando o deploy em VM única. Pode ser extraído para microserviço independente em versão futura.

## 3. Componentes

### 3.1 Frontend Web — Angular

| Atributo | Detalhe |
|---|---|
| Framework | Angular 16+ |
| Build | Angular CLI + Nginx (build estático) |
| Comunicação com back-end | HttpClient — HTTP REST (JSON) |
| Autenticação | JWT armazenado em localStorage; interceptor Angular injeta header `Authorization: Bearer <token>` em todas as requisições autenticadas |
| Módulos principais | AuthModule, SearchModule, AlertModule, HistoryModule, NotificationModule, SupportModule |
| Biblioteca UI | Angular Material |
| Deploy | Nginx na VM Linux — serve o build estático e faz proxy_pass para o Spring Boot |

### 3.2 Servidor Central — Spring Boot

| Atributo | Detalhe |
|---|---|
| Linguagem / Framework | Java 17 + Spring Boot 3.x |
| Arquitetura interna | Camadas: Controller → Service → Repository (Spring Data JPA) |
| Banco de dados | PostgreSQL — conexão via HikariCP (connection pool) |
| ORM | Hibernate via Spring Data JPA |
| Migrações de schema | Flyway — versionadas no diretório `resources/db/migration` |
| Autenticação | Spring Security + JWT (biblioteca `io.jsonwebtoken`) |
| Agendamento | Spring Scheduler — dispara rastreamento periódico nas rotas assinadas |
| Notificações e-mail | Spring Mail — SMTP configurado via variáveis de ambiente |
| Build | Maven |
| Deploy | JAR executável gerenciado por systemd service na VM Linux (reinício automático) |

### 3.3 Motor de Rastreamento — Selenium

| Atributo | Detalhe |
|---|---|
| Linguagem | Java 17 (componente do mesmo módulo Spring Boot) |
| Driver | Selenium WebDriver 4.x com ChromeDriver (headless Chrome) |
| Gerenciamento do ChromeDriver | WebDriverManager — resolve automaticamente a versão compatível com o Chrome instalado |
| Modo headless | `--headless=new` (nova API headless do Chrome; menos detectável que `--headless` legado) |
| Bypass Akamai | Configurações: `--disable-blink-features=AutomationControlled`, user-agent real de desktop, viewport 1920×1080, delays variáveis (300–1500ms) entre ações, reutilização de cookies de sessão. Decisão completa em GDE-MILHASFACIL01-001 |
| Pool de drivers | Máximo 5 instâncias ChromeDriver simultâneas para não sobrecarregar a VM Linux |
| Tratamento de falhas | Retry com backoff exponencial (3 tentativas); falha persistente registrada em `sessoes_scraping` com status `falha` e log de erro |
| Integração com servidor | Invocado pelo Spring Scheduler; resultado persistido no PostgreSQL via Spring Data JPA |

## 4. Modelo de dados — principais entidades

| Entidade | Tabela | Atributos principais |
|---|---|---|
| Usuário | `usuarios` | id, email, senha_hash, criado_em |
| Rota de interesse | `rotas` | id, usuario_id, origem, destino, programa, data_inicio, data_fim, ativo |
| Busca | `buscas` | id, usuario_id, origem, destino, criado_em |
| Resultado de busca | `resultados_busca` | id, busca_id, programa, milhas, escalas, disponivel, coletado_em |
| Alerta | `alertas` | id, rota_id, resultado_id, notificado_em, lido |
| Sessão de scraping | `sessoes_scraping` | id, programa, status, iniciado_em, concluido_em, erro |
| Favorito | `favoritos` | id, usuario_id, origem, destino, criado_em |

## 5. Endpoints principais — Servidor Central

| Método | Rota | RF coberto |
|---|---|---|
| POST | /auth/register | RF-01 |
| POST | /auth/login | RF-02 |
| POST | /auth/logout | RF-03 |
| POST | /buscas | RF-04 (dispara rastreamento síncrono nos 5 programas) |
| GET | /buscas/historico | RF-12 |
| POST | /rotas | RF-10 |
| GET | /rotas | RF-10 |
| DELETE | /rotas/{id} | RF-10 |
| GET | /alertas | RF-14 |
| PUT | /alertas/{id}/lido | RF-14 |
| GET | /favoritos | RF-13 |
| POST | /favoritos | RF-13 |
| DELETE | /favoritos/{id} | RF-13 |

## 6. Infraestrutura e deploy

| Componente | Configuração |
|---|---|
| Sistema operacional | Ubuntu Server 22.04 LTS (VM Linux provisionada pelo cliente) |
| Nginx | Reverse proxy; porta 80 redireciona para 443; proxy_pass para Spring Boot na porta 8080; serve build Angular |
| Spring Boot | Porta 8080; arquivo de serviço systemd com reinício automático |
| PostgreSQL | Porta 5432; credenciais em variáveis de ambiente da VM; backup automático configurado |
| Chrome / ChromeDriver | Chrome instalado na VM; versão gerenciada pelo WebDriverManager |
| CI/CD | Azure DevOps Pipelines — estágios: build Maven, testes unitários, build Angular, deploy via SSH na VM Linux |
| Segredos e variáveis sensíveis | Azure DevOps Variable Groups (criptografados); nunca versionados no repositório Git |

## 7. Decisões de design relevantes

As decisões arquiteturais de alto impacto estão registradas em GDE-MILHASFACIL01-001. Sumário das principais:

| Decisão | Escolha | Referência |
|---|---|---|
| Tecnologia do motor de rastreamento | Selenium WebDriver (headless Chrome) — escolhido por contornar Akamai | GDE-MILHASFACIL01-001 |
| Estrutura do back-end | Monolito modular (servidor central + motor de rastreamento no mesmo JAR) — simplifica deploy em VM única | GDE-MILHASFACIL01-001 |
| Migrações de banco | Flyway — garante rastreabilidade e reversibilidade do schema | — |
| Autenticação | JWT stateless — compatível com front-end Angular SPA sem estado de sessão no servidor | — |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 02/06/2025 | Time de Melhoria Contínua | Documento inicial — arquitetura base definida na Sprint 0 |
