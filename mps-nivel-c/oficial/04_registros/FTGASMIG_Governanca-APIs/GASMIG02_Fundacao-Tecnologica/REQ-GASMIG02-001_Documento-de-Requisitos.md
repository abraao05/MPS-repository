# Documento de Requisitos — Fundação Tecnológica GASMIG · OS-PARCELA-001

| Campo | Valor |
|---|---|
| **Documento** | REQ-GASMIG02-001 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-001 |
| **Cliente** | GASMIG — Companhia de Gás de Minas Gerais |
| **Versão** | 1.0 |
| **Data** | 29/04/2026 |
| **Responsáveis (Discovery)** | Abraão Oliveira (PO) / Cézar Hiraki (Tech Lead) / João Victor Cruz Silva (Engenheiro) |

---

## 1. Contexto e objetivo

A GASMIG necessita compartilhar dados operacionais com grandes clientes (ArcelorMittal, Usiminas) e parceiros da cadeia de suprimento de gás de forma padronizada, segura e escalável. O modelo atual é manual (e-mails, planilhas) e não suporta o crescimento previsto de integrações.

O objetivo desta OS é estabelecer a **Fundação Tecnológica de Integração** da GASMIG — uma plataforma corporativa de APIs sobre o Azure API Management que servirá de base reutilizável para todas as futuras integrações, sem necessidade de reconfiguração da infraestrutura a cada novo projeto.

Esta OS (OS-PARCELA-001) cobre exclusivamente a **infraestrutura e governança** da plataforma. O desenvolvimento de APIs de negócio é escopo de projetos subsequentes que aproveitarão esta fundação.

## 2. Partes interessadas

| Parte interessada | Necessidade principal |
|---|---|
| GASMIG — TI e Telecomunicação (Sérgio Villaça) | Plataforma de APIs governada, segura e sob controle corporativo |
| GASMIG — Arquitetura de TI (Eduardo Yasuda, José Geraldo) | Fundação técnica escalável, em padrão Microsoft e boas práticas internacionais |
| GASMIG — Gestão (Murilo Morgado) | Visibilidade e controle sobre o consumo de APIs por clientes |
| ArcelorMittal | Acesso segregado e controlado às APIs da GASMIG |
| Usiminas | Acesso segregado e controlado às APIs da GASMIG |
| Timeware (equipe técnica) | Ambiente Azure configurado e acessível para execução dos projetos de API |

## 3. Visão geral da solução

A solução é 100% de configuração na plataforma Microsoft Azure — especificamente no **Azure API Management (APIM)**. Não há desenvolvimento de software ou interface de usuário pela Timeware nesta OS.

O portal do desenvolvedor (componente nativo do APIM) será configurado como catálogo corporativo de APIs, com acesso diferenciado para consumidores internos e externos.

**Resultado ao final desta OS:** Ambiente Azure API Management configurado e operacional com governança, workspaces por cliente (ArcelorMittal e Usiminas), catálogo corporativo e sandbox acessíveis e funcionais — validado em sessão de apresentação ao time técnico GASMIG.

## 4. Requisitos funcionais

| ID | Requisito | Prioridade | Critérios de aceite |
|---|---|---|---|
| RF-01 | Como gestor de APIs da GASMIG, quero que o Azure API Management esteja configurado com governança corporativa seguindo o padrão Microsoft, para garantir controle centralizado de todas as APIs presentes e futuras. | Alta | APIM provisionado; estrutura de produtos, assinaturas e grupos configurada; nomenclatura e políticas globais padronizadas conforme boas práticas Microsoft. |
| RF-02 | Como administrador de TI da GASMIG, quero gerenciar o controle de acesso por usuário com políticas de expiração e renovação de credenciais, para manter a segurança dos acessos ao longo do tempo. | Alta | Políticas de ciclo de vida de subscription keys configuradas; fluxo de expiração e renovação documentado e funcional no ambiente. |
| RF-03 | Como equipe de TI da GASMIG, quero barreiras de segurança para acesso pela rede corporativa interna, para garantir que usuários internos acessem apenas o que está autorizado para uso interno. | Alta | Política de segurança para tráfego interno configurada e validada; segregação de acesso interno/externo comprovada em teste. |
| RF-04 | Como equipe de TI da GASMIG, quero barreiras de segurança para acesso externo de parceiros e grandes clientes, para controlar quem pode consumir as APIs publicadas externamente. | Alta | Política de segurança para consumidores externos configurada; validação de credenciais e restrições de acesso externo funcionais. |
| RF-05 | Como desenvolvedor ou analista da GASMIG, quero um ambiente de sandbox configurado para testes e validações pré-produção, para testar integrações sem impactar o ambiente produtivo. | Alta | Ambiente sandbox provisionado e acessível; APIs de exemplo disponíveis para teste; segregação do ambiente produtivo comprovada. |
| RF-06 | Como consumidor interno ou externo de APIs da GASMIG, quero um catálogo corporativo de APIs com exibição padronizada, para descobrir, entender e assinar as APIs disponíveis. | Alta | Portal do desenvolvedor configurado com catálogo; layout e informações padronizados; acesso diferenciado por perfil (interno/externo) funcional. |
| RF-07 | Como equipe técnica da ArcelorMittal, quero um workspace dedicado no APIM da GASMIG, para consumir as APIs de forma segregada, com credenciais e políticas independentes dos demais clientes. | Alta | Workspace ArcelorMittal criado; produtos, assinaturas e grupos associados configurados; acesso isolado dos demais workspaces comprovado. |
| RF-08 | Como equipe técnica da Usiminas, quero um workspace dedicado no APIM da GASMIG, para consumir as APIs de forma segregada, com credenciais e políticas independentes dos demais clientes. | Alta | Workspace Usiminas criado; produtos, assinaturas e grupos associados configurados; acesso isolado dos demais workspaces comprovado. |
| RF-09 | Como gestor de APIs da GASMIG, quero políticas de rate limiting configuradas por workspace, para controlar o volume de requisições de cada cliente e proteger os backends. | Média | Rate limiting ativo por workspace (ArcelorMittal, Usiminas); limites configurados; comportamento de rejeição validado em teste. |
| RF-10 | Como gestor de APIs da GASMIG, quero políticas de throttling configuradas por workspace, para proteger o ambiente de picos de carga e garantir disponibilidade a todos os consumidores. | Média | Throttling configurado por workspace com limites definidos; comportamento de degradação graceful validado em teste. |

## 5. Requisitos não funcionais

| ID | Requisito não funcional | Critério |
|---|---|---|
| RNF-01 | Toda a configuração deve seguir as melhores práticas da Microsoft para Azure API Management e padrões internacionais de governança de APIs. | Configuração auditável contra checklist de boas práticas Microsoft/Azure (Azure Well-Architected Framework). |
| RNF-02 | Todo o trabalho deve ser realizado exclusivamente dentro da plataforma Microsoft Azure (tenant GASMIG), sem dependência de infraestrutura externa. | 100% dos recursos provisionados no Azure; nenhum componente fora do ecossistema Microsoft. |
| RNF-03 | O portal do Azure API Management deve suportar login automático via SAML com Entra ID da Microsoft (SSO corporativo GASMIG). | SSO via Entra ID configurado e funcional no portal do desenvolvedor APIM. |
| RNF-04 | A fundação deve ser escalável para receber novas APIs e novos workspaces de clientes sem reconfiguração da base existente. | Arquitetura documentada com workspaces e políticas parametrizáveis; evidência de que a adição de novo workspace não exige alteração das políticas globais. |
| RNF-05 | A configuração deve ser rastreável e versionada no repositório de configuração (IaC / Azure DevOps GASMIG). | Scripts e configurações armazenados no repositório Azure DevOps da GASMIG conforme combinado. |

## 6. Restrições e premissas

**Restrições:**
- Prazo máximo: 15 dias corridos a partir de 29/04/2026
- Plataforma: exclusivamente Microsoft Azure
- Pagamento: 100% condicionado ao aceite formal da GASMIG após sessão de validação
- Workspaces desta OS: ArcelorMittal e Usiminas (demais clientes em projetos futuros)

**Premissas:**
- A GASMIG dispõe de subscription Azure ativa e provisionará os acessos necessários ao time Timeware
- O tenant Entra ID da GASMIG suporta a configuração de SSO/SAML para o portal APIM
- As definições de nomenclatura de recursos Azure serão alinhadas com o time de TI GASMIG no início da execução
- Os requisitos técnicos de segurança (IPs de whitelist, políticas de rede) serão fornecidos pela GASMIG durante a execução

## 7. Validação dos requisitos

| Requisito/conjunto | Forma de validação | Data | Resultado |
|---|---|---|---|
| Escopo macro da OS-PARCELA-001 (RF-01 a RF-10) | Reuniões e e-mails de pré-venda (jan–abr/2026); DE ACORDO formal por e-mail em 29/04/2026 | 29/04/2026 | Validado — escopo aceito pelo Gestor do Contrato (Sérgio Villaça) |
| Detalhamento técnico e critérios de aceite | Sessão de apresentação ao time técnico GASMIG (Eduardo Yasuda, José Geraldo) | ~14/05/2026 | A realizar |

## 8. Confirmação de entendimento e compromisso

| Envolvido | Papel | Confirmação | Data |
|---|---|---|---|
| Sérgio Guimarães Villaça | Gestor do Contrato — GASMIG | Entendimento e aceite do escopo confirmados via e-mail (DE ACORDO) | 29/04/2026 |
| Abraão Oliveira | Gerente de Projeto — Timeware | Compromisso da equipe assumido | 29/04/2026 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 29/04/2026 | Abraão Oliveira / Cézar Hiraki | Versão inicial — requisitos baseados no escopo da OS-PARCELA-001 |
