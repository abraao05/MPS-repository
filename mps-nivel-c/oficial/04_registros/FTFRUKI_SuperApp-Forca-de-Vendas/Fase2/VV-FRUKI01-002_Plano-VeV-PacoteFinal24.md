# Plano de Verificação e Validação — SuperApp Fruki · Pacote Final 24

| Campo | Valor |
|---|---|
| **Documento** | VV-FRUKI01-002 |
| **Projeto** | SuperApp Fruki — Pacote Final 24 |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |

---

## 1. Itens a verificar e validar (VV 1)

| Item | Método |
|---|---|
| Módulo Pedidos Não Alocados (RF-05 a RF-08) | Testes manuais via APK Expo + revisão de PR (Jardel) + validação cliente |
| Módulo Regra de Ouro (RF-09 a RF-11) | Testes manuais via APK Expo + revisão de PR (Jardel) + validação cliente |
| Módulo PDV / Rota PDV (RF-12 a RF-14) | Testes manuais via APK Expo + revisão de PR (Jardel) + validação cliente |
| Requisitos RF-05 a RF-14 e RNF-01 a RNF-05 | Validação com Cecília Ribeiro, Alexsandro de Vargas Braga e Jardel |
| Build AAB versão 2.0 | Smoke test do AAB antes de enviar para publicação na Play Store |
| Documento de Requisitos (REQ-FRUKI01-002) | Revisão por pares (Abraão + Brenda) |

---

## 2. Métodos e critérios (VV 3)

- **Testes manuais do desenvolvedor:** execução dos cenários definidos neste plano em dispositivo Android físico antes de cada entrega; critério: cenários happy path sem erros; sad paths com mensagens amigáveis
- **APK de teste por módulo:** build Expo distribuído via link para Cecília validar antes do merge; critério: fluxo principal funcional conforme protótipo aprovado
- **Revisão de PR por Jardel:** cada módulo entregue via PR no Azure DevOps; critério: PR aprovada sem retrabalho estrutural
- **Validação de aceite final:** reunião via Microsoft Teams em 15/01/2026 com Leandro e Cecília; critério: aceite formal registrado em ata
- **Ambiente:** dispositivos Android físicos (Android 8.0+); builds APK (homologação) e AAB (produção)

---

## 3. Revisão por pares (VV 2)

O code review segue o mesmo processo do Pacote 1:

1. Desenvolvedor Timeware abre PR na branch do módulo correspondente no Azure DevOps
2. Jardel Dargas Silva revisa o código: padrões do projeto, performance, corretude da integração, autenticação e tratamento de erros
3. Aprovação de Jardel é pré-requisito para o merge
4. Revisão interna Timeware: Abraão revisa artefatos de processo; Brenda revisa telas antes da entrega ao cliente
5. PR #57 foi o primeiro merge do Pacote Final 24 (Módulo Pedidos Não Alocados — 25/10/2025)

---

## 4. Execução e registro (VV 4)

| Ciclo | Módulo | Itens verificados | Defeitos | Situação |
|---|---|---|---|---|
| Sprint 1 — Out/2025 | Pedidos Não Alocados | RF-05 a RF-08 | 1 — formato não padronizado da API de pedidos | Tratado no front-end (normalização em `pedidosNaoAlocadosService.ts`) |
| PR #57 — 25/10/2025 | Pedidos Não Alocados | Código do módulo | 0 | PR aprovada e mergeada por Jardel |
| Sprint 2 — Nov/2025 | Regra de Ouro | RF-09 a RF-11 | 0 | Módulo entregue conforme protótipo |
| PR Regra de Ouro | Regra de Ouro | Código do módulo | 0 | PR aprovada e mergeada por Jardel |
| Sprint 3 — Dez/2025–Jan/2026 | PDV / Rota PDV | RF-12 a RF-14 | 1 — API Rota PDV recebida apenas em 08/01/2026; desenvolvimento e integração finalizados após recebimento | Integração concluída em Jan/2026 |
| Build AAB v2.0 | Todos os módulos | RNF-01, RNF-03 | 0 | AAB gerado e entregue para publicação |
| Aceite final — 15/01/2026 | Todos os módulos | RF-05 a RF-14 | 0 | Aceite formal via Microsoft Teams |

---

## 5. Análise e comunicação dos resultados (VV 5)

Os defeitos encontrados foram comunicados via WhatsApp (alinhamentos técnicos ágeis) e e-mail (registros formais). Nenhum defeito escapou para produção. O atraso da API de Rota PDV (recebida apenas em 08/01/2026) foi gerenciado com desenvolvimento paralelo da interface antes da integração. Os resultados alimentam os indicadores M5 e M6 do PLA-MED-001.

---

## 6. Cenários de teste (Gherkin) e evidências

```gherkin
Funcionalidade: Módulo Pedidos Não Alocados

  Cenário: Visualizar lista de pedidos não alocados — happy path
    Dado que o vendedor está autenticado no SuperApp Fruki
    Quando acessa o módulo Pedidos Não Alocados
    Então vê cards com: nome fantasia do cliente, localização, número do pedido e motivo de não alocação
    E os dados são carregados da API

  Cenário: Filtrar pedidos por data e cliente — happy path
    Dado que o vendedor está na tela de Pedidos Não Alocados
    Quando aplica filtro por período ou cliente
    Então a lista é atualizada exibindo apenas os pedidos que correspondem ao filtro

  Cenário: Lista vazia de pedidos não alocados — sad path
    Dado que não há pedidos não alocados para o vendedor
    Quando acessa o módulo Pedidos Não Alocados
    Então uma mensagem informativa amigável é exibida

  Cenário: API retorna formato não padronizado — sad path
    Dado que a API de pedidos não alocados retorna dados em formato não padronizado
    Quando o front-end processa a resposta
    Então os dados são normalizados e exibidos corretamente na tela

Funcionalidade: Módulo Regra de Ouro

  Cenário: Visualizar composição da Regra de Ouro — happy path
    Dado que o vendedor está autenticado
    Quando acessa o módulo Regra de Ouro
    Então vê todos os indicadores da Regra de Ouro com progresso real vs. meta
    E gráficos circulares distinguem indicadores acima e abaixo da meta

  Cenário: Pesquisar SKU na Regra de Ouro — happy path
    Dado que o vendedor está na tela Regra de Ouro
    Quando digita um SKU no campo de pesquisa
    Então a lista de indicadores é filtrada em tempo real mostrando apenas o SKU pesquisado

Funcionalidade: Módulo PDV / Rota PDV

  Cenário: Visualizar rota do PDV — happy path
    Dado que o vendedor está autenticado
    Quando acessa o módulo Rota PDV
    Então vê a lista de PDVs da sua rota com status (visitado/pendente)

  Cenário: Realizar pesquisa de execução de PDV — happy path
    Dado que o vendedor está em um PDV pendente
    Quando acessa o formulário de pesquisa e responde todas as perguntas
    E o GPS está ativo e a geolocalização foi capturada
    Quando confirma o envio
    Então os dados são enviados para a API de Rota PDV com sucesso
    E o status do PDV muda para "visitado"

  Cenário: Tentar enviar formulário PDV sem GPS — sad path
    Dado que o GPS do dispositivo está desativado
    Quando tenta enviar o formulário de pesquisa de PDV
    Então o envio é bloqueado
    E uma mensagem solicita a ativação do GPS para validar a presença
```

| Cenário | Tipo | Evidência | Situação |
|---|---|---|---|
| Lista de pedidos não alocados — happy path | Happy | APK Sprint 1 — validado por Cecília out/2025 | Aprovado |
| Filtros por data e cliente | Happy | APK Sprint 1 — validado por Cecília | Aprovado |
| Lista vazia | Sad | Testado com mock de resposta vazia | Aprovado |
| Normalização de formato não padronizado | Sad | Validado durante desenvolvimento Sprint 1 | Aprovado |
| Regra de Ouro — indicadores e gráficos | Happy | APK Sprint 2 — validado por Cecília nov/2025 | Aprovado |
| Pesquisa de SKU em tempo real | Happy | APK Sprint 2 — testado com lista real | Aprovado |
| Rota PDV — lista de PDVs | Happy | Validado após recebimento da API (Jan/2026) | Aprovado |
| Formulário PDV com geolocalização | Happy | APK Sprint 3 — testado em campo | Aprovado |
| Formulário PDV sem GPS | Sad | Testado com GPS desativado no dispositivo | Aprovado |
| Build AAB v2.0 | — | AAB gerado e entregue para publicação na Play Store | Aprovado |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 09/10/2025 | Abraão Oliveira | Versão inicial — registro retroativo (projeto executado out/2025–jan/2026) |
