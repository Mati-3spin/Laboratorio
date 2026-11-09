# Reserva de Salas

Sistema de gestión de salas y reservas usando Python + SQLAlchemy + SQLite.

## Datos
- Curso: ICINF1109 - Programación II
- Estudiante: Matias Espinoza
- Fecha: 09/11/2026
## Dependencias

| Paquete | Versión mínima | Uso |
|---------|---------------|-----|
| `sqlalchemy` | 2.0 | ORM, engine, sesiones |

> `sqlite3`, `re`, `datetime` son de la librería estándar.

## Instalación

```bash
pip install sqlalchemy   
```
## Arquitectura
```
Workspace/Programacion2/Laboratorio/
├── main.py          # Menú y flujo principal
├── Conexion.py      # Engine y sessionmaker
├── Modelo.py        # ORM (Sala, Reserva)
├── CrearTabla.py    # create_all
├── Registrar.py     # Insertar salas y reservas
├── Consultar.py     # Listado de salas y reservas
└── Cancelar.py      # Borrar reserva  
```

