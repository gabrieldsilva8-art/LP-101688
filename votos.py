idade = int(input ("Digite sua idade"))

if idade < 16:
    print("nao pode vota")
if 16 <= idade <= 17:
    print("voto opcional")
if 18 <= idade <= 65:
    print("voto obrigatorio")
if 65 <= idade:
    print("nao é obrigado")