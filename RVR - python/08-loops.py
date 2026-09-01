#loop for
for i in range(1, 6):
    print(i)

frutas = ["maça", "banana", "uva"]
for fruta in frutas:
    print(fruta)

#loop for continue (pula o 5)
for j in range(1,11):
    if j == 5:
        continue
    print(j)

#loop for coom break (para o 4)
for m in range(1,11):
    if m == 5:
        break
    print(m)

#usando o continue e brek juntos
for n in range(1, 11):
    if n == 5:
        continue #pula o número 5

    if n == 8:
        break #para o loop quando chegar no 8

    print(n)


#l0op while
texto = ""

while texto != "sair":
    texto = input("Digite algo (ou 'sair' parar): ")


contador = 1

while contador <= 5:
    print(contador)
    contador += 1 #incremento

#não devemos fazer - loop infinito
#while True:
    #print("Este loop é infinito!")


#loop com try e except
while True:
    try:
        n = int(input("Digite um número: "))
        print(n)
        break
    except ValueError:
        if input("Tentar novamente? (s/n): ").lower() != 's':
            break
         