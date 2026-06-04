# Plano de Verificação e Validação — Fundação Tecnológica GASMIG · OS-PARCELA-001

| Campo | Valor |
|---|---|
| **Documento** | VV-GASMIG02-001 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-001 |
| **Versão** | 1.0 |
| **Data** | 29/04/2026 |

---

## 1. Itens a verificar e validar (VV 1)

| Item | Método |
|---|---|
| Instância APIM — governança e estrutura global | Verificação de configuração (checklist técnico) + revisão por pares |
| Controle de acesso e ciclo de vida de credenciais | Teste funcional de configuração |
| Barreiras de segurança — acesso interno | Teste funcional (requisição via IP interno simulado) |
| Barreiras de segurança — acesso externo | Teste funcional (requisição via IP externo) |
| Ambiente de sandbox | Teste funcional (chamada à API de exemplo no produto sandbox) |
| Catálogo corporativo / portal do desenvolvedor | Validação visual + teste de acesso por perfil (interno/externo) |
| Workspace ArcelorMittal | Teste funcional de isolamento e acesso com credenciais do workspace |
| Workspace Usiminas | Teste funcional de isolamento e acesso com credenciais do workspace |
| Rate limiting por workspace | Teste de carga controlada (verificar bloqueio ao atingir limite) |
| Throttling por workspace | Teste de rajada (verificar degradação controlada) |
| SSO SAML / Entra ID no portal | Teste de autenticação com conta do tenant GASMIG |
| Scripts IaC (Bicep/ARM) | Revisão por pares (Cézar Hiraki) + validação de idempotência |
| Documento de Requisitos e Plano de Projeto | Revisão por pares (completude e consistência) |

## 2. Métodos e critérios (VV 3)

**Verificação de configuração (checklist técnico):**
- Cada item de configuração verificado contra os critérios de aceite do `REQ-GASMIG02-001`
- Checklist executado por Fernando Oliveira / João Cruz e revisado por Cézar Hiraki
- Evidência: capturas de tela do portal Azure (blade de configuração do APIM)

**Testes funcionais de configuração:**
- Testes executados diretamente no portal Azure e via cliente HTTP (ex.: Postman / curl) contra o endpoint do APIM
- Cenários: happy path (acesso permitido com credenciais corretas) e sad path (acesso negado — IP incorreto, credencial expirada, limite excedido)
- Evidência: capturas de tela ou logs do APIM (trace de requisição)

**Revisão por pares:**
- Cézar Hiraki revisa o trabalho técnico dos engenheiros antes da sessão de aceite
- Registro em TPL-VV-002 (Registro de Revisão por Pares)

**Validação com cliente:**
- Sessão presencial ou videoconferência com o time técnico GASMIG (Eduardo Yasuda, José Geraldo)
- Demonstração ao vivo dos itens configurados no portal Azure
- Aceite registrado em ATA-GASMIG02-002 (Ata de Aceite)

**Ferramentas:**
- Portal Azure (validação visual e de configuração)
- Postman / curl (testes de requisição HTTP)
- Azure APIM Trace (diagnóstico de políticas)

**Ambientes:**
- Ambiente produtivo GASMIG (único ambiente desta OS; sandbox é um produto dentro deste ambiente)

## 3. Revisão por pares (VV 2)

A revisão por pares cobre os produtos de trabalho técnicos antes da sessão de aceite:

- **Quem revisa:** Cézar Hiraki (Tech Lead / Arquiteto)
- **O que é revisado:** Configuração do APIM (políticas, workspaces, produtos, catálogo), scripts IaC (Bicep/ARM), documentos de requisitos e design
- **Quando:** 13/05/2026 (dia anterior à sessão de aceite)
- **Via:** Portal Azure (navegação conjunta) + revisão de PRs no Azure DevOps
- **Registro:** TPL-VV-002 — Registro de Revisão por Pares (a preencher em 13/05/2026)

## 4. Execução e registro (VV 4)

Os resultados de cada caso de teste são registrados na tabela abaixo à medida que são executados. Defeitos encontrados são corrigidos imediatamente (janela de 15 dias não comporta ciclos de defeito).

| Ciclo | Casos executados | Defeitos encontrados | Situação |
|---|---|---|---|
| Verificação interna (13/05/2026) | CT-01 a CT-14 | — | A executar |
| Validação com cliente — sessão de aceite (~14/05/2026) | Demonstração dos itens | — | A executar |

## 5. Análise e comunicação dos resultados (VV 5)

- Os resultados da verificação interna são comunicados a Abraão Oliveira (GP) pelo Cézar Hiraki no dia 13/05
- Qualquer defeito crítico identificado na revisão por pares é corrigido antes da sessão de aceite
- Os resultados da sessão de aceite com o cliente são registrados em ATA-GASMIG02-002
- Indicadores de V&V (casos executados, defeitos, cobertura) alimentam a medição do projeto conforme PLA-MED-001

## 6. Cenários de teste (Gherkin) e evidências

```gherkin
Funcionalidade: Governança corporativa do Azure API Management

  Cenário: Acesso autenticado ao catálogo via SSO SAML (happy path)
    Dado que um usuário GASMIG possui conta ativa no Entra ID corporativo
    Quando acessa o portal do desenvolvedor APIM
    Então é redirecionado para autenticação SAML do Entra ID
    E após autenticação retorna ao portal com perfil de grupo correto (interno ou externo)

  Cenário: Acesso ao catálogo sem autenticação (sad path)
    Dado que um usuário não autenticado tenta acessar o portal do desenvolvedor
    Quando acessa a URL do portal
    Então é redirecionado ao fluxo de autenticação
    E não visualiza nenhuma API sem completar o login

Funcionalidade: Barreiras de segurança por origem de acesso

  Cenário: Requisição interna com IP autorizado (happy path)
    Dado que o cliente possui IP pertencente à rede corporativa GASMIG
    Quando realiza uma requisição à API no produto interno
    Então recebe status 200 com a resposta esperada

  Cenário: Requisição de IP externo bloqueado no produto interno (sad path)
    Dado que o cliente possui IP externo (fora da rede GASMIG)
    Quando realiza uma requisição à API no produto interno
    Então recebe status 403 Forbidden
    E a política de IP restriction foi aplicada

Funcionalidade: Isolamento de workspaces por cliente

  Cenário: Cliente ArcelorMittal acessa apenas seu workspace (happy path)
    Dado que o cliente ArcelorMittal possui subscription key válida do workspace ws-arcelormittal
    Quando realiza uma requisição com essa chave
    Então acessa as APIs do seu workspace
    E não tem visibilidade das APIs ou credenciais do workspace Usiminas

  Cenário: Subscription key de ArcelorMittal rejeitada em workspace Usiminas (sad path)
    Dado que o cliente utiliza a subscription key do workspace ArcelorMittal
    Quando tenta acessar uma API no workspace Usiminas
    Então recebe status 401 Unauthorized

Funcionalidade: Rate limiting por workspace

  Cenário: Requisições dentro do limite permitido (happy path)
    Dado que o workspace ArcelorMittal possui limite de N requisições por minuto
    Quando realiza N requisições em menos de 1 minuto
    Então todas recebem status 200

  Cenário: Requisições que excedem o rate limit (sad path)
    Dado que o workspace ArcelorMittal possui limite de N requisições por minuto
    Quando realiza N+1 requisições em menos de 1 minuto
    Então a N+1ª requisição recebe status 429 Too Many Requests
    E o header Retry-After indica quando pode tentar novamente

Funcionalidade: Ambiente de sandbox

  Cenário: Acesso ao sandbox com credenciais de sandbox (happy path)
    Dado que o usuário possui subscription de sandbox
    Quando faz chamada à API de exemplo no produto sandbox
    Então recebe resposta simulada com status 200
    E a chamada não afeta nenhum backend de produção

  Cenário: Credencial de produção rejeitada no sandbox (sad path)
    Dado que um usuário possui subscription key de produção
    Quando tenta utilizar essa chave no produto sandbox
    Então recebe status 401 Unauthorized
```

| Caso | ID | Tipo | Evidência | Situação |
|---|---|---|---|---|
| SSO SAML — acesso autenticado | CT-01 | Happy | Screenshot portal + trace APIM | A executar |
| SSO SAML — acesso sem auth | CT-02 | Sad | Screenshot redirecionamento | A executar |
| Barreira interna — IP autorizado | CT-03 | Happy | Screenshot trace APIM (200) | A executar |
| Barreira interna — IP externo bloqueado | CT-04 | Sad | Screenshot trace APIM (403) | A executar |
| Barreira externa — credencial válida | CT-05 | Happy | Screenshot trace APIM (200) | A executar |
| Barreira externa — credencial inválida | CT-06 | Sad | Screenshot trace APIM (401) | A executar |
| Workspace ArcelorMittal — acesso correto | CT-07 | Happy | Screenshot trace APIM (200) | A executar |
| Workspace Usiminas — acesso correto | CT-08 | Happy | Screenshot trace APIM (200) | A executar |
| Workspace — isolamento cross-workspace | CT-09 | Sad | Screenshot trace APIM (401) | A executar |
| Rate limiting — dentro do limite | CT-10 | Happy | Screenshot logs APIM | A executar |
| Rate limiting — excedendo o limite | CT-11 | Sad | Screenshot 429 + Retry-After | A executar |
| Throttling — excedendo a rajada | CT-12 | Sad | Screenshot resposta degradada | A executar |
| Sandbox — acesso com credencial sandbox | CT-13 | Happy | Screenshot trace APIM (200) | A executar |
| Sandbox — credencial prod rejeitada | CT-14 | Sad | Screenshot trace APIM (401) | A executar |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 29/04/2026 | Abraão Oliveira / Cézar Hiraki | Versão inicial — plano de V&V da OS-PARCELA-001 |
