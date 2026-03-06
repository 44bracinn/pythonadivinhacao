import adivinhacao
import forca

print("\n")
print("Escolha seu Jogo")
print("\n")

print("(1) Adivinhação (2) Forca")

opcao_jogo = int(input("Escolha seu Jogo: "))

if(opcao_jogo == 1):
    print("Escolhendo Adivinhação")
    adivinhacao.jogar_adivinhacao()
elif(opcao_jogo == 2):
    print("Escolhendo Forca")
    forca.jogar_forca()