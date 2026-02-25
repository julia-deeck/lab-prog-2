dia_da_semana = int(input("Informe um dia da semana entre 1 e 7: "))

match dia_da_semana:
    case 1:
        print("Segunda")
    case 2:
        print("Terça")
    case 3:
        print("Quarta")
    case 4: 
        print("Quinta")
    case 5:
        print("Sexta")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Dia inválido")

match dia_da_semana:
    case 1 | 2 | 3 | 4 | 5:
        print("Dia da semana")
    case 6 | 7:
        print("Fim de semana")
    case _:
        print("Dia inválido")