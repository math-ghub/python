import library.estilos as style

def arquivoExiste(name):
    try:
        a = open(name, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(name):
    try:
        a = open(name, "wt+")
        a.close()
    except:
        print("Houve um erro na criação do arquivo!")
    else:
        print(f"Arquivo {name} criado com sucesso!")

def lerArquivo(name):
    try:
        a = open(name, "rt")
    except:
        print("Erro ao ler o arquivo!")
    else:
        style.mark("PESSOAS CADASTRADAS")
        for linha in a:
            dados = linha.split(";")
            dados[1] = dados[1].replace("\n","")
            print(f"{dados[0]:<32}{dados[1]} anos")
    finally:
        a.close()

def cadastrarPessoa(arq,nome="desconhecido",idade=0):
    try:
        a = open(arq, "at")
    except:
        print("Erro")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um erro na hora de escrever os dados!")
        else:
            print(f"Novo registro de {nome} adicionado.")
            a.close()