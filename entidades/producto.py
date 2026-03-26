from enums.tipo_producto import TipoProducto

class Producto:
    def __init__ (self, nombre: str, precio_unitario: float, cantidad_existencias: int, tipo_producto: TipoProducto):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad_existencias = cantidad_existencias
        self.tipo_producto = tipo_producto

    def comprar_producto(self):
        if self.cantidad_existencias > 0:
            self.cantidad_existencias -= 1
            operacion = pago - self.precio_unitario#Variable carlos
            return f"Compra procesada del articulo. Precio: {self.precio_unitario}, Cambio {operacion}, Gracias por su compra."
