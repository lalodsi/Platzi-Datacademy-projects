from os import kill, system

def limpiar_pantalla():
    system('cls')
    print("""Bienvenido a este programa, elige una opción
    [1] convertir de millas a kilómetros
    [2] convertir de kilómetros a millas
    """)

def convertir_km_millas():
    kilometros = int(input('Teclea la cantidad de kilometros que deseas convertir a millas: '))
    KM_A_MILLAS = 0.6214
    millas = kilometros * KM_A_MILLAS
    print(f'{kilometros} kilometros equivale a {millas} millas')

def convertir_millas_km():
    millas = int(input('Teclea la cantidad de millas que deseas convertir a km: '))
    KM_A_MILLAS = 0.6214
    kilometros = millas / KM_A_MILLAS
    print(f'{millas} millas equivale a {kilometros} kilometros')

def main():
    data = 3
    limpiar_pantalla()
    data = input('Opción: ')
    while(data != "1" and data != "2"):
        limpiar_pantalla()
        print("No existe esa opción, intenta de nuevo")
        data = input('Opción: ')
    data = int(data)
    if (data == 1):
        convertir_millas_km()
    elif (data == 2):
        convertir_km_millas()
    print('FIN DEL PROGRAMA')

if __name__ == '__main__':
    main()