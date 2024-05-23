import random
alunos = ['Joao', ' Maria', ' Pedro', 'Guilherme', 'Ana']
print(f' Lista: {alunos}')
# Embaralhar a Lista
random.shuffle(alunos)
print(f' Lista embaralhada: {alunos}')
# Ordenar a Lista Crescente
alunos.sort()
print (f'Lista crescente: {alunos}')
# Ordenar a Lista Decrescente
alunos.sort(reverse=True)
print(f' Lista decrescente:{alunos}')