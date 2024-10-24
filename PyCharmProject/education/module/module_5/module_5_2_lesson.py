class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.age = age
        self.surname = surname
        self.say_info()


    def say_info(self):
        print(f'привет меня зовут {self.name}, мне {self.age}')

    def berthday(self):
        self.age +=1
        print(f'у меня день рождения, мне {self.age}')

    def __len__(self):
        return self.age

    def __del__(self):
        print(f'{self.name} ушёл')


egor = Human('Егор','Думов', 22)
Roman = Human('Рома', 'Уразовский', 22)