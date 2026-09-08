#Execrício 1: Pet Shop - Cálculo do Banho

#coleta de variáveis
nomePet =''
pesoPet = 0

valorBanho = 0

nomePet = input("Digite o nome do Pet")
pesoPet = float(input("Digite o peso do Pet"))

def calcularBanho(pesoPet):
    if pesoPet <10:
        valorBanho = 30
        return valorBanho
    elif (pesoPet >= 10) & (pesoPet <= 20):
        valorBanho = 50
        return valorBanho
    elif pesoPet > 20:
        valorBanho = 70
        return valorBanho

#retorno
print(f"Pet: {nomePet} \nValor do Banho: R${calcularBanho(pesoPet):.2f}")

#Exercício 2: Empresa de Frota de Motos - Controle de Quilometragem

#2 - Frota de Motos
quantidadedemotos = int(input("Quantas motos há na frota? "))

totalQuilometragem = 0
mediaQuilometragem = 0
maiorQuilometragem = 0

for moto in range(1, (quantidadedemotos + 1)):

    quilometragem = float(input("Qual a quilometragem desta moto? "))
    
    if quilometragem > maiorQuilometragem:
        maiorQuilometragem = quilometragem

    totalQuilometragem = totalQuilometragem + quilometragem

mediaQuilometragem = totalQuilometragem / quantidadedemotos

print(f"O total de quilometragem percorridos foi de {totalQuilometragem} KM")
print(f"A média da quilometragem percorridos foi de {mediaQuilometragem} KM")
print(f"A maior quilometragem registrada foi de {maiorQuilometragem} KM")


#Exercício 3: Lanchonete de Hot Dog - Pedido do Cliente 

precoHotDogSimples = 10.00 
precoHotDogDuplo = 15.00
precoRefrigerante = 6.00  
 
#quantidadesimples = int(input("Deseja incluir quantos Hot Dog Simples no pedido?"))
#quantidadesdupo = int(input("Deseja incluir quantos Hot Dog Duplo no pedido?"))
#quantidadesrefrigeramtes = int(input("Deseja incluir quantos Refrigerantes no pedido?"))

print(f"precoHotDogSimples = R${precoHotDogSimples:.2f}") 
print(f"precoHotDogDuplo = R${precoHotDogDuplo:.2f}") 
print(f"precoRefrigerante = R${precoRefrigerante:.2f}")    
quantidadeHotDogSimples = int(input("Quantos itens de Hot Dog Simples você deseja comprar? "))
quantidadeHotDogDuplo = int(input("Quantos itens de Hot dog Duplo você deseja comprar? "))
quantidadeRefrigerante = int(input("Quantos itens de Refrigerante você deseja comprar? "))


valorTotal = quantidadeHotDogSimples * precoHotDogSimples
valorTotal += quantidadeHotDogDuplo * precoHotDogDuplo
valorTotal += quantidadeRefrigerante * precoRefrigerante

print(f"Você escolheu {quantidadeHotDogSimples} hot dos(s), {quantidadeHotDogDuplo} hot dos(s), {quantidadeRefrigerante} hot dos(s). O total a pagar é: R$ {valorTotal:.2f}")


