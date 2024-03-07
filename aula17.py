# grupo = []
# individuo = []

# for r in range(0,5):
#     individuo.append(input("Nome da pessoa: "))
#     individuo.append(int(input("Peso da pessoa: ")))
#     grupo.append(individuo[:])
#     individuo.clear()

# pesosOrganizados = []
# for i in grupo:
#     pesosOrganizados.append(i[1])

# pesosOrganizados.sort()

# maiorPeso = ""
# menorPeso = ""

# for i in grupo:
#     if i[1] == pesosOrganizados[-1]:
#         maiorPeso += f"[{i[0]}] "
#     if i[1] == pesosOrganizados[0]:
#         menorPeso += f"[{i[0]}] "

# print(f"Existem {len(grupo)} pessoas dentro do grupo.")
# print(f"O maior peso foi {pesosOrganizados[-1]}. Peso de {maiorPeso}")
# print(f"O menor peso foi {pesosOrganizados[0]}. Peso de {menorPeso}")

# valores = [[],[]]

# for i in range(0,7):
#     localVal = int(input("Coloque um valor: "))
#     if localVal % 2 == 0:
#         valores[0].append(localVal)
#     else:
#         valores[1].append(localVal)

# valores[0].sort()
# valores[1].sort()

# print(valores)

# lista = [[],[],[]]
# somapares = 0
# soma3Coluna = 0
# maiorValor2Colun = 0

# for i in lista:
#     while len(i) < 3:
#         i.append(int(input(f"o valor: ")))

# for matriz in lista:
#     print(matriz)
#     for numb in matriz:
#         if numb % 2 == 0:
#             somapares += numb
#         if matriz.index(numb) == 2:
#             soma3Coluna += numb
#         if lista.index(matriz) == 1:
#             if numb > maiorValor2Colun:
#                 maiorValor2Colun = numb

# print(somapares)
# print(soma3Coluna)
# print(maiorValor2Colun)

# from random import randint as r
# lista = []

# rodadas = int(input("Quantos jogos vai participar? "))

# for i in range(0,rodadas):
#     numerosUsados = []
#     palpite = []
#     for num in range(0,6):
#         numeroAleatorio = r(1,60)
#         while numeroAleatorio in numerosUsados:
#             numeroAleatorio = r(1,60)
#         numerosUsados.append(numeroAleatorio)
#         palpite.append(numeroAleatorio)
#     palpite.sort()
#     lista.append(palpite[:])
#     palpite.clear()
    
# print(f"{"Sorteando":=^40}")
# for i,v in enumerate(lista):
#     print(f"Jogo {i + 1}: {v}")

# boletim = []
# adicionando = True

# while adicionando:
#     nomeAluno = input("Nome: ")
#     Nota1 = float(input("Nota1: "))
#     Nota2 = float(input("Nota2: "))

#     boletim.append([nomeAluno, [Nota1, Nota2]])
#     resposta = input("Quer continuar? [S/N] ")
#     if resposta in "Nn":
#         adicionando = False
# print("-=" * 40)
# print(f"{"Boletim":^30}")
# print(f"{"No. NOME":<20}","MÉDIA")
# print("-" * 30)
# for i, v in enumerate(boletim):
#     print(f"{i}   {v[0]:<17} {(v[1][0] + v[1][1]) / 2}")
# print("-" * 30)

# pesquisando = 0

# while pesquisando != 999:
#     val = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
#     pesquisando = val

#     if val != 999:
#         print(f"As notas de {boletim[val][0]} são {boletim[val][1]}")
#         print("-" * 35)