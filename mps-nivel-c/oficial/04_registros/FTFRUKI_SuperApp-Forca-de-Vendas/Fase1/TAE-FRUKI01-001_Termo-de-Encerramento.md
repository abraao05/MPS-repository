# Termo de Encerramento e Aceite do Projeto — SuperApp Fruki · Pacote 1 — Módulo Metas e RV

| Campo | Valor |
|---|---|
| **Documento** | TAE-FRUKI01-001 |
| **Projeto** | SuperApp Fruki — Pacote 1 — Módulo Metas e Remuneração Variável |
| **Cliente** | Fruki Bebidas S.A. |
| **Versão** | 1.0 |
| **Data de encerramento** | Set/2025 |
| **Gerente de Projeto** | Abraão Oliveira |

---

## 1. Resumo do projeto

O Pacote 1 do SuperApp Fruki entregou o Módulo de Metas e Remuneração Variável (RV), permitindo que os representantes e supervisores comerciais da Fruki visualizem, em tempo real, seus indicadores de performance (volume por família, cobertura, drop size, positivação) e a composição de sua remuneração variável diretamente no aplicativo mobile.

O projeto foi executado de junho a setembro de 2025, com kickoff em 05/06/2025, levantamento formal de requisitos em 25/06/2025, acesso ao repositório Azure DevOps em 26/06/2025, piloto com vendedores selecionados em 05/08/2025 e encerramento após ajustes pós-piloto em setembro de 2025.

---

## 2. Entregas realizadas

| Entrega | Situação | Observação |
|---|---|---|
| Módulo Metas/RV — Tela de metas por família de produtos | Concluída | RF-01 — integração com API `/acompanhamentoMetasFamilias` |
| Módulo Metas/RV — Indicadores de cobertura, drop size e positivação | Concluída | RF-02 |
| Módulo Metas/RV — Composição de RV estimada por perfil | Concluída | RF-03 |
| Adaptação de telas por perfil de vendedor (representante / supervisor) | Concluída | RF-04 |
| Tratamento de latência de API e normalização de dados no front-end | Concluída | RNF-01 — deduplicação de famílias e ordenação alfabética |
| APK de teste gerado via Expo para piloto (05/08/2025) | Concluída | Distribuído para vendedores selecionados pela Fruki |
| Ajustes pós-piloto (duplicação de famílias, cálculo de positivação) | Concluída | Corrigidos após feedback do piloto |
| Pull Request entregue e mergeada no Azure DevOps Fruki | Concluída | Revisada e aprovada por Jardel Dargas Silva |

---

## 3. Escopo: planejado × realizado

Todos os itens previstos no PLA-FRUKI01-001 foram entregues. Não houve change requests ou expansão de escopo durante o Pacote 1.

| Item de escopo | Planejado | Realizado |
|---|---|---|
| RF-01 a RF-04 — Módulo Metas/RV | Sim | Sim |
| Integração com 4 APIs Fruki | Sim | Sim |
| Piloto com vendedores selecionados | Sim | Sim |
| Entrega via PR no Azure DevOps | Sim | Sim |
| APIs (responsabilidade Fruki) | Não incluído | Não aplicável |
| Versão iOS | Não incluído | Não aplicável |

---

## 4. Aceite do cliente

| Cliente / responsável | Aceite | Data | Ref. da ata |
|---|---|---|---|
| Leandro Lottermann (Coordenador de Sistemas — Fruki) | Aprovado | Set/2025 | Comunicação via e-mail / Teams após merge da PR e validação do piloto |
| Cecília Ribeiro (Analista Digital — Fruki) | Validado | Ago/Set 2025 | Validação dos ajustes pós-piloto com aprovação final |

---

## 5. Transição / sustentação

O código do Módulo Metas/RV foi entregue via Pull Request, revisado e mergeado por Jardel Dargas Silva no repositório Azure DevOps da Fruki (`https://dev.azure.com/fruki/superapp/_git/fruki-app.git`). A partir do merge, o código integra o codebase do SuperApp Fruki sob custódia da equipe de TI da Fruki. A Timeware não mantém ambiente de sustentação — novas demandas seguem nova proposta comercial.

Sequência natural: encerramento do Pacote 1 → abertura do Pacote Final 24 (out/2025), com continuidade na mesma base de código.

---

## 6. Lições aprendidas

| Tema | O que ocorreu | Lição / recomendação |
|---|---|---|
| Dependência de APIs externas | As APIs fornecidas pela Fruki apresentaram latência elevada (~3,10s) e retorno de dados duplicados; a Fruki não tinha disponibilidade para corrigir no prazo | Em projetos onde o back-end é responsabilidade do cliente, incluir no plano de projeto um sprint técnico inicial para validação das APIs antes do início do desenvolvimento das telas |
| Piloto revelou defeitos | A duplicação de famílias e o cálculo inconsistente de positivação foram identificados apenas no piloto (05/08/2025), não durante o desenvolvimento | Incluir cenários de teste com dados reais de API antes do APK de piloto; usar mocks que simulem casos extremos da API (duplicados, valores nulos) |
| Levantamento de regras de negócio via reunião | Uma reunião focada com Cecília (25/06/2025) foi suficiente para levantar e validar todas as regras de metas e RV do Pacote 1 | Reunião de levantamento estruturada com PO do cliente antes do início do desenvolvimento é suficiente para projetos de módulo único e bem delimitado |
| Parceria nova com fornecedor substituto | A Timeware assumiu um projeto já em andamento (SuperApp existente) sem documentação de arquitetura; o onboarding no codebase exigiu tempo adicional | Em projetos de substituição de fornecedor, solicitar ao cliente a documentação técnica e o acesso ao repositório pelo menos 1 semana antes do início do desenvolvimento |

---

## Registro de encerramento

| Evento | Data | Ref. |
|---|---|---|
| Piloto com vendedores selecionados | 05/08/2025 | APK gerado via Expo — feedback coletado |
| Ajustes pós-piloto e entrega final via PR | Ago/Set 2025 | Azure DevOps Fruki — PR revisada e mergeada por Jardel |
| Aceite do Pacote 1 | Set/2025 | E-mail / Teams — Leandro Lottermann |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 01/09/2025 | Abraão Oliveira | Versão inicial — registro retroativo (projeto executado jun–set/2025) |
