# exercicio 01
nome_cliente = input("Nome do cliente: ")
print(f'Bem-vindo ao PetVida, {nome_cliente}')

# exercicio 02
idade_pet = int(input("Digite a idade do pet: "))
if idade_pet < 2:
    print("Filhote")
elif idade_pet > 7:
    print("Idoso")
else:
    print("Adulto")

# exercicio 03
peso_pet = float(input("Digite o peso do pet: "))
if peso_pet >= 40: 
    print("Atendimento especial") 
else: 
    print("Atendimento normal")

# exercicio 04
temp_pet = float(input("Digite a temperatura do pet: "))
if temp_pet >= 39:
    print("Febre")
else:
    print("Temperatura normal")

# exercicio 05
vacinado = input("O pet é vacinado?: ")
if vacinado == "s":
    vacinado = True
elif vacinado == "n":
    vacinado = False
else:
    print("Digite um comando válido")

if vacinado == True and idade_pet >= 1: 
    print("Pode usar o hotelzinho") 
else: 
    print("Não pode usar o hotelzinho")

# exercicio 06
if idade_pet > 10 or peso_pet < 2: print("Grupo de risco")

# exercicio 07
servico = input("Serviço desejado: ")
if servico == None:
    print("Erro! Digite o serviço desejado")

# exercicio 08
telefone = int(input("Digite o telefone: "))
if nome_cliente or telefone == None: print("Cadastro inválido. Informe nome e telefone")

# exercicio 09
tipo_pet = input("Digite o tipo do pet:\n[1] - Cachorro\n[2] - Gato\n[3] - Ave")
match tipo_pet:
    case 1:
        print("Cachorro")
    case 2:
        print("Gato")
    case 3:
        print("Ave")
    case _:
        print("Inválido")

# exercicio 10
plano_cliente = int(input("Digite o plano do cliente:\n[1] - Básico\n[2] - Premium\n[3] - VIP"))
match plano_cliente:
    case 1:
        print("Benefícios Básico: Descontos em produtos para pet")
    case 2:
        print("Benefícios Premium: Vacinação com desconto")
    case 3:
        print("Benefícios VIP: Acompanhamento mensal com desconto")
    case _:
        print("Inválido")

# exercicio 11
nota_satis = int(input("Digite a nota de satisfação de 0 a 10: "))
if nota_satis >= 9:
    print("Excelente")
elif nota_satis >= 7:
    print("Bom")
elif nota_satis >= 5:
    print("Regular")
else:
    print("Ruim")

# exercicio 12
idade_pet = int(input("Digite a idade do pet: "))
if idade_pet < 2:
    print("Filhote")
elif idade_pet > 7:
    print("Idoso")
else:
    print("Adulto")

# exercicio 13
if idade_pet >= 1 and peso_pet >= 2:
    print("Pet pode fazer cirurgia")

# exercicio 14
tranquilo = None
agitado = None
comport = input("Qual o comportamento do pet: [1]tranquilo ou [2]agitado")
if comport == 1:
    tranquilo = True
elif comport == 2:
    agitado = True
else:
    print("Comportamento inválido")

if temp_pet >= 39 and agitado == True: print("Emergência")

# exercicio 15
valor_compra = float("Valor da compra: ")

if valor_compra >= 200 or plano_cliente == 3:
    print("Compra com desconto")

# exercicio 16
senha = 123456
login_senha = int(input("Digite sua senha: "))

if login_senha == senha:
    print("Logado com sucesso")
else:
    print("Acesso negado")

# exercicio 17
pet_nome = input("Digite o nome do pet: ")

if pet_nome == None:
    pass
else:
    print("Pet registrado")

# exercicio 18
nota_profi = int(input("Digite uma nota para o profissional que lhe atendeu de 0 a 5: "))
nota_servi = int(input("Digite uma nota para avaliar o serviço de 0 a 5: "))

media_serv = nota_servi + nota_profi / 2

if media_serv > 3:
    print("Boa avaliação")
else:
    print("Avaliação ruim")

# exercicio 19
if temp_pet >= 39:
    print("Emergência")
elif peso_pet < 2:
    print("Atenção")
elif idade_pet > 10:
    print("Monitoramento")
else:
    print("Normal")