#Formatação de Strings
from datetime import datetime
ano_atual = datetime.now() .year
clube = 'Corinthians'
ano_fundacao =1890
campeonato_mundial = 7
print(f"{clube} possui { campeonato_mundial} titulos mundiais. ")
print(f" São { ano_atual - ano_fundacao} anos de existência.")
 