"""Definiremos el Main para implementar los metodos para productos
ingresar precios"""

from entidades.producto import Producto
from enums.tipo_producto import TipoProducto 

print("_______________________")
print("Expender Machine")
print("_______________________")



ob1 = Producto("Cocacola", 25, 100, TipoProducto.BEBIDA)
ob2 = Producto("Pan integral", 30, 500, TipoProducto.PAN)
ob3 = Producto("Ostia Coronado", 15, 666, TipoProducto.SNACK)
ob4 = Producto("Tostitos", 24, 60, TipoProducto.OTRO)

productos = [ob1, ob2, ob3, ob4]


def ver_menu():
    """
    Displays a menu with the available options to manage the list of products.
    
    Args:
        None
    
    Returns:
        int: Number corresponding to the option selected by the user.
    """
    print("""Select your product:
        1.- Ver productos
        2.- Exit
        """)
    return int(input())

def ver_productos():
    print(productos)

print("Desea ver los productos? (si/no)")
respuesta = input()

if respuesta == "si":
    opcion = ver_menu()
    if opcion == 1:
        ver_productos()
    elif opcion == 2:
        print("Has salido")
elif respuesta == "no":
    print("Has salido")
else:
    print("Opción no válida")

def ver_productos():
    print(productos)


