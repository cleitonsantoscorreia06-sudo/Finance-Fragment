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
            "Categoria" : categoria
        })
        break
    
    except ValueError:
        print("Valor inválido. Digite um número !")
def adicionar_receita():
       while True:
            try:
                valor=float(input("Valor Da Receita R$ : "))
                dados.receitas.append(valor)
                print(f"Total de Receitas R$ : {sum(dados.receitas):.2f}")
                break
            except ValueError:
                 print("Digite somente números !")


def mostrar_relatorio():
    if len(dados.receitas) == 0 and len(dados.despesas) == 0:
                print('''
    Você não adicionou nenhuma receita ou despesas.
    Para ver o relatório acrescente ao menos uma receita ou despesa !
                ''')


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
                cat=d["Categoria"]
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

def editar_despesas():
     if len(dados.despesas) == 0:
         print("Sem despesas para editar .")
         return


     else:
        for i , item in enumerate(dados.despesas):
            print(f"Indice -> {i} | dicionário -> {item}")
            

     
        while True:
            try:
                indice=int(input("Indice -> "))
                if indice < 0 or indice >= len(dados.despesas):
                     print("Indice inválido.")
                     continue
                campo=input("Qual informação ? ").strip()
                if campo.lower() == "valor":
                     campo="Valor"            
                     informacao=float(input("Digite a informação que deseja inserir : "))

                elif campo.lower() in ("descricao","descrição"):
                     campo="Descrição"
                     informacao=input("Digite a informação que deseja alterar : ").strip()

                elif campo.lower() == "categoria":
                     campo="Categoria"
                     informacao=input("Digite a informação que deseja alterar : ").strip()

                else:  
                    print("Somente campos válidos ! Use -> Descrição,Valor,Categoria.")
                    continue
               
                dados.despesas[indice][campo]=informacao
                print(f'''
                    Informação atualizada : 
                    {dados.despesas[indice]}
                ''')
                break
            except ValueError:
                 print("Digite apenas números .")
            except IndexError:
                 print("Índice digitado não encontrado ! ")



def excluir_despesa():
     if len(dados.despesas) == 0 :
          print("Sem despesas cadastradas !")
          return
     else:
          for c , item in enumerate(dados.despesas):
               print(f"Índice -> {c} | Despesa {item['Descrição']} , {item['Valor']} , {item['Categoria']}")

          while True :
                try:
                        indice=int(input("Digite o índice : "))
                        if indice < 0 or indice >=  len(dados.despesas):
                             print("Indice inválido.")
                             continue

                        
                        dados.despesas.pop(indice)
                        break

                except ValueError:
                        print("Digite somente números !")
                except IndexError:
                        print("indice inválido.")
                

def editar_receita():
     if len(dados.receitas) == 0 :
          print("Nenhuma receita foi colocada .")
          return
    
     for c,s in enumerate(dados.receitas):
          print(f'Indice : {c} -> {s}')
        
     while True:
        try:
            indice=int(input('Digite o índice : '))
            if indice < 0 or indice >=len(dados.receitas):
                 print("Indice inválido .")
                 continue
            valor=float(input("Novo valor R$ : "))
            dados.receitas[indice]=valor
            print(f"Atualizado ✅ ")
            break

        except IndexError:
            print("Erro de Index .")

        except ValueError:
            print("Digite números e letras nos campos adequados .")

def excluir_receita():
     if len(dados.receitas) == 0:
          print("Sem receitas .")
          return
     for c , s in enumerate(dados.receitas):
          print(f"Indice {c} -> {s}")
     while True:
          try:
               exclusao=int(input("Digite o indice : "))
               if exclusao < 0 or exclusao >= len(dados.receitas):
                    print("index inválido . ")
                    continue
               
               dados.receitas.pop(exclusao)
               print(f"Excluido ✅ ")
               break


          except IndexError:
               print("Indice inválida . ")
          except ValueError:
               print("Digite somente números ou palavras em seus respectivos campos.")
