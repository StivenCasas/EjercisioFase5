# Datos del estudiante
print('\nEstudiante: Brayan Stiven Casas Cardenas \nGrupo: 213022_807 \nPrograma:Ingenieria en Sistemas \nCodigo fuente: autoria propia')
# SISTEMA DE AUDITORÍA DE INVENTARIO

# Matriz de artículos
# [Código, Nombre, Stock Actual, Stock Mínimo]

inventario = []

# FUNCIÓN PARA CALCULAR REABASTECIMIENTO

def calcular_pedido(stock_actual, stock_minimo):
    """
    Calcula la cantidad exacta que debe pedirse.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0
    

# REGISTRO DE ARTÍCULOS

cantidad_articulos = int(
    input("¿Cuántos artículos desea registrar?: ")
)

for i in range(cantidad_articulos):

    print(f"\n--- Registro del artículo #{i + 1} ---")

    codigo = int(input("Ingrese el código: "))
    nombre = input("Ingrese el nombre del artículo: ")
    stock_actual = int(input("Ingrese el stock actual: "))
    stock_minimo = int(input("Ingrese el stock mínimo requerido: "))

    inventario.append([
        codigo,
        nombre,
        stock_actual,
        stock_minimo
    ])

#REPORTE DE PEDIDOS

print("\n========================================")
print("   REPORTE DE REABASTECIMIENTO")
print("========================================")

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(
        stock_actual,
        stock_minimo)
    print(f"\nArtículo: {nombre}")
    print(f"Código: {codigo}")
    print(f"Stock actual: {stock_actual}")
    print(f"Stock mínimo: {stock_minimo}")
    print(f"Cantidad a pedir: {cantidad_pedir}")

print("\nAuditoría finalizada.")