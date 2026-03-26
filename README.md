Documentacion aportada por Zefirka en 25/03/2026


# Máquina Expendedora - Sistema de Venta

Este proyecto implementa una máquina expendedora interactiva por consola, desarrollada en Python. Permite visualizar productos, realizar compras y gestionar el inventario, con mensajes en color para mejorar la experiencia de usuario.

## Estructura del Proyecto

```
vending/
├── entidades/
│   └── producto.py          # Clase Producto
├── enums/
│   └── tipo_producto.py     # Enumeración TipoProducto
├── main.py                  # Punto de entrada y lógica de interacción
└── README.md
```

## Descripción de Archivos

### `entidades/producto.py`

Define la clase `Producto` que representa un artículo de la máquina expendedora. Sus atributos son:

- `nombre`: nombre del producto (str)
- `precio_unitario`: precio por unidad (float)
- `cantidad_existencias`: unidades disponibles (int)
- `tipo_producto`: categoría del producto (enumeración `TipoProducto`)

La clase incluye el método `comprar_producto(pago: float)`, que procesa una compra:

- Valida si hay stock disponible.
- Verifica que el pago sea suficiente.
- Si la compra es exitosa, reduce el stock y devuelve un mensaje junto con el cambio.
- Retorna una tupla `(exito, mensaje, cambio)` para que la interfaz maneje los colores correspondientes.

### `enums/tipo_producto.py`

Contiene la enumeración `TipoProducto` con las categorías:

- `PAN`
- `BEBIDA`
- `SNACK`
- `OTRO`

### `main.py`

Punto de entrada del programa. Realiza las siguientes funciones:

1. **Inicializa productos** de ejemplo (`Cocacola`, `Pan integral`, `Ostia Coronado`, `Tostitos`) con sus respectivos precios, existencias y tipos.
2. **Define funciones auxiliares**:
   - `ver_productos()`: Muestra la lista de productos con precio y stock.
   - `comprar_producto()`: Controla el flujo de compra (selección, pago, actualización) y muestra mensajes en verde (éxito) o rojo (error) usando `colorama`.
   - `menu()`: Bucle principal que presenta las opciones hasta que el usuario decide salir.
3. **Utiliza `colorama`** para dar color a los mensajes de la consola:
   - `Fore.GREEN` para compras exitosas y mensajes informativos.
   - `Fore.RED` para errores (producto agotado, pago insuficiente, opción inválida).
   - Se inicializa con `init(autoreset=True)` para restablecer el color tras cada impresión.

## Requisitos

- Python 3.6 o superior.
- Librería `colorama`. Instalación:
  ```
  pip install colorama
  ```

## Cómo Ejecutar

1. Asegúrate de estar en el directorio raíz del proyecto.
2. Ejecuta el archivo principal:
   ```
   python main.py
   ```
3. Sigue las instrucciones en pantalla:
   - **Opción 1**: Ver todos los productos con su stock.
   - **Opción 2**: Realizar una compra (seleccionar producto, ingresar monto).
   - **Opción 3**: Salir del programa.

## Flujo de Compra

1. El usuario selecciona la opción **2** en el menú.
2. Se muestra la lista de productos disponibles con su precio.
3. El usuario ingresa el número del producto deseado.
4. Se solicita el monto a pagar.
5. El sistema verifica:
   - Si hay stock y el pago es suficiente:
     - Se actualiza el stock.
     - Se calcula el cambio (si existe).
     - Se muestra un mensaje verde de éxito.
   - En caso contrario, se muestra un mensaje rojo indicando el motivo (falta de stock o pago insuficiente).


