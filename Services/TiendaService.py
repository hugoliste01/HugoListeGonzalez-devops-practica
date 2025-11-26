import models.Usuario
import models.Pedido

class TiendaService:


    def __init__(self):
        self.users = {}
        self.products = {} 
        self.pedidos = []
        

    def register_user(self, tipo, id, name, email, dir=None):
        if tipo.lower() == "cliente":
            user = models.Usuario.Cliente(id, name, email, dir)
        elif tipo.lower() == "administrador":
            user = models.Usuario.Administrador(id, name, email)

        self.users[id] = user
        return user
        
    def añadir_producto(self, producto):
        self.products[producto.id] = producto

    def eliminar_producto(self, producto_id):
        del self.products[producto_id]

    def listar_productos(self):
        return list(self.products.values())
    
    def realizar_pedido(self, cliente_id, products_cantidades):

        cliente = self.users[cliente_id]

        # Verificar stock
        for producto, cantidad in products_cantidades:
            if producto.id not in self.products:
                raise ValueError(f"El producto {producto.name} no existe en la tienda")
            if producto.stock < cantidad:
                raise ValueError(f"Stock insuficiente para {producto.name}")

        # Descontar stock
        for producto, cantidad in products_cantidades:
            producto.stock -= cantidad

        # Crear pedido
        pedido = models.Pedido.Pedido(cliente, products_cantidades)
        self.pedidos.append(pedido)
        return pedido

    # ---------- HISTORIAL ----------
    def listar_pedidos_user(self, cliente_id):
        pedidos_cliente = [p for p in self.pedidos if p.client.id == cliente_id]
        pedidos_cliente.sort(key=lambda p: p.date)  # ordenar por fecha
        return pedidos_cliente