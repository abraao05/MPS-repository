# Documento de Requisitos — SuperApp Fruki · Pacote Final 24

| Campo | Valor |
|---|---|
| **Documento** | REQ-FRUKI01-002 |
| **Projeto** | SuperApp Fruki — Pacote Final 24 |
| **Cliente** | Fruki Bebidas S.A. |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Responsáveis (Discovery)** | Abraão Oliveira (PO) / Brenda Chrystie (UX/Analista) |

---

## 1. Contexto e objetivo

Continuação do Pacote 1 (Módulo Metas/RV, jun–ago/2025). Com o módulo de metas em operação, a Fruki identificou três novas demandas prioritárias para fechar o roadmap 2025: (1) rastreabilidade de pedidos não alocados, que geravam retrabalho sem visibilidade para o vendedor em campo; (2) visualização detalhada da Regra de Ouro, a composição da caixa preta da remuneração variável; e (3) execução digital da pesquisa de PDV, substituindo formulários físicos por um processo digitalizado com geolocalização.

## 2. Partes interessadas

| Parte interessada | Necessidade principal |
|---|---|
| Vendedores (representantes) | Visualizar pedidos não alocados, Regra de Ouro e executar pesquisa de PDV no celular, em campo |
| Supervisores de vendas | Acompanhar a execução de PDV por rota |
| Cecília Ribeiro (Analista Digital — Fruki) | Validar regras de negócio de RV, Regra de Ouro e fluxo de não alocados |
| Leandro Lottermann (Coordenador de Sistemas — Fruki) | Encerrar o roadmap 2025 no prazo e dentro do escopo acordado |
| Jardel / Renan (Devs — Fruki) | Disponibilizar APIs de não alocados, Regra de Ouro e Rota PDV |
| Alexsandro de Vargas Braga (Responsável PDV — Fruki) | Digitalizar a pesquisa de execução de PDV com o formulário correto de perguntas |

## 3. Visão geral da solução

Três novos módulos no SuperApp Fruki (React Native / Expo), integrados às APIs REST fornecidas pela Fruki. Distribuição: APK de teste via Expo para validação; AAB para publicação na Play Store (versão 2.0). Código entregue via Pull Requests revisadas pelo Jardel no Azure DevOps.

## 4. Requisitos funcionais

### Módulo — Pedidos Não Alocados

| ID | Requisito (história) | Prioridade | Critérios de aceite |
|---|---|---|---|
| RF-05 | Como vendedor, quero visualizar a lista dos meus pedidos não alocados com informações do cliente e motivo de não alocação, para resolver pendências em campo | Alta | Painel exibe cards com: nome fantasia do cliente, localização, número do pedido e motivo de não alocação; dados via API; dados normalizados no front-end independentemente da estrutura retornada pela API |
| RF-06 | Como vendedor, quero filtrar os pedidos não alocados por data e cliente, para focar nas pendências mais relevantes | Média | Filtros funcionais por período e cliente; lista atualizada ao aplicar filtro |
| RF-07 | Como sistema, devo exibir mensageria informativa quando não houver pedidos não alocados | Baixa | Mensagem amigável exibida quando a lista estiver vazia |
| RF-08 | Como sistema, devo normalizar no front-end os dados de pedidos não alocados quando a API retornar formato não padrão | Alta | Manipulação no front-end React Native; pedidos exibidos corretamente independentemente do formato da API |

### Módulo — Regra de Ouro (Caixa Preta)

| ID | Requisito (história) | Prioridade | Critérios de aceite |
|---|---|---|---|
| RF-09 | Como vendedor, quero visualizar meus indicadores de Regra de Ouro (composição da "caixa preta" da RV), para entender quais indicadores impactam meu bônus | Alta | Tela exibe todos os indicadores da Regra de Ouro; progresso de cada indicador visível (real vs. meta); nome "Regra de Ouro" adotado (renomeado de "caixa preta") |
| RF-10 | Como vendedor, quero ver gráficos do progresso dos indicadores da Regra de Ouro, para identificar rapidamente onde estou abaixo da meta | Média | Gráficos circulares ou de barra por indicador; distinção visual entre indicadores acima e abaixo da meta |
| RF-11 | Como sistema, devo permitir pesquisa de SKUs dentro do módulo Regra de Ouro | Média | Campo de pesquisa funcional; resultado filtrado em tempo real |

### Módulo — PDV (Ponto de Venda) / Rota PDV

| ID | Requisito (história) | Prioridade | Critérios de aceite |
|---|---|---|---|
| RF-12 | Como vendedor, quero realizar a pesquisa de execução de PDV diretamente no SuperApp, para substituir o formulário físico por digital com geolocalização | Alta | Formulário digital disponível; perguntas conforme lista fornecida por Alexsandro; geolocalização capturada e enviada via API |
| RF-13 | Como sistema, devo integrar o módulo PDV com a API de Rota PDV, para que os dados sejam registrados no sistema central Fruki | Alta | Dados enviados corretamente para `https://api.fruki.com.br/comercial/v1/`; resposta de sucesso confirmada |
| RF-14 | Como vendedor, quero visualizar a rota do PDV (sequência de pontos de venda a visitar), para planejar minha jornada de field sales | Alta | Lista de PDVs da rota exibida; status de cada PDV indicado (visitado/pendente) |

## 5. Requisitos não funcionais

| ID | Requisito não funcional | Critério |
|---|---|---|
| RNF-01 | Versionamento do aplicativo | Versão incrementada para 2.0; AAB gerado para publicação na Play Store |
| RNF-02 | Geolocalização no PDV | Captura obrigatória de geolocalização no módulo PDV para validação da presença do vendedor |
| RNF-03 | Compatibilidade | Android first; React Native / Expo; Android 8.0+ |
| RNF-04 | Integração com repositório Fruki | Código entregue via PR no Azure DevOps; revisão e merge pelo Jardel |
| RNF-05 | Desempenho | Front-end trata e normaliza dados da API; exibição de loading state durante chamadas às APIs |

## 6. Restrições e premissas

**Restrições:**
- Tecnologia: React Native / Expo
- APIs são de responsabilidade exclusiva da Fruki; Timeware não altera backend
- Prazo máximo: aceite via Microsoft Teams em 15/01/2026
- Código sempre em branches separadas; merge somente após revisão do Jardel

**Premissas:**
- APIs de cada módulo disponibilizadas pelo time Fruki com antecedência mínima de 1 semana antes do início de cada sprint
- Cecília Ribeiro valida protótipos antes do desenvolvimento de cada módulo
- Alexsandro de Vargas Braga fornece a lista completa de perguntas do formulário de PDV antes do desenvolvimento
- A API de Rota PDV é fornecida por Jardel antes do início da sprint 3

## 7. Validação dos requisitos

| Requisito / conjunto | Forma de validação | Data | Resultado |
|---|---|---|---|
| RF-05 a RF-08 — Pedidos Não Alocados | Reunião "Entendimento novas demandas Fruki" + Apresentação Proposta Não Alocados | 19/09/2025 e 26/09/2025 | Validado — Leandro aprovou proposta; Cecília confirmou requisitos |
| RF-05 a RF-08 — Pedidos Não Alocados | Entrega via PR #57 no Azure DevOps | 25/10/2025 | Aceito pelo Jardel via merge da PR |
| RF-09 a RF-11 — Regra de Ouro | Reunião "Entendimento Demanda Caixa Preta" + prototipagem e revisão com Cecília | 09/10/2025 e 22/10/2025 | Validado — regras de composição de RV fornecidas; protótipo revisado |
| RF-12 a RF-14 — PDV / Rota PDV | Reunião "Demandas Fruki Bebidas" (Alexsandro) + Alinhamento PDV | 21/08/2025 e 04/12/2025 | Validado — formulário de perguntas confirmado; API Rota PDV recebida em 08/01/2026 |
| Todos os módulos — entrega final | Aceite via Microsoft Teams | 15/01/2026 | Aceito formalmente pelo cliente |

## 8. Confirmação de entendimento e compromisso

| Envolvido | Papel | Confirmação | Data |
|---|---|---|---|
| Leandro Lottermann | Gestor do Contrato — Fruki | Entendimento confirmado — proposta aprovada e aceite final via Teams | 09/10/2025 e 15/01/2026 |
| Cecília Ribeiro | Analista Digital / PO cliente — Fruki | Entendimento confirmado — validou protótipos e regras de cada módulo | Reuniões recorrentes out/2025–jan/2026 |
| Abraão Oliveira | Gerente de Projeto — Timeware | Compromisso assumido | 09/10/2025 |
| Brenda Chrystie | UX/Analista — Timeware | Compromisso assumido | 09/10/2025 |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 09/10/2025 | Abraão Oliveira | Versão inicial — registro retroativo (projeto executado out/2025–jan/2026) |
