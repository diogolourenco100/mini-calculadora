import time
import os

z = 50
while z != 99:

    os.system("cls")
    print("")


    v1 = input("Enter the value 1: ")
    v2 = input("Enter the value 2: ")
    time.sleep(0.2)

    os.system("cls")

    print("")

    print("1 - Soma")
    print("2 - Multiplicação")
    print("3 - Subtração")
    print("4 - Divisão")
    print("")
    print("99 - Sair")

    print("")

    z = int(input("Choose an option: "))

# =======================OPERAÇÕES===========================
    if z == 1:
        soma = int(v1) + int(v2)
        print("Soma: " + str(soma))
        print("")
        print("Cleaning terminal...")
        time.sleep(2)
        os.system("cls")

    elif z == 2:
        mult = int(v1) * int(v2)
        print("Multiplicação: " + str(mult))
        print("")
        print("Cleaning terminal...")
        time.sleep(2)
        os.system("cls")

    elif z == 3:
        sub = int(v1) - int(v2)
        print("Subtração: " + str(sub))
        print("")
        print("Cleaning terminal...")
        time.sleep(2)
        os.system("cls")
    
    elif z == 4:

        div = int(v1) / int(v2)
        print("Divisão: " + str(div))
        print("")
        print("Cleaning terminal...")
        time.sleep(2)
        os.system("cls")

    elif z == 99:
        print("Ending the service...")
        time.sleep(1)
        os.system("cls")

    else:
        print("Please enter a valid value.")
        time.sleep(2)
        os.system("cls")
