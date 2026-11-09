from sqlalchemy import select
from Conexion import Session
from Modelo import 

def consultar_productos():
    with Session() as session:
        consulta = select(Producto)
        productos = session.scalars(consulta).all()

        print("\n---------Listado de Productos---------\n")
        if not productos:
            print("No existen Productos")
            return
        for producto in productos:
            print("-------------------------------------")
            print("ID : ", producto.id)
            print("Nonbre : ", producto.nombre)
            print("Stock : ", producto.stock)

        print("------------------------------------------")