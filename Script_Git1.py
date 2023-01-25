import os
from datetime import datetime

hoy = datetime.strftime(datetime.now().date(),"%d-%m-%Y")
edad = datetime.now() - datetime.strptime("1992-09-04", "%Y-%m-%d")
print("Hola Mundo!")
print("Directorio de trabajo:", os.getcwd())
print(f"La fecha de hoy: {hoy}")
print(f"Mi nombre es: David")
print(f"Mi edad es {round(edad.days/365)}")


