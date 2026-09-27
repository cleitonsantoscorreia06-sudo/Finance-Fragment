print('Finance Fragment')
print('SEJA BEM VINDO AO SOFTWARE DE ORGANIZAÇÃO FINANCEIRO MAIS SIMPLES E FUNCIONAL.')
#ENTRADAS
nome=input('Qual é o seu nome : ').strip().title()

#PROCESSO/Saída

while True:
    print('''
    Opções Finance-Fragment
    1-Calcular Saldo
    2-Sair
''')
    opcao=input('Digite o número da opção : ').strip()
    if opcao=='1':
        receita=float(input('Informe o valor da receita : '))
        despesa=float(input('Informe o valor da despesa : '))

        saldo=receita-despesa

        print(f'''
                Finance Fragment
        --------------------------------------
        Usuário: {nome}
        --------------------------------------  
        Receita : R$ {receita:.2f}
        --------------------------------------
        Despesa : R$ {despesa:.2f}
        --------------------------------------
        Saldo Disponível : R$ {saldo:.2f}
        --------------------------------------
        ''')
        print('='*60)
        if saldo >0:
            print('Saldo positivo : ✅  Parabéns, você está com um bom saldo.')
        elif saldo == 0:
            print('Saldo zero : Você zerou seu saldo.')
        else:
            print('Saldo negativo : Atenção você está no vermelho ! ')

        print('='*60)
        input()
    elif opcao=='2':
        print('Encerrando Finance-Fragment ...')
        break

    else:
        print('Opção inválida.')
        input()
    

