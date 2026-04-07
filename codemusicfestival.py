#Questão 1
nome_artista = input("Nome do artista: ")
temp_show = int(input("Tempo de show em minutos: "))
cache_artista = float(input("Cachê do artista: "))
print()
custo_min = cache_artista/temp_show
print(f'Artista: {nome_artista}\nDuração: {temp_show} minutos\nCusto por minuto: R$ {custo_min:.2f}')

#Questão 2
if cache_artista > 1 and cache_artista <= 5000:
    print("Artista Independente")
elif cache_artista > 5000 and cache_artista <= 20000:
    print("Artista Popular")
elif cache_artista > 20000:
    print("Headliner")
print()    
# Questão 3
lineup = []
for i in range(4):
    nome = input(f'Informe o {i+1}º do lineup: ')
    lineup.append(nome)
print()
for nomes in lineup:
    print(nomes)
print()
print(f'Primeiro: {lineup[0]}\nÚltimo: {lineup[-1]}')
print()
# Questão 4
publico = int(input("Informe a quantidade de pessoas que entraram no festival: "))
for i in range(1, publico+1):
    texto = "pessoa entrou" if i == 1 else "pessoas entraram"
    print(f'{i} {texto} no festival')
print()
# Questão 5
notas = []
for i in range(4):
    nota = float(input(f'Informe uma nota de 0 a 10 para o {i+1} artista do lineup: '))
    notas.append(nota)
print()
for i in range(4):
    print(f'{lineup[i]} - {notas[i]:.1f}')

soma = 0
for nota in notas:
    soma += nota
media = soma / len(notas)
print(f'Média das avaliações: {media:.1f}')
print()
# Questão 6
qtd_ingressos = int(input("Informe a quantidade de ingressos vendidos: "))
i = 0
inteira = 100
meia = 50
total = 0
inteira_qtd = 0
meia_qtd  = 0
while i < qtd_ingressos:
    tipo = int(input(f'Ingresso {i+1} (1 - Inteira / 2 - Meia): '))
    if tipo != 1 and tipo != 2:
        print("Tipo inválido")
        continue
    if tipo == 1:
        total += inteira
        inteira_qtd += 1
    elif tipo == 2:
        total += meia
        meia_qtd += 1 
    i += 1
print()
print(f'Total arrecadado: R$ {total:.2f}\nQuantidade de ingressos: {qtd_ingressos}\nInteiras: {inteira_qtd}\nMeias: {meia_qtd}')
print()
# Questão 7
busca = input("Informe o nome de um artista para buscar no lineup: ")
if busca in lineup:
    print("Artista confirmado no festival!")
else:
    print("Artista não encontrado.")