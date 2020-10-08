temperatura = 'frio'
if temperatura == 'quente':
  print('vou a praia')
else:
  print('Vou comer um chocolate')

horario = 'noite'
if horario == 'manhã':
  print('O sol está quente')
elif horario == 'tarde':
  print('Está infinitamente quente')
else:
  print('Dá pra viver hoje')

idade = 21
if idade >= 18:
  print('Liberado beber bibadas alcoolicas')
else:
  print('Menor de idade, não pode beber bebidas alcoolicas')

temperatura1 = 25
if temperatura1 <= 30:
  print('ACEITÁVEL')
else:
  print('ME SALVA TO NO INFERNO')

altura = 1.76
if altura > 1.80:
  print('Pagão é alto')
else:
  print('Pagão é tipo baixo')

quente = False
gosta_praia = False
gosta_chocolate_quente = True
if quente == True:
  print('Está quente')
  if gosta_praia == True:
    print('Vá para a praia')
  else:
    print('Não vá a praia')
else:
  print('Está frio')
  if gosta_chocolate_quente == True:
    print('Tome um chocolate quente')
  else:
    print('Não tome chocolate quente')


dia = 'sabado'
if dia == 'sabado':
  print('É fim de semana :D')
elif dia == 'domingo':
  print('É fim de semana :D')
else:
  print('Não é fim de semana D:')


dia = input('Qual é o dia atua? ')
if dia == 'sabado' or dia == 'domingo':
  print('É fim de semana :D')
else:
  print('Não é fim de semana D:')

horario1 = 'manha'
sol = True
if horario1 == 'manha' and sol == True:
  print('Manhã bela e ensolarada')

meu_nome = 'Gabriel'
nome = input('Digite seu nome: ')
meu_sobrenome = 'Paganini'
sobrenome = input('Digite seu sobrenome: ')
if nome == meu_nome and sobrenome == meu_sobrenome:
  print('Vocé é o Gabriel Paganini')
else:
  print('Você não é o Gabriel Paganini')

for numero in range(1,10):
  print(numero)

for numero1 in range(5):
  print(numero1)

for numero2 in range(1, 11):
  print('O número atual é: ', numero2)

nomes = ['Gabriel', 'Fabiana', 'Amanda', 'Anderson']
for nome in nomes:
  print('O nome é: ', nome)
  if nome == 'Gabriel':
    print('(Ou Pagão)')

notas = [6, 7.5, 9, 10]
soma = 0
for nota in notas:
  soma = soma + nota
print(soma)
media = soma / len(notas)
print('A média é: ', media)

def mostrar_nome():
  print('Gabriel Paganini')
mostrar_nome()

def mostra_nome(nome_atual):
  print(nome_atual)
mostra_nome('Gabriel')
mostra_nome('Amanda')

def calc_media(nota1, nota2):
  soma1 = nota1 + nota2
  media1 = soma1 / 2
  print(media1)
primeira_nota = float(input('Sua primeira nota: '))
segunda_nota = float(input('Sua segunda nota: '))
calc_media(primeira_nota, segunda_nota)


def calcular_media(nota1, nota2):
  soma = nota1 + nota2
  media = soma / 2
  return media
media_calculada = calcular_media(10,8)
print(media_calculada)

def num_quadrado(num):
  quadrado = num * num
  return quadrado
def calcular_imc(peso, altura):
  altura_quadrada = num_quadrado(altura)
  meu_imc = peso / altura_quadrada
  return meu_imc
def classificar_imc(meu_imc):
  if imc < 18.5:
    print('Magreza')
  elif imc >= 18.5 and imc < 25:
    print('Normal')
  elif imc >= 25 and imc < 30:
    print('Sobrepeso')
  elif imc >= 30 and imc < 40:
    print('Obesidade')
  else:
    print('Obesidade Grave')
imc = calcular_imc(66,1.76)
print('Seu IMC é: ', imc)
print('Sua classificação é: ')
classificar_imc(imc)