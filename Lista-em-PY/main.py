lista = []


while True:
  valor = int(input('Digite um valor inteiro: '))
  if valor not in lista:
    lista.append(valor)
    print('Valor adicionado!')

  else:
    print('Valor duplicado!')
    
  continuar = str(input('Quer continuar? [S/N] '))

  if continuar in 'Nn':
    break

lista.sort()
print(lista)