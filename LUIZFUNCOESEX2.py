class Lampada:
    def __init__(self):
        self.acesa = False

    def acender(self):
        self.acesa = True

    def apagar(self):
        self.acesa = False

    def status(self):
        return "Acesa" if self.acesa else "Apagada"

def exibeOpcoes():
    print("Opções:")
    print("(0) Sair")
    print("(1) Acender luz")
    print("(2) Apagar luz")
    print("(3) Consultar estado atual")

def main():
    lampada = Lampada()

    while True:
        exibeOpcoes()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo do programa.")
            break
        elif opcao == "1":
            lampada.acender()
            print("Lâmpada acesa.")
        elif opcao == "2":
            lampada.apagar()
            print("Lâmpada apagada.")
        elif opcao == "3":
            print(f"Estado atual da lâmpada: {lampada.status()}")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()