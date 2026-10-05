print('Finance Fragment')
print('SEJA BEM VINDO AO SOFTWARE DE ORGANIZAÇÃO FINANCEIRO MAIS SIMPLES E FUNCIONAL.')
#ENTRADAS
nome=input('Qual é o seu nome : ').strip().title()

#PROCESSO/Saída

receitas=[]
despesas=[]


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
        descricao=input("Descrição : ").strip()
        valor=float(input("Valor R$ : "))
        categoria=input("Categoria : ").strip().lower()
        despesas.append({
            "Descrição" : descricao,
            "Valor" : valor,
            "categoria" : categoria
        })
        

        input()

    elif opcao == "2":
        valor=float(input("Valor Da Receita R$ : "))
        receitas.append(valor)
        print(f"Total de Receitas R$ : {sum(receitas)}")
        input()

    elif opcao == "3":
        if len(receitas) == 0 and len(despesas) == 0:
            print('''
Você não adicionou nenhuma receita ou despesas.
Para ver o relatório acrescente ao menos uma receita ou despesa !
            ''')
            input()
        else:
            total_despesas=0
            for d in despesas:
                total_despesas+=d["Valor"]
            saldo=sum(receitas)-total_despesas

            print("."*20,"Relatório Financeiro","."*20)
            print("-"*60)
            print(f"Total de Receitas R$ : {sum(receitas):.2f}")
            print("-"*60)
            print(f"Total de Despesas R$ : {total_despesas:.2f}")
            print("-"*60)
            print(f"Saldo final R$ : {saldo:.2f}")
            print("-"*60)

            por_categoria= {}
            for d in despesas:
                cat=d["categoria"]
                if cat in por_categoria:
                    por_categoria[cat] += d["Valor"]
                else:
                    por_categoria[cat]=d["Valor"]
            for cat , valor in por_categoria.items():
                print(f"{cat} : R$ {valor:.2f} ")

            print("-"*60)
            

            if saldo >0:
                    print(f'Saldo positivo : ✅  Parabéns {nome}, você está com um bom saldo.')
            elif saldo == 0:
                print(f'Saldo zero : ❌ {nome} Você zerou seu saldo.')
            else:
                print(f'Saldo negativo :⚠️  {nome}, atenção você está no vermelho ! ')
            print("."*60)
            input()
    
    elif opcao == "0" :
        print("Finance-Fragment Fechado.")
        break

    else:
        print("Opção inválida .")
        input()

    

