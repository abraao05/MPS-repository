# Mini-manual — Integração do Produto

| Campo | Valor |
|---|---|
| **Documento** | GUIA-CAP-006 — Mini-manual ITP |
| **Versão** | 1.1 |
| **Data** | 22/09/2025 |

---


**O que é.** O processo que monta os componentes do produto numa solução integrada, consistente com o design e os requisitos, e a entrega às partes interessadas.

**O que ele garante.** Que (1) existe uma estratégia de integração com procedimentos, critérios e descrição de interfaces — não se integra "no improviso"; (2) há um ambiente de integração; (3) cada componente é avaliado como pronto antes de entrar; (4) o produto integrado é testado contra requisitos, design e compatibilidade de interfaces; e (5) o produto e seu material de apoio são entregues.

**Por que fazer.** Componentes que funcionam isolados podem quebrar ao se juntar (interfaces incompatíveis, suposições conflitantes). A integração disciplinada pega esses problemas no momento certo, com critérios definidos antes, em vez de descobrir na produção.

**Como usar no dia a dia.**
1. Defina a estratégia de integração cedo (procedimentos, critérios, ordem, interfaces) — seção 1.
2. Garanta um ambiente de integração (build, homologação) — seção 2.
3. Antes de integrar cada componente, confirme sua prontidão — seção 3.
4. Integre seguindo a estratégia e registre — seção 4.
5. Teste o produto integrado e registre os resultados — seção 5.
6. Prepare e entregue produto + material de apoio — seção 6.

**Erro comum a evitar.** Tratar integração como "só dar merge". Sem critérios de prontidão e sem teste do conjunto, a integração vira o ponto onde os bugs se acumulam. E não esquecer o material de apoio: produto entregue sem instrução de uso é entrega incompleta.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 10/03/2025 | Time de Melhoria Contínua | Versão inicial |
| 1.1 | 22/09/2025 | Time de Melhoria Contínua | Inclusão do fluxo detalhado de ambientes Timeware (Dev → QA → Homolog → Stage → Prod) |
