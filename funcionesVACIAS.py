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
    indiceDeProductoAleatorio = random.randrange(0, len(lista_productos)-1) # Tira un numero random entre 0 y el largo de la lista de productos, representaría el índice del producto
    producto = lista_productos[indiceDeProductoAleatorio] # Guardo el producto en variable. [ 'Silla de oficina', 1111, 2222 ]
    calidadAleatoria = random.randrange(0,2) # Tira un numero random entre 0 y 1, representando 0 para calidad economico, 1 para calidad premium
    if calidadAleatoria == 0: # Si la calidad es economico, guardo en la variable producto una nueva lista con el nombre del producto, la leyenda correspondiente a la calidad "economico", y el precio correspondiente a esa calidad
        producto = [producto[0], "(economico)", producto[1]]
        return producto
    else: # De lo contrario, la lista será conformada por la leyenda "premium" y el precio correspondiente
        producto = [producto[0], "(premium)", producto[2]]
        return producto
        #producto = ["Silla de oficina", "(premium)", 4391]
        

#Devuelve True si existe el precio recibido como parametro y aparece al menos 3 veces. Debe considerar el Margen.
def esUnPrecioValido(precio, lista_productos, margen): # precio = 2500, margen 1000 -> precio - margen: 1500
    contador = 0
    for producto in lista_productos:   
        precioComparar = producto[2]
        # verifica que producto candidato esté dentro del margen del producto principal
        if (abs(precioComparar - precio) <= margen): # toma el valor absoluto de la diferencia entre los precios
            contador = contador + 1
    if contador >= 3:
        return True
    else:
        return False


# Elige el producto. Debe tener al menos dos productos con un valor similar
def dameProducto(lista_productos, margen):
    productoPpal = buscar_producto(lista_productos) #producto = ["Silla de oficina", "(premium)", 4391]
    productoValido = esUnPrecioValido(productoPpal[2], lista_productos, margen)
    if productoValido: # true o false
        return productoPpal #producto = ["Silla de oficina", "(premium)", 4391]

# Busca el precio del producto_principal y el precio del producto_candidato, si son iguales o dentro
# del margen, entonces es valido y suma a la canasta el valor del producto. No suma si eligió directamente
#el producto
def procesar(producto_principal, producto_candidato, margen):
    precioPpal = producto_principal[2]
    precioCandidato = producto_candidato[2]
    
    """ print("precioPpal: ", precioPpal)
    print("precioCandidato: ", precioCandidato)
    print("diferencia: ", abs(precioCandidato-precioPpal)) """
    
    if (abs(precioCandidato - precioPpal) <= margen):
        return 1
    else:
        return 0

# Sin repetidos:
def estaEnLista (producto, lista):
    for element in lista:
        if (element == producto):
            return True
    
#Elegimos productos aleatorios, garantizando que al menos 2 tengan el mismo precio.
#De manera aleatoria se debera tomar el valor economico o el valor premium. Agregar al nombre '(economico)' o '(premium)'
#para que sea mostrado en pantalla.
def dameProductosAleatorios(producto, lista_productos, margen):
    productos_seleccionados = []
    productos_seleccionados.append(producto)
    
    for element in lista_productos:
        productoValido = dameProducto(lista_productos, margen)
        # verifico que no esté en la lista antes de agregarlo
        if not estaEnLista(element[0], productos_seleccionados[0]):
            productos_seleccionados.append(productoValido)
        
        if len(productos_seleccionados) == 6: # 6??
            return productos_seleccionados
