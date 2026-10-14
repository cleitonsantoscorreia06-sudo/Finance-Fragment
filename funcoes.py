import dados 

def adicionar_despesas():
   descricao=input("Descrição : ").strip()
   categoria=input("Categoria : ").strip().lower()
   while True:
    try:
        valor=float(input("Valor R$ : "))
        dados.despesas.append({
            "Descrição" : descricao,
            "Valor" : valor,
            "categoria" : categoria
        })
        break
    
    except ValueError:
        print("Valor inválido. Digite um número !")
def adicionar_receita():
       while True:
            try:
                valor=float(input("Valor Da Receita R$ : "))
                dados.receitas.append(valor)
                print(f"Total de Receitas R$ : {sum(dados.receitas)}")
                break
            except ValueError:
                 print("Digite somente números !")


def mostrar_relatorio():
    if len(dados.receitas) == 0 and len(dados.despesas) == 0:
                print('''
    Você não adicionou nenhuma receita ou despesas.
    Para ver o relatório acrescente ao menos uma receita ou despesa !
                ''')
                input()

    else:
            total_despesas=0
            for d in dados.despesas:
                total_despesas+=d["Valor"]
            saldo=sum(dados.receitas)-total_despesas
            print("."*20,"Relatório Financeiro","."*20)
            print("-"*60)
            print(f"Total de Receitas R$ : {sum(dados.receitas):.2f}")
            print("-"*60)
            print(f"Total de Despesas R$ : {total_despesas:.2f}")
            print("-"*60)
            print(f"Saldo final R$ : {saldo:.2f}")
            print("-"*60)

            por_categoria= {}
            for d in dados.despesas:
                cat=d["categoria"]
                if cat in por_categoria:
                    por_categoria[cat] += d["Valor"]
                else:
                    por_categoria[cat]=d["Valor"]
            for cat , valor in por_categoria.items():
                print(f"{cat} : R$ {valor:.2f} ")

            print("-"*60)
            

            if saldo >0:
                    print(f'Saldo positivo : ✅  Parabéns {dados.nome}, você está com um bom saldo.')
            elif saldo == 0:
                print(f'Saldo zero : ❌ {dados.nome} Você zerou seu saldo.')
            else:
                print(f'Saldo negativo :⚠️  {dados.nome}, atenção você está no vermelho ! ')
            print("."*60)