"""Funcoes de engenharia de variaveis para o projeto NPS Preditivo."""
from __future__ import annotations

import pandas as pd

# Cortes canonicos da categorizacao do NPS (Reichheld, 2003).
# Detrator: nota 0-6
# Neutro:   nota 7-8
# Promotor: nota 9-10
#
# Como o nps_score do nosso dataset esta em float (passos de 0.1),
# usamos os cortes em formato semi-aberto a esquerda para preservar
# a regra canonica: nota 6.9 ainda e detrator, nota 7.0 vira neutro.
CORTE_DETRATOR_NEUTRO = 7
CORTE_NEUTRO_PROMOTOR = 9
CATEGORIAS_NPS_ORDEM: tuple[str, str, str] = ("detrator", "neutro", "promotor")


def classificar_nps(nota: float) -> str:
    """Classifica uma nota de NPS escalar nos buckets canonicos.

    Util para chamada pontual (uma nota por vez). Para classificar uma
    coluna inteira de DataFrame, prefira `adicionar_categoria_nps`, que
    e vetorizada e mais rapida.

    Parametros
    ----------
    nota : float
        Nota de NPS na escala 0 a 10.

    Retorno
    -------
    str
        Uma das tres categorias: "detrator", "neutro" ou "promotor".
    """
    if nota < CORTE_DETRATOR_NEUTRO:
        return "detrator"
    if nota < CORTE_NEUTRO_PROMOTOR:
        return "neutro"
    return "promotor"


def adicionar_categoria_nps(
    dados: pd.DataFrame,
    coluna_origem: str = "nps_score",
    coluna_destino: str = "categoria_nps",
) -> pd.DataFrame:
    """Adiciona ao DataFrame uma coluna categorica ordenada com o bucket de NPS.

    Implementacao vetorizada via `pd.cut`, preservando a regra canonica
    do NPS (intervalos fechados a esquerda).

    Parametros
    ----------
    dados : pd.DataFrame
        DataFrame contendo a coluna de origem com a nota de NPS.
    coluna_origem : str
        Nome da coluna com a nota numerica. Default: "nps_score".
    coluna_destino : str
        Nome da coluna a ser criada com o bucket categorico. Default: "categoria_nps".

    Retorno
    -------
    pd.DataFrame
        Copia do DataFrame original com a nova coluna categorica ordenada
        (detrator < neutro < promotor).
    """
    resultado = dados.copy()
    resultado[coluna_destino] = pd.cut(
        resultado[coluna_origem],
        bins=[-float("inf"), CORTE_DETRATOR_NEUTRO, CORTE_NEUTRO_PROMOTOR, float("inf")],
        labels=list(CATEGORIAS_NPS_ORDEM),
        right=False,
        ordered=True,
    )
    return resultado
