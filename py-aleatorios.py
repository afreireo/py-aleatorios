import os,sys, math
import scipy.stats as stats

def limpiar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def menu_principal():
    limpiar_pantalla()

    print("*** MENÚ PRINCIPAL ***\n")
    print("0 .- Salir")
    print("1 .- Generar números pseudoaleatorios")
    print("2 .- Comprobar números pseudoaleatorios\n")
    
    opcion = input("--> Ingrese una opción: ")

    match opcion:
        case "0":
            sys.exit()
        case "1":
            menu_generar()
            #Metodo generar 1
        case "2":
            menu_comprobar()
            #Método generar 2
        case _:
            menu_principal()


def menu_generar():
    limpiar_pantalla()

    print("*** GENERAR ***\n")
    print("0 .- Volver al menú principal")
    print("1 .- Método Mitad Cuadrado")
    print("2 .- Método Congruencial Lineal")
    print("3 .- Método Congruencial Mixto\n")
    
    opcion = input("--> Ingrese una opción: ")

    match opcion:
        case "0":
            menu_principal()
        case "1":
            metodo_generar_mitad_cuadrado()
            #Metodo generar 1
        case "2":
            metodo_generar_congruencial_lineal()
            #Método generar 2
        case "3":
            metodo_generar_congruencial_mixto()
        case _:
            menu_generar()


def metodo_generar_mitad_cuadrado():
    limpiar_pantalla()
    print("*** METÓDO MITAD CUADRADO ***\n")
    
    semilla = input("--> Ingrese una semilla: ")
    iteraciones = input("--> Ingrese cantidad de iteraciones: ")
    numeros_aleatorios = []
    x = int(semilla)

    for _ in range(int(iteraciones)):
        
        x_cuadrado = x ** 2
        digitos_medio = str(x_cuadrado).zfill(8)[2:6]
        x = int(digitos_medio)
        numero_aleatorio = x / 10000
        numeros_aleatorios.append(numero_aleatorio)

    print("\nNúmeros aleatorios generados:")
    with open("numeros.txt","w") as archivo:
        for i, num in enumerate(numeros_aleatorios, start=1):
            print(f"Iteración {i}: {num:.4f}")
            archivo.write(f"{num}\n")
    
    print("\nArchivo numeros.txt creado")


def metodo_generar_congruencial_lineal():
    limpiar_pantalla()
    print("*** METÓDO GENEARAR CONGRUENCIAL LINEAL ***\n")
    print("Formula: x_siguiente = (a * x_anterios) // m\n")

    semilla = input("--> Ingrese una semilla (x): ")
    a = input("--> Ingrese el valor de a: ")
    m = input("--> Ingrese el valor de m: ")
    iteraciones = input("--> Ingrese la cantidad de iteraciones: ")
    
    numeros_aleatorios = []
    numeros_aleatorios.append(int(semilla))
    print("")

    for i in range(int(iteraciones)):
        if (i != 0):
            aleatorio = (int(a)*int(numeros_aleatorios[i-1]))%int(m)
            numeros_aleatorios.append(aleatorio)
            print("Aleatorio " + str(i) + ": " + str(numeros_aleatorios[i]))

    with open("numeros.txt","w") as archivo:
        for num in numeros_aleatorios:
            archivo.write(f"{num}\n")
    
    print("\nArchivo numeros.txt generado correctamente")


def metodo_generar_congruencial_mixto():
    limpiar_pantalla()
    print("*** METÓDO GENERAR CONGRUENCIAL MIXTO ***\n")
    print("Formula: x_siguiente = (a * x_anterios + c) // m\n")

    semilla = input("--> Ingrese una semilla (x): ")
    a = input("--> Ingrese el valor de a: ")
    c = input("--> Ingrese el valor de c: ")
    m = input("--> Ingrese el valor de m: ")
    iteraciones = input("--> Ingrese la cantidad de iteraciones: ")
    
    numeros_aleatorios = []
    numeros_aleatorios.append(int(semilla))
    print("")

    for i in range(int(iteraciones)):
        if (i != 0):
            aleatorio = ((int(a)*int(numeros_aleatorios[i-1])) + int(c)) % int(m)
            numeros_aleatorios.append(aleatorio)
            print("Aleatorio " + str(i) + ": " + str(numeros_aleatorios[i]))

    with open("numeros.txt","w") as archivo:
        for num in numeros_aleatorios:
            archivo.write(f"{num}\n")
    
    print("\nArchivo numeros.txt generado correctamente")




    
def menu_comprobar():
    limpiar_pantalla()

    print("*** COMPROBAR ***\n")
    print("0 .- Volver al menú principal")
    print("1 .- Método Chi Cuadrado")
    print("2 .- Método 2\n")
    
    opcion = input("--> Ingrese una opción: ")

    match opcion:
        case "0":
            menu_principal()
        case "1":
            metodo_comprobar_chi_cuadrada()
        case "2":
            menu_comprobar()
            #Método generar 2
        case _:
            menu_comprobar()


def metodo_comprobar_chi_cuadrada():
    numeros = []
    limites = []

    xi_cuadrado = 0
    suma = 0
    minimo = 0
    maximo = 0
    rango = 0
    datos = 0
    intervalos = 0
    tamano_intervalo = 0

    with open("numeros.txt","r") as archivo:
        for linea in archivo:
            numero = float(linea.strip())
            numeros.append(numero)

    minimo = min(numeros)
    maximo = max(numeros)
    rango = maximo - minimo
    datos = len(numeros)
    intervalos = math.ceil(math.sqrt(datos))
    tamano_intervalo = rango/intervalos
    frecuencia_esperada = datos/intervalos
    libertad = intervalos - 1
    probabilidad = 0.05

    limite = minimo
    while limite < maximo:
        limite += tamano_intervalo
        limites.append(limite)

    for limite in limites:
        frecuencia = 0
        for i in range(datos):
            numero = numeros[i]
            if (numero < limite):
                if limite == limites[0]:
                    frecuencia += 1
                else:
                    if numero >= (limite-tamano_intervalo):
                        frecuencia += 1
                
        xi_cuadrado += (frecuencia/frecuencia_esperada)*(frecuencia/frecuencia_esperada)/frecuencia_esperada

    xi_tabla = stats.chi2.isf(probabilidad, libertad) 

    print("\nChi Cuadrado: " + str(xi_cuadrado))
    print("Chi Tabla: " + str(xi_tabla))

    if(xi_tabla > xi_cuadrado):
        print("\n --> Se acepta")
    else:
        print("\n --> Se rechaza")


menu_principal()

