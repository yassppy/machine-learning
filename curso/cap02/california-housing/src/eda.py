from typing import cast

import pandas as pd


def resumen_general(df: pd.DataFrame) -> None:
    """
    Muestra un resumen general del DataFrame.
    """
    print("=" * 50)
    print(f"shape: {df.shape}")
    print(f"columns: {df.columns}")
    print("=" * 50)


def valores_nulos(df: pd.DataFrame) -> pd.Series:
    """Retorna la cantidad de valores nulos por columna."""
    nulos = cast(pd.Series, df.isnull().sum())
    nulos = cast(pd.Series, nulos[nulos > 0])

    if len(nulos) == 0:
        print("✅ No hay valores nulos en el DataFrame.")
        return nulos

    print(f"⚠️ {nulos.sum()} valores nulos en {len(nulos)} columnas.")
    return nulos


def info(df: pd.DataFrame) -> None:
    """Muestra información sobre el DataFrame."""
    print("=" * 50)
    print(f"info: {df.info()}")
    print("=" * 50)


def ocean_proximity(df: pd.DataFrame) -> None:
    """Muestra la distribución de la columna ocean_proximity."""
    print("=" * 50)
    print(f"ocean_proximity: {df['ocean_proximity'].value_counts()}")
    print("=" * 50)


def estadisticas(df: pd.DataFrame) -> None:
    """Muestra estadísticas descriptivas del DataFrame."""
    print("=" * 50)
    print(f"estadísticas: {df.describe()}")
    print("=" * 50)
