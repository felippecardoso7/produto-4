# Produto instruções

# Estrutura do produto
Produto ={'Nome': '', 'Preço': 0.0, 'Quantidade': 0.0, 'Disponivel': False}

# Entrada
print('\n\t\t\t -- Produto do Mercado --\n')
Produto['Nome'] = input('informe o nome: ')
Produto['Preço'] = float(input(('informe o Preço')))
Produto['Quantidade'] = float(input(('informe a Quantidade')))
total = Produto['Preço'] * Produto['Quantidade']


# Processamento
Produto['Disponivel'] = True

# Saida
print(f'Nome........{Produto["Nome"]}')
print(f'Preço........{Produto["Preço"]}')
print(f'Quantidade.......{Produto["Quantidade"]}')
print(f'Disponivel.......{Produto["Disponivel"]}')
print(f'Total R$ {total}')
