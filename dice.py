import random

def rolar_dado(lados):
    return random.randint(1, lados)

while True:
    print("\n=== Simulador de Dados ===")
    print("1 - D6")
    print("2 - D10")
    print("3 - D20")
    print("4 - Sair")

    escolha = input("Escolhe uma opção: ")

    if escolha == "1":
        print(f"Você rolou um D6 e tirou {rolar_dado(6)}")
    elif escolha == "2":
        print(f"Você rolou um D10 e tirou {rolar_dado(10)}")
    elif escolha == "3":
        print(f"Você rolou um D20 e tirou {rolar_dado(20)}")
    elif escolha == "4":
        print("Você saiu")
        break
    else:
        print("Opção inválida, tenta de novo.")
