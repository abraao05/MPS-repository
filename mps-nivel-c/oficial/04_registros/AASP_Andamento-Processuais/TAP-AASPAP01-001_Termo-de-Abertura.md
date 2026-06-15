# Termo de Abertura do Projeto — AASP_AndamentosProcessuais

| Campo | Valor |
|---|---|
| **Documento** | TAP-AASPAP01-001 |
| **Projeto** | AASP_AndamentosProcessuais — Refatoração da Solução de Captura de Andamentos |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.0 |
| **Data de abertura** | 11/06/2026 |
| **Gerente de Projeto** | Cezar Hiraki Velazquez |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Objetivo do projeto

Refatorar a solução legada .NET de captura de andamentos processuais da AASP (API AndamentosProcessuais + CapturaServer, com cerca de 20 anos de operação) para suportar o novo modelo de captura DataJud/CNJ via WorkerAndamentos. A refatoração introduz fila unificada (RabbitMQ, independente do tribunal de origem), webhook de indexação multi-fonte, histórico de movimentações por instância, verificação e desligamento automático nas APIs parceiras após captura via CNJ e controle de erros e de segredo de justiça por instância — tudo por evolução cirúrgica e delimitada, sem reescrita do sistema legado e sem interromper a operação existente durante a transição.

## 2. Escopo macro

- **Incluído (macro):**
  - Refatoração do CapturaServer para publicação na fila WorkerAndamentos (RabbitMQ) com `SegmentoTribunal`, independente do tribunal de origem.
  - Webhook de indexação multi-fonte, sem campos fixos por tribunal.
  - Histórico de movimentações por instância (inativação do registro anterior e criação de novo, sem sobrescrita).
  - Verificação e desligamento do NUP nas APIs parceiras (Solucionário, Botmax) após captura via CNJ, com registro do retorno.
  - Campo `CodigoFonteAPI` e endpoint de atualização; campo `Observacao` para erro por instância; campo `Segredo` por instância.
  - Tratamento de erros parciais por instância e desmembramento do RunUpdater para priorização de retornos.

- **Não incluído:**
  - O restante da solução AndamentosProcessuais permanece inalterado (alterações cirúrgicas).
  - Sem migração de dados no Elasticsearch; sem alteração estrutural do `IModelElastic`; sem reescrita do sistema legado.

## 3. Partes interessadas

| Parte interessada | Responsabilidade | Organização |
|---|---|---|
| Marcos Correa Fernandez Turnes (Representante / Sponsor / PO) | Autorização do projeto, validação de requisitos, homologação e aceite formal das entregas | AASP |
| Cezar Hiraki Velazquez (Gerente de Projeto / Tech Lead / Arquiteto) | Alinhamento com o cliente, decisões técnicas e gestão das entregas | Timeware Brasil |
| Patrocinador interno | Patrocínio do projeto e priorização de portfólio | Timeware Brasil |

## 4. Equipe do projeto

| Papel | Responsável |
|---|---|
| Gerente de Projeto / Tech Lead / Arquiteto | Cezar Hiraki Velazquez |
| Desenvolvedor Sênior (Principal) | Raony Chagas |
| Desenvolvedor (Suporte) | Mateus Veloso (incorporado em Abr/2026) |
| Analista de QA / Testes | Caroline Sousa (Fase 4) |
| Infraestrutura / DevOps | Lucas Batista (Fases 2 e 5) |
| Auditor GQA (independente) | Jonathan Barbosa |

## 5. Macroplanejamento (datas-alvo)

| Marco | Data-alvo |
|---|---|
| Kickoff / início do ciclo | 15/12/2025 |
| Fim das Fases 1–2 (Webhook / CapturaServer / RabbitMQ) | Mar/2026 |
| Fim da Fase 3 (Refatoração CNJ) | Mai/2026 |
| Fim da Fase 4 (Tratamento de erros e validação) | Jun/2026 |
| Implantação (Fase 5) | Jun/2026 |
| Encerramento previsto | 30/06/2026 |

## 6. Agenda das próximas atividades (na abertura)

- Definição do primeiro entregável (webhook de indexação dedicado para EPROC/ESAJ).
- Preparação do ambiente de homologação compartilhado com o projeto AASP_CNJ.
- Alinhamento do fluxo de captura com o time ampliado.

## 7. Premissas e restrições iniciais

**Premissas:**
- A solução legada em produção permanece operante durante a transição (refatoração com retrocompatibilidade).
- O ambiente de homologação é compartilhado com o projeto irmão AASP_CNJ (mesmo time e ciclo).
- As APIs parceiras (Solucionário, Botmax) expõem endpoints de verificação e exclusão de NUP.

**Restrições:**
- Não há ambiente de Elasticsearch dedicado para testes; a homologação é feita por amostragem.
- As alterações na solução legada devem ser cirúrgicas, sem reescrita e sem alteração estrutural do `IModelElastic`.
- A implantação em produção segue o rito de GMUD (pacotes versionados + scripts DDL no Azure DevOps).

---

## Registro de abertura

O projeto foi aberto com o início do ciclo de refatoração em 15/12/2025. O alinhamento técnico formal do novo fluxo de captura via API CNJ com o time ampliado está registrado em ATA de alinhamento de 07/04/2026. A baseline do Plano (REG-AASPAP01-001 v1.0) foi aprovada em 08/06/2026.

| Marco de abertura | Ref. |
|---|---|
| Início do ciclo de refatoração | 15/12/2025 |
| Alinhamento técnico — fluxo da API CNJ | Ata de alinhamento (07/04/2026) |
| Aprovação do Plano (baseline) | REG-AASPAP01-001 v1.0 (08/06/2026) |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Termo de abertura consolidado a partir do Registro de Projeto AASP_AndamentosProcessuais (REG-AASPAP01-001 v1.0, 08/06/2026) e do levantamento de projeto (INTAKE-PROJETO_AASPAP01 v1.0). |
