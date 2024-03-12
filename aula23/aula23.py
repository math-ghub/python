# def leiaInt():
#     inp = 0
#     while True:
#         try:
#             inp = int(input("Digite um Inteiro: "))
#         except (TypeError, ValueError):
#             print("Valor invalido. Tente novamente.")
#             continue
#         else:
#             return inp

# def leiaFloat():
#     inp = 0
#     while True:
#         try:
#             inp = float(input("Digite um Real: "))
#         except:
#             print("Valor invalido. Tente novamente.")
#             continue
#         else:
#             return inp

# inteiro = leiaInt() or 0
# real = leiaFloat() or 0

# print(f"Número inteiro: {inteiro}\nNúmero real: {real}")

# import urllib
# import urllib.request

# try:
#     site = urllib.request.urlopen("https://www.youtube.com/watch?v=8jAykqxIeqw")
# except:
#     print("Deu erro")
# else:
#     print("Tudo ok")

import library.estilos as style, library.arquivos as arquivo

arq = "cursoemvideo.txt"

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

Ativado = True
style.mark("MENU PRINCIPAL")
style.add("Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do Sistema")
style.mark()

while Ativado:
    selected = input("\033[33mSua Opção:\033[m ")

    if selected == "1":
        arquivo.lerArquivo(arq)
        style.mark()
    elif selected == "2":
        style.mark("NOVO CADASTRO")
        nome = input("Nome: ")
        idade = input("Idade: ")
        arquivo.cadastrarPessoa(arq, nome, idade)
    elif selected == "3":
        style.mark("Saindo do sistema, até logo!")
        break
    else:
        print("\033[31mDigite uma opção valida!\033[m")