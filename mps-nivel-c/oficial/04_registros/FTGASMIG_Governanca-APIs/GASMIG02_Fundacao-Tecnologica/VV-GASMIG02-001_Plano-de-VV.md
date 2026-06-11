# Plano de Verificação e Validação — Fundação Tecnológica GASMIG · OS-PARCELA-001

| Campo | Valor |
|---|---|
| **Documento** | VV-GASMIG02-001 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-001 |
| **Versão** | 1.1 |
| **Data** | 29/04/2026 |

> **Nota de adaptação:** Este é um projeto de configuração de ferramenta (Azure API Management), não de desenvolvimento de software. A verificação é realizada por checklist de configuração e navegação no portal Azure, não por testes unitários, de integração ou cenários BDD/Gherkin. Conforme ADAP-GASMIG02-001.

---

## 1. Itens a verificar e validar (VV 1)

| Item | Método |
|---|---|
| Governança APIM — estrutura global, políticas e nomenclatura | Checklist de configuração + verificação no portal Azure |
| Controle de acesso e ciclo de vida de credenciais | Checklist + verificação no portal Azure |
| Barreiras de segurança — acesso interno | Checklist + chamada HTTP de verificação |
| Barreiras de segurança — acesso externo | Checklist + chamada HTTP de verificação |
| Ambiente de sandbox | Checklist + chamada HTTP ao endpoint de sandbox |
| Catálogo corporativo / portal do desenvolvedor | Verificação visual no portal + checklist de visibilidade por perfil |
| Workspace ArcelorMittal | Checklist + verificação de isolamento no portal |
| Workspace Usiminas | Checklist + verificação de isolamento no portal |
| Rate limiting por workspace | Checklist + chamada HTTP que excede o limite |
| Throttling por workspace | Checklist + chamada HTTP em rajada |
| SSO SAML / Entra ID no portal | Checklist + acesso com conta do tenant GASMIG |
| Scripts IaC (Bicep/ARM) | Verificação técnica por Cézar Hiraki no Azure DevOps |
| Documentos de requisitos e design | Verificação técnica por Cézar Hiraki (completude e consistência) |

## 2. Métodos e critérios (VV 3)

**Checklist de verificação de configuração (método principal):**
- Cada item de configuração verificado contra os critérios de aceite do `REQ-GASMIG02-001`
- Executado pelos engenheiros (Fernando Oliveira / João Cruz) e revisado por Cézar Hiraki
- Evidência: capturas de tela do portal Azure para cada item do checklist

**Chamadas HTTP de verificação (smoke check):**
- Requisições via Postman ou curl contra o endpoint do APIM
- Objetivo: confirmar que as políticas configuradas produzem o comportamento esperado (acesso permitido ou bloqueado conforme a regra)
- Evidência: captura de tela da resposta HTTP (status code + body)

**Verificação técnica por Cézar Hiraki:**
- Navegação conjunta no portal Azure revisando a configuração de cada item
- Revisão dos scripts Bicep/ARM no Azure DevOps
- Registro dos pontos verificados e eventuais ajustes no documento de registro (seção 4)

**Validação com o cliente:**
- Sessão ao vivo (videoconferência / Teams) com o time técnico GASMIG (Eduardo Yasuda, José Geraldo)
- Demonstração da configuração no portal Azure: workspaces, catálogo, sandbox, SSO
- Aceite registrado em ATA-GASMIG02-002

**Ferramentas:**
- Portal Azure (verificação visual e de configuração)
- Postman / curl (smoke checks de chamadas HTTP)
- Azure APIM Test Console (testes rápidos direto no portal)
- Azure DevOps GASMIG (verificação dos scripts IaC)

## 3. Verificação técnica da configuração (VV 2)

> Em projetos de configuração de ferramenta, a verificação técnica substitui a revisão de código. O responsável técnico verifica se a configuração realizada pelos engenheiros está correta, completa e alinhada ao design antes da apresentação ao cliente.

- **Quem verifica:** Cézar Hiraki (Tech Lead / Arquiteto)
- **O que é verificado:** toda a configuração do APIM (políticas, workspaces, produtos, catálogo, SSO) e os scripts IaC
- **Quando:** 13/05/2026 — dia anterior à sessão de aceite com o cliente
- **Como:** navegação no portal Azure + revisão no Azure DevOps
- **Registro:** tabela de verificação na seção 4 deste documento

## 4. Execução e registro (VV 4)

Cada item do checklist é marcado após verificação no portal Azure. A coluna "Evidência" indica a captura de tela correspondente (a ser anexada ou referenciada após execução).

### Checklist de Verificação de Configuração

**Governança e estrutura global (RF-01)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| Instância APIM provisionada no tenant GASMIG | APIM ativo, visível no portal, sem erros de provisionamento | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Estrutura de produtos criada | `prod-gasmig-interno`, `prod-gasmig-externo`, `prod-gasmig-sandbox` existentes | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Grupos de usuários configurados | Grupos interno, externo e administradores criados e com associações corretas | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Políticas globais aplicadas | HTTPS enforced, headers de segurança presentes, política base ativa | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Named values configurados | Thresholds de rate/throttle e IPs internos cadastrados como named values | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Policy fragments criados | `pf-ratelimit` e `pf-throttle` criados e referenciados nas políticas dos workspaces | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |

**Controle de acesso e ciclo de vida de credenciais (RF-02)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| TTL de subscription keys configurado | Expiração definida nas assinaturas; configuração visível no portal | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Fluxo de renovação documentado | Processo de renovação descrito e acessível ao time GASMIG | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |

**Barreiras de segurança — acesso interno (RF-03)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| Política de restrição de IP no produto interno | IP restriction ativa no `prod-gasmig-interno` com IPs da rede GASMIG | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Smoke check — IP interno autorizado | Chamada via IP interno: resposta 200 | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Smoke check — IP externo bloqueado | Chamada via IP externo ao produto interno: resposta 403 | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |

**Barreiras de segurança — acesso externo (RF-04)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| Política de validação de credenciais no produto externo | Política ativa no `prod-gasmig-externo` | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Smoke check — credencial válida | Chamada com subscription key válida: resposta 200 | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Smoke check — credencial inválida | Chamada sem chave ou com chave inválida: resposta 401 | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |

**Ambiente de sandbox (RF-05)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| Produto sandbox provisionado | `prod-gasmig-sandbox` ativo com API de exemplo publicada | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Isolamento do ambiente produtivo | Credencial sandbox não acessa produtos de produção | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Smoke check — acesso ao sandbox | Chamada com credencial sandbox à API de exemplo: resposta 200 | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |

**Catálogo corporativo / portal do desenvolvedor (RF-06)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| Portal do desenvolvedor ativo e acessível | URL do portal acessível sem erro | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Visibilidade diferenciada por perfil | Usuário interno vê APIs internas; usuário externo vê apenas APIs externas | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| SSO Entra ID funcional | Login com conta do tenant GASMIG redireciona e autentica corretamente | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |

**Workspace ArcelorMittal (RF-07)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| Workspace `ws-arcelormittal` criado | Workspace visível no portal, ativo | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Produto e assinaturas configurados | Produto dedicado + subscription keys geradas | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Isolamento: credencial ArcelorMittal não acessa Usiminas | Chamada com chave ArcelorMittal ao workspace Usiminas: 401 | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |

**Workspace Usiminas (RF-08)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| Workspace `ws-usiminas` criado | Workspace visível no portal, ativo | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Produto e assinaturas configurados | Produto dedicado + subscription keys geradas | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Isolamento: credencial Usiminas não acessa ArcelorMittal | Chamada com chave Usiminas ao workspace ArcelorMittal: 401 | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |

**Rate limiting por workspace (RF-09)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| Named values de rate limit configurados | `nv-ratelimit-arcelormittal` e `nv-ratelimit-usiminas` com valores definidos | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Policy fragment `pf-ratelimit` aplicado nos workspaces | Fragment referenciado nas políticas dos workspaces | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Smoke check — bloqueio ao exceder limite | Chamadas que excedem o limite retornam 429 Too Many Requests | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |

**Throttling por workspace (RF-10)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| Named values de throttle configurados | `nv-throttle-arcelormittal` e `nv-throttle-usiminas` com valores definidos | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Policy fragment `pf-throttle` aplicado nos workspaces | Fragment referenciado nas políticas dos workspaces | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Smoke check — comportamento ao exceder rajada | Chamadas em rajada retornam 429 com Retry-After | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |

**SSO / Entra ID (RNF-03)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| Provedor de identidade Entra ID configurado | IdP Entra ID (SAML 2.0) cadastrado no portal APIM | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Login com conta GASMIG funcional | Fluxo de autenticação SAML completo e funcional | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |

**IaC e versionamento (RNF-05)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| Scripts Bicep/ARM exportados | Configuração exportada como IaC no repositório | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |
| Repositório Azure DevOps GASMIG configurado | Commits com histórico rastreável no repositório da GASMIG | ✅ | Verificado por Cézar Hiraki em 13/05/2026 |

## 5. Análise e comunicação dos resultados (VV 5)

- Resultado da verificação técnica (checklist preenchido) comunicado por Cézar Hiraki a Abraão Oliveira em 13/05/2026
- Eventuais itens pendentes são corrigidos antes da sessão de aceite
- Resultado da sessão de aceite com o cliente registrado em ATA-GASMIG02-002
- Indicadores (itens verificados / total, pendências resolvidas) alimentam a medição do projeto conforme PLA-MED-001

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 29/04/2026 | Abraão Oliveira / Cézar Hiraki | Versão inicial |
| 1.1 | 04/06/2026 | Abraão Oliveira | Substituídos testes de software e Gherkin por checklist de verificação de configuração — adequação ao tipo de projeto (configuração de ferramenta, não desenvolvimento de software) |
| 1.2 | 10/06/2026 | Time de Melhoria Contínua | Checklist preenchido com resultados da verificação técnica de 13/05/2026 (Cézar Hiraki — 36 itens ✅, 0 não conformidades) |
