# Registro de Adaptação do Processo — Fundação Tecnológica GASMIG · OS-PARCELA-001

| Campo | Valor |
|---|---|
| **Documento** | ADAP-GASMIG02-001 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-001 |
| **Versão** | 1.4 |
| **Data** | 13/06/2026 |
| **Responsável pela adaptação** | Abraão Oliveira |
| **Processo-padrão de referência** | PRO-GPC-001 v2.2 |
| **Guia de adaptação de referência** | GUIA-GPC-001 v1.2 |

---

## 1. Decisões de adaptação

| Eixo de adaptação | Decisão | Justificativa |
|---|---|---|
| Tipo de produto (com/sem front-end) | Sem UX/UI — projeto de infraestrutura e configuração cloud | O escopo é 100% configuração do Azure API Management; nenhuma interface de usuário é desenvolvida pela Timeware. O portal do desenvolvedor é um componente nativo do APIM, configurado mas não desenvolvido. |
| Origem dos requisitos e do design | Cliente fornece contexto de negócio; Timeware elabora especificação técnica | A GASMIG definiu as necessidades de negócio; a Timeware conduziu o discovery técnico e especificou os requisitos de configuração. |
| Porte do projeto | Médio — formalidade padrão | Equipe de 3 pessoas, prazo de 15 dias, escopo bem delimitado. |
| Equipe e papéis (acúmulo) | Cézar Hiraki acumula Tech Lead, Arquiteto e GCO | Equipe enxuta; viável dado o porte e a natureza da entrega. |
| Criticidade e regulação | Padrão | Fundação corporativa de integração, sem processamento de dados regulados nesta OS. |
| Cadência de entrega ao cliente | Por marco — aceite único ao final da OS | Não há sprints com entregas parciais. A entrega é a OS completa, validada em sessão de apresentação ao time técnico GASMIG. |
| Ambiente de stage | Sandbox é parte do escopo da entrega | O ambiente de sandbox não é pré-requisito externo; sua configuração é um dos itens de entrega desta OS. |
| Verificação e Validação (VV) | Checklist de verificação de configuração + smoke checks HTTP + verificação técnica por Cézar Hiraki | Projeto de configuração de ferramenta: não há código desenvolvido. Testes de software (unitários, integração, BDD/Gherkin) não se aplicam. A verificação é realizada por checklist estruturado e navegação no portal Azure. Ver VV-GASMIG02-001. |
| GQA | COO (Operações) | Designado antes da primeira auditoria de processo, garantindo independência em relação à equipe de projeto. |

## 2. Etapas aplicáveis e não aplicáveis

| Etapa / artefato | Aplicável? | Observação |
|---|---|---|
| Design de UX/UI | **Não** | Projeto sem desenvolvimento de interface de usuário. |
| Documento de Design (arquitetura) | **Sim** | Registra a topologia do Azure API Management, estrutura de workspaces, políticas e decisões de design. |
| Documento de Requisitos | **Sim** | Requisitos de configuração documentados em REQ-GASMIG02-001. |
| Matriz de rastreabilidade | **Sim** | Rastreabilidade entre requisitos, itens de design e checklist de verificação. |
| Plano de Projeto | **Sim** | Com adaptação: cronograma por atividades, não por sprints. |
| Estratégia de Integração (ITP) | **Não aplicável nesta OS** | Não há integração entre componentes de software desenvolvidos. Aplicável na OS-PARCELA-002 e projetos de API subsequentes. |
| Testes de software (unitários, integração, BDD/Gherkin) | **Não aplicável** | Não há desenvolvimento de código. Não existe comportamento de software a ser especificado em BDD nem lógica a ser testada em testes unitários ou de integração. |
| Verificação de configuração (checklist) | **Sim — substitui testes de software** | Cada requisito de configuração é verificado por checklist estruturado no portal Azure. Ver VV-GASMIG02-001. |
| Revisão técnica da configuração | **Sim — substitui revisão de código** | Cézar Hiraki verifica a configuração realizada pelos engenheiros no portal Azure antes da sessão de aceite (equivalente funcional da revisão por pares para projetos de configuração). |
| Smoke checks HTTP | **Sim** | Chamadas HTTP via Postman/curl para confirmar que as políticas configuradas produzem o comportamento esperado (acesso permitido ou bloqueado). |
| Change Request | **Sim, se acionado** | Qualquer alteração de escopo após baseline segue o fluxo de change request (TPL-GPR-006). |
| Termo de Encerramento | **Sim** | Encerramento formal após aceite da sessão de apresentação. |
| Aquisição (AQU) | **Não aplicável** | Não há subcontratação de terceiro responsável por entrega. Os serviços Azure (APIM, sandbox) são software de prateleira/infraestrutura, expressamente fora do escopo de AQU (PRO-AQU-001 §2). |

## 3. Pontos de controle obrigatórios (não adaptáveis)

Conforme GUIA-GPC-001 v1.2, os seis pontos a seguir são obrigatórios e não passíveis de supressão em nenhum projeto.

- [x] Abertura — Termo de Abertura elaborado e aprovado antes do início das atividades (TAP-GASMIG02-001)
- [x] Requisitos — Requisitos especificados, rastreáveis e validados antes da configuração (REQ-GASMIG02-001)
- [x] Design — Documento de Design técnico elaborado e aprovado antes do deploy (PCP-GASMIG02-001)
- [x] Verificação — Checklist de verificação de configuração executado e resultados registrados (VV-GASMIG02-001)
- [x] Homologação — Sessão de aceite com o cliente realizada e registrada (ATA-GASMIG02-002)
- [x] Encerramento — Termo de Encerramento emitido com aceite formal (TAE-GASMIG02-001)

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 29/04/2026 | Abraão Oliveira | Versão inicial |
| 1.1 | 04/06/2026 | Abraão Oliveira | Adicionada adaptação explícita de VV: testes de software não aplicáveis; verificação por checklist de configuração e smoke checks HTTP; revisão técnica substitui revisão de código |
| 1.2 | 05/06/2026 | Abraão Oliveira | Definição do papel de GQA como COO (Operações), garantindo independência em relação à equipe de projeto |
| 1.3 | 11/06/2026 | Time de Melhoria Contínua | Adicionada referência ao processo-padrão base (PRO-GPC-001 v2.2) e ao guia de adaptação (GUIA-GPC-001 v1.2); pontos de controle obrigatórios expandidos para os 6 definidos no GUIA-GPC-001 v1.2 com artefatos produzidos |
| 1.4 | 13/06/2026 | Time de Melhoria Contínua | Registrada explicitamente a não aplicabilidade do processo de Aquisição (AQU) neste projeto, conforme PRO-AQU-001 §2 |
