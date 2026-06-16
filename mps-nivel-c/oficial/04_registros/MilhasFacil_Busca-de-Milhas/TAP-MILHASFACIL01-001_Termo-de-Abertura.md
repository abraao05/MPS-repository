# Termo de Abertura do Projeto — MilhasFacil · Busca de Milhas

| Campo | Valor |
|---|---|
| **Documento** | TAP-MILHASFACIL01-001 |
| **Projeto** | MilhasFacil — Plataforma de Busca e Alerta de Passagens por Milhas |
| **Código do projeto** | MILHASFACIL01 |
| **Cliente** | Hub de Milhas |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.1 |
| **Data** | 15/06/2026 |
| **Situação** | Aprovado |
| **Gerente de Projeto** | Abraão |
| **Tech Lead / Arquiteto / DevOps** | Cézar Velazquez |
| **Processo MPS-SW** | GPR (evidência de projeto — Termo de Abertura) |

---

## 1. Objetivo do projeto

Desenvolver a plataforma MilhasFacil, uma solução de busca e alerta de passagens aéreas por milhas que consulta em paralelo os programas Smiles, Azul e Latam, registra o histórico de buscas do usuário e dispara alertas automáticos quando rotas favoritas atingem o preço-alvo em milhas. A solução é composta por três aplicações integradas: uma API REST em Spring Boot 3.2.5 / Java 21 (base `/api/v1`, autenticação JWT HS256 stateless), um front-end web em Angular 17.3 standalone e um serviço de crawler em FastAPI 0.111 / SeleniumBase 4.27.4 responsável pela raspagem das companhias. O sistema cobre cadastro e login com tokens de acesso e refresh, busca paralela com tempo médio de 8,3 s, histórico paginado, rotas favoritas com alertas via WhatsApp (Z-API) e controle de assinaturas.

## 2. Justificativa

O Hub de Milhas necessita de uma ferramenta própria que centralize a consulta de disponibilidade de passagens por milhas nas três principais companhias do mercado, hoje pesquisadas manualmente em portais distintos. A plataforma MilhasFacil elimina esse esforço manual ao paralelizar as buscas, persistir o histórico e notificar proativamente o usuário quando uma rota favorita atinge o limite de milhas desejado, agregando valor direto ao serviço prestado pelo Hub de Milhas a seus clientes.

## 3. Escopo macro

- **Incluído (RF01–RF15):**
  - RF01 — Cadastro de usuário com senha protegida por BCrypt
  - RF02 — Login com emissão de tokens JWT de acesso e refresh
  - RF03 — Busca paralela nas companhias Smiles, Azul e Latam
  - RF04 — SearchPage com skeleton de carregamento (Angular)
  - RF05 — Histórico de buscas paginado
  - RF06 — Rotas favoritas com configuração de alertas
  - RF07 — Perfil do usuário (GET/PATCH `/users/me`)
  - RF08 — Alertas agendados via Spring Scheduler
  - RF09 — Notificação WhatsApp via Z-API
  - RF10 — Assinaturas BASIC/PRO/ENTERPRISE
  - RF11 — Rotação de refresh token
  - RF12 — Logout com blacklist de jti em Redis
  - RF13 — Filtros avançados de busca (maxMiles / cabinType) — entregue na release v0.9.0 (main)
  - RF14 — Exportação de histórico em CSV UTF-8 com BOM — entregue na release v0.9.0 (main)
  - RF15 — Notificações push PWA

- **Não incluído:**
  - Telas de perfil, alertas e assinatura no front-end web (não há, no escopo atual, rotas dedicadas para esses fluxos)
  - Integração com programas de milhas além de Smiles, Azul e Latam

## 4. Equipe do projeto (Timeware)

| Papel | Responsável | Identificação / evidência no tooling |
|---|---|---|
| Gerente de Projeto (gestão; não codifica; fora do DevOps) | Abraão | Jira: conta a ser provisionada |
| Tech Lead / Arquiteto / DevOps (revisor de PR; no DevOps) | Cézar Velazquez | Jira `cezar.hiraki`; nas evidências legadas a aprovação de PR aparece sob `Mateus Veloso` e os commits de infra/arquitetura sob `Raony Chagas`/`Mateus Sousa` (= Cézar) |
| QA (teste manual; gera evidências; no DevOps) | Jonathan Alves | Jira/Azure: conta a ser provisionada (`jonathan@timeware.com.br`) |
| GQA independente (auditoria; não codifica; fora do DevOps) | Carol (Caroline) | (não assina issues) |
| Dev (no DevOps) | Felipe Santos | Jira `Felipe Siqueira` |
| Dev (no DevOps) | Lucas Batista | Jira `Lucas Batista de Sousa` |
| Dev (no DevOps) | Henry Oliveira | Jira `Henry Komatsu` |

> **DevOps (Azure) = 5 pessoas:** Cézar (TL) + Henry/Lucas/Felipe (devs) + Jonathan (QA). Abraão (GP) e Carol (GQA) ficam fora do DevOps. O aprovador de PR é **Cézar Velazquez (Tech Lead)**; quem aprova o escopo/CR é o **GP Abraão**.

> Nota de equivalência: em textos de gestão são usados os nomes reais do time atual. Quando uma evidência do Jira ou do Azure DevOps citar o autor/assignee/revisor de uma issue ou PR, é usada a conta legada registrada na API (a aprovação de PR sob a conta `Mateus Veloso` corresponde a Cézar; commits de infra/arquitetura sob `Raony Chagas`/`Mateus Sousa` correspondem a Cézar).

## 5. Partes interessadas

| Parte interessada | Papel |
|---|---|
| PO Hub de Milhas | Product Owner — Cliente (Hub de Milhas) |
| Abraão | Gerente de Projeto — Timeware |
| Cézar Velazquez | Tech Lead / Arquiteto / DevOps — Timeware |
| Carol (Caroline) | Auditora de Garantia da Qualidade (GQA independente) — Timeware |

## 6. Premissas e restrições iniciais

**Premissas:**
- Os programas Smiles, Azul e Latam mantêm os portais públicos acessíveis à raspagem pelo serviço de crawler (SeleniumBase).
- A Z-API permanece disponível para envio de notificações WhatsApp; falha no envio não interrompe o fluxo de alerta.
- O agente de CI Windows (Default) está disponível para execução das pipelines com tasks PowerShell@2.
- A planilha de gestão GEST-MILHASFACIL01-001 é a fonte da verdade de gestão do projeto.

**Restrições:**
- Equipe enxuta: GP (Abraão) que faz gestão e não codifica e fica fora do DevOps; GQA independente (Carol) que não codifica e fica fora do DevOps; um Tech Lead/Arquiteto/DevOps que revisa os PRs (Cézar Velazquez); QA de teste manual (Jonathan Alves); e três desenvolvedores efetivos (Felipe, Lucas, Henry). DevOps no Azure = 5 (Cézar + Henry/Lucas/Felipe + Jonathan).
- Autenticação stateless obrigatória (JWT HS256), CSRF desabilitado, sessão STATELESS; rotas públicas restritas a `/api/v1/auth/**` e `/actuator/health`.
- Política de branches: PR obrigatório para develop, aprovação de PR pelo Tech Lead (Cézar Velazquez), gate de CI e nomenclatura `feat/` ou `fix/` + `MF-XX`; branch policy de revisor (≥1 revisor) ativa em develop nos três repositórios. A aprovação de escopo/CR é do GP (Abraão).

## 7. Cronograma macro (Sprints S1–S12)

Modelo de sprints de 2 semanas. Início do projeto em 09/02/2026, término previsto em 26/07/2026.

| Sprint | Período | Foco macro |
|---|---|---|
| S1 | 09–22/02/2026 | Cadastro (RF01) e login JWT (RF02); SearchPage inicial |
| S2 | 23/02–08/03/2026 | Busca paralela Smiles/Azul/Latam (RF03); skeleton (RF04) |
| S3 | 09–22/03/2026 | Histórico paginado (RF05); rotas favoritas e alertas (RF06) |
| S4 | 23/03–05/04/2026 | Perfil (RF07); alertas Spring Scheduler (RF08); gate de cobertura ativado |
| S5 | 06–19/04/2026 | Assinaturas (RF10); rotação de refresh token (RF11) |
| S6 | 20/04–03/05/2026 | Estabilização e observabilidade |
| S7 | 04–17/05/2026 | Notificação WhatsApp Z-API (RF09) |
| S8 | 18–31/05/2026 | Logout blacklist Redis jti (RF12); correções de parsers |
| S9 | 01–14/06/2026 | Filtros avançados (RF13) e export CSV (RF14) entregues; airport ILIKE (MF-64); release v0.9.0 promovida a main |
| S10 | 15–28/06/2026 | Push PWA (RF15) |
| S11 | 29/06–12/07/2026 | Refinamentos e testes |
| S12 | 13–26/07/2026 | Fechamento e entrega |

**Status atual:** Sprint 9 em andamento (01–14/06/2026); projeto ABERTO (S9 de 12). Release **v0.9.0** promovida a main (tag nos três repositórios) em 15/06/2026, com RF13/RF14/MF-64 entregues.

## 8. Riscos iniciais

| ID | Risco | Prob. | Impacto | Exposição | Resposta / status |
|---|---|---|---|---|---|
| R-01 | Redesign das companhias quebra os parsers do crawler | 3 | 3 | 9 | Ocorreu na S8 (MF-59), corrigido |
| R-02 | Cobertura de testes abaixo de 80% | 3 | 3 | 9 | NC-001 (S2–S4), encerrada na S5 |
| R-03 | Indisponibilidade da Z-API | 2 | 2 | 4 | Fallback por e-mail; falha não interrompe o fluxo |
| R-04 | Mudança de escopo | 2 | 3 | 6 | Tratada via CR-MF-001 |
| R-05 | Pipeline de CI em agente Windows | 2 | 2 | 4 | Padronização com tasks PowerShell@2 |

---

## 9. Registro de abertura

| Item | Valor |
|---|---|
| Início do projeto | 09/02/2026 |
| Término previsto | 26/07/2026 |
| Situação na emissão | Aprovado — projeto ABERTO (Sprint 9 de 12 em andamento) |
| Processos no projeto | GPR · REQ · PCP · ITP · VV · GCO · MED · GDE · CAP · GQA(GPC) |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Emissão inicial — evidência do ciclo S1–S9 (MR-MPS-SW:2024 Nível C). |
| 1.1 | 15/06/2026 | Time de Melhoria Contínua | Correção do nome do plano de assinatura no RF10 (PREMIUM → PRO), alinhando ao enum real do código e ao REQ/PCP. |
