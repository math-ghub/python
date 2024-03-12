def mark(text = ""):
    print("-" * 40)
    if text != "":
        print(f"{text:^40}")
        print("-" * 40)

def add(*strings):
    for i,v in enumerate(strings):
        print(f"\033[1;33m{i + 1}\033[m - \033[1;34m{v}\033[m")