# Termo de Abertura — Milhas3 · Plataforma de Busca e Monitoramento de Milhas

| Campo | Valor |
|---|---|
| **Documento** | TAP-MILHASFACIL01-001 — Termo de Abertura |
| **Versão** | 1.0 |
| **Data** | 16/05/2025 |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Projeto** | Milhas3 — Plataforma de Busca e Monitoramento de Milhas |
| **Cliente** | Hub de Milhas (Felipe) |
| **Gerente de Projeto** | Abraão Oliveira |
| **Processo MPS-SW** | GPR — Gerência de Projeto |

---

## 1. Objetivo e justificativa

O Hub de Milhas necessita de uma plataforma centralizada para busca e monitoramento de disponibilidade de passagens aéreas em programas de fidelidade (milhas e pontos). O modelo atual — baseado em consultas manuais e dispersas em múltiplos sites de companhias aéreas — não escala e resulta em perda de oportunidades pelo cliente final, dado que disponibilidades em milhas surgem e desaparecem de forma imprevisível.

A plataforma **Milhas3** é a resposta a essa necessidade: uma solução automatizada que rastreia continuamente a disponibilidade de assentos nos principais programas de milhas brasileiros e internacionais, consolida os resultados em uma interface única e notifica o usuário proativamente quando uma oportunidade relevante é identificada.

## 2. Escopo macro

### 2.1 Incluído

- Interface web (Angular) para busca, gerenciamento de preferências e recebimento de notificações
- Servidor central (Java / Spring Boot) responsável por autenticação, histórico de buscas, assinaturas de rotas, alertas e lógica de negócio
- Motor de rastreamento automatizado (Java / Spring Boot + Selenium) que acessa os sites das companhias aéreas em tempo real para coleta de disponibilidade e preços em milhas
- Integração com programas de fidelidade: LATAM Pass, Smiles (GOL), TudoAzul (Azul), TAP Miles&Go, Iberia Plus
- Sistema de alertas e notificações (in-app, e-mail)
- Histórico de buscas e preferências de rotas por usuário
- Canal de chat / suporte integrado
- Pipeline CI/CD no Azure DevOps; implantação em VM Linux

### 2.2 Não incluído

- Aplicativos móveis nativos (iOS / Android)
- Compra ou reserva de passagens dentro da plataforma
- Integração com companhias aéreas além das cinco definidas neste escopo
- Suporte a programas de pontos de cartões de crédito (ex.: Livelo, Esfera, Multiplus)

## 3. Equipe do projeto

| Papel | Responsável | Dedicação |
|---|---|---|
| Gerente de Projeto | Abraão Oliveira | Parcial |
| UI/UX Designer | Igor Santana | Parcial |
| QA | Caroline Sousa | Parcial |
| Tech Lead / Back-End | Henry Komatsu | Integral |
| Back-End (Java) | Mateus Veloso | Integral |
| Front-End (Angular) | Beatriz Nunes | Integral |
| Front-End (Angular) | Lucas Batista | Integral |
| GQA de Processo | COO (Operações) | Parcial |

## 4. Macroplanejamento

| Marco | Data prevista |
|---|---|
| Kickoff | 16/05/2025 |
| Sprint 0 — Setup e infraestrutura | 16/05 – 30/05/2025 |
| Início do desenvolvimento (Sprint 1) | 02/06/2025 |
| Motor de rastreamento operacional (5 programas) | 25/07/2025 |
| Funcionalidades de alertas e assinaturas entregues | 22/08/2025 |
| Início de homologação com cliente | 06/10/2025 |
| Aceite formal e encerramento | 16/11/2025 |

## 5. Premissas

- O cliente (Hub de Milhas) provê credenciais de contas de teste nos programas de fidelidade para uso durante o desenvolvimento e homologação
- Os sites das companhias aéreas mantêm estrutura HTML estável o suficiente para rastreamento via Selenium durante o ciclo do projeto; alterações estruturais são tratadas como escopo de manutenção pós-entrega
- A VM Linux de produção é provisionada pelo cliente antes do início do Sprint 1 (prazo: 30/05/2025)
- Revisões de protótipos (UI/UX) são realizadas pelo cliente em até 3 dias úteis após envio

## 6. Restrições

- Prazo fixo: encerramento em 16/11/2025
- Infraestrutura de produção em VM Linux (sem Kubernetes ou PaaS neste projeto)
- Rastreamento restrito às cinco companhias definidas no escopo
- A plataforma não realiza transações financeiras

## 7. Partes interessadas

| Nome | Organização | Papel |
|---|---|---|
| Felipe | Hub de Milhas | Patrocinador / Product Owner (cliente) |
| Abraão Oliveira | Timeware | Gerente de Projeto |
| Igor Santana | Timeware | UI/UX Designer |
| Henry Komatsu | Timeware | Tech Lead / Back-End |
| COO | Timeware | GQA de Processo |

## 8. Registro de abertura

Projeto formalmente aberto em reunião de kickoff realizada em 16/05/2025 (ATA-MILHASFACIL01-001). Aprovação do escopo macro e da equipe confirmada por Felipe (Hub de Milhas) em 16/05/2025.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 16/05/2025 | Time de Melhoria Contínua | Documento inicial — abertura do projeto |
