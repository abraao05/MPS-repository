# CLAUDE.md — Instruções para o Claude Code

Este arquivo define **como trabalhar neste repositório**. São regras de comportamento — siga-as em toda sessão. (Para entender *o que* é o projeto, veja o README.md.)

---

## Contexto do repositório

Repositório dos ativos de processo da **Timeware** para a avaliação **MPS-SW Nível C (MR-MPS-SW:2024)**. Contém a camada de definição dos 12 processos (políticas, processos, estratégias, planos, guias, templates) e, futuramente, as evidências de projetos.

- **Idioma:** português brasileiro. Datas em `dd/mm/aaaa`, moeda em `R$`.
- **Avaliadora:** ASR Consultoria.

## Regras inegociáveis

1. **Nunca infira informação.** Se faltar um dado, deixe um placeholder explícito apenas no que falta e avise no chat — nunca preencha com suposição. 

2. **Nunca deixe recados ou comentários para o usuário dentro dos documentos.** Nada de "a confirmar", "ver com fulano", "TODO", "[verificar]" no corpo dos arquivos. Qualquer alerta, dúvida ou observação vai **no chat**, não no documento. O documento entregue fica limpo.
   - **Exceção:** os templates (`TPL-*`) têm campos a preencher (`[ ]`, `<dd/mm/aaaa>`) e instruções em itálico — isso é intencional e deve ser mantido.

3. **Datas e históricos retroativos são intencionais.** Nunca conteste, "corrija" ou alerte sobre datas no passado. Elas refletem a linha do tempo de implantação dos processos. O histórico de versões fica **dentro de cada documento** (não depende do controle de versão da ferramenta).

4. **Autores no histórico de revisões — regra por tipo de documento:**
   - **Documentos de processo organizacional** (POL, PRO, EST, GUIA, TPL): use `"Time de Melhoria Contínua"` como autor.
   - **Registros de projeto** (TAP, PLA, REQ, ATA, PCP, ITP, VV, RASTR, TAE, RAC, GQA, MED, GDE, GCO, LI, CR, ADAP e similares): use o **nome real** da pessoa que criou ou atualizou o documento. Quem fez faz a entrada — GP assina o que é de gestão, time técnico assina o que é técnico.
   - A assinatura do CEO (Tiago Barbosa Nascimento, Founder e CEO) na Política Organizacional (POL-ORG-001) é mantida, pois evidencia patrocínio da alta direção.
   - Os registros de capacitação (`REG-CAP-*`) e a matriz de papéis (`MAPA-ORG-001`) usam nomes reais — exigência do modelo para evidenciar competência.

## Convenção de nomenclatura e versionamento

- Formato: **`TIPO-PROCESSO-NÚMERO`** (ex.: PRO-GPR-001, TPL-VV-001).
- Tipos: `POL`, `CONV`, `PRO`, `EST`, `PLA`, `TPL`, `GUIA`, `MAPA`, `DIAG`.
- Processo: sigla MPS (GPR, REQ, GPC, VV...) ou `ORG` (organizacional).
- **Versão:** `MAIOR.MENOR`, sem data no nome do arquivo.
- Detalhes completos em `CONV-ORG-001`.

### Ao editar um documento
  - **Registros de projeto** (`oficial/04_registros/`): autor = **nome real** da pessoa que criou ou atualizou o documento — GP assina o que é de gestão (TAP, PLA, RAC, CR, ADAP), time técnico assina o que é técnico (PCP, ITP, RASTR), auditor de GQA independente assina o GQA. A **data reflete o momento real do artefato na linha do tempo do projeto** (datas retroativas são intencionais — regra 3), não a data de consolidação.
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

---

## Planilha de indicadores ASR (auditoria MPS-SW)

### Arquivos envolvidos

| Arquivo | Descrição |
|---|---|
| `_interno/_fill_planilha.py` | Script Python que gera a planilha preenchida |
| `_interno/PlanilhaIndicadores_SW_2024_NivelC_PREENCHIDA.xlsx` | Saída gerada — entregue à ASR |
| `_interno/MAPADRIVE_IndicedeLinks.csv` (upload) | Índice de links do Google Drive (exportado antes de rodar) |
| Template ASR `.xlsx` (upload) | Template original fornecido pela ASR |

### Como gerar/atualizar a planilha

1. Atualizar o CSV de links (`MAPADRIVE_IndicedeLinks.csv`) exportando o índice atual do Drive.
2. Ajustar os dicionários de projeto no script (`PROF`, `GAS`, `FRU`, `AASP`) se novos documentos foram adicionados.
3. Rodar: `python mps-nivel-c/_interno/_fill_planilha.py`
4. A saída é `PlanilhaIndicadores_SW_2024_NivelC_PREENCHIDA.xlsx`.

### Estrutura da planilha (como a ASR espera)

Cada aba corresponde a um dos 12 processos MPS (GPR, REQ, PCP, ITP, VV, AQU, GCO, MED, GDE, CAP, GPC, OSW) + abas de capacidade (CP_Projeto, CP_Organizacional).

Dentro de cada bloco de indicador (ex: GPR 1, GPR 2+...):
- **Col A das linhas em branco** → nome do documento que evidencia aquele indicador (uma linha por tipo de doc)
- **Cols C/D/E/F** (projetos) ou **col C** (ORG) da mesma linha → `x` com hyperlink para o Drive
- **Linha `(T,L,P,N,NA)`** → autoavaliação: `T` (totalmente implementado) ou `NA` (não aplicável)
- **Col B** e coluna **Final** → intocadas (o auditor da ASR preenche)

### Projetos e colunas

| Coluna | Projeto |
|---|---|
| C | Projeto 1 (PROFARMA / Rede D1000 — Cadastro de Clientes) |
| D | Projeto 2 (GASMIG — Governança de APIs, fases 1 e 2) |
| E | Projeto 3 (FRUKI — Super App Força de Vendas, fases 1 e 2) |
| F | Projeto 4 (AASP_CNJ — Integração EPROC/ESAJ/CNJ) |
| G | Final (auditor ASR — não preencher) |

### AQU = Não Aplicável

Nenhum dos 4 projetos teve subcontratação/aquisição de desenvolvimento externo (equipe própria Timeware). Todos os indicadores AQU recebem `NA`. O PRO-AQU-001 é referenciado como processo organizacional definido, mesmo sem instâncias de uso.

### Atualizando para novos projetos ou documentos

Para adicionar um 5º projeto:
1. Criar novo dicionário de roles (ex: `NOVO = {'TAP':['TAP-NOVOPROJ01-001'], ...}`)
2. Adicionar ao `PROJECTS` e ao `PCOL` com a coluna correta
3. Adicionar os registros de projeto (GCO, MED, GDE, GQA, etc.) às listas `*_REG`

Para adicionar um documento não presente no CSV:
```python
LINKS.setdefault('CODIGO-DO-DOC', {})['docx'] = ('CODIGO-DO-DOC', 'https://drive.google.com/...')
```
