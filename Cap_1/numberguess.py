###############################################################################
##########        Universidade Federal do Rio Grande do Norte        ##########
##########            Centro de Ensino Superior do Seridó            ##########
##########          Departamento de Computação e Tecnologia          ##########
##########        Flavius Gorgônio - flavius.gorgonio@ufrn.br        ##########
###############################################################################

import random

def main():
    menor = int(input("Informe o limite inferior: "))
    maior = int(input("Informe o limite superior: "))
    numero = random.randint(menor, maior)
    cont = 0

    while True:
        cont += 1
        palpite = int(input("Informe seu palpite: "))
        if palpite < numero:
            print("Sobe!")
        elif palpite > numero:
            print("Desce!")
        else:
            print("Você acertou em", cont, "tentativas!")
            break

if __name__ == "__main__":
    main()
