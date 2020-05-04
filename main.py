import AnnoBisiesto

print('El programa determina si el anno ingresado es bisiesto')
ano = (input('Ingrese un ano: '))


while AnnoBisiesto.excepcion(ano)==False:
    print(ano,' no es un numero o es un decimal')
    ano = (input('Ingrese un ano: '))

while AnnoBisiesto.Negativo(ano)==True:
    print(ano,' debe ser un numero positivo')
    ano = (input('Ingrese un ano: '))    

if AnnoBisiesto.Bisiesto(ano)==True:
    print('El anno ',ano,' es bisiesto')
else:
    print('El anno ',ano,' no es bisiesto')