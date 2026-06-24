class Animal:
    def voice(self):
        pass

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
Burenka = Cow()
Murzik = Cat()
print (Sharik.voice())
print(Burenka.voice())
print(Murzik.voice())