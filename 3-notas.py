lista = []
contador = 1

while contador <=4:
    nota = float(input("Digite a " +str(contador) + "° nota"))
    lista.append(nota)
    contador = contador + 1

##print(lista)

media = (lista [0] + lista [1] + lista [2] + lista [3])/4

print (media)

if media > 7:
    print("Sua média é" + str(media) + ". Você está aprovado!")
elif (media < 7) and (media > 5.5):
    print("Sua média é" +str(media) + ". Você está de recuperação!")
else:
    print("Sua média é" +str(media) + ". Você está reprovado!")