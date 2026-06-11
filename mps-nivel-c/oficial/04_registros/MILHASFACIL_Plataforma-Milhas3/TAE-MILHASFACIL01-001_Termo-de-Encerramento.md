# Termo de Encerramento — Milhas3

| Campo | Valor |
|---|---|
| **Documento** | TAE-MILHASFACIL01-001 — Termo de Encerramento |
| **Versão** | 1.0 |
| **Data** | 16/11/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Milhas3 — Plataforma de Busca e Monitoramento de Milhas |
| **Cliente** | Hub de Milhas (Felipe) |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR — Gerência de Projeto |

---

## 1. Identificação do projeto

| Campo | Valor |
|---|---|
| Projeto | Milhas3 — Plataforma de Busca e Monitoramento de Milhas |
| Cliente | Hub de Milhas (Felipe) |
| Início | 16/05/2025 |
| Encerramento | 16/11/2025 |
| Duração realizada | 26 semanas |
| Sprints executadas | 13 sprints + Sprint 0 (setup) |

## 2. Sumário da entrega

A plataforma **Milhas3** foi desenvolvida e implantada em produção conforme o escopo definido em REQ-MILHASFACIL01-001 e TAP-MILHASFACIL01-001. A entrega compreende:

- **Interface web** (Angular 16+) — busca de voos em milhas, assinatura de rotas de interesse, histórico de buscas, preferências / rotas favoritas, notificações in-app, chat de suporte
- **Servidor central** (Java 17 / Spring Boot 3.x + PostgreSQL) — autenticação JWT, lógica de negócio, persistência, orquestração de alertas, notificações por e-mail
- **Motor de rastreamento automatizado** (Selenium WebDriver + headless Chrome) — integrado aos portais LATAM Pass, Smiles (GOL), TudoAzul (Azul), TAP Miles&Go e Iberia Plus, com contorno da proteção Akamai Bot Manager (GDE-MILHASFACIL01-001)
- **Pipeline CI/CD** configurado no Azure DevOps; deploy em VM Linux provisionada pelo cliente
- **Documentação MPS-SW completa** (17 documentos) arquivada em `04_registros/MILHASFACIL_Plataforma-Milhas3/`

Todos os 16 requisitos funcionais (RF-01 a RF-16) foram entregues. Requisitos não funcionais de performance, segurança, qualidade e disponibilidade atendidos conforme critérios de REQ-MILHASFACIL01-001 §5.

## 3. Desvios em relação ao plano

| Dimensão | Planejado | Realizado | Desvio |
|---|---|---|---|
| Prazo | Aceite em 16/11/2025 | Aceite em 16/11/2025 | Nenhum |
| Escopo | RF-01 a RF-16 | RF-01 a RF-16 entregues | Nenhum |
| Qualidade | 0 defeitos críticos ao encerramento | 0 defeitos críticos | Nenhum |
| Sprints | 13 + Sprint 0 | 13 + Sprint 0 | Nenhum |
| Riscos | R-01 como risco de probabilidade 3 | R-01 materializado parcialmente (Smiles, Sprint 7) | Resolvido em 1 dia, sem impacto no prazo |

## 4. Documentação MPS-SW entregue

| Documento | Código | Versão |
|---|---|---|
| Termo de Abertura | TAP-MILHASFACIL01-001 | 1.0 |
| Plano de Projeto | PLA-MILHASFACIL01-001 | 1.0 |
| Registro de Adaptação | ADAP-MILHASFACIL01-001 | 1.0 |
| Documento de Requisitos | REQ-MILHASFACIL01-001 | 1.0 |
| Documento de Design | PCP-MILHASFACIL01-001 | 1.0 |
| Estratégia de Integração | ITP-MILHASFACIL01-001 | 1.0 |
| Matriz de Rastreabilidade | RASTR-MILHASFACIL01-001 | 1.0 |
| Plano de VV | VV-MILHASFACIL01-001 | 1.0 |
| Registro de Análise de Decisão | GDE-MILHASFACIL01-001 | 1.0 |
| Registro de Configuração | GCO-MILHASFACIL01-001 | 1.0 |
| Registro de GQA | GQA-MILHASFACIL01-001 | 1.0 |
| Registro de Medição | MED-MILHASFACIL01-001 | 1.0 |
| Ata de Kickoff | ATA-MILHASFACIL01-001 | 1.0 |
| Ata de Aceite Final | ATA-MILHASFACIL01-002 | 1.0 |
| Relatório de Acompanhamento | RAC-MILHASFACIL01-001 | 1.0 |
| Lições Aprendidas | LI-MILHASFACIL01-001 | 1.0 |
| Termo de Encerramento | TAE-MILHASFACIL01-001 | 1.0 |

## 5. Aceite formal

O encerramento do projeto foi formalizado na reunião de aceite realizada em 16/11/2025. **Felipe (Hub de Milhas) declarou aceite formal** de todos os requisitos entregues, conforme registrado em ATA-MILHASFACIL01-002.

## 6. Transferência de responsabilidades

A partir de 16/11/2025, a responsabilidade pela operação, manutenção e evolução da plataforma Milhas3 é transferida integralmente ao Hub de Milhas. O acesso aos repositórios Azure DevOps (`milhas3-backend`, `milhas3-frontend`, `milhas3-infra`) foi transferido ao cliente em 16/11/2025.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 16/11/2025 | Time de Melhoria Contínua | Documento final — encerramento formal do projeto |
