import random

def primalidad_fermat(numero, k_veces):
    for j in range(1, k_veces):
        a = random.randrange(1, numero)
        if (a**(numero-1) % numero) != 1:
            print( 'Se encontró que ' + str(a) + '^' + '(' + str(numero) + '-1) = ' + str(a**(numero-1)) )
            print(str(a**(numero-1)) + ' % ' + str(numero) + ' = ' + str(a**(numero-1) % numero))
            return 'El número ' + str(numero) + ' no es primo'
    return 'Es posible que ' + str(numero) + ' sea un número primo'

def run():
    numero = int(input('Escribe un numero: '))
    k_veces = int(input('Cuántas veces quieres repetir el algoritmo?: '))
    print(primalidad_fermat(numero, k_veces))

if __name__ == '__main__':
    run()