# Registro de Adaptação do Processo — Fundação Tecnológica GASMIG · OS-PARCELA-002

| Campo | Valor |
|---|---|
| **Documento** | ADAP-GASMIG02-002 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-002 |
| **Versão** | 1.2 |
| **Data** | 13/06/2026 |
| **Responsável pela adaptação** | Abraão Oliveira |
| **Processo-padrão de referência** | PRO-GPC-001 v2.2 |
| **Guia de adaptação de referência** | GUIA-GPC-001 v1.2 |

> As mesmas decisões de adaptação da OS-PARCELA-001 (ADAP-GASMIG02-001) se mantêm nesta OS, com os ajustes anotados abaixo.

---

## 1. Decisões de adaptação

| Eixo de adaptação | Decisão | Justificativa |
|---|---|---|
| Tipo de produto | Sem UX/UI — projeto de configuração cloud | Igual à OS-001. Escopo é 100% configuração de Azure APIM, Key Vault e Azure Monitor. |
| Origem dos requisitos | Cliente fornece contexto; Timeware elabora especificação técnica | Igual à OS-001. |
| Porte do projeto | Médio — formalidade padrão | Mesmo porte e equipe da OS-001. |
| Equipe e papéis | Cézar Hiraki acumula Tech Lead, Arquiteto e GCO | Igual à OS-001. |
| Criticidade | **Padrão com atenção reforçada em segurança** | Esta OS implementa autenticação (OAuth 2.0), gestão de secrets (Key Vault) e homologação end-to-end — componentes de segurança crítica. Verificação técnica de Cézar Hiraki cobre especificamente esses itens. |
| Cadência de entrega | Por marco — aceite único ao final da OS | Igual à OS-001. |
| Ambiente de stage | Sandbox já entregue na OS-001 | O sandbox é utilizado na homologação desta OS, não provisionado aqui. |
| Verificação e Validação (VV) | Checklist de verificação de configuração + smoke checks + verificação técnica Cézar Hiraki | Mesma abordagem da OS-001. Adicionado: verificação de fluxo OAuth 2.0 end-to-end e validação de secrets no Key Vault. |
| GQA | COO (Operações) | Mantido da OS-001. Independência em relação à equipe de projeto garantida. |

## 2. Etapas aplicáveis e não aplicáveis

| Etapa / artefato | Aplicável? | Observação |
|---|---|---|
| Design de UX/UI | **Não** | Igual à OS-001. |
| Documento de Design (arquitetura) | **Sim** | Estende o design da OS-001 com Key Vault, OAuth 2.0, Application Insights e Azure Monitor. |
| Documento de Requisitos | **Sim** | Requisitos documentados em REQ-GASMIG02-002. |
| Matriz de rastreabilidade | **Sim** | Estende RASTR-GASMIG02-001 com os novos requisitos. |
| Plano de Projeto | **Sim** | Com adaptação: cronograma por atividades, não por sprints. |
| Estratégia de Integração (ITP) | **Sim — parcialmente aplicável nesta OS** | A integração entre APIM, Key Vault e Entra ID (OAuth 2.0) constitui integração entre serviços Azure; documentada no Documento de Design. |
| Testes de software (unitários, BDD/Gherkin) | **Não aplicável** | Igual à OS-001 — projeto de configuração, sem desenvolvimento de código. |
| Verificação de configuração (checklist) | **Sim** | Cada item verificado por checklist no portal Azure e nas ferramentas de monitoramento. |
| Verificação técnica Cézar Hiraki | **Sim** | Com foco reforçado em OAuth 2.0, Key Vault e alertas — componentes de maior criticidade desta OS. |
| Smoke checks HTTP | **Sim** | Verificação de fluxo OAuth 2.0 end-to-end e de alertas disparados. |
| Change Request | **Sim, se acionado** | Mesmo fluxo da OS-001. |
| Termo de Encerramento | **Sim** | Encerramento formal após sessão de homologação. |
| Aquisição (AQU) | **Não aplicável** | Igual à OS-001: sem subcontratação de terceiro responsável por entrega; serviços Azure (APIM, Key Vault, Entra ID, Monitor) são software de prateleira/infraestrutura, fora do escopo de AQU (PRO-AQU-001 §2). |

## 3. Pontos de controle obrigatórios (não adaptáveis)

Conforme GUIA-GPC-001 v1.2, os seis pontos a seguir são obrigatórios e não passíveis de supressão em nenhum projeto.

- [x] Abertura — Termo de Abertura elaborado e aprovado antes do início das atividades (TAP-GASMIG02-002)
- [x] Requisitos — Requisitos especificados, rastreáveis e validados antes da configuração (REQ-GASMIG02-002)
- [x] Design — Documento de Design técnico elaborado e aprovado antes do deploy (PCP-GASMIG02-002)
- [x] Verificação — Checklist de verificação de configuração executado e resultados registrados (VV-GASMIG02-002)
- [x] Homologação — Sessão de homologação end-to-end com o cliente realizada e registrada (ATA-GASMIG02-003)
- [x] Encerramento — Termo de Encerramento emitido com aceite formal (TAE-GASMIG02-002)

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão Oliveira | Versão inicial — adaptações da OS-PARCELA-002 |
| 1.1 | 11/06/2026 | Time de Melhoria Contínua | Adicionada referência ao processo-padrão base (PRO-GPC-001 v2.2) e ao guia de adaptação (GUIA-GPC-001 v1.2); GQA atualizado para COO (Operações); pontos de controle expandidos para os 6 obrigatórios do GUIA-GPC-001 v1.2; todos marcados como concluídos (OS-002 encerrada em 09/06/2026) |
| 1.2 | 13/06/2026 | Time de Melhoria Contínua | Registrada explicitamente a não aplicabilidade do processo de Aquisição (AQU) nesta OS, conforme PRO-AQU-001 §2 |
