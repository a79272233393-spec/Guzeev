from itertools import count


class Animal(object):
    def voice(self):
        pass
    count = 0
    def __init__(self):
        Animal.count +=1
    def summa(self):
        print('Количество всех созданных экземпляров животных = '+ str(Animal.count))
    summa = staticmethod(summa)

class Dog(Animal):
    def voice(self):
        print('ГАВ-ГАВ')


class Cow(Animal):
    def voice(self):
        print('МУУ-МУУ')


class Cat(Animal):
    def voice(self):
        print('МЯУ-МЯУ')



Sharik = Dog()
Rex = Dog()
Burenka = Cow()
Mumu = Cow()
Murzik = Cat()
Vaska = Cat()
Piq = Animal()

Animal.summa(count)

