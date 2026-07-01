# RELATÓRIO DE NÃO-CONFORMIDADES
## Documento: Registro de Análise de Decisão
**Código:** GDE-AASP01-001
**Versão auditada:** 1.2
**Data do documento:** 24/06/2026
**Data da auditoria:** 30/06/2026
**Auditor:** Claude — Auditor MPS.BR Nível C

---

## RESUMO EXECUTIVO

| Categoria | Graves | Moderadas | Leves | Obs |
|---|---|---|---|---|
| Estrutural (EST) | 0 | 0 | 0 | 0 |
| Conteúdo (CNT) | 0 | 0 | 2 | 1 |
| Datas (DT) | 0 | 0 | 0 | 0 |
| Papéis (PAP) | 0 | 0 | 0 | 0 |
| Coerência (CON) | 0 | 1 | 0 | 0 |
| MPS.BR (MPS) | 0 | 0 | 0 | 0 |
| **TOTAL** | **0** | **1** | **2** | **1** |

**Veredicto:** CONFORME

---

## OBSERVAÇÕES POSITIVAS

O GDE-AASP01-001 é um dos documentos melhor estruturados do projeto. As duas decisões (GDE-001 e GDE-002) contêm contexto claro, alternativas avaliadas, critérios com peso explícito, matriz de decisão preenchida, decisão justificada com raciocínio, e impactos documentados. A decisão GDE-002 (Soft Delete) é particularmente bem fundamentada, conectando a escolha técnica ao requisito de rastreabilidade do MPS.BR. O documento serviu corretamente como referência para o PCP e para a ATA-001.

---

## NÃO-CONFORMIDADES DETALHADAS

### NC-GDE-01 — GDE-001 afirma que EF Core tem "suporte limitado ao .NET FW 5.0" — afirmação tecnicamente incorreta
**Severidade:** 🟡 Moderada
**RAP impactado:** GDE — decisão baseada em fatos verificáveis
**Localização:** Seção GDE-001, campo 5 — Decisão
**Problema:** O documento afirma "O Entity Framework Core em suas versões modernas tem suporte limitado ao .NET FW 5.0". Esta afirmação está tecnicamente incorreta: o EF Core 5.x e 6.x têm suporte pleno ao .NET 5.0 (net5.0 é um target framework válido para ambos). A justificativa correta — e documentada na própria matriz de decisão (seção 4) — é a consistência com o padrão do projeto e a performance. A afirmação incorreta pode ser questionada em avaliação.
**Evidência:** > "O Entity Framework Core em suas versões modernas tem suporte limitado ao .NET FW 5.0. Além disso, o banco auxo3 possui schema legado com convenções de nomenclatura que dificultam o mapeamento automático do EF Core."
**Referência normativa:** GDE — decisões devem ser baseadas em critérios verificáveis e tecnicamente corretos.
**Ação corretiva:** Corrigir para: "O EF Core 5.x e 6.x suportam o .NET 5.0 (net5.0), mas introduziriam um segundo padrão de acesso a dados no projeto, divergindo do padrão Dapper estabelecido nos demais módulos do Gerenciador AASP. O Dapper foi mantido por consistência arquitetural e por oferecer performance superior em queries de leitura complexas sobre o schema legado auxo3."

---

### NC-GDE-02 — Apenas 2 decisões registradas — ausência de decisões arquiteturais da Sprint 2 e 3
**Severidade:** 🟢 Leve
**RAP impactado:** GDE — registro completo de decisões significativas
**Localização:** Ausência — nenhuma decisão além de GDE-001 e GDE-002
**Problema:** O documento cobre apenas 2 decisões tomadas no kickoff. O projeto avançou para a Sprint 2 com a decisão de como implementar a integração com ms.temis.vinculos (mecanismo de retry, tratamento de falhas, timeout) e a auditoria de operações. Estas são decisões arquiteturais significativas que deveriam ser registradas no GDE. O ITP-AASP01-001 admite "mecanismo a definir" para a integração — esta decisão, quando tomada, deve ser registrada.
**Evidência:** ITP §4.1: > "Autenticação | Service-to-service (mecanismo a definir; segredos exclusivamente via variáveis de ambiente)"
**Referência normativa:** GDE — todas as decisões arquiteturais significativas devem ser registradas com alternativas avaliadas.
**Ação corretiva:** Registrar as decisões tomadas na Sprint 2 sobre: (a) mecanismo de autenticação service-to-service para ms.temis.vinculos; (b) estratégia de tratamento de falhas na integração (retry, fallback, circuit breaker); (c) modelo de dados da tabela AuditoriaGrupos.

---

### NC-GDE-03 — "Time de Melhoria Contínua" sem identificação nominal
**Severidade:** 🔵 Obs
**RAP impactado:** GCO RAP 2
**Localização:** Histórico de revisões — versão 1.2
**Problema:** Problema sistêmico.
**Evidência:** > "1.2 | 24/06/2026 | Time de Melhoria Contínua | Reconciliação..."
**Referência normativa:** GCO RAP 2.
**Ação corretiva:** Identificar o responsável nominal.
