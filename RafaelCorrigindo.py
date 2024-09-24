funcionarios = []
maior = 0

for i in range(4):
    d ={}
    d["nome"] = input("Digite um nome: ")
    d["funcao"] = input("Digite ums função: ")
    d["salario"] = float(input("Digite um salario: "))
    funcionarios.append(d)

    if d["salario"] > maior:
        maior = d["salario"]

for pessoa in funcionarios:
    if pessoa["salario"] == maior:
        print(f"Pessoa com maior salario é {pessoa["nome"]}")

    