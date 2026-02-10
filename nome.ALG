Algoritmo "semnome"

Var
// Seção de Declarações das variáveis 
   primeira_nota: real
   segunda_nota: real
   soma: real
   media: real
   resultado: caractere
   nome: caractere
   idade: inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
 //ENTRADA DE DADOS
 
    escreval("Digite seu nome")
    leia(nome)
    
    escreval("Digite sua idade")
    leia(idade)
    
    
   escreva("Digite a primeira nota: ")
   leia(primeira_nota)
   
   escreva("Digite a segunda nota: ")
   leia(segunda_nota)
   
   //PROCESSAMENTO
   soma <- primeira_nota + segunda_nota
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