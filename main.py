import dados
import funcoes

dados.carregar()

print('Finance Fragment')
print('SEJA BEM VINDO AO SOFTWARE DE ORGANIZAÇÃO FINANCEIRO MAIS SIMPLES E FUNCIONAL.')

if not dados.nome.strip():
    dados.nome=input('Qual é o seu nome : ').strip().title()


while True :
    print('''   
        Opções Finance-Fragment
            0-Encerrar
            1-Adicionar Despesas 💲
            2-Adicionar Receitas 💵
            3-Relatório Financeiro 📊
            4-Editar Despesas💲
            5-Excluir Despesa 💲
            6-Editar Receitas 💵
            7-Excluir Receitas 💵        
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
    elif opcao=="4":
        funcoes.editar_despesas()
        input()
    
    elif opcao == "0" :
        dados.salvar()
        print("Finance-Fragment Fechado.")
        break

    elif opcao=="5":
        funcoes.excluir_despesa()
        input()

    elif opcao == "6":
        funcoes.editar_receita()
        input()

    elif opcao == '7':
        funcoes.excluir_receita()
        input()

    else:
        print("Opção inválida .")
        input()

