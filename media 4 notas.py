total = 0
for c in range(1,5):
    nota = float(input('Digite a {}º nota: '.format(c)))
    total += nota
media = total / 4
print('A média das 4 notas é: {}'.format(media))

