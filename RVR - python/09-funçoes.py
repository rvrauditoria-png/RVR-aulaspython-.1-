#Função - void
def saudacao():
    print("Olá, tudo bem?")
 
#acessando a função
saudacao()
 
#Função com parâmetro
def saudacao(nome):
    print("Olá,", nome)
 
#Acessando a Função
saudacao("João")
 
#função de retorno
def soma(a, b):
    return a + b
 
resultado = soma(5, 3)
print(resultado)
 
#Exemplo com tratamento de erro
try:
    numero = int(input("Digite um número: "))
    print(numero)
except:
    print("Você digitou algo inválido!")

#Try e Except usando Else e Finally juntos
try:
    numero = float(input("digite um NOVO número: "))
except ValueError:
    print("Erro: entrada inválida")
else:
    print("Você digitou:",numero)
finally:
    print("Programa finalizado")

    #exemplo de funÇão com try e except
    def dividir(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Erro: divisão por zero"

    print(dividir(10, 2))
    print(dividir(23, 0))

    #entrada do usuário
    a = float(input("Digite o primeiro número: "))
    b= float(input("Digite o segundo número: "))
    print(dividir(a, b))
    

