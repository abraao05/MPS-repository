# Documento de Requisitos — SuperApp Fruki · Novas Features Força de Vendas

| Campo | Valor |
|---|---|
| **Documento** | REQ-FRUKI01-001 |
| **Projeto** | SuperApp Fruki — Novas Features Força de Vendas |
| **Cliente** | Fruki Bebidas S.A. |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Responsáveis (Discovery)** | Abraão Oliveira (PO) / Brenda Chrystie (UX/Analista) |

---

## 1. Contexto e objetivo

A Fruki Bebidas opera uma extensa rede de representantes e supervisores comerciais em campo (Rio Grande do Sul e demais estados). Esses profissionais utilizam o SuperApp Fruki — aplicativo mobile React Native / Expo — para acompanhar sua performance diária de vendas.

O problema central é a falta de visibilidade dos vendedores sobre seus próprios indicadores de desempenho e remuneração variável (RV) em tempo real. O relatório de planejamento diário existia apenas em formato de planilha/relatório web, inacessível em campo. Adicionalmente, pedidos não alocados a clientes geravam retrabalho sem rastreabilidade e a execução de PDV era feita com formulários físicos sem integração digital.

O objetivo deste projeto é desenvolver quatro módulos no SuperApp que resolvam esses problemas: (1) Metas e Remuneração Variável, (2) Pedidos Não Alocados, (3) Regra de Ouro (Caixa Preta) e (4) PDV / Rota PDV.

## 2. Partes interessadas

| Parte interessada | Necessidade principal |
|---|---|
| Vendedores (representantes comerciais) | Visualizar suas metas, indicadores de RV e pedidos não alocados em tempo real no celular, em campo |
| Supervisores de vendas | Acompanhar a performance da equipe e a execução de PDV por rota |
| Cecília Ribeiro (Analista Digital — Fruki) | Garantir que as regras de negócio de RV e metas estejam corretamente implementadas |
| Leandro Lottermann (Coordenador de Sistemas — Fruki) | Evolução do SuperApp dentro do orçamento e roadmap aprovado |
| Jardel Dargas Silva (Dev Jr — Fruki) | Integração correta entre as APIs desenvolvidas pela Fruki e o front-end Timeware |
| Alexsandro de Vargas Braga (Responsável Comercial PDV — Fruki) | Digitalizar e geolocalizar a pesquisa de execução de PDV |

## 3. Visão geral da solução

Evolução do SuperApp Fruki (React Native / Expo, repositório Azure DevOps) com quatro novos módulos de interface móvel, integrados às APIs REST da Fruki (`https://api.fruki.com.br/comercial/v1/`). O aplicativo já existia com funcionalidades básicas; as novas features são adicionadas via Pull Requests revisadas pelo time técnico da Fruki.

A solução envolve:
- UX/UI: protótipos em Figma validados com Cecília Ribeiro antes de cada sprint de desenvolvimento
- Integração com APIs: REST fornecidas pela Fruki (Jardel/Renan) com documentação Swagger
- Distribuição: APK de teste via Expo para validação; AAB para publicação na Play Store (versão 2.0)

## 4. Requisitos funcionais

### Módulo 1 — Metas e Remuneração Variável (RV)

| ID | Requisito | Prioridade | Critérios de aceite |
|---|---|---|---|
| RF-01 | Como vendedor, quero visualizar meu percentual de atingimento de meta de volume por família de produtos no SuperApp, para acompanhar minha performance em campo | Alta | Tela exibe volume real, meta e percentual de atingimento por família; dados atualizados conforme API; famílias ordenadas alfabeticamente |
| RF-02 | Como vendedor, quero visualizar indicadores de cobertura, drop size e positivação, para entender minha performance multidimensional | Alta | Todos os indicadores exibidos na tela de metas; valores calculados conforme regras de negócio da Fruki |
| RF-03 | Como vendedor, quero visualizar minha remuneração variável (RV) estimada com base nos indicadores atingidos, para projetar meu ganho mensal | Alta | Cálculo de RV exibido conforme composição de metas por perfil de vendedor (cada perfil tem composição diferente de indicadores) |
| RF-04 | Como sistema, devo adaptar a visualização de indicadores e composição de RV conforme o perfil do vendedor logado (vendedor padrão, representante, etc.) | Alta | Tela de metas adapta indicadores exibidos ao perfil do usuário; regras de composição por perfil confirmadas por Cecília Ribeiro |

### Módulo 2 — Pedidos Não Alocados

| ID | Requisito | Prioridade | Critérios de aceite |
|---|---|---|---|
| RF-05 | Como vendedor, quero visualizar a lista de meus pedidos não alocados a clientes, com informações do cliente e motivo de não alocação, para resolver pendências em campo | Alta | Painel exibe cards por pedido com: nome fantasia do cliente, localização, número do pedido e motivo de não alocação; dados via API |
| RF-06 | Como vendedor, quero filtrar os pedidos não alocados por data e cliente, para focar nas pendências mais relevantes | Média | Filtros funcionais por período e por cliente; atualização da lista ao aplicar filtro |
| RF-07 | Como sistema, devo exibir mensageria informativa quando não houver pedidos não alocados, para que o vendedor saiba que está em dia | Baixa | Mensagem amigável exibida quando a lista de não alocados estiver vazia |
| RF-08 | Como vendedor, quero que os dados de pedidos não alocados sejam corretamente normalizados no front-end quando a API retornar dados em formato não padrão | Alta | Manipulação de dados realizada no front-end React Native; pedidos exibidos corretamente independentemente da estrutura retornada pela API |

### Módulo 3 — Regra de Ouro (Caixa Preta)

| ID | Requisito | Prioridade | Critérios de aceite |
|---|---|---|---|
| RF-09 | Como vendedor, quero visualizar meus indicadores de Regra de Ouro (composição da "caixa preta" da RV), para entender quais indicadores impactam meu bônus de remuneração variável | Alta | Tela exibe todos os indicadores que compõem a Regra de Ouro; progresso de cada indicador visível (real vs. meta); nome "Regra de Ouro" adotado (renomeado de "caixa preta") |
| RF-10 | Como vendedor, quero ver representações visuais (gráficos) do progresso dos indicadores da Regra de Ouro, para identificar rapidamente onde estou abaixo da meta | Média | Gráficos circulares ou de barra exibidos por indicador; distinção visual entre indicadores acima e abaixo da meta |
| RF-11 | Como sistema, devo permitir pesquisa de SKUs dentro do módulo Regra de Ouro, para que o vendedor encontre produtos específicos na composição de suas metas | Média | Campo de pesquisa funcional para SKUs na tela; resultado filtrado em tempo real |

### Módulo 4 — PDV (Ponto de Venda) / Rota PDV

| ID | Requisito | Prioridade | Critérios de aceite |
|---|---|---|---|
| RF-12 | Como vendedor, quero realizar a pesquisa de execução de PDV diretamente no SuperApp, para substituir o formulário físico por um digital com geolocalização | Alta | Formulário digital de pesquisa de PDV disponível no app; perguntas do formulário conforme lista fornecida por Alexsandro; geolocalização capturada e enviada via API |
| RF-13 | Como sistema, devo integrar o módulo PDV com a API de Rota PDV (`https://api.fruki.com.br/comercial/v1/`), para que os dados de pesquisa sejam registrados no sistema central Fruki | Alta | Dados do formulário enviados corretamente para a API; resposta de sucesso confirmada; logs de erros tratados |
| RF-14 | Como vendedor, quero visualizar a rota do PDV (sequência de pontos de venda a visitar), para planejar minha jornada de field sales | Alta | Lista de PDVs da rota exibida; status de cada PDV indicado (visitado/pendente); integração com API Rota PDV |

## 5. Requisitos não funcionais

| ID | Requisito não funcional | Critério |
|---|---|---|
| RNF-01 | Desempenho da API de metas | Tempo de resposta aceitável para o usuário mobile; otimizações no front-end para compensar latência da API (identificada como ~3,10s para 5 pedidos inicialmente) |
| RNF-02 | Compatibilidade | Android primeiro (piloto); React Native / Expo compatível com dispositivos dos representantes; versão mínima Android 8.0 |
| RNF-03 | Versionamento do aplicativo | Versão incrementada de 1.9.1 para 2.0 no pacote final; AAB gerado para publicação na Play Store |
| RNF-04 | Integração com repositório Fruki | Todo código entregue via Pull Request no Azure DevOps (`https://dev.azure.com/fruki/superapp/_git/fruki-app.git`); revisão e merge pelo Jardel antes da publicação |
| RNF-05 | Confiabilidade da geolocalização | Geolocalização capturada obrigatoriamente no módulo PDV para validação da presença do vendedor no local |
| RNF-06 | UX adaptada ao contexto de campo | Interface simples, com elementos grandes e leitura fácil em dispositivos mobile; cores seguindo identidade visual Fruki |

## 6. Restrições e premissas

**Restrições:**
- Tecnologia obrigatória: React Native / Expo (arquitetura do SuperApp existente)
- APIs são de responsabilidade exclusiva da Fruki (Jardel/Renan); a Timeware não altera a camada de backend
- Qualquer manipulação necessária nos dados da API deve ser feita no front-end
- O desenvolvimento não pode bloquear a branch principal do repositório Fruki; todas as features em branches separadas

**Premissas:**
- As APIs serão disponibilizadas pelo time Fruki com antecedência mínima de 1 semana antes do início da sprint de cada módulo
- Cecília Ribeiro valida os protótipos de UX antes do início do desenvolvimento de cada módulo
- Leandro Lottermann e Cecília Ribeiro têm autoridade para validar os critérios de aceite de cada entrega
- As regras de composição de RV por perfil de vendedor serão fornecidas por Cecília em formato estruturado antes do desenvolvimento do Módulo 1

## 7. Validação dos requisitos

| Requisito / conjunto | Forma de validação | Data | Resultado |
|---|---|---|---|
| RF-01 a RF-04 — Módulo Metas/RV | Reunião "Levantamento demanda Metas" + prototipagem com Cecília | 25/06/2024 | Validado — regras de negócio levantadas; Leandro e Cecília confirmaram estrutura |
| RF-01 a RF-04 — Módulo Metas/RV | Piloto com vendedores selecionados (APK de teste) | 05/08/2024 | Validado com ajustes — identificado problema de duplicação de famílias; corrigido |
| RF-05 a RF-08 — Pedidos Não Alocados | Reunião "Entendimento novas demandas Fruki" + Apresentação Proposta Não Alocados | 19/09/2024 e 26/09/2024 | Validado — Leandro aprovou proposta e escopo; Cecília confirmou requisitos |
| RF-05 a RF-08 — Pedidos Não Alocados | Entrega via PR #57 no Azure DevOps | 25/10/2024 | Aceito pelo Jardel via merge da PR |
| RF-09 a RF-11 — Regra de Ouro | Reunião "Entendimento Demanda Caixa Preta" + prototipagem Brenda | 09/10/2024 e 22/10/2024 | Validado — Cecília forneceu regras de composição de RV; protótipo revisado |
| RF-12 a RF-14 — PDV / Rota PDV | Reunião "Demandas Fruki Bebidas" com Alexsandro + Alinhamento PDV | 21/08/2024 e 04/12/2024 | Validado — formulário de perguntas fornecido por Alexsandro; API Rota PDV compartilhada por Jardel (08/01/2025) |
| Entrega final — todos os módulos | Status report + aceite presencial (RS) | Jan/2025 | Aceito formalmente |

## 8. Confirmação de entendimento e compromisso

| Envolvido | Papel | Confirmação | Data |
|---|---|---|---|
| Cecília Ribeiro | Analista Digital / PO cliente — Fruki | Entendimento confirmado — validou protótipos e regras de negócio de cada módulo | Reuniões recorrentes out/2024–jan/2025 |
| Leandro Lottermann | Coordenador de Sistemas / Gestor do Contrato — Fruki | Entendimento confirmado — aprovou proposta e aceite final | 09/10/2024 e jan/2025 |
| Abraão Oliveira | Gerente de Projeto — Timeware | Compromisso assumido — gestão das entregas dentro do Pacote Final 24 | 09/10/2024 |
| Brenda Chrystie | UX/Analista — Timeware | Compromisso assumido — protótipos e levantamento de regras de negócio | 09/10/2024 |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — registro retroativo (projeto executado jun/2024–jan/2025) |
