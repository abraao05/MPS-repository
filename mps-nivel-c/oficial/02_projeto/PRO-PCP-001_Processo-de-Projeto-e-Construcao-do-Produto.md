# Processo de Projeto e Construção do Produto — TIMEWARE

| Campo | Valor |
|---|---|
| **Documento** | PRO-PCP-001 — Processo de Projeto e Construção do Produto |
| **Versão** | 1.0 |
| **Data** | `<dd/mm/aaaa>` |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Aprovação** | COO (Operações) |
| **Processos MPS-SW relacionados** | PCP 1, PCP 2, PCP 3 |
| **Classificação** | Ativo de processo organizacional |

---

## 1. Propósito

Este processo define como a Timeware projeta (design) e constrói o produto de software, a partir dos requisitos, garantindo que a solução seja desenhada com base em critérios, avaliada antes da construção, e implementada conforme o design — com rastreabilidade entre requisitos, design e código.

> **Mapa de resultados atendidos neste documento:**
> - Seção 3 → **PCP 1** (design desenvolvido, baseado em critérios e rastreável)
> - Seção 4 → **PCP 2** (design avaliado e problemas tratados)
> - Seção 5 → **PCP 3** (produto implementado conforme o design)

## 2. Visão geral

O design opera em **trilha antecipada** ao desenvolvimento (de uma a duas sprints à frente) e compreende duas dimensões:

- **Design de produto (UX/UI):** aplicável a projetos com interface de usuário. Quando aplicável, parte de wireframes de baixa fidelidade validados com o cliente.
- **Design técnico (arquitetura):** sempre aplicável. Arquitetura, modelo de dados e integrações, definidos pelo Arquiteto/Tech Lead.

A aplicabilidade do design de UX/UI é definida na adaptação do projeto (GUIA-GPC-001): projetos sem front-end (APIs, serviços) mantêm apenas o design técnico.

## 3. Desenvolvimento do design (PCP 1)

- O design é desenvolvido a partir dos **requisitos** (PRO-REQ-001), buscando uma solução adequada com base em **critérios** (atendimento ao requisito, viabilidade técnica, manutenibilidade, desempenho, segurança).
- Quando há mais de uma alternativa de solução relevante, a escolha pode seguir o processo de **Gerência de Decisões** (PRO-GDE-001).
- O design é documentado no **Documento de Design** (TPL-PCP-001), abrangendo, conforme aplicável: arquitetura, modelo de dados, integrações e, quando houver UX/UI, telas/protótipos.
- É mantida a **rastreabilidade** entre requisitos e elementos de design (registrada na Matriz de Rastreabilidade — TPL-REQ-002).

## 4. Avaliação do design (PCP 2)

- O design é **avaliado antes da construção**, verificando aderência aos requisitos, consistência e viabilidade.
- Quando há UX/UI, o protótipo é **validado com o cliente**; o design técnico é revisado pela equipe técnica (Arquiteto/Tech Lead).
- Problemas identificados na avaliação são **tratados** antes de a construção do item correspondente iniciar.

## 5. Construção do produto (PCP 3)

- O produto é **implementado conforme o design** validado, em sprints, seguindo o fluxo do processo-padrão (PRO-GPC-001).
- O código é versionado e controlado conforme a Gerência de Configuração (PLA-GCO-001).
- Cada item segue a **Definição de Pronto**: critérios de aceite atendidos, code review aprovado, testes do QA executados, entrega em homologação/staging.
- As informações de construção (código, documentação técnica) são mantidas e rastreáveis em relação ao design e aos requisitos.

## 6. Papéis

| Papel | Responsabilidade |
|---|---|
| **Arquiteto / Tech Lead** | Definem o design técnico; avaliam o design; lideram tecnicamente a construção. |
| **UX/UI** | Elabora e valida o design de interface (quando aplicável). |
| **Equipe de Desenvolvimento** | Implementa o produto conforme o design; realiza code review. |
| **Product Owner** | Valida o design de produto com o cliente. |
| **QA** | Verifica a implementação conforme a Definição de Pronto (ver VV). |

## 7. Documentos e artefatos relacionados

- PRO-GPC-001 — Processo-Padrão Organizacional
- PRO-REQ-001 — Processo de Engenharia de Requisitos
- TPL-PCP-001 — Template de Documento de Design
- TPL-REQ-002 — Template de Matriz de Rastreabilidade
- PLA-GCO-001 — Plano de Gerência de Configuração
- PRO-GDE-001 — Processo de Gerência de Decisões
- Processo de Verificação e Validação (VV)

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | `<dd/mm/aaaa>` | Time de Melhoria Contínua | Definição inicial do processo de projeto e construção do produto |
