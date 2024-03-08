# aluno = []

# nome = input("Nome do aluno: ")
# media = float(input(f"Média de {nome}: "))

# aluno.append(nome)
# aluno.append(media)

# print(list(x for x in aluno))
# if aluno[1] > 6:
#     print("aprovado")
# else:
#     print("reprovado")

from random import randint

jogadores = {}
for i in range(0,4):
    jogadores[f"jogador {i + 1}"] = randint(1,6)

ranking = {}

ranking = sorted(jogadores.items(), key=lambda item: item[1],reverse=True)
print(ranking)