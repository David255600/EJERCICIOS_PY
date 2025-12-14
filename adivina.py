
import random
import math

# Numero secreto: 1 to 10
num1 = math.ceil(random.random() * 10)

intentos = 0

while True:
    num2 = int(input("Que numero estoy pensando? (1-10): "))

    if num1 == num2:
        break
    elif num2 < num1:
        print("No, mi numero es mayor, intentalo de nuevo")
    else:
        print("No, mi numero es menor, intentalo de nuevo")

    intentos = intentos + 1

print("Muy bien mi numero era", num1, "necesitaste", intentos, "intentos")