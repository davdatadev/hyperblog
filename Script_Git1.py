import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

#Script de muestra
hoy = datetime.strftime(datetime.now().date(),"%d-%m-%Y")
#edad = datetime.now() - datetime.strptime("1992-09-04", "%Y-%m-%d")
edad = relativedelta(datetime.now(), datetime.strptime("1992-09-04", "%Y-%m-%d")).years
print("Hola Mundo!")
print("Directorio de trabajo:", os.getcwd())
print(f"La fecha de hoy: {hoy}")
print(f"Mi nombre es: David")
print(f"Mi edad es {edad}")