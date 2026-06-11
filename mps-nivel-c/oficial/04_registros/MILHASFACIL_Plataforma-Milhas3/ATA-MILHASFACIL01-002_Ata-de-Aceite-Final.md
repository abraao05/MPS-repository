# Ata de Reunião — Aceite Final · Milhas3

| Campo | Valor |
|---|---|
| **Documento** | ATA-MILHASFACIL01-002 — Ata de Aceite Final |
| **Versão** | 1.0 |
| **Data** | 16/11/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Milhas3 — Plataforma de Busca e Monitoramento de Milhas |
| **Cliente** | Hub de Milhas (Felipe) |
| **Processo MPS-SW** | GPR — Gerência de Projeto / ORG |

---

## 1. Identificação da reunião

| Campo | Valor |
|---|---|
| Tipo | Reunião de aceite formal e encerramento do projeto |
| Data | 16/11/2025 |
| Canal | Microsoft Teams |
| Moderador | Abraão Oliveira |
| Duração | [A CONFIRMAR] |

## 2. Participantes

| Nome | Organização | Papel |
|---|---|---|
| Felipe | Hub de Milhas | Patrocinador / Product Owner |
| Abraão Oliveira | Timeware | Gerente de Projeto |
| Henry Komatsu | Timeware | Tech Lead |
| Caroline Sousa | Timeware | QA |

## 3. Pauta

1. Demonstração da plataforma Milhas3 em ambiente de produção
2. Validação dos requisitos funcionais de prioridade Alta e Média
3. Confirmação dos resultados de homologação (Sprints 11 e 12)
4. Aceite formal do produto entregue
5. Alinhamento sobre transferência de acesso (repositório Azure DevOps, credenciais de ambiente)
6. Encerramento formal do projeto

## 4. Demonstração realizada

Henry Komatsu realizou demonstração ao vivo da plataforma Milhas3 em produção, cobrindo:

| Funcionalidade demonstrada | RF coberto | Resultado |
|---|---|---|
| Cadastro e login na plataforma | RF-01, RF-02 | Funcional |
| Busca de voos em milhas — GRU → GIG (5 programas simultâneos) | RF-04–09 | Resultados retornados em ≤ 30s |
| Cadastro de rota GRU → LIS (TAP Miles&Go) e disparo de alerta | RF-10, RF-11 | Alerta disparado em ≤ 5 min |
| Visualização de histórico de buscas | RF-12 | Histórico exibido corretamente |
| Notificação in-app e e-mail recebido | RF-14, RF-15 | Notificações funcionais |
| Chat / suporte — envio de mensagem de teste | RF-16 | Funcional |

## 5. Decisões tomadas

| ID | Decisão |
|---|---|
| D-01 | **Felipe (Hub de Milhas) declara aceite formal da plataforma Milhas3 v1.0** — todos os requisitos de prioridade Alta e Média atendidos conforme REQ-MILHASFACIL01-001 |
| D-02 | Acesso ao repositório Azure DevOps (`milhas3-backend`, `milhas3-frontend`, `milhas3-infra`) transferido ao cliente em 16/11/2025 |
| D-03 | Projeto encerrado — responsabilidade de operação, manutenção e evolução transferida ao Hub de Milhas a partir desta data |

## 6. Encaminhamentos pós-encerramento

| ID | Ação | Responsável | Prazo |
|---|---|---|---|
| A-01 | Emitir Termo de Encerramento (TAE-MILHASFACIL01-001) | Abraão Oliveira | 16/11/2025 |
| A-02 | Registrar Lições Aprendidas (LI-MILHASFACIL01-001) | Abraão Oliveira | 16/11/2025 |
| A-03 | Criar tag `v1.0.0` no repositório e finalizar pipeline de build | Henry Komatsu | 16/11/2025 |
| A-04 | Finalizar registro de Medição (MED-MILHASFACIL01-001) | Abraão Oliveira | 16/11/2025 |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 16/11/2025 | Time de Melhoria Contínua | Documento inicial |
