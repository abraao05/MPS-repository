# Registro de Adaptação do Processo — SuperApp Fruki · Pacote 1 — Módulo Metas e RV

| Campo | Valor |
|---|---|
| **Documento** | ADAP-FRUKI01-001 |
| **Projeto** | SuperApp Fruki — Pacote 1 — Módulo Metas e Remuneração Variável |
| **Versão** | 1.2 |
| **Data** | 13/06/2026 |
| **Responsável pela adaptação** | Abraão Oliveira |

---

## 1. Decisões de adaptação

| Eixo de adaptação | Decisão | Justificativa |
|---|---|---|
| Tipo de produto (com/sem front-end) | Com UX/UI — aplicativo mobile | SuperApp Fruki é um aplicativo React Native / Expo; todas as features envolvem desenvolvimento de telas e experiência do usuário |
| Origem dos requisitos e do design | Timeware elabora protótipos; cliente valida regras de negócio | Cecília Ribeiro (Fruki) fornece as regras de negócio e valida os protótipos; Brenda Chrystie (Timeware) é responsável pelo design; APIs e dados são fornecidos pelo time técnico Fruki (Jardel/Renan) |
| Porte do projeto | Médio — nível de documentação padrão | Módulo único (Metas/RV) entregue em ~3 meses; equipe de 5 pessoas; escopo bem delimitado ao Pacote 1 |
| Equipe e papéis (acúmulo) | Abraão Oliveira: GP + Product Owner; Brenda Chrystie: UX + analista de negócio | Equipe enxuta; Abraão gerencia o projeto e representa o produto junto ao cliente; Brenda conduz levantamento de regras e produz protótipos |
| Criticidade e regulação | Padrão | Aplicativo comercial interno sem regulação específica (não há dados sensíveis de consumidores externos ou requisitos regulatórios) |
| Cadência de entrega ao cliente | Entrega única do módulo + piloto | Desenvolvimento contínuo com piloto em agosto/2025 e aceite após ajustes; entrega via Pull Request no Azure DevOps e APK para testes |
| Ambiente de stage | Adotado — Expo APK + branch feature no Azure DevOps | Builds de teste (APK) gerados via Expo antes de cada merge; revisão técnica do Jardel antes do merge na branch principal; link Expo compartilhado com cliente para validação |

## 2. Etapas aplicáveis e não aplicáveis

| Etapa / artefato | Aplicável? | Observação |
|---|---|---|
| Design de UX/UI | Sim | Protótipos criados em Figma por Brenda Chrystie e validados por Cecília Ribeiro antes de cada sprint de desenvolvimento |
| Documento de Requisitos | Sim | Levantamento formal das features por módulo, com regras de negócio fornecidas pela Fruki |
| Plano de V&V | Sim | Testes funcionais via APK com cliente e verificação técnica via revisão de PR |
| Estratégia de integração | Aplicável — simplificada | Integração com 4 APIs REST da Fruki via endpoints documentados; versionamento de branches no Azure DevOps. Ver `ITP-FRUKI01-001_Estrategia-de-Integracao.md` |
| Mapa de rastreabilidade | Sim | Requisitos rastreados aos módulos entregues e às PRs no Azure DevOps |
| Revisão por pares | Sim | Revisão técnica das PRs pelo Jardel (Fruki) antes do merge; revisão interna de código pela equipe Timeware |
| Registro de capacitação | Não aplicável | Não há treinamento formal de usuários no escopo deste projeto; a equipe técnica da Fruki acessa o repositório e as APIs diretamente |
| Gestão de decisões arquiteturais (GDE) | Aplicável — simplificada | Decisão técnica de tratamento de latência e normalização no front-end registrada em `GDE-FRUKI01-001_Registro-de-Decisao.md` |
| Aquisição (AQU) | Não aplicável | Squad próprio Timeware; não há subcontratação de terceiro respondendo por entrega. As APIs e os dados fornecidos pela Fruki são insumos do cliente, fora do escopo de AQU (PRO-AQU-001 §2). |

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
| 1.0 | 25/06/2025 | Abraão Oliveira | Versão inicial — registro retroativo (projeto executado jun/2025–set/2025) |
| 1.1 | 05/06/2026 | Abraão Oliveira | ITP e GDE referenciados explicitamente na tabela de etapas |
| 1.2 | 13/06/2026 | Abraão Oliveira | Registrada explicitamente a não aplicabilidade do processo de Aquisição (AQU) neste projeto, conforme PRO-AQU-001 §2 |
