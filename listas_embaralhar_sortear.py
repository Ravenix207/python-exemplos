import random
alunos = ['Joao', ' Maria', ' Pedro', 'Guilherme', 'Ana']
print(f' Lista: {alunos}')
# Embaralhar a Lista
random.shuffle(alunos)
print(f' Lista embaralhada: {alunos}')
# Escolher um aluno aleatóriamente
aluno_sorteado = random.choice(alunos)
print(f' Aluno sorteado: { aluno_sorteado}')