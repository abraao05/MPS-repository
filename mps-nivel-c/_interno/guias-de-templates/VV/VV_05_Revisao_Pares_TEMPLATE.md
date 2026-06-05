# Registro de Revisão por Pares

> **O que é este documento.** Registro de uma revisão por pares realizada sobre um produto de trabalho (código, design, documento de requisitos, etc.). Cada revisão gera um registro separado — ou pode referenciar o Pull Request correspondente, que serve como evidência equivalente.
>
> **Como usar.** Preencha os campos marcados `[preencher]`. O apontamento vazio é inválido — revisão sem achado registrado não é evidência de qualidade, é evidência de revisão pro forma. Se nada foi encontrado, escreva explicitamente "Nenhum apontamento."

---

## 0. Identificação

| Campo | Valor |
|---|---|
| ID / referência | `[preencher — ex.: REV-PROJ-001 ou link do Pull Request]` |
| Projeto | `[preencher]` |
| Item revisado | `[preencher — ex.: módulo de autenticação / história DA-35 / seção 3 do doc de requisitos]` |
| Tipo de revisão | `[preencher — revisão de código / revisão de design / revisão de documento]` |
| Data | `[preencher]` |

---

## 1. Participantes

| Papel | Nome / identificação |
|---|---|
| Autor | `[preencher]` |
| Revisor(es) | `[preencher]` |

---

## 2. Itens revisados

> Liste os arquivos, módulos ou seções examinados. Ser específico aqui é o que torna a revisão rastreável.

`[preencher — ex.: src/modules/auth/login.service.ts, src/modules/auth/auth.guard.ts]`

---

## 3. Apontamentos

> **Regra:** todo apontamento tem severidade, tratamento e situação. Uma revisão sem apontamentos é válida — desde que explícita ("Nenhum apontamento").

| # | Apontamento | Severidade | Tratamento | Situação |
|---|---|---|---|---|
| 1 | `[preencher]` | `[alta / média / baixa]` | `[preencher — o que foi ou será feito]` | `[aberto / resolvido]` |

---

## 4. Resultado

| Campo | Valor |
|---|---|
| Resultado | `[preencher — Aprovado / Aprovado com ressalvas / Reprovado]` |
| Decisão de merge / avanço | `[preencher — aprovado para merge / aguarda correções / bloqueado]` |
| Data da decisão | `[preencher]` |
| Responsável pela decisão | `[preencher]` |

> **Aprovado com ressalvas** = pode avançar, mas os apontamentos abertos devem ser tratados antes da entrega. **Reprovado** = retorna ao autor para retrabalho antes de nova revisão.
