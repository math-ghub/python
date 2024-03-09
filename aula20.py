# area = lambda a, b : a * b

# print(f"A aréa do terreno {10}x{7} é de {area(10, 7):.1f}m².")

# def escreva(txt):
#     print("~" * len(txt) + "~~~~")
#     print(f"{txt:^{len(txt) + 4}}")
#     print("~" * len(txt) + "~~~~")

# escreva("Teste de frase alo")

# def contador(i, f, p):
#     if i < f:
#         list(print(x) for x in range(i,f + 1, p))
#     else:
#         list(print(x) for x in range(i, f - 1, -p))

# contador(90,40,10)

# def Maior(*args):
#     lista = [*args]
#     print(lista, end=" = ")
#     print(len(lista))
#     lista.sort()
#     print(lista[-1])

# Maior(1,5,76,4)

numeros = []
from random import randint

def sorteia():
    for x in range(0,5):
        numeros.append(randint(0,10))
def somaPar():
    soma = sum(x for x in numeros if x % 2 == 0)
    print(soma)
sorteia()
print(numeros)
somaPar()
# import pyautogui
# from time import sleep

# sleep(5)
# for i in range(5):
#     pyautogui.typewrite("teste")
#     pyautogui.hotkey("enter")
#     sleep(0.1)