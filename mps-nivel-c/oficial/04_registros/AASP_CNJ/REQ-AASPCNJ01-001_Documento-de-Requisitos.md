# Documento de Requisitos — AASP_CNJ · WorkerAndamentos

| Campo | Valor |
|---|---|
| **Documento** | REQ-AASPCNJ01-001 |
| **Projeto** | AASP_CNJ — WorkerAndamentos: Agente de Captura de Andamentos Processuais |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Responsáveis (Discovery)** | Abraão Oliveira (GP / Tech Lead) · Cézar Hiraki (Arquiteto) |

---

## 1. Contexto e objetivo

A AASP oferece a seus associados uma plataforma centralizada de monitoramento de processos judiciais em múltiplos tribunais. A Timeware opera o sistema de captura que consulta as fontes dos tribunais e persiste os dados na base da AASP, indexando-os em Elasticsearch. O modelo de captura vigente apresentava instabilidade dos crawlers, cobertura incompleta, custo elevado (~R$ 16.500/mês) e arquitetura monolítica sem observabilidade. A fila de processamento chegou a acumular 137 mil itens não processados. O objetivo é reconstruir a captura com base em um agente nativo EPROC/ESAJ para o TJSP e na API DataJud/CNJ como fonte primária universal, com roteamento por processo e fallback estruturado.

## 2. Partes interessadas

| Parte interessada | Necessidade principal |
|---|---|
| Associados da AASP | Acompanhamento confiável e atualizado dos andamentos em todos os tribunais |
| Carlos Alves (Representante do Cliente — AASP) | Cobertura ampla, custo reduzido e estabilidade da captura |
| Operação Timeware | Observabilidade, reprocessamento seletivo e escalonamento independente |

## 3. Visão geral da solução

Dois componentes coordenados: o **CapturaServer** (serviço Windows que identifica NUPs pendentes e os enfileira no RabbitMQ) e o **WorkerAndamentos** (workers que leem a fila, consultam as fontes e enviam os resultados à API AndamentosProcessuais via webhook). O roteamento de fonte é feito pelo campo `CodigoFonteAPI`. Projeto de back-end, **sem interface de usuário** (UX/UI não aplicável).

## 4. Requisitos funcionais

| ID | Origem | Requisito | Prioridade |
|---|---|---|---|
| RF-01 | Custo e cobertura | Consultar a API DataJud/CNJ como fonte primária para todos os NUPs com `CodigoFonteAPI` nulo | Alta |
| RF-02 | Instabilidade de crawler | Capturar via engine EPROC/ESAJ para processos do TJSP quando a API CNJ não retornar resultado | Alta |
| RF-03 | Arquitetura monolítica | Ler a fila RabbitMQ de forma unificada, independente do tribunal de origem | Alta |
| RF-04 | Custo de APIs parceiras | Após captura via CNJ, identificar e desligar o processo nas APIs parceiras, registrando log | Alta |
| RF-05 | Necessidade operacional | Gerenciar o token Bearer da API CNJ de forma compartilhada entre instâncias, com renovação automática | Alta |
| RF-06 | Necessidade operacional | Registrar `CodigoFonteAPI` na tabela `ProcessoCaptura` para rastrear a fonte de cada captura | Média |
| RF-07 | Necessidade operacional | Tratar fallback para APIs parceiras quando CNJ e EPROC/ESAJ falharem, por ordem de prioridade | Alta |
| RF-08 | Necessidade operacional | Tratar todos os retornos das parceiras: NUP inválido, vazio/aguardando, erro total e erro parcial por instância | Alta |
| RF-09 | Observabilidade | Registrar erros detalhados no campo `Observacao` das tabelas de controle, por instância | Alta |
| RF-10 | Necessidade de negócio | Identificar e registrar processos em segredo de justiça por instância, diferenciando acessíveis de restritas | Alta |
| RF-11 | Necessidade operacional | Enviar os dados capturados à API AndamentosProcessuais via webhook para indexação no Elasticsearch | Alta |
| RF-12 | Necessidade operacional | O CapturaServer deve enfileirar todos os processos no RabbitMQ de forma unificada, independente do tribunal | Alta |

## 5. Requisitos não funcionais

| ID | Categoria | Requisito | Critério |
|---|---|---|---|
| RNF-01 | Desempenho | Suportar múltiplos workers concorrentes na mesma fila | Sem conflito de token ou de reserva de NUP |
| RNF-02 | Confiabilidade | Retomar o processamento após travamento de fila | Sem intervenção manual |
| RNF-03 | Rastreabilidade | Registrar todos os estados de captura nas tabelas de controle | Data, status e observação de erro quando aplicável |
| RNF-04 | Manutenibilidade | Permitir adição de novas fontes de captura | Sem refatoração do fluxo principal |
| RNF-05 | Segurança | Armazenar e renovar o token Bearer da CNJ de forma centralizada | Sem exposição em logs de aplicação |
| RNF-06 | Custo | Reduzir o custo de captura | Redução ≥ R$ 150.000 anuais vs. modelo anterior |

## 6. Restrições e premissas

**Restrições:**
- A API DataJud/CNJ não retorna dados de processos em segredo de justiça (fallback obrigatório).
- Diferentes tribunais exigem diferentes credenciais para segredo (usuário/senha, certificado A1, QR Code).
- Homologação por amostragem, sem ambiente de Elasticsearch dedicado para testes.

**Premissas:**
- A API DataJud/CNJ permanece disponível, com a cobertura declarada e custo de R$ 0,01/processo.
- Associados com processos em segredo fornecem as credenciais necessárias via gerenciador quando solicitado.

## 7. Validação dos requisitos

| Requisito/conjunto | Forma de validação | Data | Resultado |
|---|---|---|---|
| Fluxo de captura CNJ (RF-01, RF-05, RF-11) | Alinhamento técnico com o time e validação de fluxo | 07/04/2026 | Validado (ATA-AASPCNJ01-001) |
| Fluxo completo e critérios de aceite | Testes de fluxo e validação por amostragem (Fase 5) | Mai–Jun/2026 | Validado (ver VV-AASPCNJ01-001 e REL-VV-AASPCNJ01-001) |

## 8. Confirmação de entendimento e compromisso

| Envolvido | Papel | Confirmação | Data |
|---|---|---|---|
| Carlos Alves | AASP | Entendimento dos objetivos de cobertura, custo e estabilidade | Out/2025 |
| Time de desenvolvimento | Timeware | Compromisso técnico assumido na apresentação do fluxo CNJ | 07/04/2026 |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Documento de requisitos consolidado a partir do Registro de Projeto AASP_CNJ v1.0 (08/06/2026). |
