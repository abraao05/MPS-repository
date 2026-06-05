# Plano de Projeto — SuperApp Fruki · Pacote 1 — Módulo Metas e Remuneração Variável

| Campo | Valor |
|---|---|
| **Documento** | PLA-FRUKI01-001 |
| **Projeto** | SuperApp Fruki — Pacote 1 — Módulo Metas e Remuneração Variável |
| **Cliente** | Fruki Bebidas S.A. |
| **Contrato** | Pacote 1 — Metas/RV |
| **Versão** | 1.1 |
| **Data** | 05/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Identificação e objetivo do projeto

Desenvolver o Módulo de Metas e Remuneração Variável (RV) no SuperApp Fruki (React Native / Expo), assumindo o desenvolvimento como novo fornecedor. O módulo entrega visibilidade em tempo real aos representantes comerciais sobre seus indicadores de performance e composição de RV, integrando-se às APIs fornecidas pela equipe de TI da Fruki.

Detalhamento de escopo: ver `REQ-FRUKI01-001_Documento-de-Requisitos.md`.

## 2. Escopo (GPR 1)

- **Incluído:** RF-01 a RF-04 conforme REQ-FRUKI01-001 — telas de indicadores de volume, cobertura, drop size, positivação e metas por família/SKU; integração com APIs `/acompanhamentoMetasFamilias`, `/acompanhamentoMetasItens`, `/acompanhamentoForaDeRota`, `/acompanhamentoVisitas`; piloto com vendedores selecionados.
- **Não incluído:** Desenvolvimento de APIs (responsabilidade Fruki); Módulos Pedidos Não Alocados, Regra de Ouro e PDV (Pacote Final 24 — PLA-FRUKI01-002); versão iOS.

## 3. Adaptação do processo (GPR 2)

Detalhamento completo em `ADAP-FRUKI01-001_Registro-de-Adaptacao.md`. Resumo:

| Item de adaptação | Decisão | Justificativa |
|---|---|---|
| Design UX/UI | Aplicável — com UX/UI | Aplicativo mobile; protótipos validados com Cecília Ribeiro antes do desenvolvimento |
| Origem dos requisitos e design | Timeware elabora, cliente valida | Regras de negócio fornecidas por Cecília; Brenda conduz o design |
| Porte do projeto | Médio | Módulo único com múltiplos indicadores; equipe de 5 pessoas |
| Combinação de papéis | Abraão: GP + PO; Brenda: UX + analista | Equipe enxuta; viável dado o porte |
| Cadência de entrega | Por entrega incremental (APK + PR) | Entregas parciais ao cliente ao longo do desenvolvimento |
| Ambiente de stage | Expo APK + branch feature no Azure DevOps | Build de teste antes de cada merge |

## 4. Estimativas (GPR 3, 4)

- **Tamanho estimado:** ~60 story points

| Requisito | Complexidade | Story Points |
|---|---|---|
| RF-01 — Indicadores de volume por família de produtos | Alta | 13 |
| RF-02 — Indicadores de cobertura, drop size e positivação | Alta | 13 |
| RF-03 — Remuneração variável (RV) estimada por perfil | Alta | 13 |
| RF-04 — Adaptação de telas por perfil de vendedor | Média | 8 |
| Integração com 4 APIs Fruki + tratamento de performance | Média | 8 |
| Builds APK, pull request, ajustes de piloto | Baixa | 5 |
| **Total** | | **~60 SP** |

- **Velocity de referência:** ~30 SP/sprint (equipe de 2 devs front-end + 1 UX; sprints de 2 semanas)
- **Esforço/prazo estimado:** ~2 sprints / 6–8 semanas (jun–ago/2024)
- **Base histórica:** Projetos anteriores de desenvolvimento React Native na Timeware

## 5. Cronograma e marcos (GPR 5)

| Marco | Data prevista / realizada |
|---|---|
| Kickoff / proposta comercial | 05/06/2024 |
| Levantamento demanda Metas | 25/06/2024 |
| Acesso ao repositório Azure DevOps e APIs Fruki | 26/06/2024 |
| Desenvolvimento Módulo Metas/RV — Sprint 1 | Jul/2024 |
| Piloto com vendedores selecionados (APK de teste) | 05/08/2024 |
| Ajustes pós-piloto (duplicação de famílias, cálculos) | Ago/2024 |
| Aceite e encerramento do Pacote 1 | Ago/Set 2024 |

**Detalhamento das atividades:**

*Jun/2024:*
- Reunião de levantamento de demanda com Leandro e Cecília (25/06)
- Recebimento de acesso ao Azure DevOps e documentação das APIs (26/06)
- Criação de branch `feature/novos-recursos-superapp` no repositório Fruki
- Início da integração com APIs de metas

*Jul–Ago/2024:*
- Desenvolvimento das telas de indicadores (volume, cobertura, drop size, positivação)
- Desenvolvimento da tela de metas por família de produtos e por SKU
- Geração de APK de teste via Expo para piloto com vendedores selecionados
- Identificação e correção de problemas pós-piloto (ex.: duplicação de famílias, ordenação alfabética)
- Pull Request submetida ao repositório Fruki para revisão do Jardel

## 6. Recursos (GPR 6, 7)

**Equipe:**

| Papel | Responsável | Dedicação |
|---|---|---|
| Gerente de Projeto / Product Owner | Abraão Oliveira | Parcial (gestão e acompanhamento) |
| COO / Apoio Comercial | Tiago Nascimento | Parcial (reuniões e alinhamento) |
| UX/UI Designer / Analista de Negócio | Brenda Chrystie | Parcial (protótipos e regras de negócio) |
| Desenvolvedor Front-End React Native | Luca Watson | Integral (desenvolvimento) |
| Desenvolvedor Front-End React Native | Thiago Gomes | Integral (desenvolvimento) |
| GQA | COO (Operações) | Parcial (auditorias de processo) |

**Ambiente e ferramentas:**

| Ferramenta / Ambiente | Uso |
|---|---|
| React Native / Expo | Framework do aplicativo mobile |
| Azure DevOps (Fruki) | Repositório — `https://dev.azure.com/fruki` |
| APIs REST Fruki (`https://api.fruki.com.br/comercial/v1/`) | Dados de metas, visitas e fora de rota |
| Expo APK | Builds de teste para piloto |
| Microsoft Teams | Reuniões de acompanhamento com time Fruki |
| Google Meet | Reuniões de levantamento e alinhamento |
| E-mail corporativo | Comunicações formais |

## 7. Partes interessadas e comunicação (GPR 9)

| Parte interessada | Interesse | Comunicação |
|---|---|---|
| Leandro Lottermann (Fruki) | Aprovação e aceite das entregas | E-mail formal de status; alinhamentos pontuais |
| Cecília Ribeiro (Fruki) | Validação de regras de negócio e telas | Reuniões de levantamento e validação de protótipos |
| Jardel / Renan (Fruki) | Disponibilização e suporte às APIs | Comunicação técnica via e-mail e Teams |
| Brenda Chrystie (Timeware) | Design e análise de negócio | Daily interno; revisão de protótipos |
| Luca Watson / Thiago Gomes (Timeware) | Desenvolvimento | Daily interno; alinhamento técnico com Jardel |

## 8. Transição (GPR 8)

O código é entregue via Pull Request ao repositório Azure DevOps da Fruki, revisado e mergeado por Jardel. O APK de produção é gerado e publicado na Play Store pelo time Fruki após o aceite. Toda a infraestrutura permanece no Azure da Fruki — não há ambiente Timeware a descomissionar.

## 9. Riscos (GPR 10)

| # | Risco | Prob. | Impacto | Resposta |
|---|---|---|---|---|
| R-01 | APIs da Fruki não disponibilizadas no prazo | 3 | 3 | Trabalhar com mock de dados no front-end; solicitar prazo formal da API no início de cada sprint; escalar via Leandro se necessário |
| R-02 | Dados incorretos ou performance inadequada nas APIs (ex.: latência > 3s) | 3 | 2 | Identificar e reportar ao time Fruki; implementar cache local ou paginação no front-end como contorno |
| R-03 | Mudança de escopo durante o desenvolvimento | 2 | 2 | Registrar toda mudança via e-mail; avaliar impacto no prazo antes de aceitar |
| R-04 | Dificuldade de agenda para validação de protótipos com Cecília | 2 | 2 | Enviar protótipos com antecedência; reuniões de validação agendadas com antecedência |

## 10. Viabilidade (GPR 11)

Viável dentro do escopo e prazo: tecnologia conhecida (React Native), APIs documentadas e fornecidas pela Fruki, escopo bem delimitado ao Módulo Metas/RV. O principal risco é a dependência da disponibilização das APIs pelo time técnico da Fruki.

## 11. Aprovação do Plano (GPR 13)

Plano acordado na reunião de kickoff em 05/06/2024 e formalizado com o envio de acesso ao repositório em 26/06/2024.

| Envolvido | Papel | Aceite | Data | Ref. |
|---|---|---|---|---|
| Leandro Lottermann | Coordenador de Sistemas / Gestor — Fruki | Aprovado (e-mail — início formalizado) | 26/06/2024 | E-mail "ENC: Instruções para Acesso ao Repositório..." 26/06/2024 |
| Abraão Oliveira | Gerente de Projeto — Timeware | Confirmado | 26/06/2024 | ATA-FRUKI01-001 |

---

## Controle de atualizações do plano

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — registro retroativo |
| 1.1 | 05/06/2026 | Abraão Oliveira | Rescopo para Pacote 1 (Metas/RV apenas); e-mail Thiago Gomes corrigido; valores comerciais removidos |
