# Registro de Adaptação do Processo — Rede D1000 · Cadastro de Clientes

| Campo | Valor |
|---|---|
| **Documento** | ADAP-PROFARMA01-001 |
| **Projeto** | Cadastro de Clientes — Rede D1000 |
| **Cliente** | Profarma S.A. / Rede D1000 |
| **Versão** | 1.1 |
| **Data** | 13/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR (evidência de projeto — adaptação do processo padrão) |

---

## 1. Objetivo

Registrar as adaptações aplicadas ao processo-padrão de desenvolvimento Timeware para a execução do projeto Cadastro de Clientes — Rede D1000, justificando cada decisão e seus impactos no planejamento.

---

## 2. Adaptações aplicadas

| # | Item do processo-padrão | Decisão de adaptação | Justificativa |
|---|---|---|---|
| A-01 | Definição completa de requisitos antes do início do desenvolvimento | Requisitos levantados de forma iterativa durante os sprints 1–4 | O cliente (D1000) não tinha documentação formal do comportamento legado do ITEC; o entendimento dos requisitos só foi possível com a análise do código legado em paralelo com o desenvolvimento |
| A-02 | Sprint Planning formal documentada desde o Sprint 1 | Sprints 1–3 operaram com planejamento informal via reuniões diárias; rastreabilidade introduzida formalmente a partir do Sprint 4 (Jira) | A equipe do cliente não utilizava gerenciamento formal de backlog no início; o Jira foi adotado gradualmente após validação interna |
| A-03 | Design de integração completo antes da implementação | Design das integrações foi evoluído incrementalmente, sprint a sprint | Dependência de informações técnicas dos sistemas satélites (BlueSoft, CloseUp, PBM) que chegaram apenas ao longo do projeto; contratos de API definidos em conjunto com os proprietários dos sistemas |
| A-04 | Ambiente de homologação independente desde o início | O ambiente de homologação foi provisionado apenas a partir de julho/2025 (após liberação do AKS pela equipe de infra D1000) | Restrição do cliente: acesso ao AKS e ao Azure DevOps foi liberado com atraso; o time Timeware trabalhou em ambiente local (Docker Compose) durante os sprints iniciais |
| A-05 | Testes de sistema executados pela própria equipe de desenvolvimento | A execução dos testes de homologação foi responsabilidade conjunta: Timeware (Lucas Batista / QA) + equipe D1000 (Julielle Santos / QA) | O cliente exigiu co-participação nos testes para validar os critérios de aceite; os roteiros de teste foram revisados em conjunto e aprovados pela D1000 antes da execução formal |
| A-06 | Nível de documentação de design técnico (PCP) simplificado | Documentação técnica mantida no nível de diagramas de fluxo e decisões arquiteturais; especificações de baixo nível mantidas nos PRs do Azure DevOps | Equipe enxuta; overhead de documentação baixo-nível comprometia a cadência de entrega; os PRs do Azure DevOps servem como documentação viva das decisões técnicas |
| A-07 | Revisão técnica (peer review) com dois revisores independentes | Revisões de código realizadas com um revisor (Tech Lead Tiago Barbosa Nascimento ou Erick Coelho por alternância) | Equipe de 4 Dev Backend; manter dois revisores independentes aumentaria o lead time dos PRs sem ganho proporcional de qualidade; o tech lead D1000 (Armando Junior) participava de revisões de mudanças arquiteturais |
| A-08 | Combinação de papéis | Tech Lead (Tiago Barbosa Nascimento) acumulou papel de Arquiteto da Solução nas primeiras 4 sprints; Gerente de Projeto (Abraão Oliveira) acumulou papel de Account Manager e GCO | Equipe contratada: 3 Dev Pleno + Tech Lead; escopo de papéis ajustado para viabilidade operacional do contrato mensalizado |
| A-09 | Deploys em produção via pipeline automatizado | Deploys em produção requereram aprovação via GMUD (Change Management da D1000) antes de cada execução de pipeline | Restrição do cliente: o processo GMUD da D1000 é obrigatório para qualquer mudança em ambiente produtivo; a Timeware adaptou o fluxo de release para incluir a abertura e aprovação de GMUD como gate pré-deploy |
| A-10 | Piloto em um único ambiente antes do rollout | Piloto restrito à loja 9, cobrindo três canais (PDV, Balcão, OMNI) antes do rollout geral para a rede | Decisão estratégica do cliente: minimizar risco de impacto operacional nas demais lojas; loja 9 escolhida por volume controlado e acesso facilitado da equipe de TI D1000 |

---

## 3. Itens sem adaptação (processo-padrão mantido)

- Controle de versão de código no Azure DevOps (Git)
- Revisão de PR obrigatória antes do merge no branch principal
- Execução de testes unitários como gate no pipeline CI
- Registro de riscos com probabilidade, impacto e plano de resposta
- Comunicação semanal de status ao cliente (relatório + reunião)
- Rastreabilidade de requisitos para casos de teste (a partir do Sprint 4)
- Formalização de mudanças de escopo via change request antes da implementação

---

## 4. Impacto das adaptações no projeto

| Adaptação | Impacto observado |
|---|---|
| A-01 (requisitos iterativos) | Gerou retrabalho nos sprints 5–7 quando requisitos inicialmente não documentados foram identificados; aceito pela equipe como custo de descoberta incremental |
| A-04 (ambiente tardio) | Atrasou o início dos testes de integração em ~6 semanas; mitigado com ambiente Docker local |
| A-09 (GMUD obrigatório) | Adicionou 2–5 dias úteis ao ciclo de release em produção; gerenciado com planejamento antecipado das janelas de mudança |
| A-10 (piloto loja 9) | Permitiu validação em condições reais sem risco para a rede; todos os ajustes necessários foram identificados e corrigidos antes do rollout |

---

## 5. Processos não aplicáveis ao projeto

| Processo | Aplicável? | Justificativa |
|---|---|---|
| Aquisição (AQU) | **Não aplicável** | Squad próprio Timeware; não há subcontratação de terceiro responsável por entrega. Os sistemas satélites (BlueSoft, CloseUp, PBM) e o ambiente AKS são integrações/insumos do cliente, tratados em ITP e Riscos, fora do escopo de AQU (PRO-AQU-001 §2). |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Time de Melhoria Contínua | Versão inicial — reconstituída com base nas reuniões de planejamento e dailys do período 04/2025–01/2026 |
| 1.1 | 13/06/2026 | Time de Melhoria Contínua | Adicionada a seção 5 (Processos não aplicáveis), registrando explicitamente a não aplicabilidade do processo de Aquisição (AQU), conforme PRO-AQU-001 §2 |
