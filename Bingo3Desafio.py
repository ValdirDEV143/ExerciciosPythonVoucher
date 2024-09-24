# Desafio extra (Não é obrigatório):
# 	Utilize alguma biblioteca para criar uma interface gráfica para esse bingo como por exemplo o TKINTER.

import tkinter as tk
import random

# Lista de números para o bingo
numeros_bingo = list(range(1, 76))

# Função para sortear um número
def sortear_numero():
    numero_sorteado = random.choice(numeros_bingo)
    numeros_bingo.remove(numero_sorteado)
    label_numero.config(text=f"Número sorteado: {numero_sorteado}")

# Configuração da janela
janela = tk.Tk()
janela.title("Bingo")
janela.geometry("300x200")

# Botão para sortear número
botao_sortear = tk.Button(janela, text="Sortear", command=sortear_numero)
botao_sortear.pack()

# Label para exibir o número sorteado
label_numero = tk.Label(janela, text="")
label_numero.pack()

janela.mainloop()