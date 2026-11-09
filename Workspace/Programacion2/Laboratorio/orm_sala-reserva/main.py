from sqlalchemy import text
from Conexion import *
from Modelo import Sala, Reserva
from CrearTabla import *
from Registrar import registra_reservas,  registra_salas
from Consultar import consultar_reserva, consultar_sala
from Cancelar import cancelar_reserva
import re

def conexion():
    with engine.connect() as conexion:
        print("Conexión SQLite exitosa")
    conexion = engine.connect()
    return conexion

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
        disponible = bool(input("Ingrese el stock del producto: "))

        if not nombre:
            print("ERROR: debe ingresar un nombre")
            return
        if not disponible:
            print("La disponibilidad debe ser verdadera")
        if not capacidad.is_finite()  or capacidad < 0:
            print("ERROR: capacidad debe ser valida y no negativa")
            return
        registra_salas(nombre, capacidad, disponible)

    except (ValueError, TypeError):
        print("ERROR : ingrese un valor numerico validoo booleano verdadero")

def insertar(nombre, capacidad, disponble):
    with Session.begin() as session:
        sala = Sala(
            nombre=nombre,
            capacidad=capacidad,
            disponble=disponble
        )
        session.add(sala)
    print("Sala registrada")

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
        
        if re.match(r"^\d{4}-\d{2}-\d{2}$", fecha):
            print("La fecha debe tener el formato AAAA-MM-DD.")
            return
        
        if not sala_id.is_finite()  or sala_id < 0:
            print("ERROR: la llave foranea debe ser valida y no negativa")
            return
        registra_reservas(estudiante, sala_id, fecha)

    except (ValueError, TypeError):
        print("ERROR : ingrese un id númerico valido de un registro existente")

def insertar(estudiante, sala_id, fecha):
    with Session.begin() as session:
        reserva = Reserva(
            estudiante=estudiante,
            sala_id=sala_id,
            fecha=fecha
        )
        session.add(reserva)
    print("Reserva registrada")


# cancelar
def eliminar_reserva():
    print("\n---------Cancelar Reserva---------")

    try:
        in_id_reserva = int(input("Ingrese el id de la reserva: "))

        if in_id_reserva <= 0 :
            print("ERROR : debe ingresar un ID valido")
            return

        confirmar = input("Confirmar el producto (S/N): ")

        if confirmar.strip().upper() == "S" :
            cancelar_reserva(in_id_reserva)
        else:
            print("ERROR : Eliminacion cancelado")

    except (ValueError):
        print("ERROR : se esperan datos validos y no negativos")




#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
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