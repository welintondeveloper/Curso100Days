# quantas semanas de vida ainda lhe resta?

# pega a idade atual através de input e converte ela em int
IdadeAtual = int(input("qual sua idade?"))
# pega uma estimativa de 90 anos e subtrai pela IdadeAtual
Restante = 90 - IdadeAtual
# segundo cálculos cada ano tem 52 semanas então sendo assim
# pega o restante multiplica pela quantidade de semanas que tem um ano
# e guarda na variavel SemanaDeVida
SemanaDeVida = Restante * 52
# imprime utilizando f-string para concatenar texto com a variável SemanaDeVida
print(f"You have {SemanaDeVida} weeks left.")