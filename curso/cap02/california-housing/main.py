from src.eda import estadisticas, info, ocean_proximity, resumen_general, valores_nulos
from src.load import load_data


def main():
    df = load_data()
    print(df.head())

    print("\n Resumen general:")
    resumen_general(df)

    print("\n Valores nulos:")
    valores_nulos(df)

    print("\n Info:")
    info(df)

    print("\n Ocean proximity:")
    ocean_proximity(df)

    print("\n Estadísticas:")
    estadisticas(df)


if __name__ == "__main__":
    main()
