# Lições Aprendidas — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | LI-AASP-GOV-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.0 |
| **Data** | 02/06/2026 |
| **Responsável** | Cezar Hiraki Velazquez (Gerente de Projeto / Tech Lead) |

---

## 1. Objetivo

Registrar as lições aprendidas no projeto, para reaproveitamento em projetos futuros de integração com APIs de terceiros.

## 2. Lições registradas

| # | Lição | Categoria | Recomendação para projetos futuros |
|---|---|---|---|
| L-01 | A validação dos contratos de API antes do desenvolvimento reduz significativamente o retrabalho na camada de integração | Requisitos / Integração | Mapear e validar os endpoints e contratos das APIs externas na fase inicial, antes de iniciar a construção dos serviços |
| L-02 | A estratégia de identificação por prefixo `#ID` no summary elimina a necessidade de estado externo e simplifica a lógica de idempotência | Arquitetura / Design | Preferir mecanismos de identificação naturais e idempotentes que dispensem persistência de estado quando a integração permitir |
| L-03 | Testes em ambiente real desde o início da homologação são essenciais para projetos de integração com APIs de terceiros | Verificação e Validação | Priorizar testes contra os ambientes reais (não mocks) quando o comportamento crítico depende da compatibilidade entre plataformas |

## 3. Reflexo no processo

As lições L-01 e L-03 reforçam decisões de adaptação já adotadas neste projeto (validação antecipada de requisitos e testes em ambiente real, ver ADAP-AASP-GOV-001). A lição L-02 é candidata a referência de design para futuros serviços de sincronização/migração.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Lições aprendidas consolidadas a partir do Registro de Projeto AASP_Automacao-Governanca v2.0 (08/06/2026). |
