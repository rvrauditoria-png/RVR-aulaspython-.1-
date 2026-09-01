#calculos
num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

soma = int(num1) + int(num2)
subtracao = int(num1) - int(num2)
divisao = int(num1) / int(num2)
moduloresto = int(num1) % int(num2)
multiplicacao = int(num1) * int(num2)
potenciacao = int(num1) ** int(num2)

print(soma)
print(subtracao)
print(divisao)
print(moduloresto)
print(multiplicacao)
print(potenciacao)

# o comando type retorna o tipo da variável
print(type(num1))
print(type(soma))

#calcular área
lado1 = input('Informe o primeiro lado: ')
lado2 = input('Informe o segundo lado: ')

area = float(lado1) * float(lado2)

print('A area do quadrado é: {}' . format(area))

nomecompleto = input('Informe o seu nome completo: ')
# função len retorno a quantidade de caracters de uma variável
print('1. Quntidade de carcters:', len(nomecompleto))

#upper = transforma um texto em maiusculo
#lower = transforma um texto em miusculo
#cpaitalize = somente a primeira letra em maiusculo
print('2. Nome em maiusculo:', nomecompleto.upper())
print('3. Nome em mnusculo:', nomecompleto.lower())
print('4. Primeira letra em maiusculo:', nomecompleto.capitalize())

      




             