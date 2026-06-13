# Plano e Registro de Verificação e Validação (V&V)

> **Modelo de preenchimento** com base no Trainer Connect (diagnóstico: suíte de testes ampla + revisões independentes consistentes; lacuna era o procedimento de revisão por pares *documentado*). Importante: a revisão por pares na Timeware é feita por **humano** no pull request, antes do merge — esse é o mecanismo padrão que satisfaz "revisão por pares".

---

## 0. Identificação

| Campo | Valor |
|---|---|
| Projeto | Trainer Connect |
| Data | 2026-06-02 |
| Responsável | *(exemplo: dev/revisor)* |

---

## 1. Produtos de trabalho selecionados para V&V

| Produto de trabalho | Verificar | Validar? | Por quê |
|---|---|---|---|
| Módulo de execução de treino | Testes + revisão por pares | Sim | É o fluxo central do aluno |
| Design da tela de montagem | Revisão por pares | Não | Verificação de conformidade ao design basta |

---

## 2. Procedimentos e material de apoio para revisão por pares

- **Procedimento:** toda alteração entra por pull request; um revisor humano (par) analisa antes do merge, registrando achados classificados por severidade (crítico / a corrigir / informativo). O merge só ocorre após o aceite do revisor.
- **Material de apoio:** checklist de revisão (cobertura de requisitos, contratos de interface, segurança).

---

## 3. Métodos, procedimentos, critérios e ambientes

| Atividade | Método | Critério de aprovação | Ambiente |
|---|---|---|---|
| Verificação | Suíte de testes automatizados + revisão por pares no PR | Testes passando + PR aprovado por revisor humano | Build/CI |
| Validação | Aceite do usuário real (trainer) | Fluxos executados com sucesso em produção | Produção |

---

## 4. Execução de V&V e tratamento de problemas

| Atividade | Resultado | Problema | Tratamento | Situação |
|---|---|---|---|---|
| Suíte de testes da fase Execução | Passou após correções | 11 regressões detectadas | Corrigidas e re-testadas | Resolvido |
| Revisão por pares do módulo | Achados de severidade média | — | Revisão → correção registrada | Resolvido |
| Validação com usuário | Aprovado | — | Sign-off do trainer | Resolvido |

---

## 5. Análise, registro e comunicação dos resultados

- **Resultados:** módulo verificado (testes + revisão) e validado (aceite do usuário em produção).
- **Análise:** as regressões concentraram-se na integração entre treino e execução; reforçou a prática de atualizar tabelas dependentes juntas.
- **Comunicado a:** equipe (registros de verificação) e patrocinador/usuário (aceite).
