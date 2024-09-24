# Criando as  listas
carrinho = []
alimentos = ['frango', 18, 'peixe', 7, 'arroz', 25]
casa = ['lençol', 107, 'talheres', 45, 'mesa', 60]
higiene = ['escova de dente', 12, 'creme dental', 9]
produtos = [alimentos, casa, higiene]
# os produtos estão  em 3 categorias diferentes que representam todos os produtos do mercado nesse momento!
while True:

    print('BEM VINDO AO NOSSO SISTEMA')
    usuario = int(input("Você é (1) cliente ou (2) funcionário (3) sair: ")) # o usuario é funcionario ou cliente
    if usuario==3:
        print('PROGRAMA ENCERRADO')
    if usuario == 1: #CLIENTE
            nome_cliente = input("Digite seu nome: ")
            cpf_cliente = input("Digite seu CPF deste modo 000.000.000-00: ")
            print(f'BEM VINDO {nome_cliente}, aqui você fará as melhores compras!')
            while True:
                print("MENU")

                print("(1) ver produtos")
                print("(2) adicionar produtos")
                print("(3) remover produtos")
                print("(4) sair")
                opcao_cliente = int(input("Digite a sua opção: "))

                if opcao_cliente == 1: # Para vizualizar estoque
                        print('Ver produtos')
                        print('Produtos disponíveis:')
                        for categoria in produtos:
                            for item in categoria:
                                print(item)
                                continue

                elif opcao_cliente == 2: #ADICIONAR PRODUTOS
                        while True:
                            print('Adicionar produtos')
                            prod = input("Digite o produto que você deseja comprar: ")
                            if prod in alimentos:
                                carrinho.append(prod)
                            elif prod in casa:
                                carrinho.append(prod)
                            elif prod in higiene:
                                carrinho.append(prod)
                            else:
                                print('Produto não encontrado')
                            print('Seu carrinho possui os seguintes produtos:')
                            for item in carrinho:
                                print(item)
                            opcao = int(input("Deseja: (1) adicionar mais produtos (2) finalizar compra (3) remover produtos:  "))
                            if opcao == 2: # PARA FINALIZAR COMPRA
                                soma = 0
                                print('Finalizar compra')
                                print(f"Produtos no carrinho: {carrinho}")
                                for compra in carrinho:
                                    if compra in alimentos:
                                        preco = alimentos[alimentos.index(compra) + 1]
                                    elif compra in casa:
                                        preco = casa[casa.index(compra) + 1]
                                    elif compra in higiene:
                                        preco = higiene[higiene.index(compra) + 1]
                                    soma += preco
                                print(f'A soma total da sua compra ficou no valor de {soma}')
                                dinheiro = 0
                                saldo = 0
                                nota=0
                                while saldo<soma:
                                    pag = int(input("digite sua opção de pagemnto: (1)dinherio (2)pix (3) cartão "))

                                    if pag ==1: #DINHEIRO
                                        saldo = float(input("digite o valor em dinheiro que vc possui: "))
                                        if saldo < soma:
                                            print("vc não possui dinheiro suficiente para efetuar o pagamento. ")
                                        elif saldo> soma:
                                            troco = saldo - soma
                                            print(f' pagmento realizado com sucesso,  aqui está o seu troco de R$:{troco} reais')
                                            nota = int(input("deseja nota fiscal: (1)Sim (2)não: "))
                                            if nota==1:
                                                    print('--'*20)
                                                    print('NOTA FISCAL')
                                                    print('--'*20)
                                                    print(f'''SUPERMERCADO NOSSO LAR
                                                        CLIENTE:{nome_cliente} ----''')
                                                    print('--'*20)
                                                    print(''' produtos''')
                                                    for i in carrinho:
                                                        print(i,end=',')

                                                    print('--'*20)
                                                    print(f'''imposto nacinal 5% - R$:{soma*0.05}
                                                            imposto federal 8% - r$:{soma *0.08}
                                                            imposto municipal 12% - R$:{soma*0.12}
                                                            empresa: R$:{soma-(soma*0.08 - soma*0.12 - soma*0.05)}
                                                            valor final: {soma}''')
                                                    print(f'''valor pago:R$:{saldo} \n troco: R$:{troco}''')
                                                    print('--'*20)

                                                    print('OBRIGADO PELA PREFERÊNCIA, VOLTE SEMPRE!')
                                                    exit()
                                            if nota==2:
                                                    exit()



                                        elif saldo ==soma:
                                            print(f' pagmento realizado com sucesso')
                                            nota = int(input("deseja nota fiscal: (1)Sim (2)não"))
                                            troco= saldo-soma
                                            if nota==1:
                                                    print('--'*20)
                                                    print('NOTA FISCAL')
                                                    print('--'*20)
                                                    print(f'''SUPERMERCADO NOSSO LAR
                                                        CLIENTE:{nome_cliente} ----
                                                        CPF: {cpf_cliente}''')
                                                    print('--'*20)
                                                    print('''PRODUTOS''')
                                                    print('--'*20)
                                                    print(f'imposto nacional 5%: {soma*0.05}')
                                                    print(f'''imposto federal 8%: {soma *0.08}''')
                                                    print(f'imposto municipal 12%: {soma*0.12}')
                                                    print(f'EMPRESA:R$:{soma-(soma*0.08 - soma*0.12 - soma*0.05)}')
                                                    print(f'''valor final: {soma}''')
                                                    print(f' Troco - RS:{troco}')
                                                    print('--'*20)

                                                    print('OBRIGADO PELA PREFERÊNCIA, VOLTE SEMPRE!')
                                            if nota==2:
                                                    exit()




                                    elif pag ==2: #PIX
                                        saldo = float(input("digite o saldo disponivel em sua conta para efetuar o pagmento: "))
                                        if saldo>soma:
                                            troco = saldo - soma
                                            print(f' pagmento realizado com sucesso,  aqui está o seu troco de R$:{troco} reais')
                                            nota = int(input("deseja nota fiscal: (1)Sim (2)não"))
                                            if nota==1:
                                                    print('--'*20)
                                                    print('NOTA FISCAL')
                                                    print('--'*20)
                                                    print(f'''SUPERMERCADO NOSSO LAR
                                                        CLIENTE:{nome_cliente} ----
                                                        CPF: {cpf_cliente}''')
                                                    print('--'*20)
                                                    print('''PRODUTOS''')
                                                    print('--'*20)
                                                    print(f'imposto nacional 5%: {soma*0.05}')
                                                    print(f'''imposto federal 8%: {soma *0.08}''')
                                                    print(f'imposto municipal 12%: {soma*0.12}')
                                                    print(f'EMPRESA:R$:{soma-(soma*0.08 - soma*0.12 - soma*0.05)}')
                                                    print(f'''valor final: {soma}''')
                                                    print(f' Troco - RS:{troco}')
                                                    print('--'*20)
                                                    exit()
                                            if nota==2:
                                                    print('OBRIGADO VOLTE SEMPRE!')
                                                    exit()

                                        elif saldo == soma:
                                            print(f' pagmento realizado com sucesso')
                                            nota = int(input("deseja nota fiscal: (1)Sim (2)não"))
                                            if nota==1:
                                                    print('--'*20)
                                                    print('NOTA FISCAL')
                                                    print('--'*20)
                                                    print(f'''SUPERMERCADO NOSSO LAR
                                                        CLIENTE:{nome_cliente} ---- CPF: {cpf_cliente}
                                                        produtos''')
                                                    print('--'*20)
                                                    print(f'''imposto nacinal 5%: {soma*0.05}
                                                            imposto federal 8%: {soma *0.08}
                                                            imposto municipal 12%: {soma*0.12}
                                                            empresa: R$:{soma-(soma*0.12-soma*0.86-soma*0.05)}
                                                            valor final: {soma}
                                                            valor pago: {saldo}
                                                            troco: {troco}''')

                                                    print('--'*20)

                                                    print('OBRIGADO PELA PREFERÊNCIA, VOLTE SEMPRE!')
                                                    exit()

                                            if nota==2:
                                                    print('OBRIGADO PELA PREFERÊNCIA, VOLTE SEMPRE!')
                                                    exit()
                                        elif nota==3:
                                            saldo = float(input("digite o saldo disponivel em sua conta para efetuar o pagmento: "))
                                        if saldo>soma:
                                            troco = saldo - soma
                                            print(f' pagmento realizado com sucesso,  aqui está o seu troco de R$:{troco} reais')
                                            nota = int(input("deseja nota fiscal: (1)Sim (2)não"))
                                            if nota==1:
                                                    print('--'*20)
                                                    print('NOTA FISCAL')
                                                    print('--'*20)
                                                    print(f'''SUPERMERCADO NOSSO LAR
                                                        CLIENTE:{nome_cliente} ----
                                                        CPF: {cpf_cliente}''')
                                                    print('--'*20)
                                                    print('''PRODUTOS''')
                                                    print('--'*20)
                                                    print(f'imposto nacional 5%: {soma*0.05}')
                                                    print(f'''imposto federal 8%: {soma *0.08}''')
                                                    print(f'imposto municipal 12%: {soma*0.12}')
                                                    print(f'EMPRESA:R$:{soma-(soma*0.08 - soma*0.12 - soma*0.05)}')
                                                    print(f'''valor final: {soma}''')
                                                    print(f' Troco - RS:{troco}')
                                                    print('--'*20)
                                                    exit()
                                            if nota==2:
                                                    print('OBRIGADO VOLTE SEMPRE!')
                                                    exit()
                                                    break
                                        elif saldo == soma:
                                            print(f' pagmento realizado com sucesso')
                                            if nota==1:
                                                    print('--'*20)
                                                    print('NOTA FISCAL')
                                                    print('--'*20)
                                                    print(f'''SUPERMERCADO NOSSO LAR
                                                        CLIENTE:{nome_cliente} ---- CPF: {cpf_cliente}
                                                        produtos''')
                                                    print('--'*20)
                                                    print(f'''imposto nacinal 5%: {soma*0.05}
                                                            imposto federal 8%: {soma *0.08}
                                                            imposto municipal 12%: {soma*0.12}
                                                            empresa: R$:{soma-(soma*0.12-soma*0.86-soma*0.05)}
                                                            valor final: {soma}
                                                            valor pago: {saldo}
                                                            troco: {troco}''')

                                                    print('--'*20)

                                                    print('OBRIGADO PELA PREFERÊNCIA, VOLTE SEMPRE!')

                                            if nota==2:
                                                    print('OBRIGADO PELA PREFERÊNCIA, VOLTE SEMPRE!')
                                                    exit()
                                    if pag==3: #CARTÃO
                                        saldo = float(input("digite o saldo disponivel em sua conta para efetuar o pagmento: "))
                                        if saldo>soma:
                                            troco = saldo - soma
                                            print(f' pagmento realizado com sucesso,  aqui está o seu troco de R$:{troco} reais')
                                            nota = int(input("deseja nota fiscal: (1)Sim (2)não"))
                                            if nota==1:
                                                    print('--'*20)
                                                    print('NOTA FISCAL')
                                                    print('--'*20)
                                                    print(f'''SUPERMERCADO NOSSO LAR
                                                        CLIENTE:{nome_cliente} ----
                                                        CPF: {cpf_cliente}''')
                                                    print('--'*20)
                                                    print('''PRODUTOS''')
                                                    print('--'*20)
                                                    print(f'imposto nacional 5%: {soma*0.05}')
                                                    print(f'''imposto federal 8%: {soma *0.08}''')
                                                    print(f'imposto municipal 12%: {soma*0.12}')
                                                    print(f'EMPRESA:R$:{soma-(soma*0.08 - soma*0.12 - soma*0.05)}')
                                                    print(f'''valor final: {soma}
                                                            valor pago: {saldo}''')
                                                    print(f' Troco - RS:{troco}')
                                                    print('--'*20)
                                                    exit()
                                            if nota==2:
                                                    print('OBRIGADO VOLTE SEMPRE!')
                                                    exit()

                                        elif saldo == soma:
                                            troco = saldo - soma
                                            print(f' pagmento realizado com sucesso')
                                            nota = int(input("deseja nota fiscal: (1)Sim (2)não"))
                                            if nota==1:
                                                    print('--'*20)
                                                    print('NOTA FISCAL')
                                                    print('--'*20)
                                                    print(f'''SUPERMERCADO NOSSO LAR
                                                        CLIENTE:{nome_cliente} ---- CPF: {cpf_cliente}
                                                        produtos''')
                                                    print('--'*20)
                                                    print(f'''imposto nacinal 5%: {soma*0.05}
                                                            imposto federal 8%: {soma *0.08}
                                                            imposto municipal 12%: {soma*0.12}

                                                             empresa: R$:{soma-(soma*0.12-soma*0.86-soma*0.05)}
                                                            valor final: {soma}
                                                            valor pago: {saldo}
                                                            troco: {troco}''')

                                                    print('--'*20)

                                                    print('OBRIGADO PELA PREFERÊNCIA, VOLTE SEMPRE!')
                                                    exit()

                                            if nota==2:
                                                    print('OBRIGADO PELA PREFERÊNCIA, VOLTE SEMPRE!')
                                                    exit()


                                        if saldo>soma:
                                            troco = saldo - soma
                                            print(f' pagmento realizado com sucesso,  aqui está o seu troco de R$:{troco} reais')
                                            nota = int(input("deseja nota fiscal: (1)Sim (2)não"))
                                            if nota==1:
                                                    print('--'*20)
                                                    print('NOTA FISCAL')
                                                    print('--'*20)
                                                    print(f'''SUPERMERCADO NOSSO LAR
                                                        CLIENTE:{nome_cliente} ----
                                                        CPF: {cpf_cliente}''')
                                                    print('--'*20)
                                                    print('''PRODUTOS''')
                                                    print('--'*20)
                                                    print(f'imposto nacional 5%: {soma*0.05}')
                                                    print(f'''imposto federal 8%: {soma *0.08}''')
                                                    print(f'imposto municipal 12%: {soma*0.12}')
                                                    print(f'EMPRESA:R$:{soma-(soma*0.08 - soma*0.12 - soma*0.05)}')
                                                    print(f'''valor final: {soma}
                                                            empresa: R$:{soma-(soma*0.12-soma*0.86-soma*0.05)}
                                                            valor pago: {saldo}
                                                            troco: {troco}''')
                                                    print('--'*20)
                                                    exit()
                                            if nota==2:
                                                    print('OBRIGADO VOLTE SEMPRE!')
                                                    exit()
                                                    break
                                        elif saldo == soma:
                                            print(f' pagmento realizado com sucesso')
                                            if nota==1:
                                                    print('--'*20)
                                                    print('NOTA FISCAL')
                                                    print('--'*20)
                                                    print(f'''SUPERMERCADO NOSSO LAR
                                                        CLIENTE:{nome_cliente} ---- CPF: {cpf_cliente}
                                                        produtos''')
                                                    print('--'*20)
                                                    print(f'''imposto nacinal 5%: {soma*0.05}
                                                            imposto federal 8%: {soma *0.08}
                                                            imposto municipal 12%: {soma*0.12}
                                                             empresa: R$:{soma-(soma*0.12-soma*0.86-soma*0.05)}
                                                            valor final: {soma}
                                                            valor pago: {saldo}
                                                            troco: {troco}''')

                                                    print('--'*20)

                                                    print('OBRIGADO PELA PREFERÊNCIA, VOLTE SEMPRE!')

                                            if nota==2:
                                                    print('OBRIGADO PELA PREFERÊNCIA, VOLTE SEMPRE!')
                                                    exit()

                                        else:
                                            print('O saldo digitado não é suficiente para efetuar o pagamento')
                            if opcao==3: #REMOVER PRODUTOS DO CARRINHO
                                print('Remover produtos')
                                if carrinho == []:
                                    print('vc não possui nenhum item no carrinho ')
                                else:
                                    print(f'vc possui os seguintes produtos no carrinho:{carrinho} ')
                                    prod = input("Digite o produto que você deseja remover: ")
                                    if prod in carrinho:
                                        carrinho.remove(prod)
                                        print(f'{prod} removido do carrinho.')
                                        break
                                    else:
                                        print('Produto não encontrado no carrinho.')


                if opcao_cliente == 3: # REMOVER PRODUTOS
                        print('Remover produtos')
                        if carrinho == []:
                            print('vc não possui nenhum item no carrinho ')
                        else:
                            print(f'vc possui os seguintes produtos no carrinho:{carrinho} ')
                            prod = input("Digite o produto que você deseja remover: ")
                            if prod in carrinho:
                                carrinho.remove(prod)
                                print(f'{prod} removido do carrinho.')
                            else:
                                print('Produto não encontrado no carrinho.')

                elif opcao_cliente == 4: # SAIR E RETORNAR PARA O MENU FUNCIONARIO/CLIENTE

                        print('Sair')

                        break

    if usuario == 2: # FUNCIONARIO

            print('Funcionário')
            matri =int(input("digite a sua matricula: "))
            nomef = str(input("digite seu nome: "))
            datanasc = str(input(f'digite sua data de nascimento dd/mm/aaaa: '))
            cpffun = int(input("digite seu cpf: "))
            print(f'--'*20)
            print(f'Olá {nomef} bem vindo ao sistema administrativo da loja')
            print("--"*20)
            op=0
            while True:# MENU
                print('''digite o que vc deseja fazer:
                            (1) vizualizar estoque
                            (2) adicionar produto no estoque
                            (3) remover produto do estoque
                            (4) alterar preço
                            (5) sair  ''')
                op = int(input("digite sua opção: "))

                if op==1: # VIZUALIZAÇÃO DO ESTOQUE
                    print(f'--'*20)
                    print(f'ESTOQUE ATUAL')
                    print("--"*20)
                    for categoria in produtos:
                        for item in categoria:
                            print(item)
                elif op==2: #ADIÇÃO DE UM PRODUTO NO ESTOQUE
                    print("adicionar produto")
                    cat = int(input("digite a categoria do novo produto: (1)alimento (2)higiene (3)casa "))# SELEÇÃO DE CATEGORIA PARA ALOCAR O PRODUTO
                    if cat==1:
                        novo = str(input("digite o nome do novo produto a ser adicionado: "))
                        cod = str(input("digite o codigo do produto: "))
                        pre = float(input("informe o preço do produto: "))
                        if novo in alimentos:
                            print('esse produto ja esta cadastrado no sistema ')
                        if novo not in alimentos:
                            alimentos.append(novo)
                            alimentos.append(pre)
                            print("produto adicionado com sucesso!")

                    if cat==2:
                        novo = str(input("digite o nome do novo produto a ser adicionado: "))
                        cod = str(input("digite o codigo do produto: "))
                        pre = float(input("informe o preço do produto: "))
                        if novo in higiene:
                            print('esse produto ja esta cadastrado no sistema ')
                        if novo not in higiene:
                            higiene.append(novo)
                            higiene.append(pre)
                            print("produto adicionado com sucesso")

                    if cat ==3:
                        novo = str(input("digite o nome do novo produto a ser adicionado: "))
                        cod = str(input("digite o codigo do produto: "))
                        pre = float(input("informe o preço do produto: "))
                        if novo in casa: # PRODUTO JA CADASTRADO NO SISTEMA
                            print('esse produto ja esta cadastrado no sistema ')
                        if novo not in casa:
                            casa.append(novo)
                            casa.append(pre)
                            print("produto adicionado com sucesso")


                elif op==3: # remover produto do estoque
                    print("remover produto: ")
                    nomeproduto = input("Digite o nome do produto a ser removido: ")

                    removed = False  # Variável para verificar se o produto foi removido

                    if nomeproduto in alimentos:
                        indice = alimentos.index(nomeproduto)
                        alimentos.pop(indice)  # Remove o produto
                        alimentos.pop(indice)  # Remove a quantidade correspondente
                        print("Produto removido com sucesso")
                        print(alimentos)
                        removed = True

                    if nomeproduto in higiene:
                        indice = higiene.index(nomeproduto)
                        higiene.pop(indice) # remove o produto
                        higiene.pop(indice+1) # remove o preço do produto
                        print("produto removido com sucesso")
                        print(higiene)
                        removed=  True
                    if nomeproduto in casa:
                        indice = casa.index(nomeproduto)
                        casa.pop(indice)
                        casa.pop(indice+1)
                        print("produto removido com sucesso")
                        print(casa)
                        removed = True
                    else: # caso o porduto a ser removido não exista no estoque
                         print("esse produto não existe no estoque ")
                elif op == 4: #ALTERAÇÃO DE PREÇO
                        produto = str(input("digite o nome do produto: "))
                        if produto in alimentos:
                            indice = alimentos.index(produto)
                            preco = indice + 1
                            print(f"O preço atual do produto é de R$:{alimentos[preco]}")
                            novo = float(input("digite o novo preço: "))
                            alimentos[preco]= novo
                            print(f"produto atualizado com o novo preço de {novo}")
                        if produto in higiene:
                            indice = higiene.index(produto)
                            preco = indice + 1
                            print(f'O preço atual do produto é de R$: {higiene[preco]}')
                            novo = float(input("digite o novo valor do produto: "))
                            alimentos[preco]= novo
                        if produto in casa:
                             indice = casa.index(produto)
                             preco = indice+1
                             print(f'O preço atual  do produto é de R$:{casa[preco]}')
                             novo = float(input("digite o novo valor do produto: "))
                             casa[preco]=novo
                            #CASO O FUNCIONARIO DIGITE UM PRODUTO QUE NÃO EXISTE NO ESTOQUE NA ALTERAÇÃO DE PREÇOS

                if op ==5:
                    print('sistema encerrado.')
                    break



            print('Programa encerrado.')
    if usuario==3:

         exit()