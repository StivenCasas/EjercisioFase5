# Datos del estudiante
print('\nEstudiante: Brayan Stiven Casas Cardenas')
print('Grupo: 213022_807')
print('Programa: Ingenieria en Sistemas')
print('Codigo fuente: autoria propia\n')

# SISTEMA DE AUDITORIA DE INVENTARIO
# Inventario de la tienda ShopTechnology

# [Codigo, Nombre, Stock actual, Stock minimo]

inventario = [
    [101, "Teclado", 25, 45],
    [102, "Mouse", 15, 65],
    [103, "Monitor", 3, 10],
    [104, "Impresora", 5, 10],
    [105, "USB", 7, 25]]

# Funcion para calcular cuanto producto hace falta
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        pedido = stock_minimo - stock_actual
        return pedido
    else:
        return 0

# Reporte final
print("REPORTE DE INVENTARIO")

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]
    cantidad_pedir = calcular_pedido(
        stock_actual,
        stock_minimo)

    print("\nArticulo:", nombre)
    print("Codigo:", codigo)
    print("Stock actual:", stock_actual)
    print("Stock minimo:", stock_minimo)
    print("Cantidad a pedir:", cantidad_pedir)

print("\nProceso terminado.")