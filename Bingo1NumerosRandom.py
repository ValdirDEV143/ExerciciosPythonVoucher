# Desenvolvendo um Sistema de Bingo em Python
# Objetivo
# Desenvolver dois programas em Python para um jogo de Bingo. Um programa será responsável por sortear os números 
# aleatórios, e o outro criará cartelas de Bingo, permitirá marcar os números sorteados e indicará quando um jogador completar um Bingo.
# Requisitos: Programa 1: Sorteio de Números
# •	Descrição: Este programa será responsável por sortear números aleatórios entre 1 e 75.
# •	Funcionalidades:
# 1.	Sortear um número aleatório não repetido de 1 a 75.
# 2.	Exibir o número sorteado.
# 3.	Armazenar os números sorteados para evitar repetições.
# 4.	Continuar sorteando números até que todos os 75 números tenham sido sorteados ou até que o programa seja interrompido pelo usuário.

import random

class Bingo:
    def __init__(self):
        self.drawn_numbers = set()

    def draw_number(self):
        """
        Draw a random number between 1 and 75 (inclusive).
        """
        while True:
            number = random.randint(1, 75)
            if number not in self.drawn_numbers:
                self.drawn_numbers.add(number)
                return number

    def play(self):
        """
        Play the Bingo game by drawing numbers until all 75 numbers are drawn.
        """
        print("Bem-vindo ao Bingo! Vamos começar a sortear os números:")
        while len(self.drawn_numbers) < 75:
            input("Pressione Enter para sortear um número...")
            number = self.draw_number()
            print(f"Número sorteado: {number}")

        print("Todos os 75 números foram sorteados. O jogo de Bingo está completo!")

if __name__ == "__main__":
    bingo_game = Bingo()
    bingo_game.play()