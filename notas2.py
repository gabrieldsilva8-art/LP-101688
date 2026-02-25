import os

os.system("cls")




nome = input("digite seu nome: ")
nota1 = int(input("digite sua primeira nota: "))
nota2 = int(input("digite sua segunda nota: "))

media = (nota1 + nota2) /2

if media >= 9:
    print("aprovado(A)")
if 7.5 <= media <= 9:
    print("aprovado(B)")
if 6 <= media <= 7.5:
    print("reprovado(C)")
if 4 <= media <= 6:
    print("reprovado(D)")
if media <= 4:
    print("reprovado(E)")