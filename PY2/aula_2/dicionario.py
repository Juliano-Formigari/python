emails = {}
#Adicionando itens ao dicionário
emails['juca'] = 'juca@gmail.com'
emails['joaozinho'] = 'joaozinho@gmail.com'
emails['mariazinha'] = 'mariazinha@google.com'

#Listar os itens em dicionário
print(emails)

#Lista o email de mariazinha
print(emails['mariazinha'])

if 'mariazinha' in emails:
    print('Existe')
    emails['mariazinha'] = 'EmailAtualizado@gmail.com'
else:
    print('Não existe')
    emails['Ana'] = 'novoEmail@gmail.com'

print(emails)

#Remover um item de email
emails.pop('juca')
print(emails)