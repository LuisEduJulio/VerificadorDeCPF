print('Desafio do Algotinho')
print('-'*20)
ListaUsuario = []
Dicionario = {'Luis':'0001'}
ListaUsuario.append(Dicionario)

quantidade = int(input('Quantos usuários deseja cadastrar? '))

contador = 0
for contador in range(quantidade):
    Name = str(input('Entre com o seu nome: '))
    CPF = str(input('Entre com o seu cpf: '))
    #verifica se o nome e cpf já existe
    if Name in Dicionario.values():
        print('Este nome já existe!')
    elif CPF in Dicionario.values():
        print('Este CPF já existe!')
    else:
        Dicionario[Name] = CPF
        print('Usuário cadastrado!')
print('-'*20)
print(ListaUsuario)