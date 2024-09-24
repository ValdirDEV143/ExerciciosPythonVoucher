#Crie um algoritmo que agende as consultas de um hospital, deve ter um menu onde possa escolher entre entrar 
# como usuário ou como médico, no usuário ele deve ser capaz de marcar uma consulta com as seguintes informações: 
# nome do paciente, cpf, idade e horario da consulta. Ele tambem deve ser capaz de verificar 
# o historico da suas consultas. O medico deve ser capaz de ver a lista de pacientes que tem 
# consulta e realizar a consulta e liberar o paciente dessa lista.
hospital_paciente = []
escolha = 0
ordem = 0

while escolha != 3:
    consultas = {}
    print("1 - Paciente\n2 - Médico\n3 - Sair")
    escolha = int(input("Escolha o que deseja fazer: "))
    if escolha == 1:
        consultas["senhas"] = ordem
        consultas["nome do paciente"] = input("Digite o seu nome: ")
        consultas["CPF do paciente"] = input("Digite o seu CPF: ")
        consultas["idade do paciente"] = int(input("Digite a sua idade: "))
        consultas["horario da consulta"] = input("Digite o horário da consulta: ")
        hospital_paciente.append(consultas)
        ordem +=1
        continuar = int(input("Deseja ver seu histórico de consultas? Aperte 1  para sim ou aperte 2 para sair"))
        if continuar == 1:
            print(consultas)
        elif continuar == 2:
            print("Obrigado por usar o nosso sistema!")
    elif escolha == 2:
        print("1 - Ver lista de paciente\n2 - Realizar consultas\n3 - Liberar paciente")
        acao = int(input("Escolha o que deseja fazer: "))
        if acao == 1:
            print(hospital_paciente)
        if acao == 2:
            consulta = input("Digite o nome do paciente: ")
            alta = int(input("Esse paciente receberá alta? (1 - Para sim e 2 - para não): "))
            if alta == 1:
                nome = int(input("Qual a senha do paciente? "))
                hospital_paciente.pop(nome)
                print("Paciente liberado com sucesso")
            elif alta == 2:
                print("Obrigado por utilizar o nosso sistema!")
        elif acao == 3:
            nome = int(input("Qual a senha do paciente? "))
            hospital_paciente.pop(nome)
            if continuar == 1:
                print(consultas)
            elif continuar == 2:
                print("Obrigado por usar o nosso sistema! ")
            elif escolha == 2:
                print("1 - Ver lista de paciente\n2 - Realizar consulta\n3 - Liberar paciente")
                acao = int(input("Escolha o que deseja fazer: "))
                if acao == 1:
                    print(hospital_paciente)
                if acao == 2:
                    consulta = input("Digite o nome do paciente: ")
                    alta = int(input("Esse paciente receberá alta? (1 - Para sim e 2 para não): "))
                    if alta == 1:
                        nome = int(input("Qual a senha do paciente?: "))
                        hospital_paciente.pop(nome)
                        print("Paciente liberado com sucesso")
                    elif alta == 2:
                        print("Paciente liberado com sucesso")
                elif acao == 3:
                    nome = int(input("Qual a senha do paciente?: "))
                    hospital_paciente.pop(nome)
                    print("Paciente liberado com sucesso")
                    while True:
                        outro = int(input("Deseja liberar outro paciente? (1 - Para sim e 2 - para não): "))
                        if outro == 1:
                            nome = int(input("Qual a senha do paciente?: "))
                            hospital_paciente.pop(0)
                            print("Paciente liberado com sucesso") 
                        elif outro == 2:
                            print("Obrigado por utilizar o nosso sistema!")
                            break
            elif escolha == 3:
                print ("Obrigado por utilizar o nosso sistema!")
                break                           




