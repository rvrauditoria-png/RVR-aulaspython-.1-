pessoa = {
        "nome": "Ana",
             "idade": 30
             }

print(pessoa)
print(pessoa["nome"])

#alterando valores
pessoa["idade"] = 31
print(pessoa)

#adicionando novo dado
pessoa["cidade"] = "São Paulo"
print(pessoa)

#adicionando novo dado
pessoa["estado"] = "SP"
print(pessoa)

#removendo chave
del pessoa ["idade"]
print(pessoa)

#removendo apenas valor
pessoa["estado"] = None
print(pessoa)

pessoasNovas = {
    1: { 
       'nome': "Vânia", 
        "idade": 50
    },
    2: {
        "nome": "Carlos", "idade": 35
    }
}

#Exibindo na tela
print(pessoasNovas)

#Excluindo apenas o Carlos (ID 2)
del pessoasNovas [2]
print(pessoasNovas)


#ver chaves
print(pessoasNovas.keys())

#ver valores
print(pessoasNovas.values())

#ver chaves
print(pessoa.keys())

#ver valores
print(pessoa.values())

#novo dicionario
paes = {
    "nome1": "Brioche",
    "tamanho1": 20,
    "nome2": "Francês",
    "tamanho2" : 15
}

print(paes)
print(paes.keys())
print(paes.values())

#ver chave e valor
print(paes.items())

#verificar se chave existe
print("nome1" in paes)
print("nome3" in paes)

#usar get
print(paes.get("nome1"))

#percorrer
for chave, valor in paes.items():
    print(chave, ":", valor)


bebidas = {
    10: {
        "nome": "Coca-Cola",
                "volume": 350
        },
    20: {
            "nome": "Suco de laranja",
            "volume": 1000
    }
}
    
print(bebidas)
print(bebidas.keys())
print(bebidas.values())



