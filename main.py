from suma import Suma
from resta import Resta
from multiplicar import Multiplicacion
from division import Division
from suma_avanzada import SumaAvanzada

def ingresar_a():
    print("Ingresa el número a: ")
    a = int(input())
    return a
def ingresar_b():
    print("Ingresa el número b: ")
    b = int(input())
    return b


def menu_opciones():
    option = 1
    while option !=0:
        print("0. Salir")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Suma avanzada")
        option = int(input())
        
        if option == 1:
            a =ingresar_a()
            b =ingresar_b()
            suma = Suma
            suma.sumar(a, b)
                

        elif option == 2:
            a =ingresar_a()
            b =ingresar_b()
            resta = Resta
            resta.restar(a, b)

        elif option == 3:
            a =ingresar_a()
            b =ingresar_b()
            multiplicacion = Multiplicacion
            multiplicacion.multiplicar(a, b)
    
        elif option == 4:
            a =ingresar_a()
            b =ingresar_b()
            division = Division
            division.dividir(a, b)

        elif option == 5:
            numero = 1
            lista_numero =[]
            while numero !=0:
                print("Pulse 0 para dejar de ingresar números")
                print("Ingrese un numero: ")
                numero = int(input())
                
                lista_numero.append(numero)
                suma = SumaAvanzada
                suma.sumar(lista_numero)
        elif option == 0:
            print("Cerrando...")
        else:
            print("No valido")
            


        

menu_opciones()