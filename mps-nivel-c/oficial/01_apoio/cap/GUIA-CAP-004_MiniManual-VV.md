# Mini-manual — Verificação e Validação

| Campo | Valor |
|---|---|
| **Documento** | GUIA-CAP-004 — Mini-manual VV |
| **Versão** | 1.2 |
| **Data** | 15/02/2026 |

---


**O que é.** O processo que garante que o produto foi construído certo (verificação) e faz o que deveria fazer (validação). Atua nas sprints, em homologação e na entrega final.

**O que ele garante.** Que (1) há um plano de V&V definindo o que será verificado/validado, os critérios e os métodos; (2) a verificação por pares é executada e registrada; (3) os testes são realizados com base nos critérios de aceite; (4) as evidências ficam registradas; (5) os resultados são analisados e comunicados.

**Por que fazer.** Sem critérios explícitos de aceite antes do teste, o que conta como "passou"? A verificação por pares captura problemas antes do teste — mais barata e mais rápida. O registro das evidências é o que transforma "testamos" em "sabemos que testamos e temos prova".

**Como usar no dia a dia.**
1. Defina o Plano de V&V no início do projeto: o que será testado, como e com qual critério (TPL-VV-001).
2. Antes de cada sprint, confirme os critérios de aceite das histórias com a equipe.
3. Execute teste exploratório em homologação e registre resultados com evidências (prints, logs, vídeo).
4. Formalize os cenários em Gherkin (Dado/Quando/Então) para o caminho feliz e os alternativos relevantes.
5. Conduza revisão por pares para produtos de trabalho relevantes (código, documentos críticos) usando TPL-VV-002.
6. Analise e comunique os resultados ao final de cada sprint/ciclo.

**Erro comum a evitar.** Registrar apenas que "os testes passaram" sem evidência concreta. Evidência é print, log, vídeo — algo ligado ao critério de aceite. Revisão por pares também não é code review silencioso: exige registro do que foi revisado, quem revisou e o que foi encontrado.

---

## Histórico de revisões

| Versão | Data | Autor | Descrição |
|---|---|---|---|
| 1.0 | 10/03/2025 | Time de Melhoria Contínua | Versão inicial |
| 1.1 | 22/09/2025 | Time de Melhoria Contínua | Inclusão de seção sobre Gherkin após baixo desempenho identificado no REL-CAP-001 |
| 1.2 | 15/02/2026 | Time de Melhoria Contínua | Atualização conforme PRO-VV-001 v1.2 |
