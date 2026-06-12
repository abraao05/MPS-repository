# Relatório de Acompanhamento (Status Report) — AASP_CNJ · WorkerAndamentos

| Campo | Valor |
|---|---|
| **Projeto** | AASP_CNJ — WorkerAndamentos: Agente de Captura de Andamentos Processuais |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Período de referência** | Junho/2026 — Fase 6 (Implantação e Complementos) |
| **Data do relatório** | 11/06/2026 |
| **Gerente de Projeto** | Abraão Oliveira |
| **Destinatários** | Carlos Alves (Representante do Cliente — AASP); Patrocinador interno (Timeware) |

---

## 1. Situação geral

Desenvolvimento concluído (Fases 1–5); o projeto está em implantação em produção (Fase 6), com encerramento previsto para 30/06/2026.

| Dimensão | Status | Comentário |
|---|---|---|
| **Prazo** | 🟡 Atenção | Desenvolvimento concluído em 01/06/2026 (~30 dias após o alvo de 02/05), por escopo adicional acordado |
| **Escopo** | 🟡 Em mudança | Captura de 2ª instância EPROC pausada e retomada em jun/2026 (CR-AASPCNJ01-001) |
| **Risco** | 🟢 Sob controle | Travamento de fila corrigido; monitoramento ativo implantado |
| **Qualidade** | 🟢 Dentro do esperado | 9 defeitos tratados; critérios de aceite validados por amostragem |

## 2. Resumo do período

A integração CNJ está concluída e validada (sucesso, fallback e erro parcial por instância). A operação migra progressivamente das APIs privadas para a fonte CNJ, com desligamento automático dos NUPs nas parceiras após a primeira captura. No período corrente, o foco é a montagem dos pacotes de GMUD, o deploy em produção e a retomada da captura de 2ª instância no EPROC.

**Indicadores do período (destaque):**

| Indicador | Valor |
|---|---|
| Esforço total realizado (parcial) | ~624 h |
| Economia mensal projetada | ~R$ 14.670 |
| Fases concluídas | 5 de 6 |

## 3. Entregas realizadas no período

| Entrega | Resultado / valor para o cliente | Situação |
|---|---|---|
| Integração DataJud/CNJ (fonte primária) | Cobertura nacional e custo R$ 0,01/processo | ✅ Concluído |
| Estratégia de fallback (3 níveis) | Resiliência da captura | ✅ Concluído |
| Desligamento automático nas parceiras | Fim do duplo pagamento na migração | ✅ Concluído |
| Controle de segredo de justiça por instância | Tratamento correto sem omissões | ✅ Concluído |
| Correção do travamento de fila (137 mil itens) | Estabilidade da operação | ✅ Concluído |

## 4. Planejado para o próximo período

| Item / marco | Data prevista | Observação |
|---|---|---|
| Deploy em produção (pacotes GMUD) | Jun/2026 | Agendamento com Infraestrutura |
| Captura de 2ª instância EPROC (retomada) | Jun/2026 | Retomada após conclusão da Fase 5 (CR-AASPCNJ01-001) |
| Encerramento formal do projeto | 30/06/2026 | TAE e ata de aceite (Onda 3) |

## 5. Indicadores do projeto (acompanhamento)

| Indicador | Meta / referência | Período atual | Tendência |
|---|---|---|---|
| Esforço estimado × realizado | ≤ 10% desvio | +~6% (601–624 h vs. 586 h) | ➡️ |
| Estabilidade da fila | Zero travamentos manuais/mês | Estável após correção da Fase 4 | ⬆️ |
| Economia de custo | ≥ R$ 12.500/mês | ~R$ 14.670/mês projetado | ⬆️ |

## 6. Diário de bordo (eventos e impactos)

| Data | Evento / motivo | Origem | Impacto | Situação |
|---|---|---|---|---|
| Mar/2026 | Timeout após captcha Cloudflare (EPROC) | Externo (portal) | Ajuste de espera | Resolvido (BUG-01) |
| Abr/2026 | Fila RabbitMQ acumulou 137 mil itens | Timeware | Estabilização | Resolvido (BUG-05/06) |
| Mai/2026 | Pausa da 2ª instância EPROC para priorizar CNJ | Acordo c/ cliente | Realocação | Resolvido (CR-001) |
| Jun/2026 | Atividades de finalização e retomada da 2ª instância | Timeware | Em curso | Em andamento |

## 7. Pontos de atenção, riscos e plano de ação

**Cobertura de segredo de justiça** — 🟡 Médio
- **Ponto:** o CNJ não retorna processos em segredo; alguns tribunais exigem credenciais específicas.
- **Risco:** instâncias sem atualização quando a credencial não está disponível.
- **Ação:** fallback por instância (EPROC/ESAJ ou parceiras com credencial); solicitação de credenciais aos associados via gerenciador.

## 8. Mudanças (change requests)

| ID | Descrição | Abertura | Status | Aceite final |
|---|---|---|---|---|
| CR-AASPCNJ01-001 | Pausa e retomada da captura de 2ª instância EPROC | Mai/2026 | Aprovada (acordada com o cliente) | — |

## 9. Decisões necessárias

| Decisão necessária | Responsável | Prazo desejado |
|---|---|---|
| Confirmação da data de aceite formal e do go-live em produção | Carlos Alves (AASP) | Jun/2026 |

---

## Cadência de reporte

| Item | Definição |
|---|---|
| Periodicidade | Por marco/fase, com reuniões de alinhamento |
| Canal | Reunião de alinhamento + devolutivas ao cliente |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Relatório de acompanhamento (Fase 6) consolidado a partir do Registro de Projeto AASP_CNJ v1.0 (08/06/2026). |
