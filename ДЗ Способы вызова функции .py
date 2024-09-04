def send_email(message='',recipient='',sender = "university.help@gmail.com"):
    key_words =['@','.com', '.ru','.net']
    check_rec=0
    check_sen=0
    for i in key_words:
        if i in recipient:
            check_rec=check_rec+1
        if i in sender:
            check_sen=check_sen+1
    if check_rec!=2:
        print('Вы допустили ошибку при написаниии адреса получателя, исправте адрес')
        return
    if check_sen!=2:
        print('Вы допустили ошибку при написаниии адреса отправителя, исправте адрес')
        return
    if recipient==sender:
        print('Вы допустили ошибку при написаниии адресов,они совпадают, исправте адрес')
        return
    if recipient=='urban.student@mail.ru':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'Нестандартный отправитель. Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')