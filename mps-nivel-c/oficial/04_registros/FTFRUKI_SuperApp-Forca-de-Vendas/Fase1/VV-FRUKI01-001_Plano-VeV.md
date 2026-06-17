# Plano de Verificação e Validação — SuperApp Fruki · Pacote 1 — Módulo Metas e RV

| Campo | Valor |
|---|---|
| **Documento** | VV-FRUKI01-001 |
| **Projeto** | SuperApp Fruki — Pacote 1 — Módulo Metas e Remuneração Variável |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |

---

## 1. Itens a verificar e validar (VV 1)

| Item | Método |
|---|---|
| Módulo Metas/RV — telas e integração com APIs | Testes manuais via APK + revisão técnica de PR |
| Requisitos RF-01 a RF-04 | Validação com cliente (Cecília Ribeiro) — piloto com vendedores selecionados |
| Documento de Requisitos (REQ-FRUKI01-001) | Revisão por pares (Abraão + Brenda) |
| Documento de Design (PCP-FRUKI01-001) | Revisão por pares (Abraão + Luca) |
| Build APK de teste | Smoke test em dispositivo Android antes de compartilhar com cliente |

---

## 2. Métodos e critérios (VV 3)

- **Testes manuais do desenvolvedor:** execução dos cenários definidos neste plano em dispositivo Android físico; critério de aprovação: todos os cenários happy path executados sem erros; sad paths com mensagens amigáveis conforme definido
- **APK de piloto:** build distribuído via Expo para vendedores selecionados pela Fruki; critério: fluxo principal utilizável sem travamentos ou dados incorretos
- **Revisão de PR:** Jardel Dargas Silva (Fruki) revisa o código antes do merge na branch principal; critério: PR aprovada e mergeada sem solicitações de retrabalho estrutural
- **Ambiente:** dispositivos Android físicos (Android 8.0+) fornecidos pela equipe Timeware e pelos vendedores selecionados no piloto

---

## 3. Revisão por pares (VV 2)

O code review é conduzido via Pull Request no Azure DevOps da Fruki:

1. Desenvolvedor Timeware (Luca Watson ou Thiago Gomes) abre PR na branch `feature/novos-recursos-superapp`
2. Jardel Dargas Silva (Fruki) revisa o código quanto a: padrões existentes do projeto, performance, segurança da autenticação e corretude da integração com as APIs
3. Aprovação de Jardel é pré-requisito para o merge
4. Revisão interna Timeware: Abraão revisa artefatos de processo; Brenda revisa telas antes da entrega ao cliente

---

## 4. Execução e registro (VV 4)

Resultados registrados neste documento e referenciados no TAE-FRUKI01-001 (Termo de Encerramento).

| Ciclo | Itens verificados | Defeitos encontrados | Situação |
|---|---|---|---|
| Desenvolvimento Sprint 1 (Jul/2025) | RF-01, RF-02, RF-03, RF-04, RNF-01 a RNF-04 | 2 — duplicação de famílias na API; latência ~3,10s | Tratados no front-end antes do piloto |
| Piloto (05/08/2025) | Todos os RFs — fluxo completo com vendedores reais | 2 — duplicação visível residual; cálculo de positivação inconsistente | Corrigidos antes do aceite (Ago/2025) |
| Revisão de PR — Jardel | Todos os RFs + código | 0 | PR aprovada e mergeada |
| Aceite final | Todos os RFs | 0 | Aceite concluído |

---

## 5. Análise e comunicação dos resultados (VV 5)

Os defeitos encontrados no piloto foram comunicados por Cecília Ribeiro via reuniões de alinhamento e tratados antes do aceite formal. Nenhum defeito escapou para produção. Os resultados alimentam o indicador M6 (defeitos em homologação × produção) do PLA-MED-001.

---

## 6. Cenários de teste (Gherkin) e evidências

```gherkin
Funcionalidade: Tela de Metas por Família de Produtos

  Cenário: Visualizar metas de volume por família — happy path
    Dado que o vendedor está autenticado no SuperApp Fruki
    Quando acessa a tela de Metas
    Então vê a lista de famílias de produtos ordenada alfabeticamente
    E cada família exibe: volume real, meta do mês e percentual de atingimento
    E os dados refletem o período atual

  Cenário: API retorna famílias duplicadas — sad path
    Dado que a API retorna registros duplicados para uma mesma família
    Quando o front-end processa a resposta
    Então apenas um registro por família é exibido na tela
    E a ordenação alfabética é mantida

  Cenário: API demora mais de 3 segundos — sad path
    Dado que o vendedor acessa a tela de Metas
    Quando a resposta da API leva mais de 1 segundo
    Então um indicador de carregamento (skeleton screen) é exibido
    E os dados aparecem corretamente após o carregamento completo

Funcionalidade: Indicadores de Cobertura, Drop Size e Positivação

  Cenário: Visualizar indicadores multidimensionais — happy path
    Dado que o vendedor está autenticado
    Quando acessa a tela de Indicadores
    Então visualiza cobertura, drop size e positivação com valores reais e metas
    E os cálculos estão de acordo com as regras confirmadas por Cecília Ribeiro

Funcionalidade: Remuneração Variável (RV) por Perfil

  Cenário: Visualizar RV estimada — happy path
    Dado que o vendedor está autenticado com perfil "representante"
    Quando acessa a tela de RV
    Então visualiza a composição da sua RV estimada
    E os indicadores exibidos correspondem ao seu perfil de vendedor
    E o cálculo segue as regras validadas por Cecília Ribeiro

  Cenário: Visualizar RV com perfil de supervisor — happy path
    Dado que o usuário está autenticado com perfil "supervisor"
    Quando acessa a tela de Metas
    Então visualiza indicadores de performance da sua equipe
    E os dados são diferentes dos indicadores de representante individual
```

| Cenário | Tipo | Evidência | Situação |
|---|---|---|---|
| Metas por família — happy path | Happy | APK piloto 05/08/2025 — tela validada por Cecília | Aprovado |
| Famílias duplicadas | Sad | Identificado no piloto; corrigido e revalidado Ago/2025 | Aprovado |
| Latência de API | Sad | Loading state validado em dispositivo antes do piloto | Aprovado |
| Indicadores multidimensionais | Happy | APK piloto — valores conferidos com Cecília | Aprovado |
| RV por perfil representante | Happy | APK piloto — cálculo validado por Cecília | Aprovado |
| RV por perfil supervisor | Happy | Validado em reunião de alinhamento Ago/2025 | Aprovado |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 01/07/2025 | Abraão Oliveira | Versão inicial — registro retroativo (projeto executado jun–set/2025) |
