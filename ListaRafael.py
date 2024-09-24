# conta = {"num":"", "saldo": "", "nome": ""}
# conta["num"] = int(input("Digite o número de sua conta "))
# conta["saldo"] = int(input("Digite o saldo de sua conta "))
# conta["nome"] = input("Digite o seu nome")
# print(conta)

#Faça um programa que armazene as informaçoes de 4 funcionários em uma lista. Cada funcionario terá as seguintes informações: Nome, função e salário. Ao final, o programa deve imprimir os funcionários da empresa e informar qual é o funcionário com maior salário.

e = []
maior_salario = 0
nome_maior_salario = "" 
for i in range(4):
    nome = input("Digite seu nome: ")
    funcao = input("Digite sua função ")
    salario = float(input("Digite seu salário "))
    e.append({"nome": nome, "funcao": funcao, "salario": salario})

for i in e:
    print(i)

for i in e:
    salario = i["salario"]
    if salario > maior_salario:
        maior_salario = salario 
        nome_maior_salario = i["nome"]

print(f"{maior_salario} e {nome_maior_salario}")
    



