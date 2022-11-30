def price(mes1, mes2, mes3):
    """"Esta función calcula el precio
    Parametros:
    Mes1, Mes2, Mes3: Son variables tipo float
    Salida:
    Precio: variable tipo float
    """
    precio = float(mes1 + mes2 + mes3) * 0.0615
    return precio

def gas2price(num):
    """"Esta funcion convierte una lista de consumos de gas de diferentes
    clientes durante tres meses en otra lista de precios por cobrar
    Parametros:
    - l_clientes : lista con un numero indeterminado de tuplas con 3 elementos
    Salida:
    l_precio : lista de precio de cada cliente en los tres meses
    """
    num = tuple(num)
    for m_cliente in num:
        precio = m_cliente.append(price(mes1, mes2, mes3))
        l_precio = list(precio)

    return l_precio





