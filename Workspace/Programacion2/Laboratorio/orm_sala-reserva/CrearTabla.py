from Conexion import engine
from Modelo import Base

Base.metadata.create_all(engine)
print("Tablas creadas")
