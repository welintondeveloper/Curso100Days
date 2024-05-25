#__________________________________________ Manipulando Strings ___________________________________________________#

# á várias maneiras de usar símbolos ou caracteres especiais dentro das strings sem que o compilador se confunda
# basta usar aspas diferentes na abertura e fechamento da string
print("A 'single quote' inside a double quote")
# pode ser com aspas duplas ou simples mais tem que diferenciar
print('A "double quote" inside a single quote')
# ou usar barra invertida como na linha acima, o compilador entenderá que trata-se de um caractere e não um comando
print("Alternatively you can just \"escape\" the quote")


#____________________________________ Manipulando Strings quebra de linha _________________________________________#
# maneira comun de imprimir varias linhas usando a função print para imprimir
print("oi qual seu nome")
print("tudo bem como você")
print("também estou bem obrigado")

# maneira mais facil de quebrar linha sem precisar criar varias funçoes de print toda ves
print(" oi qual seu nome\n tudo bem como você\n também estou bem obrigado")

#______________________________________ Manipulando Strings concatenar ____________________________________________#

# aqui somente juntamos as duas palavras sem colocar nenhum espaço entre elas po mais
# que coloquemos enpaço entre as strings o compilador só irá juntas as duas palavras na mesma linha
print("Olá" +     "welinton")
# agora quando colocamos um espaço dentro das aspas ai sim o compilador irá entender que queremos um espaço ali
print("Olá "+"welinton")
# na linha abaixo a outra maneira de colocarmos um espaço entre as duas strings usando uma estringue com espaço
print("Olá"+" "+"Welinton")
#______________________________________ Manipulando Strings identação _____________________________________________#

#este codigo nos retornará um erro pois ele esta com um espaço antes do código
#    print("Olá mundo") 
# a meneira correta pois o compilador python entendo que toda identaçao tem algum significado
print("Olá mundo") 

# sempre que encontrar um erro pode copiar o codigo do erro e jogar no google ou diretamente no stackoverflow
# possivelmente alguem irá te ajudar com o erro no seu codigo
# utilizar uma plataforma mais moderna como o vizual studio code ou o pycharm ajuda a evitar erros

#_________________________________________ Manipulando Strings input ______________________________________________#
# depois que a funçao imput capturar o seu nome ela substituirá a string pelo dado que foi capturado
# entao imprimirá apenas o nome
print(input("olá"+" Qual é o seu nome"))

# já neste caso imprimirá Olá qual o seu nome depois substitui a string anterior pela nova string que foi capturada
# tambem irá concatenar com a frase "Olá seja bem vindo" com a nova string seu nome no caso
print("Olá seja bem vindo "+input("Olá, Qual o seu nome\n"))

# Obs existe um programa gratuito que e muito prático para quem está aprendendo chama-se thonny 
# ele consegue fazer um debug completo e mostrar passo a passo a execução do código

#______________________________________ Manipulando Strings função len ____________________________________________#

contando as letras incluindo os espaços da string a função len conta quantas letras tem em uma string exemplo:
numeroDeCaracteres = len("welinton de sousa  ")
print(numeroDeCaracteres)
numeroDeCaracteres = len("welinton  ")
print(numeroDeCaracteres)
numeroDeLetras = len("welinton ")
print(numeroDeLetras)
numeroDeLetras = len("welinton")
print(numeroDeLetras)

# agora para pegarmos todas as entrada do usuario e saber quantas letras contem a string, temos este exemplo
# para lermos esta linha de codigo entenda que tudo que está dentro das primeiras aspas e executado primeiro
# ou seja devemos ler os codigos de dentro para fora no exemplo abaixo tem a seguinte ordem 
# 1-imprime na tela ("escreva qualquer palavra ou fraze para saber quantas letras tem\n") chaves mais interna
# 2-coleta os dados do usuario (input("escreva qualquer palavra ou fraze para saber quantas letras tem\n"))
# 3-usa a função len para contar os caracteres da palavra ou frase inserida
# 4-imprime a quantidade de palavras na tela que e o resultado da função len
print(len(input("escreva qualquer palavra ou fraze para saber quantas letras tem\n")))

