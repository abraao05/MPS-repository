# CLAUDE.md — Instruções para o Claude Code

Este arquivo define **como trabalhar neste repositório**. São regras de comportamento — siga-as em toda sessão. (Para entender *o que* é o projeto, veja o README.md.)

---

## Contexto do repositório

Repositório dos ativos de processo da **Timeware** para a avaliação **MPS-SW Nível C (MR-MPS-SW:2024)**. Contém a camada de definição dos 11 processos aplicáveis (políticas, processos, estratégias, planos, guias, templates) e, futuramente, as evidências de projetos.

- **Idioma:** português brasileiro. Datas em `dd/mm/aaaa`, moeda em `R$`.
- **Avaliadora:** ASR Consultoria.

## Regras inegociáveis

1. **Nunca invente informação.** Se faltar um dado, deixe um placeholder explícito apenas no que falta e avise no chat — nunca preencha com suposição. Não fabrique números, nomes, datas ou referências.

2. **Nunca deixe recados ou comentários para o usuário dentro dos documentos.** Nada de "a confirmar", "ver com fulano", "TODO", "[verificar]" no corpo dos arquivos. Qualquer alerta, dúvida ou observação vai **no chat**, não no documento. O documento entregue fica limpo.
   - **Exceção:** os templates (`TPL-*`) têm campos a preencher (`[ ]`, `<dd/mm/aaaa>`) e instruções em itálico — isso é intencional e deve ser mantido.

3. **Datas e históricos retroativos são intencionais.** Nunca conteste, "corrija" ou alerte sobre datas no passado. Elas refletem a linha do tempo de implantação dos processos. O histórico de versões fica **dentro de cada documento** (não depende do controle de versão da ferramenta).

4. **Papéis genéricos, sem nomes de pessoas.** Use "Time de Melhoria Contínua", "Gerente de Projeto", "COO", etc. **Exceção:** a assinatura do CEO (Tiago Barbosa Nascimento, Founder e CEO) na Política Organizacional (POL-ORG-001) é mantida, pois evidencia patrocínio da alta direção.

## Convenção de nomenclatura e versionamento

- Formato: **`TIPO-PROCESSO-NÚMERO`** (ex.: PRO-GPR-001, TPL-VV-001).
- Tipos: `POL`, `CONV`, `PRO`, `EST`, `PLA`, `TPL`, `GUIA`, `MAPA`, `DIAG`.
- Processo: sigla MPS (GPR, REQ, GPC, VV...) ou `ORG` (organizacional).
- **Versão:** `MAIOR.MENOR`, sem data no nome do arquivo.
- Detalhes completos em `CONV-ORG-001`.

### Ao editar um documento
- Toda alteração relevante **incrementa a versão** (menor para ajustes, maior para mudanças estruturais).
- **Adicione uma linha no histórico de revisões** ao final do documento, com versão, data, autor ("Time de Melhoria Contínua") e descrição da mudança.
- Atualize o campo **Data** do cabeçalho para a data da versão atual.
- Se o documento for referenciado no `MAPA-ORG-001`, atualize a versão lá também.

## Estrutura de pastas

```
oficial/                  ← evidência MPS (auditada pela ASR)
  00_governanca/          ← política, processo-padrão, GQA, riscos, OSW, diagrama
  01_apoio/               ← MED, CAP, GDE, GCO, AQU
  02_processos_projeto/   ← GPR, REQ, PCP, ITP, VV
  03_templates/           ← TPL-*
  04_capacidade/          ← mapa de capacidade
_interno/                 ← apoio/gestão (NÃO vai para a avaliação)
```

- **[OFICIAL]** = evidência MPS → pasta `oficial/`.
- **[INTERNO]** = apoio/gestão → pasta `_interno/`.
- Ao criar um documento novo, classifique-o ([OFICIAL]/[INTERNO]) e coloque na pasta correta.

## Formato dos documentos

- Documentos em **Markdown**. Só converter para Word quando explicitamente pedido (a ASR audita em Word, mas a edição é feita em `.md`).
- Cada documento começa com uma tabela de metadados (Documento, Versão, Data, etc.) e termina com o histórico de revisões.
- Produção organizacional → projeto: a biblioteca de processos é estável; as evidências de projeto derivam dela e referenciam o processo de origem.

## Estilo de interação (preferências do usuário)

- Calibre o tamanho da resposta pela pergunta: simples = curta; decisão complexa = pode estender.
- Para decisões com trade-off, mostre os lados e depois a recomendação. Separe **fato → interpretação → recomendação**.
- Aponte problemas com franqueza, sem suavizar — mas respeite a decisão final do usuário e não repita o alerta depois de decidida.
- Sem elogio gratuito, preâmbulo desnecessário ou disclaimers repetidos.
- Se faltar contexto, **pergunte antes de chutar**.

## Antes de commitar

- Mostre/permita revisão do `git diff` antes de commits em massa.
- Não commite alterações em lote sem o usuário revisar, especialmente em datas, versões e numeração.
