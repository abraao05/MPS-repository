# Registro de Verificação Técnica da Configuração — Fundação Tecnológica GASMIG · OS-PARCELA-001

| Campo | Valor |
|---|---|
| **Documento** | REV-GASMIG02-001 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-001 |
| **Versão** | 1.0 |
| **Data da verificação** | 18/05/2026 |
| **Responsável pela verificação** | Cézar Hiraki (Tech Lead / Arquiteto) |

> Evidência de que a configuração foi revisada tecnicamente antes do aceite do cliente, conforme VV-GASMIG02-001 seção 3. Verificação realizada ao final da reunião de 18/05/2026 com demonstração ao vivo do portal Azure para Sérgio Villaça (GASMIG).

---

## Resultado da verificação

**Status geral:** ✅ Aprovado — todos os itens verificados. Configuração apresentada ao cliente em sessão ao vivo no portal Azure.

---

## Checklist de Verificação

### Governança e estrutura global (RF-01)

| Item | Verificado | Evidência |
|---|---|---|
| Instância APIM provisionada no tenant GASMIG | ✅ | Portal Azure — APIM ativo, demonstrado ao vivo em reunião 18/05/2026 |
| Estrutura de produtos criada | ✅ | `prod-gasmig-interno`, `prod-gasmig-externo`, `prod-gasmig-sandbox` visíveis no portal |
| Grupos de usuários configurados | ✅ | Grupos interno, externo e administradores configurados |
| Políticas globais aplicadas | ✅ | HTTPS enforced, headers de segurança ativos |
| Named values configurados | ✅ | Thresholds e variáveis globais configurados como named values |
| Policy fragments criados | ✅ | `pf-ratelimit` e `pf-throttle` aplicados |

### Controle de acesso (RF-02)

| Item | Verificado | Evidência |
|---|---|---|
| TTL de subscription keys configurado | ✅ | Expiração configurada nas assinaturas — visível no portal |
| Fluxo de renovação documentado | ✅ | Processo documentado e repassado ao time GASMIG |

### Barreiras de segurança — acesso interno (RF-03)

| Item | Verificado | Evidência |
|---|---|---|
| Política de restrição de IP no produto interno | ✅ | IP restriction configurada no `prod-gasmig-interno` |
| Smoke check — IP interno autorizado | ✅ | Verificado no portal Azure via APIM Test Console |
| Smoke check — IP externo bloqueado (403) | ✅ | Verificado no portal Azure |

### Barreiras de segurança — acesso externo (RF-04)

| Item | Verificado | Evidência |
|---|---|---|
| Política de validação de credenciais no produto externo | ✅ | Política ativa no `prod-gasmig-externo` |
| Smoke check — credencial válida (200) | ✅ | Verificado via APIM Test Console |
| Smoke check — credencial inválida (401) | ✅ | Verificado via APIM Test Console |

### Ambiente de sandbox (RF-05)

| Item | Verificado | Evidência |
|---|---|---|
| Produto sandbox provisionado com API de exemplo | ✅ | `prod-gasmig-sandbox` ativo com mock de API publicado |
| Isolamento do ambiente produtivo | ✅ | Credenciais de sandbox segregadas — verificado no portal |
| Smoke check — acesso ao sandbox (200) | ✅ | Chamada a API de exemplo no sandbox: resposta 200 |

### Catálogo corporativo / portal do desenvolvedor (RF-06)

| Item | Verificado | Evidência |
|---|---|---|
| Portal do desenvolvedor ativo e acessível | ✅ | Demonstrado ao vivo — Sérgio com acesso ao portal em 18/05 |
| Identidade visual GASMIG aplicada | ✅ | Citado na reunião: *"tá com a identidade visual da Gasmig e ficou bem bonito"* |
| Visibilidade diferenciada por perfil | ✅ | Confirmado no portal: perfis interno/externo com visibilidades distintas |
| SSO Entra ID funcional | ✅ | Login via conta corporativa GASMIG funcional no portal |

### Workspace ArcelorMittal (RF-07)

| Item | Verificado | Evidência |
|---|---|---|
| Workspace `ws-arcelormittal` criado | ✅ | Demonstrado na reunião — workspace visível e ativo |
| Produto e assinaturas configurados | ✅ | Produto `prod-ws-arcelormittal` + subscription keys geradas |
| Isolamento: credencial ArcelorMittal não acessa Usiminas (401) | ✅ | Verificado no portal Azure |

### Workspace Usiminas (RF-08)

| Item | Verificado | Evidência |
|---|---|---|
| Workspace `ws-usiminas` criado | ✅ | Demonstrado na reunião — workspace visível e ativo |
| Produto e assinaturas configurados | ✅ | Produto `prod-ws-usiminas` + subscription keys geradas |
| Isolamento: credencial Usiminas não acessa ArcelorMittal (401) | ✅ | Verificado no portal Azure |

### Rate limiting (RF-09)

| Item | Verificado | Evidência |
|---|---|---|
| Named values de rate limit configurados | ✅ | Thresholds configurados como named values por workspace |
| Policy fragment `pf-ratelimit` aplicado | ✅ | Fragment referenciado nas políticas dos workspaces |
| Smoke check — bloqueio ao exceder limite (429) | ✅ | Verificado via chamadas controladas ao APIM |

### Throttling (RF-10)

| Item | Verificado | Evidência |
|---|---|---|
| Named values de throttle configurados | ✅ | Thresholds configurados como named values por workspace |
| Policy fragment `pf-throttle` aplicado | ✅ | Fragment referenciado nas políticas dos workspaces |
| Smoke check — comportamento em rajada (429) | ✅ | Verificado via chamadas em rajada ao APIM |

### SSO / Entra ID (RNF-03)

| Item | Verificado | Evidência |
|---|---|---|
| Provedor de identidade Entra ID configurado | ✅ | IdP Entra ID (SAML 2.0) configurado no portal APIM |
| Login com conta GASMIG funcional | ✅ | Demonstrado em reunião com Sérgio — acesso confirmado |

### IaC e versionamento (RNF-05)

| Item | Verificado | Evidência |
|---|---|---|
| Scripts Bicep/ARM exportados | ✅ | Configuração exportada como IaC |
| Repositório Azure DevOps GASMIG configurado | ✅ | Commits com histórico rastreável no repositório GASMIG |

---

## Pendências identificadas na verificação

Nenhuma pendência. Todos os itens verificados e aprovados antes da apresentação ao cliente.

## Conclusão

Configuração da OS-PARCELA-001 verificada e aprovada em 18/05/2026. Material de evidência (PDF com capturas de tela) preparado e enviado ao cliente junto com a NF em 18/05/2026 às 18:37.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 18/05/2026 | Cézar Hiraki | Verificação técnica concluída — todos os itens aprovados |
