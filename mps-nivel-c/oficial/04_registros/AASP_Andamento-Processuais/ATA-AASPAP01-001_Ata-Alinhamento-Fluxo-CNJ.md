# Ata de Reunião — Alinhamento e revisão do fluxo de captura (refatoração AndamentosProcessuais)

| Campo | Valor |
|---|---|
| **Documento** | ATA-AASPAP01-001 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Versão** | 1.0 |
| **Data** | 11/06/2026 |
| **Gerente de Projeto / Responsável pela ata** | Cezar Hiraki Velazquez |
| **Processo MPS-SW** | GPR (acompanhamento — evidência de projeto) |
| **Local / meio** | Videoconferência |

---

Esta ata consolida o alinhamento técnico do fluxo (07/04/2026) e a revisão do fluxo com o time ampliado (08/05/2026), conforme o BLOCO 10 do levantamento do projeto.

## 1. Participantes

| Nome | Papel | Organização |
|---|---|---|
| Cezar Hiraki Velazquez | Gerente de Projeto / Tech Lead / Arquiteto | Timeware |
| Raony Chagas | Desenvolvedor Sênior (Principal) | Timeware |
| Mateus Veloso | Desenvolvedor (Suporte) | Timeware |
| Caroline Sousa | Analista de QA | Timeware |
| Lucas Batista | DevOps / Infraestrutura | Timeware |

---

## Sessão 1 — Alinhamento do fluxo da API CNJ (07/04/2026)

### 2. Pauta

- Apresentação do novo fluxo de captura multi-fonte (DataJud/CNJ + EPROC/ESAJ + parceiras).
- Definição das responsabilidades de cada componente no novo modelo.
- Integração do desenvolvedor de suporte (Mateus Veloso), incorporado em Abr/2026.

### 3. Discussões e definições

O Gerente de Projeto apresentou o fluxo completo da refatoração: migração do `CapturaServer` para a fila unificada `WorkerAndamentos` (RabbitMQ) com `SegmentoTribunal`, webhook de indexação parametrizado para múltiplas fontes, histórico de movimentações por inativação de registro, e verificação/desligamento nas APIs parceiras (Solucionário, Botmax) na camada da API após a captura via CNJ.

### 4. Decisões e aceites

| Decisão / aceite | Responsável | Data |
|---|---|---|
| Parametrizar o webhook para suporte multi-fonte (D03) | Cezar Hiraki Velazquez / time | 07/04/2026 |
| Histórico de movimentações por inativação de registro (D04) | Raony Chagas | 07/04/2026 |
| Verificação/desligamento das parceiras na camada da API (D05) | Raony Chagas | 07/04/2026 |

(Decisões detalhadas em GDE-AASPAP01-001.)

### 5. Ações (follow-up)

| Ação | Responsável | Prazo |
|---|---|---|
| Refatorar o webhook para múltiplas fontes | Raony Chagas | Abr/2026 |
| Implementar a lógica de movimentações por inativação | Raony Chagas | Abr/2026 |
| Onboarding do desenvolvedor de suporte no fluxo | Cezar Hiraki Velazquez | Abr/2026 |

---

## Sessão 2 — Revisão do fluxo e definição de atividades (08/05/2026)

### 6. Pauta

- Revisão completa do fluxo com o time ampliado.
- Redistribuição de atividades entre os dois projetos correlatos (AASP_AndamentosProcessuais e AASP_CNJ).
- Planejamento da continuidade do time durante o período de férias do GP (06–08/05/2026).

### 7. Discussões e definições

Revisado o andamento das Fases 3–4: webhook multi-fonte e movimentações entregues; foco no tratamento de erros por instância (campo `Observacao`), no controle de segredo de justiça por instância (campo `Segredo`, decisão D07) e na atualização do `CodigoFonteAPI`. Esse escopo adicional foi formalizado no CR-AASPAP01-002. Acordada a continuidade autônoma do time durante a ausência do gestor.

### 8. Decisões e aceites

| Decisão / aceite | Responsável | Data |
|---|---|---|
| Controlar segredo de justiça por instância — campo `Segredo` (D07) | Raony Chagas | 08/05/2026 |
| Formalizar o escopo adicional da Fase 4 (CR-AASPAP01-002) | Cezar Hiraki Velazquez / Marcos Correa Fernandez Turnes | Mai/2026 |
| Redistribuir atividades entre AASP_AndamentosProcessuais e AASP_CNJ | Cezar Hiraki Velazquez / time | 08/05/2026 |

### 9. Próximos passos

Conclusão da Fase 4 (tratamento de erros, segredo e validação E2E + regressão EPROC) e preparação da Fase 5 (montagem do pacote GMUD e deploy em produção).

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Ata consolidando o alinhamento de 07/04/2026 e a revisão de 08/05/2026, reconstituída a partir do INTAKE-PROJETO_AASPAP01 v1.0 (14/06/2026, BLOCO 10) e do Registro de Projeto REG-AASPAP01-001. |
