Algoritmo "semnome"

Var
// Seção de Declarações das variáveis 
//ENTRADA DE DADOS
  primeira_nota: real
  segunda_nota: real
  terceira_nota: real
  soma: real
  media: real
  resultado: caractere
      
      



Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
 escreva("Digite a primeira nota: ")
   leia(primeira_nota)

   escreva("Digite a segunda nota: ")
   leia(segunda_nota)

   escreva("Digite a terceira nota: ")
   leia(terceira_nota)

   //PROCESSAMENTO

   soma <- primeira_nota + segunda_nota + terceira_nota
   media <- soma / 2

   se media >=7 entao
      resultado <- "aprovado"
     senao
      
      resultado <- "reprovado"
   fimse
   
   //SAIDA
   
   
   escreval
   escreval("Media: ", media)
   escreval("Resultado: ", resultado)
   
   
   

Fimalgoritmo