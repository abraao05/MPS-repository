# Plano de Verificação e Validação — Fundação Tecnológica GASMIG · OS-PARCELA-002

| Campo | Valor |
|---|---|
| **Documento** | VV-GASMIG02-002 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-002 |
| **Versão** | 1.0 |
| **Data** | 26/05/2026 |

> **Nota de adaptação:** Mesma abordagem da OS-PARCELA-001 (VV-GASMIG02-001). Verificação por checklist de configuração e smoke checks, não testes de software. Conforme ADAP-GASMIG02-002.

---

## 1. Itens a verificar e validar (VV 1)

| Item | Método |
|---|---|
| Azure Key Vault provisionado e integrado ao APIM | Checklist + verificação no portal Azure |
| Named values como Key Vault references (sem hard-code) | Checklist + auditoria de configuração |
| OAuth 2.0 — App Registration Entra ID + validate-jwt | Checklist + smoke check de fluxo completo |
| API Keys com controle granular | Checklist + smoke checks |
| Políticas de versionamento (APIM Versions) | Checklist + verificação no portal |
| Políticas de ciclo de vida e deprecation header | Checklist + verificação no portal |
| Dashboards Application Insights / Azure Monitor | Verificação visual dos dashboards |
| Regras de alerta e Action Group | Checklist + teste de disparo de alerta |
| Políticas CORS por API | Checklist + smoke check de origem bloqueada |
| Validação de payload (validate-content) | Checklist + smoke check de payload inválido |
| Homologação end-to-end (toda a fundação OS-001 + OS-002) | Sessão ao vivo com time técnico GASMIG |
| Scripts IaC atualizados (Bicep/ARM) | Verificação técnica Cézar Hiraki no Azure DevOps |

## 2. Métodos e critérios (VV 3)

Mesmos métodos da OS-PARCELA-001. Adicionados:
- **Smoke check OAuth 2.0:** obter token no Entra ID → usar no header `Authorization: Bearer` → chamada validada pelo APIM (200) e rejeitada sem token (401)
- **Teste de alerta:** forçar condição de alerta (ex.: requisições com erro) e confirmar disparo no Azure Monitor dentro de 5 minutos
- **Validação end-to-end (RF-19):** navegação completa pelo fluxo com time GASMIG: autenticação → chamada API → visualização de dados no dashboard

## 3. Verificação técnica da configuração (VV 2)

- **Quem verifica:** Cézar Hiraki
- **Quando:** 09/06/2026
- **Foco especial:** Key Vault (sem secrets hard-coded), OAuth 2.0 (fluxo completo), alertas (thresholds e destinatários corretos)

## 4. Execução e registro (VV 4)

### Checklist de Verificação de Configuração

**Azure Key Vault e secrets (RF-11 / RNF-06)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| Azure Key Vault provisionado | Key Vault ativo no portal, no mesmo resource group do APIM | ☐ | — |
| Managed Identity do APIM com acesso ao Key Vault | Permissão de leitura configurada; sem credenciais hard-coded | ☐ | — |
| Named values como Key Vault references | Todos os valores sensíveis referenciados via Key Vault; auditoria sem hard-codes | ☐ | — |

**OAuth 2.0 (RF-12 / RNF-07)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| App Registration criada no Entra ID GASMIG | App visível no Entra ID com escopo APIM configurado | ☐ | — |
| Política validate-jwt configurada no APIM | Política presente nas APIs/produtos configurados | ☐ | — |
| Smoke check — token válido aceito (200) | Chamada com Bearer token válido: resposta 200 | ☐ | — |
| Smoke check — sem token rejeitado (401) | Chamada sem Authorization header: resposta 401 | ☐ | — |
| Smoke check — token inválido rejeitado (401) | Chamada com token expirado ou falsificado: resposta 401 | ☐ | — |

**API Keys granulares (RF-13)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| Controle de chave configurado por API onde aplicável | Política de subscription key em nível de operação configurada | ☐ | — |
| Smoke check — chave válida aceita (200) | Chamada com chave correta: resposta 200 | ☐ | — |
| Smoke check — chave inválida rejeitada (401) | Chamada com chave incorreta: resposta 401 | ☐ | — |

**Versionamento (RF-14)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| APIM Versions configuradas (path-based) | URLs de versão criadas (`/v1/`, etc.); roteamento correto | ☐ | — |
| APIM Revisions configuradas para minor changes | Revisões criadas; versão atual definida | ☐ | — |

**Ciclo de vida (RF-15)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| Estados de ciclo de vida documentados e aplicados | APIs com estado correto (Current, Preview, etc.) no portal | ☐ | — |
| Deprecation header em APIs deprecated | Header de aviso presente em respostas de APIs deprecated | ☐ | — |

**Monitoramento — Application Insights e dashboards (RF-16 / RNF-08)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| Application Insights integrado ao APIM | Logger configurado; telemetria visível no portal | ☐ | — |
| Dashboards configurados no Azure Monitor | Dashboards de volumetria, latência e erros visíveis e com dados | ☐ | — |
| Retenção ≥ 30 dias configurada | Política de retenção do Application Insights ≥ 30 dias | ☐ | — |

**Alertas automatizados (RF-17 / RNF-09)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| Regras de alerta criadas (latência, erros, indisponibilidade) | Regras ativas no Azure Monitor com thresholds definidos | ☐ | — |
| Action Group com destinatários GASMIG configurado | E-mails/Teams webhook dos destinatários cadastrados | ☐ | — |
| Frequência de avaliação ≤ 5 minutos | Configuração da regra: período de avaliação ≤ 5 min | ☐ | — |
| Teste de disparo de alerta | Alerta disparado e notificação recebida pelos destinatários em ≤ 5 min | ☐ | — |

**CORS e validação de payload (RF-18)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| Política CORS configurada por API | Origens permitidas definidas; política ativa | ☐ | — |
| Smoke check — origem bloqueada (403/CORS error) | Chamada de origem não permitida: bloqueada | ☐ | — |
| Política validate-content configurada | Validação de schema ativa nas APIs com payload | ☐ | — |
| Smoke check — payload inválido rejeitado (400) | Payload malformado: resposta 400 antes de atingir backend | ☐ | — |

**IaC atualizado (RNF-05 — continuidade)**

| Item | Critério | Verificado | Evidência |
|---|---|---|---|
| Scripts Bicep/ARM atualizados com OS-002 | Configuração de Key Vault, OAuth, alertas exportada como IaC | ☐ | — |
| Commits no Azure DevOps GASMIG | Histórico de commits com os novos recursos | ☐ | — |

## 5. Análise e comunicação dos resultados (VV 5)

- Resultado da verificação técnica comunicado por Cézar Hiraki a Abraão Oliveira em 09/06/2026
- Sessão de homologação end-to-end agendada para ~10/06/2026 com Eduardo Yasuda e José Geraldo (GASMIG)
- Aceite registrado em ATA-GASMIG02-003 (Ata de Aceite OS-002)
- Indicadores de V&V alimentam a medição consolidada do projeto conforme PLA-MED-001

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão Oliveira / Cézar Hiraki | Versão inicial |
