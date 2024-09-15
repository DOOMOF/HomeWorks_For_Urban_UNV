#Класс Базы данных где, храниться логин и пароль
class DataBase:
    def __init__(self):
        self.data = {}
    def add_user(self, username, password):
        self.data[username] = password
#Класс Пользователя
class User:
    """
    Класс пользователя, держащий атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
         self.username = username
         if password == password_confirm:
             self.password = password


if __name__ == '__main__':
    Database = DataBase()

    while True:
        print('--------------------------------------------')
        choice = int(input('Приветствую, Шнырь! Выбери действие: \n1 - Вход\n2 - Регистрация\n'))
        if choice == 1:
            login = input('Введи имя: ')
            if login != login1:
                print(f'пошел нахуй, {login}')
                continue
            password = input(f'Введи пароль, {login}: ')
            if password != password2:
                print('пшол нахуй, пароль не верный')
                continue
            if login in Database.data:
                if password == Database.data[login]:
                    print('здравствуйте, Господин!')
                    break
            else:
                print('Ты кто такой, сука ?')
        if choice ==2:
            user = User(login1 := input('Введите логин: '), password := input('Введите пароль: '),
                        password2 := input('Повторите пароль: '))
            if password != password2:
                print('пароли не совпадают, ИДИ подумай еще раз')
                print('--------------------------------------------')
                continue
            Database.add_user(user.username, user.password)

