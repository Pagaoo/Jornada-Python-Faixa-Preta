nome = 'Gabriel'
sobrenome = 'Paganini'
apelido = "Pagão"
idade = 21

nome_completo = nome + ' ' + sobrenome
print(nome_completo)
print("--------------------")

texto_10 = '10'
numero_20 = 20
type(texto_10) #a função type mostra o tipo de dado
type(numero_20)
#Convertendo string para int
numero_10 = int(texto_10)
type(numero_10)
print(type(numero_10))
#convertendo int para string
texto_20 = str(numero_20)
print(type(texto_20))

esta_chovendo = True
esta_frio = False
print("------------------------")
print(esta_frio)
print(esta_chovendo)
print("------------------------")

soma = 10 + 20
subtracao = 10 - 20
mult = 2 * 3
div = 10 / 10
print(soma)
print(subtracao)
print(mult)
print(div)
print(soma + div)
print("-----------------------")

primeiro_numero = 20
segundo_numero = 30
terceiro_numero = 10
quarto_numero = 5

valor_final = (primeiro_numero + segundo_numero - terceiro_numero) * quarto_numero
print(valor_final)
print("------------------------")

nome = input("Insira seu nome: ")
print(input)
print(nome)
print("-------------------------")

numero1= 10
numero2 = 20

soma = numero1 + numero2

print("O valor da soma  é de: ", soma)
print("-------------------------")

nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")
print("O",nome, "tem", idade, "anos")
print("---------------------------")

valor_numero1 = float(input("Insira o primeiro numero: "))
valor_numero2 = float(input("Insira o segundo numero: "))

multiplicacao = valor_numero1 * valor_numero2

print("A multiplicação de", valor_numero1, "e de", valor_numero2, "é de: ", multiplicacao)
print("----------------------------")

lista_animais = ['Cachorro', 'Gato', 'Coelho', 'Furão', 'Passáro', 'Peixe']
furao = lista_animais[3]
gato = lista_animais[1]
print("A Shura é um", furao)
print("O Doctor é um", gato)
print("--------------------------")
