import json

receitas=[]
despesas=[]
nome=" "

def salvar():
    dados_para_salvar={
        'nome':nome,
        'despesas':despesas,
        'receitas':receitas
    }

    with open('dados.json','w',encoding='utf-8') as arquivo:
        json.dump(dados_para_salvar,arquivo,indent=4,ensure_ascii=False)



def carregar():
    global nome,receitas,despesas
    try:

        with open('dados.json','r',encoding='utf-8') as arquivo :
            conversao=json.load(arquivo)

        nome=conversao['nome']
        despesas=conversao['despesas']
        receitas=conversao['receitas']

    except FileNotFoundError:
        pass
