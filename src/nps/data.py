"""Funcoes de carregamento de dados para o projeto NPS Preditivo."""
from pathlib import Path

import pandas as pd

# Raiz do projeto resolvida a partir do proprio modulo.
# Caminho: src/nps/data.py -> volta dois niveis = raiz do repo.
RAIZ_PROJETO = Path(__file__).resolve().parents[2]
PASTA_DADOS_BRUTOS = RAIZ_PROJETO / "data" / "raw"
PASTA_DADOS_PROCESSADOS = RAIZ_PROJETO / "data" / "processed"
NOME_DATASET_BRUTO = "desafio_nps_fase_1.csv"


def carregar_dataset_bruto() -> pd.DataFrame:
    """Carrega o dataset bruto desafio_nps_fase_1.csv como DataFrame.

    Retorna o CSV original sem nenhuma transformacao. E o ponto de entrada
    de todos os notebooks que precisam dos dados brutos, garantindo que
    todos eles partam exatamente do mesmo arquivo.
    """
    caminho = PASTA_DADOS_BRUTOS / NOME_DATASET_BRUTO
    return pd.read_csv(caminho)
