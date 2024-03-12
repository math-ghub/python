def aumentar(n, val, format):
    if format:
        return moeda(n + (n * val / 100))
    return n + (n * val / 100)

def diminuir(n, val, format):
    if format:
        return moeda(n - (n * val / 100))
    return n - (n * val / 100)

def dobro(n, format):
    if format:
        return moeda(n * 2)
    return n * 2

def metade(n, format):
    if format:
        return moeda(n / 2)
    return n / 2

def moeda(n):
    return f"R${n:.2f}"

def resumo(n, aum, red):
    print("-" * 30)
    print(f"{"Resumo do Valor":^30}")
    print("-" * 30)
    print(f"{"Preço analisado:":<22}{moeda(n)}".replace(".",","))
    print(f"{"Dobro do preço:":<22}{dobro(n, True)}".replace(".",","))
    print(f"{"Metade do preço:":<22}{metade(n, True)}".replace(".",","))
    print(f"{f"{aum}% de aumento:":<22}{aumentar(n, aum, True)}".replace(".",","))
    print(f"{f"{red}% de redução:":<22}{diminuir(n, red, True)}".replace(".",","))
    print("-" * 30)