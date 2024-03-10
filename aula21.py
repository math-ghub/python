# from datetime import date

# def voto(nasc):
#     idade = date.today().year - nasc
#     valor = "obrigatório" if idade >= 18 and idade < 65 else "opcional" if idade > 15 and idade < 18 or idade >= 65 else "negado"
#     return valor, idade
# nascimento = 1950

# print(f"Paulo tem o seu direito a voto {voto(nascimento)[0]}, pois tem {voto(nascimento)[1]} anos.")

def fatorial(n, show=False):
    fatList = ""
    result = val = n
    while val > 1:
        fatList += str(val) + " x "
        result *= val - 1
        val -= 1
    fatList += "1 = " if len(fatList) > 2 and fatList[-2] == "x" else ""
    if show:
        return fatList + str(result)
    return result

print(fatorial(100, True))