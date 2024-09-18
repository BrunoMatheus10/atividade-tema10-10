# Criar um dicionário para um determinado animal de estimação
animal_estimacao = {
    "Nome": "Rex",
    "Espécie": "Cachorro",
    "Raça": "Labrador",
    "Idade": 5,
    "Peso": 30.5,
    "Cor": "Marrom"
}

# Exibir as informações armazenadas no dicionário
print("Informações do animal de estimação:")
for chave, valor in animal_estimacao.items():
    print(chave,":", valor)
