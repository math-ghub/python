extenso = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")

val = input("Digite um número entre 0 e 20: ")
while not val.isnumeric():
    val = input("Digite um número entre 0 e 20: ")

print(f"Você digitou o número: {extenso[int(val)]}")