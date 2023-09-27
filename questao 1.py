lista = list()
alunos = dict()
#
soma = total = 0 
media = 0
#
while(True):
    total+=1
    alunos['Nome'] = input('Nome: ')
    alunos['Idade'] = int(input('Idade: '))
    alunos['Altura'] = float(input('Altura: '))
    soma+=alunos['Altura']
    media =+  (soma/ total)
    lista.append(alunos.copy())
    alunos.clear()
    if(int(input('Deseja continuar: [1]SIM / [2]NAO: '))== 2):
        break
#
for valor in lista:
    if(valor['Altura'] > media and valor['Idade'] < 15):
        print(f' O aluno {valor["Nome"]} tem {valor["Idade"]}anos e altura {valor["Altura"]} portanto esta apto')