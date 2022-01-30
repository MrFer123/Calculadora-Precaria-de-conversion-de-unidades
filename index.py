# python index.py
print('')

print('Bienvenido a la calculadora de conversion de unidades a otras unidades! ')

print('')

menu = input('Por favor introduce una unidad a convertir => ')

print('')

print('Unidades recibidas')

if menu == 'cm a m':

    print('')

    paso1 = int(input('Por favor diga los centimetros a convertir a metro => '))

    print('')

    print('Procesando')

    print('')

    resultado = paso1/100

    print(f'{paso1} centimetros a metros son , {resultado} metros!')

if menu == 'm a cm':

    print('')

    paso1 = int(input('Por favor diga los metros a convertir a centimetros => '))

    print('')

    print('Procesando')

    print('')

    resultado = paso1*100

    print(f'{paso1} metros a centimetros son , {resultado} centimetros!')

if menu == 'm a km':

        print('')

        paso1 = int(input('Por favor diga los metros a convertir a kilometros => '))

        print('')

        print('Procesando')

        print('')

        resultado = paso1/1000

        print(f'{paso1} metros a kilometros son , {resultado} kilometros!')

if menu == 'km a m':

    print('')

    paso1 = int(input('Por favor diga los kilometros a convertir a metros => '))

    print('')

    print('Procesando')

    print('')

    resultado = paso1*1000

    print(f'{paso1} kilometros a metros son , {resultado} metros!')

if menu == 'cm a km':

    print('')

    paso1 = int(input('Por favor diga los centimetros a convertir a kilometros => '))

    print('')

    print('Procesando')

    print('')

    resultado = paso1/100000

    print(f'{paso1} centimetros a kilometros son , {resultado} kilometros!')

if menu == 'km a cm':

    print('')

    paso1 = int(input('Por favor diga los kilometros a convertir a centimetros => '))

    print('')

    print('Procesando')

    print('')

    resultado = paso1*100000

    print(f'{paso1} kilometros a centimetros son , {resultado} centimetros!')
