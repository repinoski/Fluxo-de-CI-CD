import random

print('╔════════════════════╗')
print('  Bem vindo ao jogo!')
print('╚════════════════════╝')


def descubra():
    num= random.randint(1,100)
    while True:
        tentativa= int(input('Tente acertar o número: '))

        if tentativa == num:
            print("Parabéns, você acertou o número")
            break
        elif tentativa > num:
            print("Seu palpite foi muito alto")
        elif tentativa < num:
            print("Seu palpite foi muito baixo")
        else:
            print("Você errou o número, tente mais uma vez")

if __name__ == '__main__':
    descubra()