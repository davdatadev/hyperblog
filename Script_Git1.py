import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

def calc_age(bithday):
    hoy = datetime.strftime(datetime.now().date(),"%d-%m-%Y")
    edad = relativedelta(datetime.now(), datetime.strptime("1992-09-04", "%Y-%m-%d")).years
    return edad, hoy

def main():
    edad, hoy = calc_age("1992-09-04")
    print("Hola Mundo!")
    print(f"Directorio de trabajo: {os.getcwd()}")
    print(f"La fecha de hoy: {hoy}")
    print(f"Mi nombre es: David")
    print(f"Mi edad es {edad}")

if __name__ == "__main__":
    main()