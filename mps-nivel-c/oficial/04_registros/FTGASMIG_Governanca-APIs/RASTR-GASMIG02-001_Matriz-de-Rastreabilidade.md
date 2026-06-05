# Matriz de Rastreabilidade — Fundação Tecnológica GASMIG · OS-PARCELA-001

| Campo | Valor |
|---|---|
| **Documento** | RASTR-GASMIG02-001 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-001 |
| **Versão** | 1.0 |
| **Data** | 29/04/2026 |

---

## Matriz

| Necessidade do cliente | Requisito (ID) | Item de design (PCP-GASMIG02-001) | Item de configuração (entregável Azure) | Caso de teste | Situação |
|---|---|---|---|---|---|
| Governança centralizada de APIs em padrão corporativo | RF-01 | Políticas globais APIM; Named values; Policy fragments; Estrutura de produtos e grupos | APIM instance + políticas globais + estrutura de produtos configurada | CT-01, CT-03 | Pendente |
| Controle de acesso com expiração de credenciais | RF-02 | Configuração de TTL de subscription keys; grupos de usuários | Subscription keys com TTL configurado; fluxo de renovação documentado | CT-05, CT-06 | Pendente |
| Segurança de acesso interno (rede GASMIG) | RF-03 | Política de restrição de IP — `prod-gasmig-interno` | Política IP restriction no produto interno com IPs da rede GASMIG | CT-03, CT-04 | Pendente |
| Segurança de acesso externo (parceiros e clientes) | RF-04 | Política de validação de credenciais — `prod-gasmig-externo` | Política de segurança no produto externo; restrições para parceiros | CT-05, CT-06 | Pendente |
| Ambiente de sandbox para testes pré-produção | RF-05 | Produto `prod-gasmig-sandbox` com APIs de exemplo | Produto sandbox provisionado; APIs de exemplo publicadas; isolamento produtivo | CT-13, CT-14 | Pendente |
| Catálogo corporativo de APIs | RF-06 | Portal do desenvolvedor configurado — layout GASMIG; visibilidade por grupo | Portal ativo com catálogo; acesso diferenciado por perfil (interno/externo) | CT-01, CT-02 | Pendente |
| Workspace dedicado ArcelorMittal | RF-07 | `ws-arcelormittal` — produtos, assinaturas e políticas isoladas | Workspace ArcelorMittal criado e configurado no APIM | CT-07, CT-09 | Pendente |
| Workspace dedicado Usiminas | RF-08 | `ws-usiminas` — produtos, assinaturas e políticas isoladas | Workspace Usiminas criado e configurado no APIM | CT-08, CT-09 | Pendente |
| Rate limiting por workspace | RF-09 | Named values `nv-ratelimit-*`; policy fragment `pf-ratelimit` | Políticas de rate limit ativas por workspace com named values configurados | CT-10, CT-11 | Pendente |
| Throttling por workspace | RF-10 | Named values `nv-throttle-*`; policy fragment `pf-throttle` | Políticas de throttle ativas por workspace com named values configurados | CT-12 | Pendente |
| Conformidade com boas práticas Microsoft | RNF-01 | Arquitetura auditável vs. Azure Well-Architected Framework | Checklist de conformidade preenchido e anexado | — (checklist) | Pendente |
| Plataforma 100% Azure | RNF-02 | Todos os componentes no Azure tenant GASMIG | Todos os recursos em subscription Azure GASMIG | — (verificação) | Pendente |
| SSO / login automático via Entra ID | RNF-03 | Entra ID SAML 2.0 integrado ao portal do desenvolvedor | Provedor de identidade Entra ID configurado no portal APIM | CT-01, CT-02 | Pendente |
| Plataforma escalável para novas APIs | RNF-04 | Named values parametrizáveis; workspaces independentes; policy fragments modulares | Arquitetura documentada; adição de novo workspace validada sem impacto nas políticas globais | — (revisão de design) | Pendente |
| Configuração rastreável e versionada | RNF-05 | Scripts Bicep/ARM exportados e versionados | Repositório IaC no Azure DevOps GASMIG com histórico de commits | — (revisão por pares) | Pendente |

## Cobertura

- **Requisitos sem cobertura de teste:** RNF-01, RNF-02, RNF-04, RNF-05 — cobertos por checklist e revisão por pares em vez de casos de teste automatizados (natureza de configuração/documentação)
- **Itens configurados sem requisito associado:** nenhum — toda a configuração deriva dos requisitos listados acima
- **Casos de teste cobertos:** CT-01 a CT-14 (14 casos) — cobertura de todos os RF e dos RNF testáveis funcionalmente
- **Lacunas identificadas:** os parâmetros exatos de rate limiting e throttling (thresholds numéricos) e os IPs da rede interna GASMIG serão obtidos durante a execução e registrados nos named values correspondentes; os casos de teste CT-03/CT-04 e CT-10/CT-11/CT-12 dependem desses valores para execução precisa

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 29/04/2026 | Abraão Oliveira | Versão inicial — rastreabilidade completa dos requisitos da OS-PARCELA-001 |
