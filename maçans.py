import os

os.system("cls")


maçãs = int(input("digite a quantidade de maçãs: "))

if maçãs < 12:
    print("1,30 cada")
    produto = maçãs * 1,30
    
if maçãs >= 12:
    print("1,00 cada")
    produto = maçãs * 1,00
        
print("valor da compra: ", produto)
    