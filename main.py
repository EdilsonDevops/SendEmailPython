python
from Função import enviaemail

# Inicialização
while True:
    print('\n\033[3;36m           Bem vindo ao envio de E-mail com python\033[m\n')
    print('''Aviso: Para ser efetuado o procedimento é preciso\n
          -Liberar o envio smtp na conta do Gmail 
          -Verificar se os dados estão preenchidos corretamente
          -Caso seja outro provedor de mensagem configurar a porta e o host SMTP
          -leia o README\n''')
    continuar = 1
    while continuar != 4:
        if continuar == 1:
            # meu_email
            while continuar != 4:
                meu_email = str(input('\033[3;35m Digite seu e-mail: \033[m'))
                continuar = int(
                    input('\033[3;32m[1] Continuar \033[m\033[3;33m[2] Corrigir \033[m\033[3;31m[3] Sair\033[m\n'))

                if continuar > 3:  # exceção maior
                    print("\033[3;31mAviso: escolha um número de 1 a 3.\033[m")
                    continuar = 2

                elif continuar < 1:  # exceção menor
                    print("\033[3;31mAviso: Opção zero inválida.\033[m")
                    continuar = 2

                while continuar != 4:
                    if continuar == 1:
                        # minha senha
                        while continuar != 4:
                            if continuar > 4:  # exceção maior
                                print("\033[3;31mAviso: escolha um número de 1 a 4.\033[m")
                            if continuar < 1:  # exceção menor
                                print("\033[3;31mAviso: Opção zero inválida.\033[m")
                            minha_senha = str(input('\033[3;35mDigite sua senha: \033[m'))  # '
                            continuar = int(
                                input(
                                    '\033[3;32m[1] Continuar \033[m\033[3;34m [2] Retornar opção anterior \033[m\033[3;33m[3] Corrigir \033[m\033[3;31m[4] Sair\033[m\n'))
                            if continuar == 1:
                                # nome cli
                                continuar2 = 1
                                while continuar2 != 4:
                                    if continuar2 > 4:  # exceção maior
                                        print("\033[3;31mAviso: escolha um número de 1 a 4.\033[m")
                                    if continuar2 < 1:  # exceção menor
                                        print("\033[3;31mAviso: Opção zero inválida.\033[m")
                                    nome_cli = str(input('\033[3;35mDigite o nome do cliente: \033[m'))
                                    continuar2 = int(
                                        input(
                                            '\033[3;32m[1] Continuar \033[m\033[3;34m [2] Retornar opção anterior \033[m\033[3;33m[3] Corrigir \033[m\033[3;31m[4] Sair\033[m\n'))
                                    if continuar2 == 1:
                                        # meu nome
                                        continuar3 = 1
                                        while continuar3 != 4:
                                            if continuar3 > 4:  # exceção maior
                                                print("\033[3;31mAviso: escolha um número de 1 a 4.\033[m")
                                            if continuar3 < 1:  # exceção menor
                                                print("\033[3;31mAviso: Opção zero inválida.\033[m")
                                            meu_nome = str(input('\033[3;35mDigite seu nome: \033[m'))
                                            continuar3 = int(input(
                                                '\033[3;32m[1] Continuar \033[m\033[3;34m [2] Retornar opção anterior \033[m\033[3;33m[3] Corrigir \033[m\033[3;31m[4] Sair\033[m\n'))
                                            if continuar3 == 1:
                                                # email cliente
                                                continuar4 = 1
                                                while continuar4 != 4:
                                                    if continuar4 > 4:  # exceção maior
                                                        print("\033[3;31mAviso: escolha um número de 1 a 4.\033[m")
                                                    if continuar4 < 1:  # exceção menor
                                                        print("\033[3;31mAviso: Opção zero inválida.\033[m")
                                                    email_cliente = str(
                                                        input('\033[3;35mDigite o email do cliente: \033[m'))
                                                    continuar4 = int(
                                                        input(
                                                            '\033[3;32m[1] Continuar \033[m\033[3;34m [2] Retornar opção anterior \033[m\033[3;33m[3] Corrigir \033[m\033[3;31m[4] Sair\033[m\n'))
                                                    if continuar4 == 1:
                                                        # assunto
                                                        continuar5 = 1
                                                        while continuar5 != 4:
                                                            if continuar5 > 4:  # exceção maior
                                                                print(
                                                                    "\033[3;31mAviso: escolha um número de 1 a 4\033[m")
                                                            if continuar3 < 1:  # exceção menor
                                                                print("\033[3;31mAviso: Opção zero inválida.\033[m")
                                                            assunto = str(input('\033[3;35mDigite o assunto: \033[m'))
                                                            continuar5 = int(input(
                                                                '\033[3;32m[1] Confirmar envio \033[m\033[3;34m [2] Retornar opção anterior \033[m\033[3;33m[3] Corrigir \033[m\033[3;31m[4] Sair\033[m\n'))
                                                            if continuar5 == 1:
                                                                # Envio do E-mail
                                                                print(
                                                                    '\033[3;33mAguarde: Envio de E-mail em processamento...\033[m')
                                                                enviaemail(meu_email, minha_senha, nome_cli, meu_nome, email_cliente, assunto)
                                                                continuar5 = 4
                                                            if continuar5 == 2:
                                                                break
                                                            if continuar5 == 4:
                                                                continuar4 = 4
                                                    if continuar4 == 2:
                                                        break
                                                    if continuar4 == 4:
                                                        continuar3 = 4
                                            if continuar3 == 2:
                                                break
                                            if continuar3 == 4:
                                                continuar2 = 4
                                    if continuar2 == 2:
                                        break
                                    if continuar2 == 4:
                                        continuar = 4
                            if continuar == 2:
                                break
                    if continuar == 2:
                        break
                    if continuar == 3:
                        continuar = 4

    pergunta = str(input('Deseja continuar?: [S/N] ')).upper()
    if pergunta == 'N':
        break
    elif pergunta != 'S':
        print('\033[0;31mAviso : Opção inválida\033[m')
        print('Digite [S/N]:')
        pergunta = str(input('Deseja continuar [S/N]? ')).upper()
        if pergunta == 'N':
            break
print("\033[0;31mPrograma encerrado.\033[m")
print('\n\033[3;36m           Obrigado por utilizar o sistema de envio de E-mail com python\033[m\n')
