"""Uma manicure atende várias clientes durante o dia. 
Solicite ao usuário: 
• Nome da cliente 
• Quantidade de unhas decoradas 
• Valor da manicure simples (R$ 30,00) 
Cada unha decorada acrescenta R$ 2,00 ao serviço. 
Exiba: 
• Nome da cliente em maiúsculo 
• Valor total a pagar 
• Quantidade de caracteres do nome"""

#usando print
print('Olá {}' . format(input('Qual o nome da cliente? ')))
qtd_decoradas = input('informe numero de unhas ')
qtd_decoradas=int(qtd_decoradas)

#calculos

valor_simples = 30.00
valor_total = valor_simples + (qtd_decoradas *2)

print(f'R$ {valor_total:.2f}')

nomecompleto = input('Informe o seu nome completo: ')
# metodos utilizados:
# upper = transforma um texto em maiusculo
# função len retorno a quantidade de caractersde uma variável
print('1. Quantidade de caracteres:', len(nomecompleto))


"""Exercício 2 - Lava a Jato          
Um lava a jato possui dois serviços: 
• Lavagem simples = R$ 25,00 
• Lavagem completa = R$ 50,00 
Solicite: 
• Nome do cliente 
• Tipo de lavagem (1 ou 2) 
Utilize if/else para mostrar: 
• Serviço escolhido 
• Valor a pagar 
Desafio: mostrar mensagem de erro caso a opção seja diferente de 1 ou 2."""
 
#calculos

valor_simples = 25.00
valor_completo = 50.00

#usando print
print('Olá {}' . format(input('Qual o nome da cliente? ')))

numero = int(input('Tipo de lavagem (1 ou 2): '))

if(numero == 1):
    print("valor a pagar {}" . format(valor_simples))
elif(numero == 2 ):
    print("valor a pagar {}" . format(valor_completo))
else:
    print('mensagem de erro digite 1 ou 2')



"""Exercício 3 - Estacionamento Pago    
Um estacionamento cobra: 
• R$ 5,00 por hora 
Solicite: 
• Nome do motorista 
• Quantidade de horas estacionadas 
Calcule: 
• Valor total 
Caso o valor seja superior a R$ 30,00, informe: 
Cliente recebeu desconto de 10% 
e aplique o desconto."""

#calculos

valor_por_hora = 5,00

#usando print
print('Olá {}' . format(input('Qual o nome do motorista? ')))



numero = int(input('Quantidade de horas estacionadas: '))
cacule:
print("valor a pagar {}". format(numero))



