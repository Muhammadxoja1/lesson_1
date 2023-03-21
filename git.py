users_list = [['admin', 'admin']]

user_login = input('Введите логин: ')
user_password = input('Введите пароль')
current_user = []
for user in users_list:
    login, password = user
    if user_login == login:
        current_user = user
        break


if not current_user:
    print("Пользователь не найден!")
    exit()


db_login, db_password = current_user
if user_password != db_password:
    print('Неправильный пароль: ')
    exit()

print('Успешно вошли на свой аккаунт!')

