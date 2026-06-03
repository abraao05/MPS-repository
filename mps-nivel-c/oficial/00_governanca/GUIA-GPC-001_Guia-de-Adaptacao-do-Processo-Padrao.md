# Guia de Adaptação do Processo-Padrão — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | GUIA-GPC-001 — Guia de Adaptação do Processo-Padrão (Tailoring) |
| **Versão** | 1.1 |
| **Data** | `<dd/mm/aaaa>` |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | Time de Melhoria Contínua |
| **Processo MPS-SW relacionado** | GPC 2 (diretrizes de adaptação do processo-padrão) |
| **Classificação** | Ativo de processo organizacional |
| **Documento de referência** | PRO-GPC-001 — Processo-Padrão Organizacional |

---

## 1. Propósito

Este guia define como cada projeto da Timeware adapta o Processo-Padrão Organizacional (PRO-GPC-001) ao seu contexto específico. A adaptação permite que o processo seja aplicado de forma proporcional ao porte, ao tipo e à criticidade de cada projeto, sem comprometer os controles essenciais de qualidade.

## 2. Princípio da adaptação (regra de ouro)

Adaptar o processo significa ajustar **como** e **com que profundidade** cada atividade é realizada — nunca eliminar arbitrariamente um ponto de controle obrigatório.

- **É permitido:** ajustar a profundidade e a formalidade dos produtos de trabalho; combinar papéis; encurtar ou simplificar atividades; dispensar atividades que **genuinamente não se aplicam** ao projeto.
- **Não é permitido:** suprimir um ponto de controle obrigatório (requisitos, design, testes, homologação, encerramento) sob a justificativa de que o projeto é pequeno ou urgente.

Uma atividade só pode ser dispensada quando **não se aplica de fato** ao projeto — por exemplo, design de interface em um projeto sem front-end —, e não por conveniência de prazo.

## 3. Pontos de controle obrigatórios (não adaptáveis)

Independentemente da adaptação, todo projeto de software sob medida mantém:

1. Abertura formal do projeto (Termo de Abertura).
2. Requisitos identificados, especificados e validados com o cliente.
3. Design técnico (arquitetura) avaliado antes da construção.
4. Definição de Pronto aplicada a cada entrega (critérios de aceite, code review, testes do QA, homologação).
5. Aprovação do cliente antes da promoção para produção.
6. Encerramento formal (Termo de Aceite).

Estes controles podem variar em profundidade, mas existem em todos os projetos.

## 4. Eixos de adaptação

A adaptação de cada projeto é decidida considerando os eixos abaixo.

### 4.1. Tipo de produto

| Situação | Adaptação |
|---|---|
| Projeto **com interface de usuário** (front-end) | Inclui design de UX/UI (wireframe → validação com cliente → design contínuo antecipado). |
| Projeto **sem front-end** (API, serviço, componente de backend) | Dispensa o design de UX/UI. Mantém o design técnico (arquitetura, modelo de dados, integrações). |
| Projeto de **integração** entre sistemas existentes | Ênfase no design técnico de interfaces e contratos de integração. UX/UI normalmente não se aplica. |
| Projeto de **migração / modernização** de legado | Inclui análise do sistema atual; o design foca na compatibilidade e na estratégia de migração. |

### 4.2. Origem dos requisitos e do design

| Situação | Adaptação |
|---|---|
| Cliente **não traz** design pronto | A Timeware conduz a criação do design (wireframe, protótipo, validação). |
| Cliente **traz** design/UX pronto | A etapa de criação de UX/UI é dispensada; o design é apenas validado e implementado. |
| Cliente **traz requisitos já detalhados** (ex.: RFP fechado) | O Discovery é mais curto, focado em confirmar entendimento e rastreabilidade, em vez de levantar do zero. |

### 4.3. Porte do projeto

| Situação | Adaptação |
|---|---|
| Projeto **pequeno / curto** | Documentação mais enxuta: requisitos podem ser registrados como histórias no Jira, em vez de documento extenso. Os controles obrigatórios (seção 3) são mantidos. |
| Projeto **grande / longo / crítico** | Maior formalidade e rastreabilidade; mais rigor nos produtos de trabalho e nos registros. |

Adaptações adicionais possíveis em projetos pequenos, desde que preservados os pontos de controle: redução de marcos intermediários e simplificação das cerimônias. A decisão é registrada na adaptação do projeto.

### 4.4. Equipe e papéis

| Situação | Adaptação |
|---|---|
| Projeto **pequeno** | Papéis podem ser acumulados por uma mesma pessoa (por exemplo, Tech Lead acumulando Arquiteto). A responsabilidade por cada papel permanece atribuída. |
| Projeto **grande** | Papéis tendem a ser exercidos por pessoas distintas. |

### 4.5. Criticidade e regulação

| Situação | Adaptação |
|---|---|
| Projeto com requisitos **críticos ou regulatórios** | Maior rigor nas atividades de verificação, validação e registro; controles reforçados conforme a exigência aplicável. |

## 5. Como registrar a adaptação em um projeto

A adaptação de cada projeto é decidida no início (entre a abertura/kickoff gerencial e o fechamento do plano) e registrada como parte do planejamento do projeto, por meio do Registro de Adaptação do Processo (associado à Gerência de Projetos — GPR).

O registro indica, para cada eixo aplicável: a decisão tomada, a justificativa e o responsável pela aprovação. As adaptações são revisadas caso o contexto do projeto mude de forma significativa ao longo da execução.

## 6. Exemplo de aplicação (caso real)

Um projeto de desenvolvimento de **API sem interface de usuário** é adaptado da seguinte forma:

- **Dispensado:** design de UX/UI (wireframe e protótipo), por não haver front-end.
- **Mantido:** abertura formal, requisitos validados, design técnico (arquitetura, modelo de dados, integrações) avaliado antes da construção, Definição de Pronto, homologação, aprovação do cliente e encerramento formal.

A decisão e a justificativa ("projeto sem front-end — UX/UI não se aplica") são registradas no Registro de Adaptação do Processo do projeto.

## 7. Documentos relacionados

- PRO-GPC-001 — Processo-Padrão Organizacional
- POL-ORG-001 — Política Organizacional de Processos
- Processo de Gerência de Projetos (GPR) e seu Registro de Adaptação
- CONV-ORG-001 — Convenção de Nomenclatura e Versionamento

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | `<dd/mm/aaaa>` | Time de Melhoria Contínua | Definição inicial do guia de adaptação do processo-padrão |
| 1.1 | `<dd/mm/aaaa>` | Time de Melhoria Contínua | Ajuste de nomenclatura de fase conforme o novo fluxo |
