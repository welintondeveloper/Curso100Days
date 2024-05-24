#__________________________________________ Manipulando Strings ___________________________________________________#

#a varias maneiras de usar símbolos ou caracteres especiais dentro das strings sem que o compilador se confunda
print("A 'single quote' inside a double quote")#basta usar aspas diferentes na abertura e fechamento da string
print('A "double quote" inside a single quote')#pode ser com aspas duplas ou simples mais tem que diferenciar
print("Alternatively you can just \"escape\" the quote")
#ou usar barra invertida como na linha acima, o compilador entenderá que trata-se de um caractere e não um comando

#____________________________________ Manipulando Strings quebra de linha _________________________________________#
#maneira comun de imprimir varias linhas usando a função print para imprimir
print("oi qual seu nome")
print("tudo bem como você")
print("também estou bem obrigado")
#maneira mais facil de quebrar linha sem precisar criar varias funçoes de print toda ves
print(" oi qual seu nome\n tudo bem como você\n também estou bem obrigado")

#______________________________________ Manipulando Strings concatenar ____________________________________________#

#aqui somente juntamos as duas palavras sem colocar nenhum espaço entre elas po mais
# que coloquemos enpaço entre as strings o compilador só irá juntas as duas palavras na mesma linha
print("Olá" +     "welinton")
#agora quando colocamos um espaço dentro das aspas ai sim o compilador irá entender que queremos um espaço ali
print("Olá "+"welinton")
#na linha abaixo a outra maneira de colocarmos um espaço entre as duas strings usando uma estringue com espaço
print("Olá"+" "+"Welinton")
#______________________________________ Manipulando Strings identação _____________________________________________#

#    print("Olá mundo") este codigo nos retornará um erro pois ele esta com um espaço antes do código
print("Olá mundo") #a meneira correta pois o compilador python entendo que toda identaçao tem algum significado

# sempre que encontrar um erro pode copiar o codigo do erro e jogar no google ou diretamente no stackoverflow
# possivelmente alguem irá te ajudar com o erro no seu codigo
# utilizar uma plataforma mais moderna como o vizual studio code ou o pycharm ajuda a evitar erros


