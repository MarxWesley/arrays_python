carros = (
    int(input('CAMARO faz quantos KM/L: ')),
    int(input('MUSTANG faz quantos KM/L: ')),
    int(input('BMW X6 faz quantos KM/L: ')),
    int(input('AUDI RS 5 faz quantos KM/L: ')),
    int(input('LAND ROVER EVOQUE faz quantos KM/L: '))
)
#
nomes = (
    'CAMARO',
    'MUSTANG',
    'BMW',
    'AUDI',
    'LAND ROVER'
)
#
maior = 0
#
for c in carros:
    if ( c > maior):
        maior = c
#
print('')
#
if (carros[0] == maior):
    print('O mais economico é o Camaro')
elif (carros[1] == maior):
    print('O mais economico é o Mustang')
elif (carros[2] == maior):
    print('O mais economico é a BMW X6')
elif (carros[3] == maior):
    print('O mais economico é o AUDI')
else:
    print('O mais economico é a LAND ROVER')
#
print('')
for v in range(len(carros)):
    consumo = 1000 / carros[v]
    custo = 5.25 * consumo
    print(f'O {nomes[v]} consome {consumo:.2f} Litros para percorrer 1000 KM e o gasto será de R${custo:.2f}')