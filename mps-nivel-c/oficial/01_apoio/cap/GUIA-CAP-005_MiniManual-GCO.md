# Mini-manual — Gerência de Configuração

| Campo | Valor |
|---|---|
| **Documento** | GUIA-CAP-005 — Mini-manual GCO |
| **Versão** | 1.2 |
| **Data** | 15/02/2026 |

---


**O que é.** O processo que mantém a integridade dos produtos de trabalho (código, documentos, migrações) e os disponibiliza a todos os envolvidos. Responde "qual é a versão correta de cada coisa, o que mudou, e quando?".

**O que ele garante.** Que (1) os itens de configuração estão identificados com ID único, tipo, descrição, situação e relações; (2) há um sistema de controle de versão e de mudanças; (3) baselines marcam pontos congelados (versões entregues); (4) o histórico de modificações é mantido e usado; e (5) auditorias verificam que tudo isso está íntegro.

**Por que fazer.** Sem gerência de configuração, ninguém sabe qual é a versão verdadeira, mudanças se perdem ou se sobrepõem, e não dá para reproduzir o que foi entregue. As baselines permitem voltar a um ponto conhecido; as auditorias pegam itens fora de controle (ex.: um entregável sem baseline marcada).

**Como usar no dia a dia.**
1. Identifique os itens de configuração com todos os campos obrigatórios (seção 1).
2. Use o sistema de versionamento e o fluxo de controle de mudanças (seção 2).
3. Marque baselines a cada entrega relevante (seção 3).
4. Mantenha o histórico de modificações e use-o (seção 4).
5. Faça auditorias periódicas de configuração — elas verificam integridade de baselines, mudanças e do sistema (seção 5).

**Erro comum a evitar.** Confiar que "o Git resolve tudo". O versionamento é a base, mas o processo pede um registro de IC com situação e relações, baselines explícitas e auditorias — itens que o histórico de commits sozinho não entrega de forma consolidada.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 10/03/2025 | Time de Melhoria Contínua | Versão inicial |
| 1.1 | 22/09/2025 | Time de Melhoria Contínua | Revisão após baixo desempenho no AVA-CAP-004: clarificação sobre baselines × releases |
| 1.2 | 15/02/2026 | Time de Melhoria Contínua | Revisão da seção de auditoria de configuração |
