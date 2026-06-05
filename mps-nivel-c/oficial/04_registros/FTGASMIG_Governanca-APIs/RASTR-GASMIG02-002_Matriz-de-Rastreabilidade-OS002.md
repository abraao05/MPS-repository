# Matriz de Rastreabilidade — Fundação Tecnológica GASMIG · OS-PARCELA-002

| Campo | Valor |
|---|---|
| **Documento** | RASTR-GASMIG02-002 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-002 |
| **Versão** | 1.0 |
| **Data** | 26/05/2026 |

> Complementa `RASTR-GASMIG02-001_Matriz-de-Rastreabilidade.md`. Cobre os requisitos RF-11 a RF-19 e RNF-06 a RNF-09 da OS-PARCELA-002.

---

## Matriz

| Necessidade do cliente | Requisito (ID) | Item de design (PCP-GASMIG02-002) | Item de configuração (entregável Azure) | Checklist de verificação | Situação |
|---|---|---|---|---|---|
| Secrets e credenciais fora do código de configuração | RF-11 | Azure Key Vault + Managed Identity APIM; named values como Key Vault references | Key Vault provisionado; named values migrados para Key Vault references | Checklist RF-11 / RNF-06 | Pendente |
| Autenticação moderna OAuth 2.0 por workspace/API | RF-12 | App Registration Entra ID; política `validate-jwt` por workspace e por API | App Registration criada; validate-jwt ativa; fluxo OAuth funcional | Smoke check OAuth (200/401) | Pendente |
| API Keys com controle granular | RF-13 | Política de subscription key por operação; coexistência com OAuth 2.0 | Políticas de API Key em nível de operação configuradas | Smoke check API Key (200/401) | Pendente |
| Versionamento de APIs sem breaking changes | RF-14 | APIM Versions (path-based `/v1/`); APIM Revisions para minor changes | Versions e Revisions configuradas; roteamento correto | Checklist RF-14 | Pendente |
| Controle do ciclo de vida das APIs | RF-15 | Estados de API (Preview/Current/Deprecated/Retired); deprecation header | Estados aplicados; política de aviso de deprecation configurada | Checklist RF-15 | Pendente |
| Visibilidade operacional da plataforma | RF-16 | Application Insights logger; dashboards Azure Monitor | Application Insights integrado; dashboards de volumetria/latência/erros ativos | Verificação visual dashboards | Pendente |
| Alertas proativos de degradação | RF-17 | Regras de alerta Azure Monitor; Action Group GASMIG | Regras de alerta ativas; Action Group configurado; alerta disparado em ≤ 5 min | Teste de disparo de alerta | Pendente |
| Políticas de segurança refinadas por API | RF-18 | Política CORS por API; política `validate-content` para payloads | CORS configurado por API; validate-content ativo | Smoke check CORS (403) + payload (400) | Pendente |
| Validação end-to-end da fundação completa | RF-19 | Sessão de homologação cobrindo OS-001 + OS-002 integralmente | Fundação completa — todos os componentes operacionais validados conjuntamente | Sessão de homologação com GASMIG | Pendente |
| Nenhum secret hard-coded | RNF-06 | 100% named values como Key Vault references | Auditoria de configuração — zero valores sensíveis hard-coded | Auditoria de configuração | Pendente |
| OAuth 2.0 conforme RFC 6749 | RNF-07 | validate-jwt com Entra ID como IdP conforme padrão OAuth 2.0 | App Registration + validate-jwt policy | Smoke check OAuth (200/401) | Pendente |
| Retenção de dados de monitoramento ≥ 30 dias | RNF-08 | Política de retenção Application Insights | Retenção configurada para ≥ 30 dias | Checklist retenção | Pendente |
| Alertas disparados em ≤ 5 minutos | RNF-09 | Frequência de avaliação das regras: 5 minutos | Regras com período de avaliação ≤ 5 min | Verificação da configuração da regra | Pendente |

## Cobertura

- **Requisitos sem cobertura de verificação:** nenhum — todos os RF e RNF têm checklist ou smoke check associado
- **Itens configurados sem requisito associado:** nenhum previsto
- **Dependências com OS-001:** RF-19 (homologação end-to-end) abrange também todos os RF-01 a RF-10 da OS-001; a aprovação desta OS confirma a cobertura completa da fundação
- **Lacunas a preencher durante a execução:** thresholds numéricos dos alertas (RF-17) e origens CORS permitidas por API (RF-18) serão definidos com a GASMIG e registrados nos respectivos named values e políticas

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão Oliveira | Versão inicial |
