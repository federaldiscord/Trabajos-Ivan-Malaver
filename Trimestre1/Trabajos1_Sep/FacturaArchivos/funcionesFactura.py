def calcular_subtotal(precios):
    return sum(precios)

def calcular_cantidad(productos):
    return len(productos)

def calcular_iva(subtotal, iva=0.19):
    return subtotal * iva

def calcular_total(subtotal, iva_total):
    return subtotal + iva_total

def iva_por_producto(precios, iva=0.19):
    return [precio * iva for precio in precios]
