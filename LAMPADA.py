#Faça um programa python para calcular o numero de lampadas 60 watts necessárias para um determinado cômodo. O programa deverá ler um 
# um conjunto de informções, tais como: tipo, largura e comprimento do cômodo. O programa termina quando o tipo de cômodo for igual -1.
# Tem que calcular a área (largura*comprimento) utilize funções.
# tabela a seguir:
# tipo do cômodo potencia(watss)

# 0   12
# 1   15
# 2   18
# 3   20
# 4   22

# def calcular_lampadas_necessarias(largura, comprimento, tipo_comodo):
#     # Tabela de potências (tipo de cômodo -> potência em watts)
#     potencias = {0: 12, 1: 15, 2: 18, 3: 20, 4: 22}
    
#     # Calcula a área do cômodo
#     area = largura * comprimento
    
#     # Supondo 1 lâmpada por cada 10 metros quadrados
#     lampadas_necessarias = area / 10
    
#     # Arredonda para o número inteiro de lâmpadas mais próximo
#     lampadas_necessarias = int(lampadas_necessarias) + 1
    
#     # Obtém a potência com base no tipo de cômodo
#     potencia = potencias.get(tipo_comodo, 0)
    
#     return lampadas_necessarias, potencia

# def main():
#     while True:
#         # Lê a entrada do usuário
#         tipo_comodo = input("Digite o tipo de cômodo (ou -1 para sair): ")
#         if tipo_comodo == "-1":
#             break
#         largura = float(input("Digite a largura do cômodo (em metros): "))
#         comprimento = float(input("Digite o comprimento do cômodo (em metros): "))
        
#         # Calcula as lâmpadas necessárias e a potência
#         lampadas, potencia = calcular_lampadas_necessarias(largura, comprimento, int(tipo_comodo))
        
#         print(f"Para o cômodo {tipo_comodo}, você precisa de {lampadas} lâmpadas de {potencia} watts.")

# if __name__ == "__main__":
#     main()

def calcular_area(largura, comprimento):
    return largura * comprimento

def calcular_lampadas_necessarias(area, tipo_comodo):
    # Tabela de potências (tipo de cômodo -> potência em watts)
    potencias = {0: 12, 1: 15, 2: 18, 3: 20, 4: 22}
    
    # Supondo 1 lâmpada por cada 10 metros quadrados
    lampadas_necessarias = area / 10
    
    # Arredonda para o número inteiro de lâmpadas mais próximo
    lampadas_necessarias = int(lampadas_necessarias) + 1
    
    # Obtém a potência com base no tipo de cômodo
    potencia = potencias.get(tipo_comodo, 0)
    
    return lampadas_necessarias, potencia

def main():
    while True:
        # Lê a entrada do usuário
        tipo_comodo = input("Digite o tipo de cômodo (ou -1 para sair): ")
        if tipo_comodo == "-1":
            break
        largura = float(input("Digite a largura do cômodo (em metros): "))
        comprimento = float(input("Digite o comprimento do cômodo (em metros): "))
        
        # Calcula a área
        area = calcular_area(largura, comprimento)
        
        # Calcula as lâmpadas necessárias e a potência
        lampadas, potencia = calcular_lampadas_necessarias(area, int(tipo_comodo))
        
        print(f"Para o cômodo {tipo_comodo}, você precisa de {lampadas:.0f} lâmpadas de {potencia} watts.")

if __name__ == "__main__":
    main()
