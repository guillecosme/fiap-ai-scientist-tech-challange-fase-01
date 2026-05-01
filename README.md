# NPS Preditivo — Tech Challenge Fase 1

Trabalho da Fase 1 do MBA em AI Scientist (FIAP / POSTECH). O objetivo é entender, a partir de dados operacionais de um e-commerce, quais fatores impactam a satisfação do cliente medida pelo NPS, e construir um modelo capaz de antecipar essa nota antes da aplicação da pesquisa.

## Problema

A empresa coleta o NPS apenas depois de encerrada a jornada de compra. Isso impede qualquer ação preventiva sobre clientes propensos a virar detratores. A pergunta central é:

> Quais fatores operacionais (logística, atendimento, perfil do pedido, perfil do cliente) explicam a variação do NPS, e dá pra prever a nota antes da pesquisa?

## Base de dados

O dataset `desafio_nps_fase_1.csv` (em `data/raw/`) tem 2.500 linhas e 19 colunas, cobrindo:

- **Cliente:** id, idade, região, tempo de relacionamento
- **Pedido:** valor, quantidade de itens, desconto, parcelas
- **Logística:** tempo de entrega, atraso, frete, tentativas
- **Atendimento:** contatos, tempo de resolução, reclamações
- **Indicadores internos:** csat interno, recompra em 30 dias
- **Target:** `nps_score` (0 a 10)

Dicionário completo em [`docs/data_dictionary.md`](docs/data_dictionary.md).

## Metodologia

CRISP-DM, dividido em notebooks numerados em `notebooks/`:

| Notebook | Fase | Conteúdo |
|---|---|---|
| `01_business_understanding.ipynb` | Business Understanding | Entendimento da dor, perguntas de pesquisa e critérios de sucesso |
| `02_data_understanding.ipynb` | Data Understanding | Perfil estatístico de cada variável, qualidade dos dados e definição da target |
| `03_data_preparation.ipynb` | Data Preparation | Limpeza, criação da `categoria_nps` e transformações; gera o dataset processado |
| `04_eda.ipynb` | EDA | Exploração visual e estatística, teste das hipóteses de negócio e modelo agregado de panorama |
| `05_modelagem_regressao.ipynb` | Modeling | Regressão linear simples com a variável dominante, com avaliação treino/teste e análise de resíduos |
| `06_modelagem_classificacao.ipynb` | Modeling + Evaluation | Classificação por threshold sobre o NPS predito, escolha do corte operacional e análise dos erros |

A avaliação técnica e a recomendação de negócio estão consolidadas nas conclusões dos notebooks 05 e 06, e serão sintetizadas no storytelling executivo (`reports/slides/`).

Código reutilizável em `src/nps/` (carregamento de dados em `data.py`, engenharia de variáveis em `features.py`). Figuras geradas pelos notebooks ficam em `reports/figures/`.

## Insights

- **Atraso na entrega é a variável dominante.** A logística pesa muito mais do que perfil do cliente, valor do pedido ou indicadores de atendimento na nota final do NPS.
- **Modelo enxuto já entrega valor.** Uma única variável preditora consegue explicar boa parte da variação do NPS e classificar bem detratores vs. não-detratores no conjunto de teste.
- **A operação tem um sinal acionável antes da pesquisa.** Existe um corte simples sobre a previsão do modelo que separa quem provavelmente virará detrator de quem não virará, viabilizando ação preventiva.
- **O modelo enxuto tem limites claros.** Detratores cuja insatisfação não vem de logística (e sim de atendimento ou qualidade percebida) escapam da regra e ficariam visíveis em uma versão multivariada futura, fora do escopo desta fase.

## Recomendações de negócio

- **Alarme operacional baseado em atraso.** Acionar o SAC proativamente nos pedidos com atraso a partir de 1 dia, antes da pesquisa de NPS.
- **Priorização do atendimento pelo NPS predito.** Usar o ranking gerado pelo modelo para distribuir a fila do SAC, atacando primeiro os clientes com maior probabilidade de virar detrator.
- **Painel executivo de NPS projetado.** Acompanhar em tempo real, no nível agregado, o NPS estimado da operação a partir dos dados de atraso, sem precisar esperar a pesquisa para ter leitura do humor da base.

## Como reproduzir

Pré-requisito: [uv](https://docs.astral.sh/uv/) instalado.

```bash
# clonar o repo e entrar
git clone git@github.com:guillecosme/fiap-ai-scientist-tech-challange-fase-01.git
cd fiap-ai-scientist-tech-challange-fase-01

# instalar dependências e criar virtualenv
uv sync

# subir o jupyter
uv run jupyter lab
```

Os notebooks devem ser rodados na ordem (01 → 06). O dataset processado já está versionado em `data/processed/dados_processados.csv` para quem quiser executar a partir do notebook 04 sem rodar a preparação de dados.

## Estrutura

```
.
├── data/
│   ├── raw/          # fonte original, imutável
│   ├── interim/      # transformações intermediárias
│   ├── processed/    # dataset final pronto para modelagem
│   └── external/     # dados externos
├── notebooks/        # um por fase CRISP-DM
├── src/nps/          # código reutilizável
├── tests/            # testes unitários leves
├── models/           # modelos serializados
├── reports/
│   ├── figures/      # imagens exportadas
│   └── slides/       # apresentação executiva
├── references/       # papers e links
└── docs/             # documentação extra
```
