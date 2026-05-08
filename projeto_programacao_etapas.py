#Critérios de avaliação
aulas_anuais = 1.200 #por dia, e não por hora.
frequencia_minima = 300 #por dia
nota_minima = 6

##########################


#Aulas de 50 minutos: Aproximadamente 1.200 aulas.
nome = input('Digite o nome do aluno: ')
frequencia_minima = 300 #dias
freq = float(input('Digite quantas aulas o aluno frequentou: '))
if freq < frequencia_minima:
    print('Reprovado (a) por falta.')
    print('          ')
else:
    print('Aprovado (a).')
    print('          ')

##########################

materias = 1
while materias < 6: 
    materia = input('Digite a matéria: ')
    materias += 1


for i in range(5):
    if i == 0:
        materia = 'Portugues'
        print('          ')
    elif i == 1:
        materia = 'Matematica'
        print('          ')
    elif i == 2:
        materia = 'Fisica'
        print('          ')
    elif i == 3:
        materia = 'Ed. Fisica'
        print('          ')
    else:
        materia = 'Ingles'
        print('          ')

    print('\n--- ' + materia + ' ---')
    
    soma_notas = 0
    bimestre = 1
    
    while bimestre <= 4:
        print('Nota', bimestre, 'de', materia, ':')
        nota = float(input())
        print('          ')
        soma_notas = soma_notas + nota
        
        
        
        bimestre = bimestre + 1

    media = soma_notas / 4
    print('Media Final em', materia, ':', media)
    print('          ')

    if media < 6:
        print('Recuperacao Final')
        print('          ')
        print('NOVA PROVA FINAL')
        nova_prova = float(input('Digite a nota da nova prova final: '))
        if nova_prova < 6:
            print('Reprovado!')
            print('          ')
        else:
            print('Aprovado!')
            print('          ')
    else:
        print('Aprovado')
        print('          ')

#O arquivo foi feito em conjunto.

