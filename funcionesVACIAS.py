from principal import *
from configuracion import *
import random
import math
from extras import *

# lee el archivo y carga en la lista lista_producto todas las palabras
def lectura():
    archivo = open("productos.txt", "r") # abre el archivo productos.txt, es un texto plano sin formato
    productosSinFormato = archivo.readlines() # lee el archivo
    listaDeProductos = []
    for productoCadena in productosSinFormato: # recorre el texto plano por cadena
        cadenaProducto = productoCadena.split(',') # separa la cadena por cada coma: 'Laptop,4650,4854\n'
        productoFormateado = [cadenaProducto[0], int(cadenaProducto[1]), int(cadenaProducto[2])] # armo una lista con los 3 elementos de la cadena original: 'nombre del producto', precioEconomico, precioPremium
        listaDeProductos.append(productoFormateado) # agrego la lista a otra lista con todos los prodcutos
    archivo.close() # cierro el archivo
    return listaDeProductos #retorno la lista de listas de productos

# De la lista de productos elige uno al azar y devuelve una lista de 3 elementos:
# el primero el nombre del producto , el segundo si es economico o premium y el tercero el precio.
def buscar_producto(lista_productos):
    producto = ["Silla de oficina", "(premium)", 4391]
    return producto

#Elige el producto. Debe tener al menos dos productos con un valor similar
def dameProducto(lista_productos, margen):
    # random
    producto = ["Silla de oficina", "(premium)", 4391]
    return producto


#Devuelve True si existe el precio recibido como parametro aparece al menos 3 veces. Debe considerar el Margen.
def esUnPrecioValido(precio, lista_productos, margen):
    return True

# Busca el precio del producto_principal y el precio del producto_candidato, si son iguales o dentro
# del margen, entonces es valido y suma a la canasta el valor del producto. No suma si eligió directamente
#el producto
def procesar(producto_principal, producto_candidato, margen):
    return 0

#Elegimos productos aleatorios, garantizando que al menos 2 tengan el mismo precio.
#De manera aleatoria se debera tomar el valor economico o el valor premium. Agregar al nombre '(economico)' o '(premium)'
#para que sea mostrado en pantalla.
def dameProductosAleatorios(producto, lista_productos, margen):
    # producto = 3 -> smart
    # lista_productos = 3 -> [ 3, 4, 5 ] precios similares según el margen... 
    # smart precio economico 2500 -> margen 1000 => productos con precio economico entre 1500 - 3500 -> productos_seleccionados =[ ... ]
    # for -> p/encontrar el producto
    # random seleccionar premium o economico
    # seleccionas el precio -> buscas precios similares considerando el margen
    # returna lista productos con precios similares
    
    # random = (1, 2)
    # if 1: retorna economico
    # if 2: retorna premium
    
    # for element in lista:
    # [ "nombre", precio econom, precio premium ] => precioElegido = element[ posicion ] 
    # if precioElegido > (precioElegido - margen) AND precioElegido < (precioElegido + margen)
    # 2500
    # 1000
    # 1500 - 3500
    # 2500 -1000 = 1500
    # 2500 +1000 = 3500
        # true -> productos_seleccionados.append(element)
    
    
    productos_seleccionados =   [["Monitor de computadora", "(premium)", 2870],
            ["Silla de oficina", "(economico)", 3174],
            ["Lavadora", "(premium)", 4197],
            ["Refrigerador", "(premium)", 4533],
            ["Laptop", "(economico)", 4650],
            ["Cafetera", "(economico)", 2358]]
    return productos_seleccionados


