# Ata de Reunião — Kickoff · Milhas3

| Campo | Valor |
|---|---|
| **Documento** | ATA-MILHASFACIL01-001 — Ata de Kickoff |
| **Versão** | 1.0 |
| **Data** | 16/05/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Milhas3 — Plataforma de Busca e Monitoramento de Milhas |
| **Cliente** | Hub de Milhas (Felipe) |
| **Processo MPS-SW** | GPR — Gerência de Projeto / ORG |

---

## 1. Identificação da reunião

| Campo | Valor |
|---|---|
| Tipo | Kickoff gerencial |
| Data | 16/05/2025 |
| Canal | Microsoft Teams |
| Moderador | Abraão Oliveira |
| Duração | [A CONFIRMAR] |

## 2. Participantes

| Nome | Organização | Papel |
|---|---|---|
| Felipe | Hub de Milhas | Patrocinador / Product Owner |
| Abraão Oliveira | Timeware | Gerente de Projeto |
| Igor Santana | Timeware | UI/UX Designer |
| Henry Komatsu | Timeware | Tech Lead / Back-End |
| Caroline Sousa | Timeware | QA |

## 3. Pauta

1. Apresentação da equipe Timeware ao cliente
2. Revisão da visão de produto (Milhas3) e validação do escopo macro
3. Confirmação dos cinco programas de fidelidade no escopo (LATAM Pass, Smiles, TudoAzul, TAP, Iberia)
4. Apresentação do macroplanejamento (16/05 – 16/11/2025, 13 sprints de 2 semanas)
5. Decisão sobre tecnologia do motor de rastreamento (Selenium + bypass Akamai)
6. Alinhamento sobre premissas, restrições e pré-condições do projeto
7. Aprovação formal do TAP-MILHASFACIL01-001 e PLA-MILHASFACIL01-001

## 4. Decisões tomadas

| ID | Decisão | Responsável | Data |
|---|---|---|---|
| D-01 | Selenium WebDriver (headless Chrome) aprovado como tecnologia do motor de rastreamento para contornar Akamai Bot Manager dos portais | Henry Komatsu | 16/05/2025 |
| D-02 | Cronograma aprovado: kickoff 16/05/2025, aceite 16/11/2025, sprints de 2 semanas | Abraão Oliveira | 16/05/2025 |
| D-03 | TAP-MILHASFACIL01-001 e PLA-MILHASFACIL01-001 aprovados formalmente nesta reunião | Felipe + Abraão | 16/05/2025 |
| D-04 | Cinco programas confirmados no escopo: LATAM Pass, Smiles (GOL), TudoAzul (Azul), TAP Miles&Go, Iberia Plus | Felipe | 16/05/2025 |

## 5. Encaminhamentos

| ID | Ação | Responsável | Prazo |
|---|---|---|---|
| A-01 | Provisionar VM Linux de produção | Felipe (Hub de Milhas) | 30/05/2025 |
| A-02 | Fornecer credenciais de contas de teste nos 5 programas de fidelidade | Felipe (Hub de Milhas) | 30/05/2025 |
| A-03 | Criar repositórios Azure DevOps e configurar pipeline CI/CD base | Henry Komatsu | 30/05/2025 |
| A-04 | Elaborar primeiros protótipos de UI (tela de busca e autenticação) | Igor Santana | 13/06/2025 (fim Sprint 1) |
| A-05 | Iniciar implementação do motor de rastreamento LATAM Pass (Sprint 2) | Henry Komatsu + Mateus Veloso | 16/06/2025 |

## 6. Próxima reunião

Sprint Review Sprint 1 — prevista para 13/06/2025 via Microsoft Teams.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 16/05/2025 | Time de Melhoria Contínua | Documento inicial |
