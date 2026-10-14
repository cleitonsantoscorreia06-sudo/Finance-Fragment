import dados
import funcoes

print('Finance Fragment')
print('SEJA BEM VINDO AO SOFTWARE DE ORGANIZAÇÃO FINANCEIRO MAIS SIMPLES E FUNCIONAL.')

dados.nome=input('Qual é o seu nome : ').strip().title()


while True :
    print('''   
        Opções Finance-Fragment
            0-Encerrar
            1-Adicionar Despesas
            2-Adicionar Receitas
            3-Relatório Financeiro

''')
    
    opcao=input("Digite o número da opção escolhida : ").strip()
    if opcao == "1":
        funcoes.adicionar_despesas()
        input()

    elif opcao == "2":
        funcoes.adicionar_receita()
        input()

    elif opcao == "3":
        funcoes.mostrar_relatorio()
        input()
    
    elif opcao == "0" :
        print("Finance-Fragment Fechado.")
        break

    else:
        print("Opção inválida .")
        input()

