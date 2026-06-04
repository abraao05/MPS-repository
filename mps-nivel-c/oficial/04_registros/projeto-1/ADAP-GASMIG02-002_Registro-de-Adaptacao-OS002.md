# Registro de Adaptação do Processo — Fundação Tecnológica GASMIG · OS-PARCELA-002

| Campo | Valor |
|---|---|
| **Documento** | ADAP-GASMIG02-002 |
| **Projeto** | Fundação Tecnológica GASMIG — OS-PARCELA-002 |
| **Versão** | 1.0 |
| **Data** | 26/05/2026 |
| **Responsável pela adaptação** | Abraão Oliveira |

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
| GQA | Responsável a definir | Mantido da OS-001. |

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

## 3. Pontos de controle obrigatórios (não adaptáveis)

- [x] Requisitos especificados e validados
- [x] Plano de Projeto aprovado pelo cliente (baseline)
- [ ] Definição de Pronto aplicada (checklist de verificação — VV-GASMIG02-002)
- [ ] Verificação e validação realizadas (verificação técnica + sessão de homologação GASMIG)
- [ ] Encerramento formal com aceite

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 26/05/2026 | Abraão Oliveira | Versão inicial — adaptações da OS-PARCELA-002 |
