def leiaDinheiro(n):
    inp = input(n).replace(",",".")
    while not inp.isnumeric() or not inp.isdecimal():
        inp = input(n).replace(",",".")
    return float(inp)