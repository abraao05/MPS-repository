# Lições Aprendidas — AASP_Automacao-Governanca · SensrJiraSync

| Campo | Valor |
|---|---|
| **Documento** | LI-AASPGOV01-001 |
| **Projeto** | AASP_Automacao-Governanca — SensrJiraSync: Serviço de Sincronização de Atividades entre Sensr e Jira |
| **Versão** | 1.0 |
| **Data** | 02/06/2026 |
| **Responsável** | Abraão Oliveira (Gerente de Projeto) |

---

## 1. Objetivo

Registrar as lições aprendidas do projeto e as ações de melhoria associadas, para reaproveitamento em projetos futuros de integração com APIs de terceiros. As lições alimentam o repositório organizacional de medidas (REG-MED-001) e as oportunidades de melhoria de processo (GPC 4).

## 2. Lições aprendidas

| ID | Lição aprendida | Ação de melhoria |
|---|---|---|
| L01 | APIs externas com formatos proprietários (ADF/Atlassian) exigem mais tempo de mapeamento do que APIs REST convencionais | Estimar +30% de esforço para fases de mapeamento de APIs com formatos proprietários (AC-01) |
| L02 | Tratamento de HTML e sanitização de campos devem ser testados desde as primeiras fases, não apenas na homologação | Incluir cenário Gherkin obrigatório para HTML e labels desde o planejamento de V&V (AC-02) |
| L03 | Contratos de API documentados no kickoff evitam surpresas e retrabalho em fases posteriores | Exigir Swagger/OpenAPI dos sistemas externos como entregável do cliente antes do início da Fase 2 |
| L04 | Credenciais por desenvolvedor precisam de validação isolada antes do início do desenvolvimento | Incluir checklist de validação de credenciais por desenvolvedor na ata de kickoff |
| L05 | GitFlow em projetos de 7 semanas pode ser simplificado sem comprometer o controle de versão | Avaliar GitFlow simplificado (apenas `main` e `feature/*`) para projetos com duração inferior a 8 semanas |
| L06 | O ambiente de homologação precisa espelhar exatamente o de produção para testes realistas de integração | Registrar no GCO os parâmetros de configuração de cada ambiente como IC próprio |
| L07 | O modelo de sprints retroativos é válido para rastreabilidade de esforço, mas precisa estar explícito no ADAP para evitar questionamentos na auditoria | Documentar explicitamente a adoção de sprints retroativos como adaptação formal no ADAP desde o início |

## 3. Oportunidades de melhoria de processo

As ações AC-01 e AC-02 foram incorporadas aos ativos organizacionais (PLA-GPR-001 e TPL-VV-001, respectivamente — ver MED-AASPGOV01-001 §6). A oportunidade de antecipar verificações intermediárias de GQA em projetos com mais de 8 semanas (OM-01, GQA-AASPGOV01-001) também foi registrada.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 15/06/2026 | Time de Melhoria Contínua | Lições aprendidas consolidadas a partir do INTAKE-AASPGOV01 (14/06/2026), Bloco 13.1. |
