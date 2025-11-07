import random
import time

print("$$-Bet-$$")
saldo = 100

while True:
    print(f"\n Seu saldo atual: R${saldo}")
    try:
        valor = int(input("Quanto quer apostar? "))
        if valor <= 0 or valor > saldo:
            print("Valor inválido!")
            continue

        escolha = int(input("Escolhe um número de 1 a 6: "))
        if escolha < 1 or escolha > 6:
            print("Só vale número de 1 a 6")
            continue

        print("\n Rolando o dado...")
        time.sleep(1.5)
        dado = random.randint(1, 6)
        print(f" O dado caiu em {dado}!")

        if escolha == dado:
            ganho = valor * 5
            saldo += ganho
            print(f" ACERTOU! Ganhou R${ganho}!")
        else:
            saldo -= valor
            print(" Errou! perdeu a aposta...")

        if saldo <= 0:
            print("\n Quebrou! Fim de jogo ")
            break

        again = input("\n Quer jogar de novo? (s/n) ").lower()
        if again != "s":
            print("\n Obrigado por jogar! ")
            break

    except ValueError:
        print(" Digita um número válido!")
