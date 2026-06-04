# Registro de Adaptação do Processo — Fundação Tecnológica GASMIG · OS-PARCELA-001

| Campo | Valor |
|---|---|
| **Documento** | ADAP-GASMIG02-001 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-001 |
| **Versão** | 1.0 |
| **Data** | 29/04/2026 |
| **Responsável pela adaptação** | Abraão Oliveira |

---

## 1. Decisões de adaptação

| Eixo de adaptação | Decisão | Justificativa |
|---|---|---|
| Tipo de produto (com/sem front-end) | Sem UX/UI — projeto de infraestrutura e configuração cloud | O escopo é 100% configuração do Azure API Management; nenhuma interface de usuário é desenvolvida pela Timeware. O portal do desenvolvedor é um componente nativo do APIM, configurado mas não desenvolvido. |
| Origem dos requisitos e do design | Cliente fornece contexto de negócio; Timeware elabora especificação técnica | A GASMIG definiu as necessidades de negócio; a Timeware conduziu o discovery técnico, fez as reuniões de levantamento e especificou os requisitos de configuração. |
| Porte do projeto | Médio — formalidade padrão | Equipe de 3 pessoas, prazo de 15 dias, escopo bem delimitado. Documentação no nível padrão. |
| Equipe e papéis (acúmulo) | Cézar Hiraki acumula Tech Lead, Arquiteto e GCO | Equipe enxuta; viável dado o porte e a natureza da entrega (configuração, não desenvolvimento). |
| Criticidade e regulação | Padrão | Fundação corporativa de integração, mas sem processamento de dados regulados ou críticos nesta OS. Reforço na OS-PARCELA-002 (secrets, autenticação). |
| Cadência de entrega ao cliente | Por marco — aceite único ao final da OS | Não há sprints com entregas parciais. A entrega é a OS completa, validada em sessão de apresentação ao time técnico GASMIG. |
| Ambiente de stage | Sandbox é parte do escopo da entrega | O ambiente de sandbox não é pré-requisito externo; sua configuração é um dos itens de entrega desta OS. |
| GQA | Responsável a definir | Será designado antes da primeira auditoria de processo. |

## 2. Etapas aplicáveis e não aplicáveis

| Etapa / artefato | Aplicável? | Observação |
|---|---|---|
| Design de UX/UI | Não | Projeto sem desenvolvimento de interface de usuário. |
| Documento de Design (arquitetura) | Sim | Aplicável para registrar a topologia do Azure API Management, estrutura de workspaces, políticas e ambientes. |
| Documento de Requisitos | Sim | Requisitos de configuração documentados em REQ-GASMIG02-001. |
| Matriz de rastreabilidade | Sim | Rastreabilidade entre requisitos e itens de configuração entregues. |
| Plano de Projeto | Sim | Aplicável com adaptação: cronograma por atividades (não por sprints). |
| Estratégia de Integração | Não aplicável nesta OS | Não há integração entre componentes de software desenvolvidos. Aplicável na OS-PARCELA-002 e projetos de API subsequentes. |
| Plano de V&V | Sim | Verificação e validação da configuração por checklist técnico e sessão de apresentação ao cliente. |
| Testes funcionais de software | Não aplicável nesta OS | Não há desenvolvimento de código. Verificação é por configuração e teste de funcionamento do APIM. |
| Registro de revisão por pares | Sim | Review técnico da configuração antes da sessão de aceite (Cézar Hiraki revisa o trabalho dos engenheiros). |
| Change Request | Sim, se acionado | Qualquer alteração de escopo após baseline do plano segue o fluxo de change request (TPL-GPR-006). |
| Termo de Encerramento | Sim | Encerramento formal após aceite da sessão de apresentação. |

## 3. Pontos de controle obrigatórios (não adaptáveis)

- [x] Requisitos especificados e validados
- [x] Plano de Projeto aprovado pelo cliente (baseline)
- [ ] Definição de Pronto aplicada (checklist de itens de configuração entregues)
- [ ] Verificação e validação realizadas (sessão de apresentação ao time técnico GASMIG)
- [ ] Encerramento formal com aceite

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 29/04/2026 | Abraão Oliveira | Versão inicial — adaptação definida no kickoff |
