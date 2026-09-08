import json
 
with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
 
print(dados)
print(dados['nome'])
 
#convertendo json em str
texto = json.dumps(dados, indent=4, ensure_ascii=False)
print(texto)

#convertendo o str em json
pessoaNova = '{"priimeironome": "Vânia","idade": 50}'

dadosNovo = json.loads(pessoaNova)
print(dadosNovo)

#autalizando
with open('dados.json', 'r', encoding='utf-8') as arquivo:
          dados = json.load(arquivo)

dados['idade'] = 36 # alteração
dados['redesocial'] = "@kau.tech" #adicionando dado
del dados['telefone']

#write = escrever
with open('dados.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

print("Dado adicionado com sucesso!")
print("Telefone removido com sucesso!")
print(dados)
