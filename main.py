"""Máquina expendedora - Sistema de venta de productos con colores en consola."""

from entidades.producto import Producto
from enums.tipo_producto import TipoProducto
from colorama import init, Fore
init(autoreset=True)  # Inicializa colorama y restablece colores automáticamente

# -------------------------------
# Datos iniciales de productos
# -------------------------------
ob1 = Producto("Cocacola", 25, 100, TipoProducto.BEBIDA)
ob2 = Producto("Pan integral", 30, 500, TipoProducto.PAN)
ob3 = Producto("Ostia Coronado", 15, 666, TipoProducto.SNACK)
ob4 = Producto("Tostitos", 24, 60, TipoProducto.OTRO)

productos = [ob1, ob2, ob3, ob4]


def ver_productos():
    """Muestra la lista de productos con su precio y stock."""
    print("\n--- Lista de productos ---")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto.nombre} - ${producto.precio_unitario} - Stock: {producto.cantidad_existencias}")


def comprar_producto():
    """Realiza el proceso de compra: selección, pago y actualización."""
    # Mostrar menú de productos
    print("\n--- Productos disponibles ---")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto.nombre} - ${producto.precio_unitario}")

    try:
        seleccion = int(input("\nSeleccione el número del producto que desea comprar: "))
        if 1 <= seleccion <= len(productos):
            producto_elegido = productos[seleccion - 1]

            # Mostrar información del producto
            print(f"\nProducto: {producto_elegido.nombre}")
            print(f"Precio: ${producto_elegido.precio_unitario}")
            pago = float(input("Ingrese el monto a pagar: $"))

            # Procesar la compra usando el método de la clase
            exito, mensaje, cambio = producto_elegido.comprar_producto(pago)

            if exito:
                # Éxito: mensaje en verde
                print(Fore.GREEN + mensaje)
                # Si hay cambio, mostrar también en verde
                if cambio > 0:
                    print(Fore.GREEN + f"Su cambio es de ${cambio}")
            else:
                # Fracaso (insuficiente o agotado): mensaje en rojo
                print(Fore.RED + mensaje)
        else:
            print(Fore.RED + "Opción no válida")
    except ValueError:
        print(Fore.RED + "Por favor, ingrese un número válido")


def menu():
    """Menú principal de la máquina expendedora."""
    while True:
        print("\n" + "=" * 30)
        print("        MÁQUINA EXPENDEDORA")
        print("=" * 30)
        print("1. Ver productos")
        print("2. Comprar producto")
        print("3. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                ver_productos()
            elif opcion == 2:
                comprar_producto()
            elif opcion == 3:
                print(Fore.GREEN + "¡Hasta luego!")
                break
            else:
                print(Fore.RED + "Opción no válida, intente de nuevo.")
        except ValueError:
            print(Fore.RED + "Por favor, ingrese un número válido.")


# -------------------------------
# Punto de entrada del programa
# -------------------------------
if __name__ == "__main__":
    menu()