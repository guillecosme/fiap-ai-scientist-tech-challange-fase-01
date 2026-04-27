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

1. Business Understanding — entendimento da dor de negócio
2. Data Understanding — perfil estatístico e qualidade dos dados
3. Data Preparation — limpeza e feature engineering
4. EDA — análise exploratória com foco em insights de negócio
5. Modeling — regressão (NPS contínuo) e classificação (promotor/detrator)
6. Evaluation — comparação técnica e recomendação final

Código reutilizável em `src/nps/`. Modelos serializados em `models/`. Figuras e slides em `reports/`.

## Como reproduzir

Pré-requisito: [uv](https://docs.astral.sh/uv/) instalado.

```bash
# clonar o repo e entrar
git clone <url-do-repo>
cd nps-preditivo

# instalar dependências e criar virtualenv
uv sync

# subir o jupyter
uv run jupyter lab
```

Os notebooks devem ser rodados na ordem (01 → 07). Datasets intermediários ficam em `data/interim/` e `data/processed/`, gerados pelos próprios notebooks a partir do CSV em `data/raw/`.

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
