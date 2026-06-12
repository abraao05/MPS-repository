# Registro de Capacitação da Equipe — AASP_CNJ · WorkerAndamentos

| Campo | Valor |
|---|---|
| **Documento** | CAP-AASPCNJ01-001 — Registro de Capacitação da Equipe |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | AASP_CNJ — WorkerAndamentos: Agente de Captura de Andamentos Processuais |
| **Aprovação** | Abraão Oliveira |

---

## 1. Objetivo

Registrar a composição da equipe e as práticas de transferência de conhecimento adotadas ao longo do projeto, em especial a integração de um desenvolvedor de suporte e a disseminação do fluxo da nova arquitetura de captura.

## 2. Equipe alocada

| Membro (papel) | Período de atuação | Fases |
|---|---|---|
| Abraão Oliveira — Gerente de Projeto / Tech Lead | Out/2025 – Jun/2026 | Todas |
| Cézar — Arquiteto de Software | Out/2025 – Mar/2026 | 1, 2, 3 |
| Raony Chagas — Desenvolvedor Sênior (Principal) | Dez/2025 – Jun/2026 | 2, 3, 4, 5, 6 |
| Levi Santos — Desenvolvedor (Suporte) | Abr/2026 – Jun/2026 | 4, 5 |
| Jonatan — Analista de Testes | Mai/2026 – Jun/2026 | 5 |
| David — Infraestrutura / DevOps | Jan/2026 e Jun/2026 | 1, 6 |

## 3. Integração formal de membro ao time

Em abril/2026, um desenvolvedor de suporte foi incorporado para auxiliar o Desenvolvedor Sênior (Raony Chagas) nas atividades de maior volume da integração CNJ. A integração foi conduzida na reunião de alinhamento de 07/04/2026 (ATA-AASPCNJ01-001), na qual foram apresentados o funcionamento da API DataJud, a lógica de roteamento por `CodigoFonteAPI`, os mecanismos de fallback e o modelo de gravação no Elasticsearch.

## 4. Práticas de transferência de conhecimento

| Prática | Descrição |
|---|---|
| Revisão de código (code review) | Revisão nas integrações de branches no Azure DevOps, garantindo ciência das mudanças por todo o time (ver REV-AASPCNJ01-001) |
| Reuniões de alinhamento periódicas | Estado do projeto e decisões técnicas compartilhados e registrados no ClickUp |
| Documentação técnica | Coleções Postman da API CNJ e registros de banco disponibilizados no Azure DevOps |
| Continuidade durante férias do GP | Alinhamento específico para garantir autonomia do time no período de ausência do gestor |

## 5. Observações

A equipe já atuava com as tecnologias core (.NET, Azure DevOps, RabbitMQ, Elasticsearch), dispensando treinamento formal específico. As ações de preparo focaram no contexto da nova arquitetura de captura (DataJud/CNJ e fallback). O Plano de Capacitação Organizacional aplicável está registrado em PLA-CAP-001.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Registro de capacitação da equipe consolidado a partir do Registro de Projeto AASP_CNJ v1.0 (08/06/2026). |
