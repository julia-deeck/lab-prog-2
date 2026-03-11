nome_cliente = input("Informe seu nome: ")
item_pedido = input(f'{nome_cliente}, deseja registrar um novo item no pedido? (S/N) ').upper()
total_pedido = 0

while item_pedido == 'S':
    valor_item = float(input(("Informe o valor do item (Digite 0 para cancelar): ")))
    if valor_item > 50:
        print("Item premium")
    elif valor_item > 20:
        print("Item normal")
    else:
        print("Item econômico")
    if valor_item == 0:
        print(f'Pedido de {nome_cliente} cancelado')
        break
    if valor_item < 0:
        print("Valor inválido, tente novamente")
        continue
    total_pedido += valor_item
    item_pedido = input(f'{nome_cliente}, deseja registrar um novo item no pedido? (S/N) ').upper()
else:
    print(f'Valor total do pedido de {nome_cliente}: R$ {total_pedido:.2f}')