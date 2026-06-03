# Plano de Verificação e Validação — [NOME DO PROJETO]

> **TEMPLATE (TPL-VV-001).** Modelo a ser preenchido por projeto. Substitua os campos `[ ]`.

| Campo | Valor |
|---|---|
| **Documento** | [CÓDIGO — ex.: VV-PROJ-XXX] |
| **Projeto** | [Nome] |
| **Versão** | [versão] |
| **Data** | [dd/mm/aaaa] |

---

## 1. Itens a verificar e validar (VV 1)

*[Liste os produtos de trabalho que serão verificados/validados e o método de cada um.]*

| Item | Método (teste / revisão por pares / validação cliente) |
|---|---|
| [código do módulo X] | [code review + testes] |
| [requisitos] | [validação com cliente] |

## 2. Métodos e critérios (VV 3)

*[Descreva os tipos de teste aplicados, os critérios de aceite/aprovação e os ambientes.]*

- **Testes do desenvolvedor:** [critérios de aceite]
- **Testes do QA:** [tipos: funcional, integração, etc.]
- **Ferramentas:** [Azure Test Plans / Jira / Xray]
- **Ambientes:** [homologação/staging]

## 3. Revisão por pares (VV 2)

*[Como o code review é conduzido neste projeto — via PR, critérios, quem revisa.]*

## 4. Execução e registro (VV 4)

*[Onde os casos de teste e resultados são registrados; como defeitos são tratados.]*

| Ciclo/sprint | Casos executados | Defeitos encontrados | Situação |
|---|---|---|---|
| [...] | [...] | [...] | [...] |

## 5. Análise e comunicação dos resultados (VV 5)

*[Como os resultados são analisados e comunicados; quais indicadores alimentam a Medição.]*

## 6. Cenários de teste (Gherkin) e evidências

*[Registre os cenários de teste no formato Gherkin (happy path e sad path) e as evidências dos testes executados. Estes cenários servem para regressão e futura automação.]*

```gherkin
# Exemplo
Funcionalidade: [nome]
  Cenário: [happy path - descrição]
    Dado [contexto]
    Quando [ação]
    Então [resultado esperado]

  Cenário: [sad path - descrição]
    Dado [contexto]
    Quando [ação inválida]
    Então [tratamento esperado]
```

| Cenário | Tipo (happy/sad) | Evidência | Situação |
|---|---|---|---|
| [...] | [...] | [print/vídeo/log] | [aprovado] |

---

## Controle de atualizações

| Versão | Data | Autor | Descrição da mudança |
|---|---|---|---|
| [v] | [data] | [autor] | [o que mudou] |
