from Conexion import *
from CrearTabla import *
from Registrar import registra_reservas, registra_salas
from Consultar import consultar_reserva, consultar_sala
from Cancelar import cancelar_reserva
import re

def conexion():
    with engine.connect():
        print("Conexión SQLite exitosa")

#Mostrar Menu
def mostrar_menu():
    print("\n================================")
    print("\n        Reserva de salas        ")
    print("1. Registrar salas")
    print("2: Consultar salas")
    print("3: Registrar reserva")
    print("4: Consultar reservas")
    print("5. Cancelar reserva")
    print("0. Salir")

#Solictar Datos e insertar sala
def ingresa_sala():
    print("\n-----------Agrgar Salas-----------")

    nombre = input("Ingrese el nombre de la sala: ").strip()
    try:
        capacidad = int(input("Ingrese el precio del producto: "))
        disponible_str = input("Ingrese el stock del producto: ").strip().lower()
        disponible = disponible_str == "s"

        if not nombre:
            print("ERROR: debe ingresar un nombre")
            return
        if not disponible:
            print("La disponibilidad debe ser verdadera")
        if capacidad < 0:
            print("ERROR: capacidad debe ser valida y no negativa")
            return
        registra_salas(nombre, capacidad, disponible)

    except (ValueError, TypeError):
        print("ERROR : ingrese un valor numerico validoo booleano verdadero")

#
def ingresa_reserva():
    print("\n-----------Realizar Reserva-----------")

    estudiante = input("Ingrese el nombre del estudiante: ").strip()
    try:
        sala_id = int(input("Ingrese el precio del producto: "))
        fecha = input("Ingrese el stock del producto: ").strip()

        if not estudiante:
            print("ERROR: debe ingresar un nombre")
            return

        if not re.match(r"^\d{4}-\d{2}-\d{2}$", fecha):
            print("La fecha debe tener el formato AAAA-MM-DD.")
            return

        if sala_id <= 0:
            print("ERROR : la llave foranea debe ser valida y no negativa")
            return
        registra_reservas(estudiante, sala_id, fecha)

    except (ValueError, TypeError):
        print("ERROR : ingrese un id númerico valido de un registro existente")


# cancelar
def eliminar_reserva():
    print("\n---------Cancelar Reserva---------")

    try:
        in_id_reserva = int(input("Ingrese el id de la reserva: "))

        if in_id_reserva <= 0:
            print("ERROR : debe ingresar un ID valido")
            return

        confirmar = input("Confirmar el producto (S/N): ")

        if confirmar.strip().upper() == "S":
            cancelar_reserva(in_id_reserva)
        else:
            print("ERROR : Eliminacion cancelado")

    except (ValueError):
        print("ERROR : se esperan datos validos y no negativos")


def main():
    conexion()
    while True:
        mostrar_menu()
        opcion = input("Selecciones Opcion: ")

        if opcion == "1":
            ingresa_sala()
        elif opcion == "2":
            consultar_sala()
        elif opcion == "3":
            ingresa_reserva()
        elif opcion == "4":
            consultar_reserva()
        elif opcion == "5":
            eliminar_reserva()
        elif opcion == "0":
            print("Saliendio del sistema")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()   