frutas = ["maça", "banana", "uva"]
print(frutas)

#ver primeiro elemento da lista
print(frutas[0])

#retornando demais elementos no seu index
print(frutas[1])
print(frutas[2])
#modificado
frutas[1] = "laranja"
print(frutas)


#adicionando itens no final da lista
frutas.append("pêra")
print(frutas)

#adicionando no começo da lista
frutas.insert(0, "abacaxi")
print(frutas)

#procurando
indice = frutas.index("uva")
print(indice)

if "uva" in frutas:
    print("Uva está na lista")

#removendo itens
frutas.remove("uva")
print(frutas)

if "uva" in frutas:
    print("Uva está na lista")
else:print("Uva foi removida")


#tamanho da lista
numeros = [100,28,4,31]
print(len(numeros))

#ordenar
numeros.sort()
print(numeros)

frutas.sort()
print(frutas)

#inverter
numeros.reverse()
print(numeros)

frutas.reverse()
print(frutas)

#verificar se existe
print(2 in numeros)
print(100 in numeros)

#adicionando varios elementos ao mesmo tempo
numeros = [10, 20, 30] + numeros
#ordenei
numeros.sort()
print(numeros)

#percorrer com for
for n in numeros:
    print(n)

print(type(n))
print(type(numeros))









