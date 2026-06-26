# Termo de Encerramento do Projeto — Rede D1000 · Cadastro de Clientes

| Campo | Valor |
|---|---|
| **Documento** | TAE-PROFARMA01-001 |
| **Projeto** | Cadastro de Clientes — Rede D1000 |
| **Cliente** | Profarma S.A. / Rede D1000 |
| **Contrato** | Squad D1000 Loja — alocação de 3 Dev Pleno |
| **Versão** | 1.0 |
| **Data de encerramento** | 29/01/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR (evidência de projeto — encerramento) |

---

## 1. Sumário executivo do projeto

O projeto Cadastro de Clientes — Rede D1000 foi desenvolvido de abril de 2025 a janeiro de 2026 pela equipe Timeware em regime de squad mensalizado (3 Dev Pleno). O objetivo era substituir a gestão de cadastro dispersa no sistema legado ITEC por uma API RESTful cloud-native em .NET 8, com PostgreSQL no Azure, CPF como chave primária única e integração a todos os canais da rede.

O projeto foi concluído com a entrega de 16 endpoints de API, 273 testes unitários, integração com ITEC, VTEX, Call Center, Propz CRM, PBM/Interplayers, BlueSoft e CloseUp, além do piloto operacional na loja 9 cobrindo os canais PDV, Balcão e OMNI.

---

## 2. Entregáveis concluídos

| Entregável | Status | Data de aceite |
|---|---|---|
| API de Cadastro de Clientes (.NET 8 / Clean Architecture) | Concluído | 29/01/2026 |
| Banco de dados PostgreSQL (Azure) — esquema, índices, migrations | Concluído | 29/01/2026 |
| 16 endpoints REST documentados | Concluído | 29/01/2026 |
| 273 cenários de teste unitário | Concluído | 29/01/2026 |
| Integração ITEC (outbox pattern + worker) | Concluído | Sprint 7 / Julho 2025 |
| Integração VTEX (canal OMNI) | Concluído | Sprint 9 / Agosto 2025 |
| Integração Call Center | Concluído | Sprint 9 / Agosto 2025 |
| Integração Propz CRM (Service Bus) | Concluído | 04/12/2025 |
| Integração PBM / Interplayers | Concluído | Sprint 11 / Setembro 2025 |
| Integração BlueSoft | Concluído | Sprint 11 / Setembro 2025 |
| Integração CloseUp | Concluído | Sprint 12 / Outubro 2025 |
| Worker de expurgo LGPD | Concluído | Sprint 10 / Setembro 2025 |
| Carga inicial da base (~7 milhões de CPFs) | Concluído | Sprint 13 / Outubro 2025 |
| Deploy em AKS (Azure Kubernetes Service) | Concluído | Setembro 2025 |
| Pipelines CI/CD no Azure DevOps | Concluído | Sprint 5 / Junho 2025 |
| Monitoramento via Datadog (APM, logs, alertas) | Concluído | Outubro 2025 |
| Piloto na loja 9 (PDV, Balcão, OMNI) | Concluído | Janeiro 2026 |
| Documentação técnica (design, APIs, IaC) | Concluído | 29/01/2026 |

---

## 3. Escopo não executado

| Item | Motivo |
|---|---|
| Modernização dos aplicativos D1000 Express e Connect D1000 | Fora do escopo contratado — objeto de contrato separado |
| Desenvolvimento de novos módulos do ITEC legado | Fora do escopo contratado |
| Sustentação pós-piloto | Objeto de contrato futuro |
| Rollout geral para toda a rede (demais lojas) | Fora do escopo deste projeto — a ser executado com apoio da equipe D1000 após este encerramento |

---

## 4. Indicadores finais

| Indicador | Planejado | Realizado |
|---|---|---|
| Início do projeto | 17/03/2025 | 28/04/2025 (início dos sprints — primeiras reuniões de design em 17/03) |
| Encerramento | Setembro/2025 (inicial) → Janeiro/2026 (revisado) | 29/01/2026 |
| Sprints realizados | — | 19 sprints |
| Endpoints entregues | 16 | 16 |
| Testes unitários | 273 | 273 |
| Change requests absorvidos | — | 12 change requests formais |
| Incidentes críticos (S1) no piloto | 0 | 0 |
| Integrações com sistemas satélites | 6 | 6 (ITEC, VTEX, Propz, PBM, BlueSoft, CloseUp) + Call Center |

---

## 5. Variâncias em relação ao plano original

| Aspecto | Planejado | Realizado | Justificativa |
|---|---|---|---|
| Prazo de encerramento | Setembro/2025 | Janeiro/2026 | Aumento de escopo (integrações BlueSoft, CloseUp, worker LGPD), atraso no ambiente de homologação, lead time GMUD |
| Escopo de integrações | ITEC, VTEX, Call Center, PBM, Propz | + BlueSoft, CloseUp | Change requests aprovados no Sprint 6–8 |
| Início dos sprints de desenvolvimento | 17/03/2025 | 28/04/2025 | Alinhamentos técnicos com a D1000 sobre o legado ITEC; acessos Azure liberados com atraso |
| Formato de backlog | Informal (sprints 1–3) | Jira a partir do Sprint 4 | Adoção gradual da ferramenta pelo cliente D1000 |

---

## 6. Principais riscos materializados

| Risco | Impacto | Como foi gerenciado |
|---|---|---|
| Ambiente de homologação AKS disponível com atraso | Desenvolvimento em ambiente local por 2,5 meses | Docker Compose local; identificação de problemas de ambiente adiada para homologação |
| Contratos de API de sistemas satélites indisponíveis no início | Adição de escopo nos Sprints 6–8 | Change requests formais; replanejamento dos sprints afetados |
| Lead time GMUD adicionou tempo aos ciclos de release | Compressão do tempo disponível para correções pré-prazo | Planejamento antecipado das janelas de GMUD nas sprints finais |
| Documentação do ITEC inexistente | Esforço adicional não planejado nos Sprints 2–4 | Engenharia reversa do legado com apoio de Alexandre Henrique (D1000) |
| Saneamento da base legada iterativo | Carga inicial levou 3 semanas a mais do que o planejado | Múltiplas rodadas de extração → validação → correção com DBA Marcus Ribeiro |

---

## 7. Lições aprendidas

Referência ao documento completo: `LI-PROFARMA01-001_Licoes-Aprendidas.md`

Principais pontos:
- Outbox pattern mostrou-se decisão arquitetural estratégica correta
- Piloto na loja 9 foi essencial para validação em condições reais
- Requisitos de integração com sistemas satélites devem ser mapeados no discovery
- Processo GMUD deve ser incluído nas estimativas de prazo desde o início
- Documentação de legado deve ser tratada como subprojeto com entregável próprio

---

## 8. Transição e pós-projeto

- O código-fonte está nos repositórios do Azure DevOps da D1000 (`profarma.visualstudio.com/rede-d1000/`)
- A documentação técnica foi entregue ao cliente no pacote de encerramento
- O ambiente AKS em produção está sob controle da equipe de Operações D1000 (Fagner Pereira)
- O monitoramento Datadog está configurado e com alertas ativos
- A sustentação pós-piloto é objeto de contrato futuro entre Profarma/D1000 e Timeware

---

## 9. Aceite formal

| Envolvido | Papel | Aceite | Data | Ref. |
|---|---|---|---|---|
| Humberto Erler | Gerente de TI — Rede D1000 | Aprovado | 29/01/2026 | Comunicação formal via Microsoft Teams / e-mail |
| Helena Moreira | Coordenadora de Projeto — Rede D1000 | Confirmado | 29/01/2026 | Comunicação formal via Microsoft Teams |
| Abraão Oliveira | Gerente de Projeto — Timeware | Confirmado | 29/01/2026 | Gerente do projeto |

---

## 10. Encerramento das atividades do projeto

Com a emissão deste termo:
- O projeto Cadastro de Clientes — Rede D1000 está **formalmente encerrado**
- A equipe Timeware é liberada das obrigações deste escopo específico
- Quaisquer novas demandas são tratadas como novo contrato ou aditivo

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 05/06/2026 | Abraão Oliveira | Versão inicial — reconstituída com base nos registros do projeto e aceite de 29/01/2026 |
