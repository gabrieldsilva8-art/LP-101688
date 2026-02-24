primeira_nota = float (input('Digite sua primeira nota'))

segunda_nota = float (input('Digite sua segunda nota'))

terceira_nota = float (input('Digite sua terceira nota'))

media = (primeira_nota + segunda_nota + terceira_nota)  /2

if media <= 7: 
    print("aprovado")
else:
    print("reprovado")
    
print ("media", media)
