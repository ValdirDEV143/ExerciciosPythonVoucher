carrinho = []
alimentos = ["carne", 13, "peixe", 6, "arroz", 21 ]
casa = ["lençol", 101, "talheres", 36, "mesa", 51, "banho", 61]
higiene = ["escova de dentes", 11, "creme dental", 16, "sabonete", 8]
produtos = [alimentos, casa, higiene]
# Os produtos estão alocados em 3 categorias diferentes que representam todos os produtos do mercado

print("Bem vindo ao nosso sistema")
usuario = int(input("Você é (1) cliente ou (2) funcionário (3) sair: "))
if usuario == 1:
    nome_cliente = input("Digite seu nome: ")
    cpf_cliente = input("Digite seu CPF deste modo 000.000.000-00: ")
    print(f"Bem vindo {nome_cliente}, aqui você fará as melhores compras!")

while True:
    if usuario == 1:
        print("Olá cliente, por favor, digite sua opção abaixo: ")
        print("(1) ver produtos")
        print("(2) adicionar produtos")
        print("(3) remover produtos")
        print("(4) sair")
        opcao_cliente = int(input("Digite a sua opção: "))

        if opcao_cliente == 1:
            print("Ver produtos")
            print("Produtos disponíveis:")
            for item in categoria:
                print(item)

        elif opcao_cliente == 2:
            while True:
                print("Adicionar produtos")
                prod  = input("Digite o produto que você deseja comprar: ")
                if prod in alimentos:
                    carrinho.append(prod)
                elif prod in casa:
                    carrinho.append(prod)
                elif prod in higiene:
                    carrinho.append(prod)
                else:
                    print("Produto não encontrado")
                print("Seu carrinho possui os seguintes produtos: ")
                for item in carrinho: 
                    print(item)
                opcao = int(input("Deseja: (1) adicionar mais produtos (2) finalizar compra "))
                if opcao == 2:
                    soma = 0
                    print("Finalizar compra")
                    print(f"Produtos no carrinho: {carrinho}")
                    for compra in carrinho:
                        if compra in alimentos: 
                            preco  = alimentos[alimentos.index(compra) + 1]
                        elif compra in casa:
                            preco = casa[casa.index(compra) + 1]
                        elif compra in higiene:
                            preco = higiene[higiene.index(compra) + 1]
                        soma += preco
                    print(f"A soma total da sua compra ficou no valor de {soma}")
                    dinheiro = 0
                    saldo = 0
                    while (dinheiro < soma) or (saldo < soma):
                        pag = int(input("Digite sua opção de pagamento: (1)Dinheiro (2)Pix (3)Cartão "))
                        if pag ==1:
                            dinheiro = float(input("Digite o valor em dinheiro que você possui: "))
                            if dinheiro < soma:
                                print("Você não possui dinheiro suficiente para efetuar o pagamento. ")
                            elif dinheiro > soma:
                                troco = dinheiro - soma
                                print(f" pagamento realizado com sucesso, aqui está o seu troco de R$: {troco} reais")
                                nota = int(input("Deseja nota fiscal: (1)Sim (2)Não: "))
                                if nota == 1:
                                        print("--"*20)
                                        print("NOTA FISCAL")
                                        print("--"*20)
                                        print(f'''SUPERMERCADO NOSSO LAR 
                                              CLIENTE:{nome_cliente} ----''')
                                        print("--"*20)
                                        print("produtos")
                                        for i in carrinho:
                                            print(i,end=',')

                                        print("--"*20)
                                        print(f'''Imposto nacional 5% - R$:{soma*0.05}
                                                Imposto federal 8% - R$:{soma*0.08})
                                                Imposto municipal 12% - R$:{soma*0.12} 
                                                empresa: R$: {soma - (soma*0.08 - soma*0.12 - soma*0.05)}
                                                valor final:{soma}''')
                                        print(f'''Valor Pago: R$: {dinheiro} \n troco: R$: {troco}''')
                                        print('--'*20)

                                        print("OBRIGADO PELA PREFERENCIA, VOLTE SEMPRE!")
                                        exit()
                            elif dinheiro == soma:
                                print(f"pagamento realizado com sucesso")
                                nota = int(input("Deseja Nota Fiscal: (1)Sim (2)Não"))
                                if nota == 1:
                                    print('--'*20)
                                    print('NOTA FISCAL')
                                    print('--'*20)
                                    print(f'''Supermercado Nosso Lar
                                        CLIENTE:{nome_cliente} ----
                                        CPF: {cpf_cliente}''')
                                    print("--"*20)
                                    print("PRODUTOS")
                                    print('--'*20)
                                    print(f'''Imposto nacional 5%:{soma*0.05}')
                                    print(f'''Imposto federal 8%: {soma*0.08}''')
                                    print(f'Imposto municipal 12%: {soma*0.12}')
                                    print(f'EMPRESA: R$:{soma-(soma*0.08 - soma*0.12 - soma*0.05)}')
                                    print(f'''valor final:{soma}''')
                                    print(f'Troco - R$: {troco}')
                                    print('--'*20)

                                    print("OBRIGADO PELA PREFERENCIA, VOLTE SEMPRE!")
                                if nota==2:
                                    exit()   

                        elif pag ==2 or pag ==3:
                            nota = 0
                            saldo = float(input("Digite o saldo disponivel em sua conta para efetuar o pagamento: "))
                            if saldo>soma:
                                troco = saldo - soma
                                print(f' pagamento re )
                            
                                     




                                                

                                



