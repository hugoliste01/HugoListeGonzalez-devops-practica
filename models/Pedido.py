import datetime
import uuid

class Pedido:

    def __init__(self, client, product_list):
        self.id = uuid.uuid4()
        self.date = datetime.date.today()
        self.client = client
        self.product_list = product_list

    
    def calculate_total(self):
        total = 0
        for producto, cantidad in self.product_list:
            total += producto.price * cantidad
        return total
    
    def __str__(self):
        productos_str = "\n".join(
            [f"- {prod.name} x{cant} = {prod.price * cant}€" 
             for prod, cant in self.product_list]
        )
        return (
            f"Pedido ID: {self.id}\n"
            f"Cliente: {self.client}\n"  # aquí usará el __str__ de Usuario
            f"Fecha: {self.date}\n"
            f"Productos:\n{productos_str}\n"
            f"TOTAL: {self.calculate_total()}€"
        )