# numb = int(input("Digite um número: "))
# soma = 0
# valDigitados = 0

# while numb != 999:
#     soma += numb
#     valDigitados += 1
#     numb = int(input("Digite um número: "))

# print(f"{valDigitados} valores foram digitados, resultando em: {soma}.")

# numb = int(input("Digite um número positivo para saber sua tabuada: "))

# while numb >= 0:
#     print("=" * 20)
#     for i in range(1,11):
#         print(f"{numb} x {i} = {numb * i}.")
#     print("=" * 20)
#     numb = int(input("Digite um número positivo para saber sua tabuada: "))

# from random import randint
# jogadorVivo = True
# vitorias = 0

# while jogadorVivo:
#     timePlayer = input("Escolha par ou ímpar: ")
#     timePc = "par" if timePlayer == "impar" else "impar"

#     jogadaPlayer = int(input("Escolha um número: "))
#     jogadaPc = randint(0,10)

#     soma = jogadaPlayer + jogadaPc

#     print("=" * 20)
#     print(f"Você escolheu: {jogadaPlayer}")
#     print(f"O computador escolheu: {jogadaPc}")
#     print(f"{jogadaPlayer} + {jogadaPc} = {soma} = {"par" if soma % 2 == 0 else "ímpar"}")
#     print("=" * 20)

#     if soma % 2 == 0:
#         if timePlayer == "par":
#             vitorias += 1
#         else:
#             jogadorVivo = False
#             break
#     else:
#         if timePlayer == "impar":
#             vitorias += 1
#         else:
#             jogadorVivo = False
#             break
#     print("Parabéns por vencer esta rodada!")

# print("Não foi dessa vez.")
# print(f"Você venceu {vitorias} partidas, parabéns!")

# cadastrando = True
# pessoas = []

# while cadastrando:
#     idade = input("Diga uma idade: ")
#     isaNumber = idade.isnumeric()
#     while not isaNumber:
#         idade = input("Diga uma idade: ")
#         isaNumber = idade.isnumeric()
#     sexo = input("Diga um sexo: ")
#     while not sexo in "MmFf":
#         sexo = input("Diga um sexo: ")
#     pessoas.append((f"idade-{idade}",f"sexo-{sexo}"))
#     print("Cadastrado com sucesso!")
#     resposta = input("Deseja continuar? (S/N) ")
#     while not resposta in "SsNn":
#         resposta = input("Deseja continuar? (S/N) ")
#     if resposta in "Nn":
#         cadastrando = False

# maisDe18 = 0
# homens = 0
# mulheresMenosDe20 = 0

# for i in pessoas:
#     idade = i[0][6:]
#     sexo = i[1][5:].upper()
#     if int(idade) > 18:
#         maisDe18 += 1
#     if sexo == "M":
#         homens += 1
#     else:
#         if int(idade) < 20:
#             mulheresMenosDe20 += 1

# print(f"{maisDe18} pessoas tem mais de 18 anos.")
# print(f"Existem {homens} homens.")
# print(f"{mulheresMenosDe20} mulheres possuem menos de 20 anos.")

# comprando = True
# produtos = []

# while comprando:
#     produtoNome = input("Nome do Produto: ")
#     produtoValor = input("Preço: R$")
    
#     while not produtoValor.isnumeric():
#         produtoValor = input("Preço: R$")
#     produtos.append((produtoNome,produtoValor))

#     resposta = input("Quer continuar? [S/N] ")
#     while not resposta in "SsNn":
#         resposta = input("Quer continuar? [S/N] ")
#     if resposta in "Nn":
#         comprando = False

# print(f"{"-":-^10}FIM DO PROGRAMA{"-":-^10}")

# totalCompras = 0
# produtosAcima1000 = 0
# produtoMaisBarato = ""
# produtoMaisBaratoValor = 0

# for i in produtos:
#     nome = i[0]
#     valor = int(i[1])
#     totalCompras += valor

#     if valor > 1000:
#         produtosAcima1000 += 1
#     if produtoMaisBarato == "":
#         produtoMaisBarato = nome
#         produtoMaisBaratoValor = valor
#     elif valor < produtoMaisBaratoValor:
#         produtoMaisBarato = nome
#         produtoMaisBaratoValor = valor

# print(f"O total da compra foi R${totalCompras}")
# print(f"Temos {produtosAcima1000} produtos custando mais de R$1000")
# print(f"O produto mais barato foi {produtoMaisBarato} que custa R${produtoMaisBaratoValor}")

valorSacar = input("Que valor você quer sacar? R$")
valoraSerEntregue = 0

cedulasDisponiveis = [50,20,10,1]
cedulasUtilizadas = {
    50: 0,
    20: 0,
    10: 0,
    1: 0
}

while not valorSacar.isnumeric():
    valorSacar = input("Que valor você quer sacar? R$")


for i in cedulasDisponiveis:
    while valoraSerEntregue + i <= int(valorSacar):
        valoraSerEntregue += i
        cedulasUtilizadas[i] += 1

for c in cedulasUtilizadas:
    if cedulasUtilizadas[c] > 0:
        print(f"Total de {cedulasUtilizadas[c]} cédulas de {c}")
print(valoraSerEntregue)