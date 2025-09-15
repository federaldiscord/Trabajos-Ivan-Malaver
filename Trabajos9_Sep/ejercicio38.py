import pandas as pd
import matplotlib.pyplot as plt


def cargar_csv(ruta):
    try:
        df = pd.read_csv(ruta)
        print(f"Archivo '{ruta}' cargado correctamente.\n")
        return df
    except Exception as e:
        print(f"Error al cargar archivo: {e}")
        return None


def mostrar_estadisticas(df):
    print("=== ESTADÍSTICAS BÁSICAS ===")
    print("Filas:", df.shape[0])
    print("Columnas:", df.shape[1])
    print("\nColumnas disponibles:", list(df.columns))

    print("\nPrimeras filas:")
    print(df.head())

    print("\nResumen estadístico:")
    print(df.describe(include="all"))


def graficar_columna(df, columna, tipo="histograma"):
    if columna not in df.columns:
        print(f"Columna '{columna}' no encontrada.")
        return

    plt.figure(figsize=(7, 4))
    if tipo == "histograma":
        df[columna].dropna().hist(bins=10, color="skyblue", edgecolor="black")
        plt.title(f"Histograma de {columna}")
    elif tipo == "barras":
        df[columna].value_counts().plot(kind="bar", color="lightgreen")
        plt.title(f"Frecuencia de {columna}")
    else:
        print("Tipo de gráfico no soportado")
        return

    plt.xlabel(columna)
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    archivo = input("Ingrese ruta del archivo CSV: ")
    df = cargar_csv(archivo)

    if df is not None:
        mostrar_estadisticas(df)

        while True:
            print("\n=== OPCIONES DE GRÁFICOS ===")
            print("1. Histograma de una columna")
            print("2. Barras de una columna categórica")
            print("0. Salir")
            op = input("Seleccione opción: ")

            if op == "1":
                col = input("Columna numérica: ")
                graficar_columna(df, col, "histograma")
            elif op == "2":
                col = input("Columna categórica: ")
                graficar_columna(df, col, "barras")
            elif op == "0":
                break
            else:
                print("Opción inválida.")