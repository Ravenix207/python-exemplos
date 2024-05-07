print(f" Programa de empréstimo\n"
      f"Responda: (0-Não ou 1-Sim)\n")
nome_negativado=int(input(" Possui nome negativado?: "))
if nome_negativado == 1:
    print(" Não pode realizar o empréstimo")
else:
    carteira_assinada=int(input(" Possui carteira assinada?: "))
    if carteira_assinada == 0:
        print(" Não pode realizar o empréstimo")
    else:
        casa_propria=int(input(" Possui casa própria?: "))
        if casa_propria == 0:
            print(" Não pode realizar o empréstimo")
        else:
            print(" Conceder empréstimo")