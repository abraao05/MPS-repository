# Registro de Adaptação do Processo — SuperApp Fruki · Pacote Final 24

| Campo | Valor |
|---|---|
| **Documento** | ADAP-FRUKI01-002 |
| **Projeto** | SuperApp Fruki — Pacote Final 24 |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Responsável pela adaptação** | Abraão Oliveira |

---

## 1. Decisões de adaptação

| Eixo de adaptação | Decisão | Justificativa |
|---|---|---|
| Tipo de produto (com/sem front-end) | Com UX/UI — aplicativo mobile | Três novos módulos com interface React Native; todas as features envolvem telas e experiência de usuário |
| Origem dos requisitos e do design | Timeware elabora protótipos; cliente valida regras de negócio | Brenda Chrystie conduz design; Cecília Ribeiro e Alexsandro de Vargas Braga validam regras de cada módulo; APIs fornecidas por Jardel/Renan |
| Porte do projeto | Médio — nível de documentação padrão | Três módulos entregues em ~3 meses; equipe de 5 pessoas; continuidade do Pacote 1 |
| Equipe e papéis (acúmulo) | Abraão: GP + PO; Brenda: UX + analista de negócio | Mesma configuração do Pacote 1; equipe enxuta; viável dado o porte e familiaridade com o projeto |
| Criticidade e regulação | Padrão | Aplicativo comercial interno; sem regulação específica |
| Cadência de entrega ao cliente | Por módulo — entrega incremental mensal | Pedidos Não Alocados (out/2024) → Regra de Ouro (nov/2024) → PDV (dez/jan 2025); entregas via PR no Azure DevOps e APK para testes |
| Ambiente de stage | Adotado — Expo APK + branch feature no Azure DevOps | Builds de teste gerados via Expo antes de cada merge; revisão técnica do Jardel antes do merge na branch principal |

## 2. Etapas aplicáveis e não aplicáveis

| Etapa / artefato | Aplicável? | Observação |
|---|---|---|
| Design de UX/UI | Sim | Protótipos para cada módulo (Não Alocados, Regra de Ouro, PDV) criados por Brenda e validados por Cecília antes de cada sprint |
| Documento de Requisitos | Sim | REQ-FRUKI01-002 — 10 RF e 5 RNF, levantados nas reuniões de entendimento de demanda |
| Plano de V&V | Sim | Testes funcionais via APK com cliente; verificação técnica via revisão de PR pelo Jardel |
| Estratégia de integração | Aplicável — simplificada | Integração com APIs REST da Fruki via endpoints documentados; versionamento de branches no Azure DevOps |
| Mapa de rastreabilidade | Sim | Requisitos rastreados aos módulos entregues e às PRs no Azure DevOps |
| Revisão por pares | Sim | Revisão técnica das PRs pelo Jardel (Fruki) antes do merge; revisão interna pela equipe Timeware |
| Registro de capacitação | Não aplicável | Sem treinamento formal de usuários no escopo |
| Gestão de decisões arquiteturais (GDE) | Simplificada | Decisões técnicas registradas em e-mails e atas; arquitetura React Native já estabelecida no Pacote 1 |

## 3. Pontos de controle obrigatórios (não adaptáveis)

- [x] Requisitos especificados e validados
- [x] Plano de Projeto aprovado pelo cliente (baseline)
- [x] Definição de Pronto aplicada
- [x] Verificação e validação realizadas
- [x] Encerramento formal com aceite (Microsoft Teams — 15/01/2025)

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — registro retroativo (projeto executado out/2024–jan/2025) |
