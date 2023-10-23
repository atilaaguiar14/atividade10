# faça um algoritimo que receba a velocidade de Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida
velocidade = int(input("digite a velocidade em km/h: "))
if velocidade> 60:
    print("você foi multado! o limite é 60km/h")
    multa = 60*7
    print("a multa custara R${:.2f}".format(multa) )
    