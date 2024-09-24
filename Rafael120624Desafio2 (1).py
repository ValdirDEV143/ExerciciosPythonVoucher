# Faça um algoritmo onde vc tem uma lista de números inteiros e que tenha uma função onde verifica 
# se o número é par ou impar e some eles em variáveis distintas mostre na tela. 

def is_even(number):
    """
    Verifica se um número é par.
    """
    return number % 2 == 0

def sum_even_and_odd(numbers):
    """
    Soma os números pares e ímpares de uma lista.
    """
    even_sum = 0
    odd_sum = 0

    for num in numbers:
        if is_even(num):
            even_sum += num
        else:
            odd_sum += num

    return even_sum, odd_sum

# Exemplo de lista de números
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calcula as somas
soma_pares, soma_impares = sum_even_and_odd(lista_numeros)

# Exibe os resultados
print(f"Soma dos números pares: {soma_pares}")
print(f"Soma dos números ímpares: {soma_impares}")