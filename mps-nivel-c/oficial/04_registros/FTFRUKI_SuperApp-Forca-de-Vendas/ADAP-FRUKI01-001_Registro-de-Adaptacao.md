# Registro de Adaptação do Processo — SuperApp Fruki · Novas Features Força de Vendas

| Campo | Valor |
|---|---|
| **Documento** | ADAP-FRUKI01-001 |
| **Projeto** | SuperApp Fruki — Novas Features Força de Vendas |
| **Versão** | 1.0 |
| **Data** | 05/06/2026 |
| **Responsável pela adaptação** | Abraão Oliveira |

---

## 1. Decisões de adaptação

| Eixo de adaptação | Decisão | Justificativa |
|---|---|---|
| Tipo de produto (com/sem front-end) | Com UX/UI — aplicativo mobile | SuperApp Fruki é um aplicativo React Native / Expo; todas as features envolvem desenvolvimento de telas e experiência do usuário |
| Origem dos requisitos e do design | Timeware elabora protótipos; cliente valida regras de negócio | Cecília Ribeiro (Fruki) fornece as regras de negócio e valida os protótipos; Brenda Chrystie (Timeware) é responsável pelo design; APIs e dados são fornecidos pelo time técnico Fruki (Jardel/Renan) |
| Porte do projeto | Médio — nível de documentação padrão | Projeto de ~7 meses com múltiplos módulos e equipe de 5 pessoas; escopo bem delimitado pelo Pacote Final 24 |
| Equipe e papéis (acúmulo) | Abraão Oliveira: GP + Product Owner; Brenda Chrystie: UX + analista de negócio | Equipe enxuta; Abraão gerencia o projeto e representa o produto junto ao cliente; Brenda conduz levantamento de regras e produz protótipos |
| Criticidade e regulação | Padrão | Aplicativo comercial interno sem regulação específica (não há dados sensíveis de consumidores externos ou requisitos regulatórios) |
| Cadência de entrega ao cliente | Por módulo/feature — entrega incremental mensal | Acordado na proposta: "em cada mês, até o fim de 2024, você terá 1 ou 2 features entregues"; entregas via Pull Request no Azure DevOps e APK para testes |
| Ambiente de stage | Adotado — Expo APK + branch feature no Azure DevOps | Builds de teste (APK) gerados via Expo antes de cada merge; revisão técnica do Jardel antes do merge na branch principal; link Expo compartilhado com cliente para validação |

## 2. Etapas aplicáveis e não aplicáveis

| Etapa / artefato | Aplicável? | Observação |
|---|---|---|
| Design de UX/UI | Sim | Protótipos criados em Figma por Brenda Chrystie e validados por Cecília Ribeiro antes de cada sprint de desenvolvimento |
| Documento de Requisitos | Sim | Levantamento formal das features por módulo, com regras de negócio fornecidas pela Fruki |
| Plano de V&V | Sim | Testes funcionais via APK com cliente e verificação técnica via revisão de PR |
| Estratégia de integração | Aplicável — simplificada | Integração com APIs REST da Fruki via endpoints documentados; versionamento de branches no Azure DevOps |
| Mapa de rastreabilidade | Sim | Requisitos rastreados aos módulos entregues e às PRs no Azure DevOps |
| Revisão por pares | Sim | Revisão técnica das PRs pelo Jardel (Fruki) antes do merge; revisão interna de código pela equipe Timeware |
| Registro de capacitação | Não aplicável | Não há treinamento formal de usuários no escopo deste projeto; a equipe técnica da Fruki acessa o repositório e as APIs diretamente |
| Gestão de decisões arquiteturais (GDE) | Simplificada | Decisões técnicas registradas em e-mails e atas de reunião; arquitetura React Native já estabelecida — não há decisão arquitetural de alto impacto neste projeto |

## 3. Pontos de controle obrigatórios (não adaptáveis)

- [x] Requisitos especificados e validados
- [x] Plano de Projeto aprovado pelo cliente (baseline)
- [x] Definição de Pronto aplicada
- [x] Verificação e validação realizadas
- [x] Encerramento formal com aceite

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — registro retroativo (projeto executado jun/2024–jan/2025) |
