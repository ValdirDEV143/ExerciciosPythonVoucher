#Desenvolva um programa, utilizando dicionários, que solicite para o usuário inserir quatro notas e mostre na tela as notas e a média entre elas.

# Solicita ao usuário para inserir as quatro notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Cria um dicionário com as notas
notas = {
    "Nota 1": nota1,
    "Nota 2": nota2,
    "Nota 3": nota3,
    "Nota 4": nota4
}

# Calcula a média das notas
media = sum(notas.values()) / len(notas)

# Exibe as notas e a média
print("\nNotas inseridas:")
for chave, valor in notas.items():
    print(f"{chave}: {valor:.2f}")

print(f"Média: {media:.2f}")