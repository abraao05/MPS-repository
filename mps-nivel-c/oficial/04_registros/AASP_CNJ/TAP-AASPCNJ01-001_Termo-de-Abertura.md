# Termo de Abertura do Projeto — AASP_CNJ · WorkerAndamentos

| Campo | Valor |
|---|---|
| **Documento** | TAP-AASPCNJ01-001 |
| **Projeto** | AASP_CNJ — WorkerAndamentos: Agente de Captura de Andamentos Processuais |
| **Cliente** | AASP — Associação dos Advogados de São Paulo |
| **Organização** | Timeware Brasil Softwares e Serviços LTDA |
| **Versão** | 1.0 |
| **Data de abertura** | 01/10/2025 |
| **Gerente de Projeto** | Gerente de Projeto / Tech Lead |
| **Processo MPS-SW** | GPR (evidência de projeto) |

---

## 1. Objetivo do projeto

Reconstruir o modelo de captura de andamentos processuais da plataforma de monitoramento da AASP, substituindo a dependência de web scrapers frágeis e de APIs privadas pagas por uma arquitetura baseada em duas fontes complementares: (1) um agente de captura nativo para o TJSP via EPROC/ESAJ e (2) a API DataJud do Conselho Nacional de Justiça (CNJ) como fonte primária e universal de captura. O resultado esperado é uma operação de captura mais estável, com cobertura nacional, custo significativamente menor (economia projetada de ~R$ 180 mil anuais) e observabilidade adequada para reprocessamento e escalonamento.

## 2. Escopo macro

- **Incluído (macro):**
  - Agente de captura nativo para o TJSP via EPROC/ESAJ (engine Puppeteer headless).
  - Integração com a API DataJud/CNJ como fonte primária de captura para todos os NUPs com `CodigoFonteAPI` nulo.
  - Roteamento inteligente de fonte por processo e estratégia de fallback em três níveis (CNJ → EPROC/ESAJ → APIs parceiras).
  - Enfileiramento unificado no RabbitMQ (independente do tribunal) e envio dos dados capturados à API AndamentosProcessuais via webhook.
  - Desligamento automático do processo nas APIs parceiras após captura bem-sucedida via CNJ, com log de desligamento.
  - Controle de segredo de justiça por instância processual.
  - Gestão centralizada do token Bearer da API CNJ com renovação automática compartilhada entre workers.

- **Não incluído:**
  - O front-end de consulta do associado e o índice Elasticsearch já existentes (a solução integra-se a eles via API AndamentosProcessuais, mas não os desenvolve).
  - Novos módulos da plataforma AASP fora do fluxo de captura.

## 3. Partes interessadas

| Parte interessada | Papel | Organização |
|---|---|---|
| Representante do Cliente | Validação de requisitos, homologação e aceite das entregas | AASP |
| Gerente de Projeto / Tech Lead | Alinhamento com o cliente, decisões técnicas e gestão das entregas | Timeware Brasil |
| Patrocinador interno | Patrocínio do projeto e priorização de portfólio | Timeware Brasil |

## 4. Equipe do projeto

| Papel | Responsável |
|---|---|
| Gerente de Projeto / Tech Lead | Gerente de Projeto / Tech Lead |
| Arquiteto de Software | Arquiteto de Software |
| Desenvolvedor Sênior (Principal) | Desenvolvedor Sênior |
| Desenvolvedor (Suporte) | Desenvolvedor (incorporado em abr/2026) |
| Analista de Testes | Analista de Testes (a partir da Fase 5) |
| Infraestrutura / DevOps | Equipe de Infraestrutura |

## 5. Macroplanejamento (datas-alvo)

| Marco | Data-alvo |
|---|---|
| Abertura / início (Fase 1 — Análise e Arquitetura) | 01/10/2025 |
| Fim do desenvolvimento EPROC/ESAJ (Fases 2–3) | Abr/2026 |
| Fim do desenvolvimento CNJ (Fase 4) | Mai/2026 |
| Testes e validação (Fase 5) | Jun/2026 |
| Implantação e complementos (Fase 6) | Jun/2026 |
| Encerramento previsto | 30/06/2026 |

## 6. Agenda das próximas atividades (na abertura)

- Estudo do comportamento do captcha Cloudflare nos portais do TJSP e estratégias de contorno.
- Definição da arquitetura da solução EPROC/ESAJ.
- Preparação dos ambientes de homologação.

## 7. Premissas e restrições iniciais

**Premissas:**
- A API DataJud/CNJ permanece disponível, com a cobertura de tribunais declarada e custo de R$ 0,01 por processo.
- Associados com processos em segredo de justiça fornecem as credenciais necessárias quando solicitado.

**Restrições:**
- A API DataJud/CNJ não retorna dados de processos em segredo de justiça, exigindo fallback obrigatório.
- Diferentes tribunais exigem diferentes credenciais para acesso a processos em segredo (usuário/senha, certificado A1, QR Code).
- Homologação realizada por amostragem, sem ambiente de Elasticsearch dedicado para testes.

---

## Registro de abertura

O projeto foi aberto com o início da Fase 1 (Análise e Arquitetura) em 01/10/2025. O alinhamento técnico formal do fluxo de captura via API CNJ com o time ampliado está registrado em ATA-AASPCNJ01-001 (07/04/2026).

| Marco de abertura | Ref. |
|---|---|
| Início da Fase 1 (Análise e Arquitetura) | 01/10/2025 |
| Alinhamento técnico — fluxo API CNJ | ATA-AASPCNJ01-001 (07/04/2026) |

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 11/06/2026 | Time de Melhoria Contínua | Termo de abertura consolidado a partir do Registro de Projeto AASP_CNJ v1.0 (08/06/2026). |
