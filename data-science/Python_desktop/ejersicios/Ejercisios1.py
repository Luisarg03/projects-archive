print("Comparacion de numeros")

Numero1=int(input("Ingresa el primer numero: "))

Numero2=int(input("Ingresa el segundo numero: "))

def DevuelveMax(Num1, Num2):

    if Num1>Num2:

        print("El primer numero ingresado es mayor que el segundo")

    elif Num1<Num2:

         print("El segundo numero ingresado es mayor que el primero")

    else:

         print("Ambos numeros son iguales")

DevuelveMax(Numero1,Numero2)