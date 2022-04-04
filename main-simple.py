from Função import enviaemail

print('\n\033[3;36m           Bem vindo ao envio de E-mail com python\033[m\n')
print('''Aviso: Para ser efetuado o procedimento é preciso\n
          -Liberar o envio smtp na conta do Gmail 
          -Verificar se os dados estão preenchidos corretamente
          -Caso seja outro provedor de mensagem configurar a porta e o host SMTP
          -leia o README\n''')

meu_email = 'MeuEMAIl@gmail.com'
minha_senha = 'Minha senha'
nome_cli = 'Nome do cliente'
meu_nome = 'Meu nome'
email_cliente = 'E-mail do Cliente'
assunto = 'Assunto'

enviaemail(meu_email, minha_senha, nome_cli, meu_nome, email_cliente, assunto)
print("\033[0;31mPrograma encerrado.\033[m")
print('\n\033[3;36m           Obrigado por utilizar o sistema de envio de E-mail com python\033[m\n')
