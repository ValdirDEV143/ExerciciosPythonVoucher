
def exibeMenu():
    print ("##### MENU #####\n")
    print("0 - SAIR\n")
    print("1 - SOMAR\n")
    print("2 - SUBTRAIR\n")
    print("3 - DIVIDIR\n")
    print("4 - MULTIPLICAR\n")
    opcao = int(input("Escolha uma opcao: "))
    return opcao
def somar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado
def subtrair(numero1, numero2):
    resultado = numero1 - numero2
    return resultado
def dividir(numero1, numero2):
    resultado = numero1 / numero2
    return resultado
def multiplicar(numero1, numero2):
    resultado = numero1 * numero2
    return resultado
i = 0
opcao = 1
num1 = 0
num2 = 0
resultado = 0
while opcao != 0:
    opcao = exibeMenu()
    if opcao == 0:
        break
    num1 = float(input("Informe o primeiro número para a operação: "))    
    num2 = float(input("Informe o segundo número para a operação: "))
    if opcao == 1:
        resultado = somar(num1, num2)
        print(f"Resultado:{resultado}")
    elif opcao == 2:
        resultado = subtrair(num1,num2)
        print(f"Resultado: {resultado}")
    elif opcao == 3:
        resultado = dividir(num1,num2)
        print(f"Resultado: {resultado}")
    elif opcao == 4:
        resultado = multiplicar(num1,num2)
        print(f"Resultado: {resultado}")
          
    