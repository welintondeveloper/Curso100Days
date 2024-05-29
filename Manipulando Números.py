# para arredondar um numero quebrado basta usar a função round() ex: 
# se o numero for 2.6 vai arredondar para 3
# se for 2.3 vai arredondar para 2
# se quiser que arredondar o número com apenas uma casa 
# basta colocar round e entre parênteses o numero
calculo1 = round(2.6)
print(calculo1)
calculo2 = round(2.4)
print(calculo2)

# também é possível acrescentar a quantidade de casas decimais você quer que arredonde Ex:
# com nenhuma casa
calculo3 = round(8/3, 0)
print(calculo3)
# com uma casa
calculo4 = round(8/3, 1)
print(calculo4)
# com duas
calculo5 = round(2.689, 2)
print(calculo5)
# com três casas
calculo6 = round(8.59699999, 3)
print(calculo6)

# em python todos números que são divididos, automaticamente saem com ponto flutuante após a divisão
# caso você não queira isso basta usar // para fazer uma divisão veja o resultado abaixo
calculo7 = (16//4)
print(calculo7)
print((10//3))

# divisão normal
calculo8 = 3/2
print(calculo8) 
# outra divisão
OutroCalculo = 3//2
print(OutroCalculo)
# por mais que não tenha resto da divisão o numero sempre será um float
print(type(calculo8))
# se usarmos // ao invés de / e conferir com type veremos que agora 
# virou um numero inteiro
print(type(OutroCalculo))

# para imprimir números junto com texto e outros tipos podemos usar f-string
# é bem mais prático do que converter todos os tipos em string 
# para poder imprimir em um único print
# Ex:

# apesar de estarmos convertendo os dados para int o valor deste calculo será um float 
# porque estamos dividindo e sempre que dividimos em python o resultado é um float
a = int("5") / int(2.7)
print(type(a))
print(a)
