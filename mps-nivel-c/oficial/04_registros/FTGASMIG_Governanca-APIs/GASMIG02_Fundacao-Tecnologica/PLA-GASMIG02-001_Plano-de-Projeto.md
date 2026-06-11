# Plano de Projeto — Fundação Tecnológica GASMIG · OS-PARCELA-001

| Campo | Valor |
|---|---|
| **Documento** | PLA-GASMIG02-001 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-001 |
| **Cliente** | GASMIG — Companhia de Gás de Minas Gerais |
| **Contrato** | Governança de APIs GASMIG |
| **Versão** | 1.2 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Identificação e objetivo do projeto

Configurar a Fundação Tecnológica de Integração da GASMIG sobre o Azure API Management, estabelecendo governança corporativa, controle de acesso, segurança segmentada (interno/externo), sandbox, catálogo corporativo e workspaces dedicados por cliente (ArcelorMittal e Usiminas). O resultado é uma plataforma reutilizável que elimina o retrabalho em futuros projetos de API da GASMIG.

Detalhamento de escopo: ver `REQ-GASMIG02-001_Documento-de-Requisitos.md`.

## 2. Escopo (GPR 1)

- **Incluído:** RF-01 a RF-10 e RNF-01 a RNF-05 conforme REQ-GASMIG02-001. Em síntese: governança APIM, controle de acesso, barreiras de segurança, sandbox, catálogo, workspaces ArcelorMittal/Usiminas, rate limiting, throttling e SSO via Entra ID.
- **Não incluído:** Azure Key Vault, OAuth 2.0 / API Keys, versionamento de APIs, monitoramento e alertas (escopo OS-PARCELA-002); desenvolvimento de APIs de negócio (projetos futuros).

## 3. Adaptação do processo (GPR 2)

Detalhamento completo em `ADAP-GASMIG02-001_Registro-de-Adaptacao.md`. Resumo:

| Item de adaptação | Decisão | Justificativa |
|---|---|---|
| Design UX/UI | Não aplicável | Projeto de infraestrutura/configuração cloud sem desenvolvimento de interface |
| Estratégia de integração de componentes | Não aplicável nesta OS | Não há integração entre componentes de software desenvolvidos |
| Nível de documentação | Padrão | Porte médio, escopo bem delimitado |
| Combinação de papéis | Cézar Hiraki acumula Tech Lead + Arquiteto + GCO | Equipe enxuta; viável dado o porte |
| Cadência de entrega | Por marco (aceite único da OS) | Não há sprints com entregas parciais ao cliente |

## 4. Estimativas e orçamento de horas (GPR 3, 4)

> **Nota:** O valor comercial (UST) é definido pelo setor comercial da Timeware e não deriva diretamente das estimativas de story points. As estimativas abaixo sustentam o planejamento de capacidade e prazo da equipe técnica.

- **Tamanho estimado:** 84 story points

| Requisito | Complexidade | Story Points |
|---|---|---|
| RF-01 — Governança corporativa APIM (estrutura global, políticas, nomenclatura) | Alta | 13 |
| RF-02 — Controle de acesso / ciclo de vida de credenciais | Média | 8 |
| RF-03 — Barreiras de segurança acesso interno | Média | 8 |
| RF-04 — Barreiras de segurança acesso externo | Média | 8 |
| RF-05 — Ambiente de sandbox | Média | 8 |
| RF-06 — Catálogo corporativo / portal do desenvolvedor | Alta | 13 |
| RF-07 — Workspace ArcelorMittal | Baixa-Média | 5 |
| RF-08 — Workspace Usiminas | Baixa-Média | 5 |
| RF-09 — Rate limiting por workspace | Baixa | 3 |
| RF-10 — Throttling por workspace | Baixa | 3 |
| RNF-03 — SSO SAML / Entra ID no portal APIM | Média | 8 |
| RNF-05 — IaC e versionamento no Azure DevOps | Baixa | 3 |
| Documentação, verificação, revisão por pares e sessão de aceite | — | 5 |
| **Total** | | **84 SP** |

- **Velocity de referência:** 56 SP/sprint (equipe de 2 engenheiros em regime integral + tech lead em dedicação parcial — base histórica de projetos de infraestrutura Azure Timeware)
- **Esforço/prazo estimado:** ~1,5 sprints / 15 dias corridos
- **Base histórica utilizada:** Projetos internos de configuração Azure da Timeware (infraestrutura cloud); velocity organizacional de referência para equipe de porte equivalente

**Orçamento de horas por papel:**

*Referência: 168 h/mês disponíveis por pessoa → ~140 h/mês efetivas (~70 h/sprint) após dedução de cerimônias e reuniões (~15%). Dedicação parcial proporcional.*

| Papel | Pessoas | Dedicação | h efetivas/sprint | Nº sprints | **h estimadas** |
|---|---|---|---|---|---|
| Gerente de Projeto / PO | 1 | 30% | 21 h | 1,5 | 32 h |
| Tech Lead / Arquiteto / GCO | 1 | 50% | 35 h | 1,5 | 53 h |
| Engenheiro Azure | 2 | 100% | 70 h | 1,5 | 210 h |
| GQA / COO | 1 | 10% | 7 h | 1,5 | 11 h |
| **Total** | | | | | **306 h** |

## 5. Cronograma e marcos (GPR 5)

| Marco | Data prevista |
|---|---|
| Kickoff — DE ACORDO formal | 29/04/2026 |
| Acesso da equipe Timeware ao Azure GASMIG | 30/04/2026 |
| Semana 1 — Governança APIM, controle de acesso, barreiras de segurança | 01/05–07/05/2026 |
| Semana 2 — Sandbox, catálogo, workspaces, rate limiting, SSO, IaC | 08/05–13/05/2026 |
| Revisão por pares (Cézar Hiraki) e preparação para aceite | 13/05/2026 |
| Sessão de apresentação e aceite com time técnico GASMIG | ~14/05/2026 |
| Encerramento OS-PARCELA-001 | 14/05/2026 |
| Início OS-PARCELA-002 | Após aceite da OS-PARCELA-001 |

**Detalhamento das atividades por semana:**

*Semana 1 (01/05–07/05):*
- Provisionamento da instância Azure API Management (modo externo + VNet)
- Configuração da estrutura global de governança: produtos, grupos, nomenclatura, políticas globais
- Configuração de controle de acesso por usuário e políticas de ciclo de vida de credenciais
- Configuração de barreiras de segurança: políticas de IP para tráfego interno (rede GASMIG) e externo

*Semana 2 (08/05–13/05):*
- Provisionamento e configuração do ambiente de sandbox (produto isolado + APIs de exemplo)
- Configuração do portal do desenvolvedor (catálogo corporativo, exibição padronizada, acesso interno/externo diferenciado)
- Criação e configuração dos workspaces ArcelorMittal e Usiminas (produtos, assinaturas, grupos)
- Configuração de políticas de rate limiting e throttling por workspace
- Configuração do SSO via SAML / Entra ID no portal do desenvolvedor
- Geração dos scripts IaC (Bicep/ARM) e armazenamento no Azure DevOps GASMIG
- Revisão por pares (Cézar Hiraki) e preparação da sessão de aceite

## 6. Recursos (GPR 6, 7)

**Equipe:**

| Papel | Responsável | Dedicação |
|---|---|---|
| Gerente de Projeto / Product Owner | Abraão Oliveira | Parcial (gestão e acompanhamento) |
| Tech Lead / Arquiteto / GCO | Cézar Hiraki | Parcial (decisões técnicas, revisão, configuração crítica) |
| Engenheiro Azure | Fernando Oliveira | Integral (execução da configuração) |
| Engenheiro Azure | João Victor Cruz Silva | Integral (execução da configuração) |
| GQA | COO (Operações) | Parcial (auditorias de processo) |

**Ambiente e ferramentas:**

| Ferramenta/Ambiente | Uso |
|---|---|
| Microsoft Azure — Azure API Management | Plataforma principal de entrega |
| Microsoft Entra ID (tenant GASMIG) | SSO e autenticação corporativa |
| Azure DevOps GASMIG | Repositório de scripts IaC (Bicep/ARM) |
| Microsoft Teams | Comunicação com o cliente (reuniões recorrentes semanais, quarta 14h) |
| E-mail corporativo | Comunicação formal e registro de decisões |

## 7. Partes interessadas e comunicação (GPR 9)

| Parte interessada | Interesse | Comunicação |
|---|---|---|
| Sérgio Villaça (GASMIG) | Acompanhamento executivo, aceite formal | E-mail semanal de status; presença na sessão de aceite |
| Eduardo Yasuda / José Geraldo (GASMIG) | Validação técnica da configuração | Reunião semanal recorrente (quarta 14h via Teams); sessão de aceite |
| Murilo Morgado (GASMIG) | Visibilidade sobre progresso | Incluído nas comunicações formais |
| Cézar Hiraki (Timeware) | Qualidade técnica e arquitetura | Daily interno; revisão técnica ao final da semana 2 |
| Fernando Oliveira / João Cruz (Timeware) | Execução | Daily interno; alinhamento contínuo com Cézar e Abraão |

## 8. Transição (GPR 8)

A entrega desta OS **é** a fundação — não há transição para um sistema legado. Ao final da OS-PARCELA-001, o ambiente Azure API Management configurado e operacional passa imediatamente ao controle da GASMIG (TI / Sérgio Villaça). A documentação técnica gerada (design, IaC, plano de V&V) é entregue ao cliente como parte do pacote de aceite.

A transição para a OS-PARCELA-002 ocorre automaticamente após o aceite formal desta OS.

## 9. Riscos (GPR 10)

| # | Risco | Prob. | Impacto | Resposta |
|---|---|---|---|---|
| R-01 | GASMIG demora a provisionar o acesso ao Azure, comprimindo o prazo de execução | 2 | 3 | Escalada imediata via Abraão → Sérgio Villaça; provisionar acesso como primeira ação; monitorar na virada do dia 1 |
| R-02 | Tenant Entra ID da GASMIG tem restrições de licenciamento que impedem o SSO/SAML no portal APIM | 2 | 2 | Verificar pré-condições técnicas na semana 1; documentar como limitação do ambiente cliente se não viável; propor alternativa |
| R-03 | Parâmetros de rede (IPs de whitelist, VNet, firewall) para barreiras interno/externo não fornecidos pela GASMIG a tempo | 3 | 2 | Solicitar formalmente por e-mail no dia 1; usar placeholder configurável e não bloquear demais entregas; ajustar quando recebido |
| R-04 | Solicitação de mudança de escopo durante a execução dos 15 dias | 2 | 3 | Formalizar qualquer mudança via Change Request (TPL-GPR-006); esclarecer ao cliente que mudanças de escopo requerem revisão formal de prazo |
| R-05 | GASMIG tem políticas internas de nomenclatura de recursos Azure não comunicadas, gerando retrabalho | 2 | 2 | Solicitar policy de nomenclatura no dia 1; usar convenção Timeware como padrão aprovado até receber o contrário |
| R-06 | Dificuldade de agenda para a sessão de aceite com o time técnico GASMIG dentro do prazo | 2 | 3 | Agendar sessão de aceite com antecedência mínima de 5 dias úteis (até 07/05); confirmar presença de Eduardo Yasuda e José Geraldo |

## 10. Viabilidade (GPR 11)

O projeto é viável dentro do escopo e prazo definidos, considerando:
- A equipe tem experiência comprovada em configuração Azure API Management (base das reuniões técnicas de pré-venda, jan–abr/2026)
- O escopo é bem delimitado e não envolve desenvolvimento de software
- O prazo de 15 dias é apertado mas atingível dado que (a) o discovery já foi concluído na pré-venda, (b) a equipe está dedicada e (c) não há dependências externas além do acesso Azure
- Os principais riscos (R-01, R-03) são mitigáveis por comunicação proativa com a GASMIG

Viabilidade condicionada à provisão oportuna de acesso Azure pela GASMIG (risco R-01).

## 11. Aprovação do Plano (GPR 13)

O plano é apresentado ao cliente na sessão de kickoff / comunicação formal de 29/04/2026 e entra em baseline com o DE ACORDO do Sérgio Villaça nesta mesma data.

| Envolvido | Papel | Aceite | Data | Ref. |
|---|---|---|---|---|
| Sérgio Guimarães Villaça | Gestor do Contrato — GASMIG | Aprovado (via e-mail — DE ACORDO) | 29/04/2026 | E-mail 29/04/2026 15:45 — ATA-GASMIG02-001 |
| Abraão Oliveira | Gerente de Projeto — Timeware | Confirmado | 29/04/2026 | ATA-GASMIG02-001 |

> A aprovação registrada acima estabelece a **baseline** do projeto. A partir dela, mudanças de escopo seguem o fluxo de change request (TPL-GPR-006).

---

## Controle de atualizações do plano

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 29/04/2026 | Abraão Oliveira | Versão inicial — baseline aprovada no kickoff |
| 1.1 | 05/06/2026 | Abraão Oliveira | Definição do papel de GQA como COO (Operações) no §6, conforme designação realizada antes da primeira auditoria |
| 1.2 | 11/06/2026 | Time de Melhoria Contínua | Acréscimo da tabela de orçamento de horas por papel em §4 (GPR 4) — 306 h totais estimadas; título do §4 atualizado para refletir GPR 3 e GPR 4 |
