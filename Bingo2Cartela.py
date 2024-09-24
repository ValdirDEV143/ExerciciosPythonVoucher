# Programa 2: Gerador de Cartelas e Verificação de Bingo
# •	Descrição: Este programa criará cartelas de Bingo, permitirá marcar os números sorteados e verificará se há um Bingo.
# •	Funcionalidades:
# 1.	Gerar cartelas de Bingo com 24 números aleatórios de acordo com os intervalos abaixo:
# •	B: Números de 1 a 15
# •	I: Números de 16 a 30
# •	N: Números de 31 a 45
# •	G: Números de 46 a 60
# •	O: Números de 61 a 75
# 2.	Exibir as cartelas de Bingo em um formato legível.
# 3.	Permitir que o usuário insira os números sorteados para marcar as cartelas.
# 4.	Indicar quando um jogador completou um Bingo (linha, coluna ou diagonal).
# 5.	Exibir a cartela com os números marcados para o usuário visualizar o progresso.
# Especificações Técnicas
# •	Utilize a biblioteca random para sortear os números.
# •	Utilize classes para organizar o código.


import random

class BingoCard:
    def __init__(self):
        self.card = self.generate_card()

    def generate_card(self):
        """
        Generate a Bingo card with 24 random numbers.
        """
        card = []
        for letter in "BINGO":
            column = random.sample(range(1, 16) if letter == "B" else range(16, 31), 5)
            card.extend(column)
        return card

    def mark_number(self, number):
        """
        Mark a number on the Bingo card.
        """
        if number in self.card:
            self.card[self.card.index(number)] = "X"

    def check_bingo(self):
        """
        Check if the Bingo card has a Bingo (line, column, or diagonal).
        """
        rows = [self.card[i:i + 5] for i in range(0, 25, 5)]
        columns = [[self.card[i], self.card[i + 5], self.card[i + 10], self.card[i + 15], self.card[i + 20]] for i in range(5)]
        diagonals = [[self.card[0], self.card[6], self.card[12], self.card[18], self.card[24]],
                     [self.card[4], self.card[8], self.card[12], self.card[16], self.card[20]]]

        for row in rows + columns + diagonals:
            if all(cell == "X" for cell in row):
                return True
        return False

    def display_card(self):
        """
        Display the Bingo card.
        """
        print("B   I   N   G   O")
        for i in range(5):
            row = self.card[i * 5: (i + 1) * 5]
            print(" ".join(str(cell).rjust(2) for cell in row))
        print("\n")

class BingoGame:
    def __init__(self):
        self.bingo_card = BingoCard()

    def play(self):
        """
        Play the Bingo game by drawing numbers and marking the card.
        """
        print("Bem-vindo ao Bingo! Vamos começar a gerar a sua cartela:")
        self.bingo_card.display_card()

        while True:
            try:
                number = int(input("Digite o número sorteado (1 a 75): "))
                if 1 <= number <= 75:
                    self.bingo_card.mark_number(number)
                    self.bingo_card.display_card()
                    if self.bingo_card.check_bingo():
                        print("Bingo! Você completou uma linha, coluna ou diagonal!")
                        break
                else:
                    print("Número inválido. Digite um número entre 1 e 75.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro entre 1 e 75.")

if __name__ == "__main__":
    bingo_game = BingoGame()
    bingo_game.play()