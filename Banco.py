extrato = ""
saldo = float(100)
qtd_saque = int(0)
menu = ""
while menu != 0:
    menu = int(input('''
                     
 -------------------------------------------
 * Seja Bem-Vindo ao Sistema Banco Pessoal *
 -------------------------------------------

 Escolha uma das opções abaixo:

 [1] Saque
 [2] Depósito
 [3] Extrato

 [0] Sair
 -------------------------------------------
                  
 >> '''))
    print()
    if menu == 1:
        saque = int(input('\n>> Digite o valor do saque: R$ '))
        if saque < 0:
            print('\n>> Valor de saque inválido. Por favor, insira um valor inteiro positivo.')
        elif saque <= saldo:
                if qtd_saque < 3:
                    if saque <= 500:
                        saldo -= saque
                        print(f'\n>> Saque efetuado!')
                        extrato += f'(-) Saque: R$ {saque}\n'
                        qtd_saque += 1
                    else:
                        print('\n>> A quantia por saque é limitado a R$ 500,00.')
                else:
                    print('\n>> Limite de 3 saques diários excedido.')
        else:
            print('\n>> Saldo insuficiente, por favor tente novamente.')
    elif menu == 2:
        deposito = int(input('\n>> Digite o valor do depósito: R$ '))
        if deposito < 0:
            print('\n>> Valor inválido. Insira um valor inteiro positivo.')
        else:
            saldo += deposito
            extrato += f'(+) Depósito: R$ {deposito}\n'
            print('\n>> Depósito efetuado!')
    elif menu == 3:
        print('-------------------------------------------')
        print('*            Extrato Bancário             *')
        print('-------------------------------------------')
        print(f'Sem movimentações.' if extrato == "" else extrato)
        print()
        print(f'Saldo atual = R$ {saldo:.2f}')
        print('-------------------------------------------')
    elif menu == 0:
        print('\n>> Encerrando a sessão...')
        print('\n>> Obrigado por utilizar o Sistema Banco Pessoal. Até logo!\n')
        break
    elif menu != 1 or menu != 2 or menu != 3 or menu != 0:
        print('\n>> Opção inválida. Por favor, tente novamente.\n')
        print()
    
