nota1 = int(input(" Digite sua primeira nota do 1°Bimestre (0-100): "))
nota2 = int(input(" Digite sua  nota do 2°Bimestre (0-100)"))
media = (nota1+nota2) /2
if media >= 60:
    print(f" Você foi aprovado com média {media}")
else:
    print(f" Você foi reprovado com média {media}")
