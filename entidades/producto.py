from enums.tipo_producto import TipoProducto

class Producto:
    """Clase que representa un producto de la máquina expendedora."""
    
    def __init__(self, nombre: str, precio_unitario: float, cantidad_existencias: int, tipo_producto: TipoProducto):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad_existencias = cantidad_existencias
        self.tipo_producto = tipo_producto

    def comprar_producto(self, pago: float):
        """
        Procesa la compra de un producto.
        
        Args:
            pago (float): Monto pagado por el cliente.
            
        Returns:
            tuple: (exito, mensaje, cambio) donde:
                - exito (bool): True si la compra fue exitosa, False en caso contrario.
                - mensaje (str): Mensaje descriptivo.
                - cambio (float): Monto de cambio (0 si no aplica).
        """
        if self.cantidad_existencias <= 0:
            return False, "Producto agotado", 0
        
        if pago < self.precio_unitario:
            faltante = self.precio_unitario - pago
            return False, f"Monto insuficiente. Faltan ${faltante}", 0
        
        self.cantidad_existencias -= 1
        cambio = pago - self.precio_unitario
        mensaje = f"Compra procesada del artículo. Precio: ${self.precio_unitario}, Cambio: ${cambio}. Gracias por su compra."
        return True, mensaje, cambio