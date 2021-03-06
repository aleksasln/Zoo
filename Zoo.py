# -*- coding: utf-8 -*-

from random import randint

class Zoo(): #Объявление класса Зоопарк
    def __init__(self, count_v = randint(1,5)):
        #Здесь записываются все те переменные, которые будут доступны всем остальным наследуемым классам 
        self.list_animals = ['Жираф'] #Список отдельно для сухопутных животных, которые есть у игрока (список будет пополняться за счёт покупок в магазине)
        self.cages = ['Клетка'] #Список вольеров для сухопутных, которые есть у игрока (животное нельзя купить, пока кол-во клеток будет меньше числа животных)
        self.aquariums = [] #Список вольеров отдельно для морских животных
        self.budget = 20 #Переменная, определяющая начальный капитал зоопарка, будет изменяться за счет покупок в магазине и продажи билетов
        self.count_v = count_v
    
    def income(self, price):
        self.price = price
        list_of_ages = [] #Список возрастов посетителей в группе 
        for age in range(self.count_v): #Цикл перебирает каждого посетителя в группе
            age = randint(1, 100) #Запись в переменную age случайный возраст посетителя
            list_of_ages.append(age) #Запись в список list_of_ages возраст каждого посетителя
        for age in list_of_ages: #Определение цены билета для покупателей
            if age < 6: #Если посетителю < 6, цена билета = 0
                continue 
            else:
                self.budget += self.price #Прибавление дохода от продаж билетов
    
    def expenditure(self, price):
        self.price = price
        if self.budget > price:
            self.budget -= price
        else:
            print('Недостаточно средств. Откройте зоопарк для посетителей, чтобы заработать монеты.')    
    
    
''' available 
Все остальные классы должны наследовать переменные класса Зоопарк, 
чтобы при покупках в магазине или при продаже билетов, их можно было изменять
'''
   
class Money():
    
    def __init__(self, budget = 20):
        self.budget = budget
        self.count_v = 0
        self.budget = 20
    
    def update_count_v(self):
        self.count_v = randint(1,5)
        return self.count_v
        
    def income(self, price):
        self.price = price
        list_of_ages = [] #Список возрастов посетителей в группе 
        for age in range(self.count_v): #Цикл перебирает каждого посетителя в группе
            age = randint(1, 100) #Запись в переменную age случайный возраст посетителя
            list_of_ages.append(age) #Запись в список list_of_ages возраст каждого посетителя
        for age in list_of_ages: #Определение цены билета для покупателей
            if age < 6: #Если посетителю < 6, цена билета = 0
                continue 
            else:
                self.budget += self.price
                
    def expenditure(self, price):
        self.price = price
        if self.budget > price:
            self.budget -= price
        else:
            print('Недостаточно средств. Откройте зоопарк для посетителей, чтобы заработать монеты.')
    
    def read_budget(self):
        print('Ваши монеты: ', self.budget)


class Visitors(Zoo): #Объявление класса посетителей 
    
    def __init__(self):
        super().__init__(count_v = 0)
        self.count_v = 0
        self.budget = 20
    
    def update_count_v(self):
        self.count_v = randint(1,5)
    
    def read_count_visitors(self):        
        #print('Количество посетителей за сегодня: '+ str(self.count_v()))
        return self.count_v
    
    def read_income(self):
        #print('Ваши монеты: ' + str(self.budget))
        return self.budget
       
    def income_from_visit(self):
        list_of_ages = [] #Список возрастов посетителей в группе 
        for age in range(self.count_v): #Цикл перебирает каждого посетителя в группе
            age = randint(1, 100) #Запись в переменную age случайный возраст посетителя
            list_of_ages.append(age) #Запись в список list_of_ages возраст каждого посетителя
        for age in list_of_ages: #Определение цены билета для покупателей
            if age < 6: #Если посетителю < 6, цена билета = 0
                continue 
            else:
                self.budget += 5 #Прибавление дохода от продаж билетов  
    
        
class Cage(Zoo):
    
    def __init__(self, kind_cage):
        super().__init__()
        self.kind_cage = kind_cage
        
    def price_cage(self, price):
        if self.budget > 0:
            self.budget -= price
        else:
            print('Недостаточно средств. Откройте зоопарк для посетителей, чтобы заработать монеты.')
    
    def list_cage(self):  
        if self.budget > 0:
            self.cages.append(self.kind_cage)
            return self.cages
        else:
            return self.cages
    
    def list_aqua(self):
        if self.budget > 0:
            self.aquariums.append(self.kind_cage)
            return self.aquariums
        else:
            return self.aquariums
    
    def read_budget(self):               
        print("Ваши монеты: " + str(self.budget))
    
    def read_cage(self):
        print('Количество клеток: ' + str(len(my_cage.list_cage())))
        
    def read_aqua(self):
        print('Количество аквариумов: '+ str(len(my_cage.list_aqua())))

class Animals(Zoo):
    
   def __init__(self, kind_animals, price):
      super().__init__()
      self.kind_animals = kind_animals
      self.price = price
      
   def update_list_animals(self, kind_animals):
       self.list_animals.append(kind_animals)
       return self.list_animals
   
   def read_list_animals(self):
       
       print('Список ваших животных:')
       i = 1
       for animal in self.list_animals:
           i += 1
           print(str(i) +'. '+ str(animal))

        
my_cage = Cage('Клетка')
my_visitors = Visitors()
my_money = Money()

while True:
        answer = int(input('''
              \n Добро пожаловать в зоопарк!
              \n Что вы хотите сделать ? (Выберите номер функции)
              \n 1. Отправиться в магазин.
              \n 2. Открыть зоопарк для посетителей.
              \n 3. Вызов справки.
              \n 4. Выйти из зоопарка.
              \n 5. Посмотреть мой профиль.
              '''))
        while answer < 1 or answer > 5:
            answer = int(input('Попробуйте еще раз! Выберите номер, соответсвующий функции. '))
        
        if answer == 1:
            answer_2 = int(input('''
                             \n Что вы хотете купить?
                             \n 1.Список вольеров
                             \n 2.Корм для животных
                             \n 3.Список животных
                             \n 4.Украшения для зоопарка
                             \n 5.Назад
                             '''))
            if answer_2 == 1:
                answer_3 = ''
                while True:
                    answer_3 = int(input('''
                                     \nВыберите тип вольера. Нажмите номер соответсвующий выбранному типу:
                                         \n 1. Клетка
                                         \n 2. Аквариум
                                         \n 3. Назад
                                         '''))
                    if answer_3 == 1:                        
                        my_cage.read_cage()
                        my_money.expenditure(10)
                        my_money.read_budget()
                        
                    elif answer_3 == 2:
                        my_cage.read_aqua()
                        my_money.expenditure(10)
                        my_money.read_budget()
                        
                    elif answer_3 == 3:
                        break   
            elif answer_2 == 3:
                choose = int(input('''Выберите животное, которое хотите купить: 
                   1.Жираф - 50 монет 
                   2.Коала - 90 монет
                   3.Орел - 70 монет
                   4.Дельфин - 75 монет
                   5.Тигр - 85 монет
                   '''))
                   
                giraffe = Animals('Жираф', 50)
                coala = Animals('Коала', 90)
                eagle = Animals('Орел', 70)
                dolphin = Animals('Дельфин', 75)
                tiger = Animals('Тигр', 85)
                
                while choose < 1 or choose > 5:
                    print(input('Попробуйте еще раз! Выберите номер, соответсвующий функции. '))
                if choose == 1:
                    giraffe.update_list_animals('Жираф')
                    my_money.expenditure(50)
                    my_money.read_budget()
                    giraffe.read_list_animals()
                if choose == 2:
                    coala.update_list_animals('Коала')
                    my_money.expenditure(90)
                    my_money.read_budget()
                    coala.read_list_animals()
                if choose == 3:
                    eagle.update_list_animals('Орёл')
                    my_money.expenditure(70)
                    my_money.read_budget()
                    eagle.read_list_animals()
                if choose == 4:
                    dolphin.update_list_animals('Дельфин')
                    my_money.expenditure(75)
                    my_money.read_budget()
                    dolphin.update_list_animals()
                if choose == 5:
                    tiger.update_list_animals('Тигр')
                    my_money.expenditure(85)
                    my_money.read_budget()
                    tiger.update_list_animals()
                    
            elif answer_2 == 4:
                while answer_3 != 5:
                    answer_3 = int(input('''
                             \n Что вы хотете купить?
                             \n 1. Цветы - 15 р. (+0,25 к рейтингу)
                             \n 2. Деревья - 20 р. (+0,25 к рейтингу)
                             \n 3. Скамьи 30 р. (+0,5 к рейтингу)
                             \n 4. Кафе 100 р. (+1 к рейтингу)
                             \n 5. Назад
                             '''))
            elif answer_2 == 5:
                break
                
        elif answer == 2:
            '''Зоопарк работает, приходят посетители'''
            
            print('Кол-во посетителей за сегодня: ', str(my_money.update_count_v()))
            my_money.income(5)
            my_money.read_budget()
        
        elif answer == 3:
            print('''Добро пожаловать в зоопарк! 
                     ...(инструкция для использования программы)
                  ''')
        elif answer == 4:
             print('''До встречи! Приходите еще!
                  ''')
             break
        elif answer == 5:
            print()
