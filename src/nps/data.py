"""Funcoes de carregamento e salvamento de dados para o projeto NPS Preditivo."""
from pathlib import Path

import pandas as pd

# Raiz do projeto resolvida a partir do proprio modulo.
# Caminho: src/nps/data.py -> volta dois niveis = raiz do repo.
RAIZ_PROJETO = Path(__file__).resolve().parents[2]
PASTA_DADOS_BRUTOS = RAIZ_PROJETO / "data" / "raw"
PASTA_DADOS_PROCESSADOS = RAIZ_PROJETO / "data" / "processed"
NOME_DATASET_BRUTO = "desafio_nps_fase_1.csv"
NOME_DATASET_PROCESSADO = "dados_processados.csv"


def carregar_dataset_bruto() -> pd.DataFrame:
    """Carrega o dataset bruto desafio_nps_fase_1.csv como DataFrame.

    Retorna o CSV original sem nenhuma transformacao. E o ponto de entrada
    de todos os notebooks que precisam dos dados brutos, garantindo que
    todos eles partam exatamente do mesmo arquivo.
    """
    caminho = PASTA_DADOS_BRUTOS / NOME_DATASET_BRUTO
    return pd.read_csv(caminho)


def salvar_dataset_processado(
    dados: pd.DataFrame,
    nome_arquivo: str = NOME_DATASET_PROCESSADO,
) -> Path:
    """Salva o DataFrame processado em data/processed/ como CSV.

    O formato CSV foi escolhido por ser legivel em qualquer editor de
    texto, mesmo perdendo os tipos categoricos. A funcao
    `carregar_dataset_processado` reconstroi esses tipos na leitura.
    """
    PASTA_DADOS_PROCESSADOS.mkdir(parents=True, exist_ok=True)
    caminho = PASTA_DADOS_PROCESSADOS / nome_arquivo
    # float_format='%.17g' preserva precisao bit-exata de float64 no round-trip,
    # evitando que valores como log1p(x) percam digitos no salvamento e recarga.
    dados.to_csv(caminho, index=False, float_format="%.17g")
    return caminho


def carregar_dataset_processado(
    nome_arquivo: str = NOME_DATASET_PROCESSADO,
) -> pd.DataFrame:
    """Carrega o dataset processado e reconstroi os tipos categoricos perdidos no CSV.

    Como CSV nao preserva o tipo Categorical, a funcao reaplica o tipo
    correto nas colunas conhecidas:
    - `categoria_nps` vira Categorical ordenada (detrator < neutro < promotor)
    - `customer_region` vira Categorical nao-ordenada
    """
    # Importacao local para evitar dependencia circular entre data.py e features.py.
    from .features import CATEGORIAS_NPS_ORDEM

    caminho = PASTA_DADOS_PROCESSADOS / nome_arquivo
    dados = pd.read_csv(caminho)

    if "categoria_nps" in dados.columns:
        dados["categoria_nps"] = pd.Categorical(
            dados["categoria_nps"],
            categories=list(CATEGORIAS_NPS_ORDEM),
            ordered=True,
        )
    if "customer_region" in dados.columns:
        dados["customer_region"] = dados["customer_region"].astype("category")

    return dados
