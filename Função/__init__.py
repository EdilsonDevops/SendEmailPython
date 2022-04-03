def enviaemail(meu_email, minha_senha, nome_cli, meu_nome, email_cliente, assunto):
    import smtplib
    from datetime import datetime
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from string import Template
    from email.mime.image import MIMEImage

    # Pasta html

    with open('template.html', 'r', encoding='utf-8') as html:
        template = Template(html.read())
        data_atual = datetime.now().strftime('%d/%m/%Y')
        corpo_msg = template.substitute(nome=nome_cli, data=data_atual)

    msg = MIMEMultipart()
    msg['from'] = meu_nome
    msg['to'] = email_cliente
    msg['subject'] = assunto

    corpo = MIMEText(corpo_msg, 'html')
    msg.attach(corpo)

    # ENVIO DE IMAGEM EM ANEXO

    # Caso queira desativar o anexo coloque hashtag neste procedimento abaixo
    # Caso queira utilizar informe onde está o arquivo
    # Para alterar o nome que aparece no anexo do e-mail altere o nome filename='nome desejado

    with open('python.jpg', 'rb') as img:
        img = MIMEImage(img.read())
        msg.attach(img)
        img.add_header('Content-Disposition', 'attachment', filename='Python.jpg')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(meu_email, minha_senha)
            smtp.send_message(msg)
            print('\033[0;36mE-mail enviado com sucesso.\033[m')
        except Exception as e:
            print('\033[0;31mE-mail não enviado...\033[m')
            print('\033[0;31mErro:\033[m', e)
