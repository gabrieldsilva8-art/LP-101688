import os

os.system("cls")

print(" _ Solicitando dados _")
ano_nascimento = int(input("Digite seu ano idade"))
sexo = input("Digite seu sexo de registro: ").lower

idade = 2026 - ano_nascimento

idade_obrigatorio = idade >=18
sexo_obrigatorio = "masculino"

if idade_obrigatorio and sexo_obrigatorio:
    prin
