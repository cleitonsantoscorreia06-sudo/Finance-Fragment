print('Finance Fragment')
print('SEJA BEM VINDO AO SOFTWARE DE ORGANIZAÇÃO FINANCEIRO MAIS SIMPLES E FUNCIONAL.')
#ENTRADAS
nome=input('Qual é o seu nome : ')
receita=float(input('Informe o valor de pelo menos uma receita : '))
despesa=float(input('informe o valor de uma despesa : '))
#PROCESSO
saldo=receita-despesa
#SAÍDA 
print('='*30)
print('Finance Fragment')
print('='*30)
print(f'Usuário: {nome}')
print('-'*30)
print(f'Receita : R$ {receita:.2f}')
print(f'Despesa : R$ {despesa:.2f}')
print('-'*30)
print(f'Saldo Disponível : R$ {saldo:.2f}')
if saldo >0:
    print('Saldo positivo : ✅  Parabéns, você está com um bom saldo.')
elif saldo == 0:
    print('Saldo zero : Você zerou seu saldo.')
else:
    print('Saldo negativo : Atenção você está no vermelho ! ')

print('='*30)
