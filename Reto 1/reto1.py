def determinar_triangulo():
    print(""" 
        Programa para determinar el tipo de triángulo
    """)
    a = input('Escribe el lado a del triángulo: ')
    b = input('Escribe el lado b del triángulo: ')
    c = input('Escribe el lado c del triángulo: ')

    if a == b or a == c:
        # Entonces el triángulo es isósceles o equilatero
        if b == c:
            print("El triángulo es equilatero porque sus tres lados son iguales")
        else:
            print("El triángulo es isósceles porque tiene dos lados iguales")
    else:
        # Entonces el triángulo es isósceles o escaleno
        if b == c:
            print("El triángulo es isósceles porque tiene dos lados iguales")
        else:
            print("Ninguno de los lados es igual, por lo que el triángulo es escaleno")

def calcular_area():
    print(""" 
        Programa para calcular el área de un triángulo
    """)
    base = int(input('Escribe la base del triángulo: '))
    altura = int(input('Escribe la altura del triángulo: '))

    Area = base * altura /2
    print('El área es: ' + str(Area))

def run():
    print("""
        Programa para triángulos:
        Elige una de las opciones
        [1]: Calcular el área del triángulo
        [2]: Determinar el tipo de triángulo""")
    opcion = 0
    opcion = int(input('¿Qué opción eliges?: '))
    while opcion != 1 and opcion != 2:
        opcion = int(input("""
        No se permite elegir esa opción
        Elige una de nuevo: """))
        print('Opcion elegida: ' + str(opcion))
    if opcion == 1:
        calcular_area()
    else:
        determinar_triangulo()



if __name__ == '__main__':
    run()