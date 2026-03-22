passageiros = ['Ana','Bruno','Carlos','Daniela','Eduardo']
for passageiro in passageiros:
    print(passageiro)

for passageiro in passageiros:
    if passageiro == "Carlos":
        print("Carlos perdeu o check-in")
        continue
    print(f'{passageiro} realizou o check-in')
    
for passageiro in passageiros:
    if passageiro == "Carlos":
        print("Carlos perdeu o embarque")
        continue
    if passageiro == "Daniela":
        break
    print(f'{passageiro} pode embarcar')
print("Embarque encerrado")

for i in range(1, 6):
    print(f'Passageiro {i}: {passageiros[i-1]}')