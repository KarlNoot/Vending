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
        2.- Comprar producto
        3.- Exit
        """)
    return int(input())

def ver_productos():
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto.nombre} - ${producto.precio} - Stock: {producto.stock}")

def comprar_producto():
    print("Productos disponibles:")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto.nombre} - ${producto.precio}")
    
    try:
        seleccion = int(input("\nSeleccione el número del producto que desea comprar: "))
        
        if 1 <= seleccion <= len(productos):
            producto_elegido = productos[seleccion - 1]
            
            if producto_elegido.stock > 0:
                print(f"\nProducto: {producto_elegido.nombre}")
                print(f"Precio: ${producto_elegido.precio}")
                
                pago = float(input("Ingrese el monto a pagar: $"))
                
                if pago >= producto_elegido.precio:
                    cambio = pago - producto_elegido.precio
                    producto_elegido.stock -= 1
                    print(f"\n¡Compra exitosa!")
                    print(f"Su cambio: ${cambio}")
                    print(f"¡Disfrute su {producto_elegido.nombre}!")
                else:
                    print(f"Monto insuficiente. Faltan ${producto_elegido.precio - pago}")
            else:
                print("Producto agotado")
        else:
            print("Opción no válida")
    except ValueError:
        print("Por favor, ingrese un número válido")

print("Desea ver los productos? (si/no)")
respuesta = input()

if respuesta == "si":
    opcion = ver_menu()
    if opcion == 1:
        ver_productos()
    elif opcion == 2:
        comprar_producto()
    elif opcion == 3:
        print("Has salido")
elif respuesta == "no":
    print("Has salido")
else:
    print("Opción no válida")