# Plano de Projeto — SuperApp Fruki · Novas Features Força de Vendas

| Campo | Valor |
|---|---|
| **Documento** | PLA-FRUKI01-001 |
| **Projeto** | SuperApp Fruki — Novas Features Força de Vendas |
| **Cliente** | Fruki Bebidas S.A. |
| **Contrato** | Pacote Final 24 |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Identificação e objetivo do projeto

Desenvolver e entregar novas funcionalidades no SuperApp Fruki — aplicativo mobile de força de vendas (React Native / Expo), utilizado pelos representantes e supervisores comerciais da Fruki Bebidas em campo. O projeto resolve a necessidade de maior visibilidade de indicadores de desempenho (Metas/RV), rastreabilidade de pedidos problemáticos (Não Alocados) e execução de PDV, substituindo relatórios manuais e planilhas por dados em tempo real no aplicativo.

Detalhamento de escopo e requisitos: ver `REQ-FRUKI01-001_Documento-de-Requisitos.md`.

## 2. Escopo (GPR 1)

- **Incluído:**
  - Módulo Metas/RV: indicadores de volume, cobertura, drop size, positivação, regra de ouro e remuneração variável por perfil de vendedor; integração com API Fruki de metas
  - Módulo Pedidos Não Alocados: painel com cards de clientes, filtros por data, geolocalização e mensageria; integração com API de pedidos não alocados
  - Módulo Regra de Ouro (Caixa Preta): visualização detalhada da composição de meta de RV, com gráficos e indicadores por família/SKU
  - Módulo PDV: formulário digital de pesquisa de ponto de venda com geolocalização, integração com API Rota PDV (`https://api.fruki.com.br/comercial/v1/`)
  - Entrega de APK para testes via Expo e builds para Play Store (AAB)
  - Pull Requests no repositório Azure DevOps da Fruki

- **Não incluído:**
  - Desenvolvimento das APIs de negócio (responsabilidade da equipe Fruki)
  - Infraestrutura Azure, DevOps pipeline, gestão de secrets
  - Versão iOS (Android first para o piloto)
  - Módulos fora do roadmap do Pacote Final 24 (gamificação, supervisores, etc.)

## 3. Adaptação do processo (GPR 2)

Detalhamento completo em `ADAP-FRUKI01-001_Registro-de-Adaptacao.md`. Resumo:

| Item de adaptação | Decisão | Justificativa |
|---|---|---|
| Design UX/UI | Aplicável — com UX/UI | Projeto de aplicativo mobile; Brenda Chrystie atua como designer com protótipos validados pelo cliente antes do desenvolvimento |
| Origem dos requisitos e do design | Timeware elabora, cliente valida | Levantamento de negócio conduzido pela Timeware com Cecília Ribeiro; APIs e regras de negócio fornecidas pela Fruki |
| Porte do projeto | Médio — nível de documentação padrão | Múltiplos módulos entregues ao longo de ~7 meses; equipe de 5 pessoas |
| Combinação de papéis | Abraão acumula GP + Product Owner; Brenda acumula UX + analista de requisitos | Equipe enxuta; viável dado o porte e a experiência dos envolvidos |
| Criticidade e regulação | Padrão | Aplicativo comercial interno sem regulação específica |
| Cadência de entrega ao cliente | Por módulo/feature (entrega incremental mensal) | Acordado na proposta: "em cada mês, até o fim de 2024, você terá 1 ou 2 features entregues" |
| Ambiente de stage | Adotado via Expo APK + branch feature no Azure DevOps | Builds de teste gerados via Expo antes de cada merge na branch principal |

## 4. Estimativas (GPR 3, 4)

> **Nota:** O valor comercial foi definido pelo setor comercial da Timeware (Pacote Final 24 — R$55.000). As estimativas abaixo sustentam o planejamento de capacidade e cronograma da equipe técnica.

- **Tamanho estimado:** ~130 story points (total do Pacote Final 24)

| Módulo / Feature | Complexidade | Story Points |
|---|---|---|
| Módulo Metas/RV — integração com APIs de indicadores | Alta | 21 |
| Módulo Metas/RV — tela de indicadores por perfil (vendedor/supervisor) | Alta | 13 |
| Módulo Pedidos Não Alocados — painel e cards | Média | 13 |
| Módulo Pedidos Não Alocados — filtros, geolocalização e mensageria | Média | 8 |
| Módulo Regra de Ouro (Caixa Preta) — visualização e gráficos | Alta | 13 |
| Módulo PDV — formulário pesquisa de PDV + geolocalização | Alta | 21 |
| Módulo PDV — integração API Rota PDV | Alta | 13 |
| Ajustes gerais e correções (pedidos não alocados no front-end) | Baixa | 5 |
| Builds APK/AAB, pull requests, versionamento (1.9.1 → 2.0) | Baixa | 5 |
| Documentação, verificação e aceite | — | 8 |
| Revisão de protótipos e alinhamentos com cliente | — | 10 |
| **Total** | | **~130 SP** |

- **Velocity de referência:** ~35 SP/sprint (equipe de 2 devs front-end + 1 UX; sprints de 2 semanas)
- **Esforço/prazo estimado:** ~4 sprints / 3–4 meses (out/2024 – jan/2025)
- **Base histórica utilizada:** Projetos anteriores de desenvolvimento React Native na Timeware; velocidade observada nas entregas parciais do próprio SuperApp Fruki (módulo Metas, jun–ago/2024)

## 5. Cronograma e marcos (GPR 5)

| Marco | Data prevista / realizada |
|---|---|
| Proposta comercial / Kickoff informal | 05/06/2024 |
| Levantamento demanda Metas (reunião formal) | 25/06/2024 |
| Início desenvolvimento Módulo Metas/RV | Jul/2024 |
| Piloto Módulo Metas/RV com vendedores selecionados | 05/08/2024 |
| Reunião demandas novas — Pedidos Não Alocados | 19/09/2024 |
| Apresentação proposta Pacote Final 24 | 26/09/2024 |
| Aprovação Pacote Final 24 / emissão NF (1/3) | 09/10/2024 |
| Kickoff formal Pacote Final 24 | 09/10/2024 |
| Entrega Módulo Pedidos Não Alocados + PR #57 | 25/10/2024 |
| Início desenvolvimento Módulo Regra de Ouro e PDV | Nov/2024 |
| Alinhamento Técnico e PDV | 02/12/2024 e 04/12/2024 |
| Status Report + entrega parcial | 27/12/2024 |
| Entrega final e aceite | 15/01/2025 |

**Detalhamento por fase:**

*Fase 1 — Módulo Metas/RV (Jun–Ago/2024):*
- Levantamento das regras de RV com Cecília e Leandro
- Integração com APIs de metas (volume, cobertura, drop size)
- Desenvolvimento das telas de indicadores no SuperApp
- Piloto com vendedores selecionados; ajustes e validação

*Fase 2 — Pacote Final 24 (Out/2024–Jan/2025):*
- Sprint 1 (out/2024): Pedidos Não Alocados — API integrada, painel, cards, filtros; entrega PR #57
- Sprint 2 (nov/2024): Regra de Ouro — protótipo validado com Cecília, desenvolvimento e telas de visualização de RV
- Sprint 3 (dez/2024): PDV — formulário, geolocalização, integração API Rota PDV; ajustes de branches
- Sprint 4 (jan/2025): Finalização, builds AAB/APK, versionamento 2.0, aceite formal

## 6. Recursos (GPR 6, 7)

**Equipe:**

| Papel | Responsável | Dedicação |
|---|---|---|
| Gerente de Projeto / Product Owner | Abraão Oliveira | Parcial (gestão, alinhamentos com cliente, definição de escopo) |
| COO / Apoio Comercial | Tiago Nascimento | Parcial (reuniões comerciais, financeiro) |
| UX/UI Designer / Analista de Negócio | Brenda Chrystie | Parcial (protótipos, levantamento de regras, validação com cliente) |
| Desenvolvedor Front-End React Native | Luca Watson | Integral (desenvolvimento) |
| Desenvolvedor Front-End React Native | Thiago Gomes | Integral (desenvolvimento) |
| GQA | COO (Operações) | Parcial (auditorias de processo) |

**Ambiente e ferramentas:**

| Ferramenta / Ambiente | Uso |
|---|---|
| React Native / Expo | Framework do aplicativo mobile |
| Azure DevOps (Fruki) | Repositório de código — `https://dev.azure.com/fruki/superapp/_git/fruki-app.git` |
| APIs REST Fruki (`https://api.fruki.com.br/comercial/v1/`) | Fonte de dados de negócio (metas, PDV, pedidos não alocados) |
| Expo APK / AAB | Build de testes e distribuição via Play Store |
| Google Meet | Reuniões de alinhamento com o cliente |
| Microsoft Teams | Reuniões de acompanhamento com time Fruki (ago/2024) |
| WhatsApp (grupo do projeto) | Comunicação ágil de alinhamentos técnicos |
| E-mail corporativo | Comunicações formais, atas e status reports |

## 7. Partes interessadas e comunicação (GPR 9)

| Parte interessada | Interesse | Comunicação |
|---|---|---|
| Leandro Lottermann (Fruki) | Aprovação e aceite formal de entregas; controle orçamentário | E-mail formal de status e proposta; presença em reuniões de aceite |
| Cecília Ribeiro (Fruki) | Validação de negócio, protótipos e regras de RV | Reuniões quinzenais recorrentes (Alinhamento de Negócio e Backlog — toda quarta 15h) |
| Jardel Dargas Silva (Fruki) | Integração técnica das APIs | Reuniões técnicas ad hoc; comunicação via e-mail e grupo WhatsApp |
| Renan Gustavo da Silva (Fruki) | Suporte técnico às APIs | Comunicação técnica via Jardel |
| Alexsandro de Vargas Braga (Fruki) | Requisitos do módulo PDV (pesquisa de execução de PDV) | Reunião específica para levantamento do formulário de PDV |
| Brenda Chrystie (Timeware) | Design e validação de UX | Daily interno; revisão de protótipos antes de cada entrega ao cliente |
| Luca Watson / Thiago Gomes (Timeware) | Desenvolvimento | Daily interno; alinhamento técnico com Jardel |

## 8. Transição (GPR 8)

O SuperApp Fruki é um produto em evolução contínua, de propriedade da Fruki Bebidas. Ao final de cada entrega, o código é integrado ao repositório Azure DevOps da Fruki via Pull Request, aprovada pelo time de TI do cliente (Jardel). A transição para operação é imediata após o merge e a publicação do build na Play Store. Não há ambiente Timeware a ser descomissionado — toda a infraestrutura permanece no Azure da Fruki. Pós-entrega do Pacote Final 24, eventuais novas demandas seguem nova proposta comercial.

## 9. Riscos (GPR 10)

| # | Risco | Prob. | Impacto | Resposta |
|---|---|---|---|---|
| R-01 | APIs da Fruki não disponibilizadas no prazo, bloqueando o desenvolvimento front-end | 3 | 3 | Trabalhar com mock de dados no front-end enquanto API não está disponível; solicitar prazo formal da API no início de cada sprint; escalar via Leandro se Jardel não responder |
| R-02 | Mudança de escopo durante a sprint (novas features solicitadas fora do Pacote Final 24) | 2 | 2 | Registrar toda mudança de escopo via e-mail e formalizar via nova proposta; manter backlog com Cecília atualizado quinzenalmente |
| R-03 | Atraso na validação de protótipos por parte do cliente (Cecília), impactando início do desenvolvimento | 2 | 2 | Reuniões recorrentes agendadas; protótipos enviados com antecedência mínima de 1 semana para revisão |
| R-04 | Problemas técnicos nas APIs (lentidão, dados incorretos, versão errada de branch) | 3 | 2 | Ambiente de staging com APK de teste; comunicação técnica rápida com Jardel; criar PR separada por feature para isolar problemas |
| R-05 | Restrições orçamentárias do cliente limitando escopo adicional | 2 | 2 | Manter rastreio de escopo vs. proposta; não iniciar trabalho fora do Pacote Final 24 sem aprovação comercial formal |
| R-06 | Dificuldade de agenda para aceite presencial (visita ao RS) | 2 | 2 | Agendar com antecedência mínima de 2 semanas; definir alternativa de aceite remoto se visita não for possível |

## 10. Viabilidade (GPR 11)

O projeto é viável dentro do escopo e prazo definidos, considerando:
- A equipe Timeware já possui familiaridade com o SuperApp Fruki e com as APIs do cliente (base do módulo Metas/RV desenvolvido em jun–ago/2024)
- As APIs são fornecidas pela equipe técnica da Fruki, com interlocutores técnicos identificados e engajados (Jardel e Renan)
- O orçamento de R$55.000 é suficiente para as features priorizadas no roadmap do Pacote Final 24
- O principal risco de prazo é a disponibilização das APIs pela Fruki — mitigado pelo trabalho com mocks e comunicação proativa

Viabilidade condicionada à disponibilização oportuna das APIs pelo time técnico da Fruki (R-01).

## 11. Aprovação do Plano (GPR 13)

O plano foi apresentado ao cliente na reunião de Apresentação da Proposta Pacote Final 24 em 26/09/2024. O aceite formal foi dado por Leandro Lottermann via e-mail subsequente, com início formalizado em 09/10/2024.

| Envolvido | Papel | Aceite | Data | Ref. |
|---|---|---|---|---|
| Leandro Lottermann | Coordenador de Sistemas / Gestor do Contrato — Fruki | Aprovado (via e-mail — proposta aceita) | 09/10/2024 | Proposta Comercial - FRUKI - Pacote final 24 v1.1.pdf; e-mail 09/10/2024 |
| Abraão Oliveira | Gerente de Projeto — Timeware | Confirmado | 09/10/2024 | Reunião Fireflies ID: HWwWGbMe3glWfXgl |

> A aprovação registrada acima estabelece a **baseline** do projeto. A partir dela, mudanças de escopo seguem o fluxo de change request (TPL-GPR-006).

---

## Controle de atualizações do plano

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — registro retroativo (projeto executado jun/2024–jan/2025) |
