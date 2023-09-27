lista = list()
#
total_comissoes = 0
#
while(True):
    nome = input('Nome do vendedor: ')
    vendas = float(input('Valor vendido R$: '))
    comissao = 0
    comissao = 200 + ((3.5/100) * vendas)
    total_comissoes+=comissao
    lista.append([nome, [vendas], [comissao]])
    if(int(input('Deseja adicionar mais vendedores [1]SIM / [2]NAO: ')) == 2):
        break
#
print('')
#
for c in lista:
    print(f'vendedor: {c[0]} vendeu R${c[1]} e comissão a ser paga é de R${c[2]}')
#
print('')
print(f'Total de comissões pagas R$: {total_comissoes}')