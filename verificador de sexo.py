sexo = str(input('Digite o sexo [M/F]')).strip()
if sexo in 'Mn':
    print('Sexo masculino')
elif sexo in 'Ff':
    print('Sexo feminino')
else:
    print('Sexo inválido')
