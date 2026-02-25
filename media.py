primeiro_numero = int (input("Digite o seu numero"))
segundo_numero = int (input("Digite seu numero"))

produto = (primeiro_numero * segundo_numero)

media = (primeiro_numero + segundo_numero)

soma = (primeiro_numero + segundo_numero) /2

if primeiro_numero < segundo_numero:
    print("primeiro é menor")
    print("segundo é maior")
if primeiro_numero > segundo_numero:
    print("primeiro é menor")
    print("segundo é maior")

if primeiro_numero == segundo_numero:
    print("sao iguais")
else: 
    print("nao sao iguais")
    
print("soma ", soma)
print("media ", media)
print("produto ", produto)