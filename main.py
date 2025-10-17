import Services.TiendaService
import models.Pedido
import models.Usuario
import models.Producto

def main():
    # Crear instancia del servicio
    tienda = Services.TiendaService.TiendaService()

    # ----- REGISTRAR USUARIOS -----
    cliente1 = tienda.register_user("cliente", 1, "Juan Pérez", "juan@mail.com", "Calle Falsa 123")
    cliente2 = tienda.register_user("cliente", 2, "María López", "maria@mail.com", "Av. Central 45")
    cliente3 = tienda.register_user("cliente", 3, "Carlos Ruiz", "carlos@mail.com", "Plaza Mayor 10")
    admin = tienda.register_user("administrador", 99, "Ana Admin", "admin@mail.com")

    # ----- CREAR PRODUCTOS -----
    p1 = models.Producto.Producto(101, "Teclado", 20.5, 10)
    p2 = models.Producto.ProductoElectronico(102, "Monitor", 150, 5, "2 años")
    p3 = models.Producto.ProductoRopa(103, "Camiseta", 15, 20, "M", "Azul")
    p4 = models.Producto.ProductoRopa(104, "Pantalón", 30, 15, "L", "Negro")
    p5 = models.Producto.ProductoElectronico(105, "Auriculares", 50, 8, "1 año")

    # ----- AÑADIR INVENTARIO -----
    tienda.añadir_producto(p1)
    tienda.añadir_producto(p2)
    tienda.añadir_producto(p3)
    tienda.añadir_producto(p4)
    tienda.añadir_producto(p5)

    # ----- LISTAR PRODUCTOS -----
    print("\n=== INVENTARIO DISPONIBLE ===")
    for prod in tienda.listar_productos():
        print(prod)
    
    # ----- SIMULAR PEDIDOS -----
    print("\n=== PEDIDOS ===")
    pedido1 = tienda.realizar_pedido(1, [(p1, 2), (p3, 1)])   # Juan compra 2 teclados + 1 camiseta
    pedido2 = tienda.realizar_pedido(2, [(p2, 1), (p5, 2)])   # María compra monitor + 2 auriculares
    pedido3 = tienda.realizar_pedido(3, [(p4, 3), (p1, 1)])   # Carlos compra 3 pantalones + 1 teclado

    print("\n--- Pedido 1 ---")
    print(pedido1)
    print("\n--- Pedido 2 ---")
    print(pedido2)
    print("\n--- Pedido 3 ---")
    print(pedido3)

    # ----- VER STOCK ACTUALIZADO -----
    print("\n=== STOCK TRAS PEDIDOS ===")
    for prod in tienda.listar_productos():
        print(prod)

    # ----- HISTÓRICO DE PEDIDOS DE UN CLIENTE -----
    print("\n=== HISTÓRICO DE PEDIDOS DE JUAN (ID=1) ===")
    for ped in tienda.listar_pedidos_user(1):
        print(ped)
        print("-" * 40)

if __name__ == "__main__":
    main()

