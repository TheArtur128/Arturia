import sys
sys.path.append("E:\Python\My Library")
from random import randint as random
from Library import remove_wich_list
from Library import found_in_list
from Library import random_name
from Library import skip_itiration

#Суперкласс для всего, кроме абстракций
class Base:
    LINKS = [] #Прострнство ссылок на все обьекты
    def __init__(self, name=None, place=None):
        __class__.LINKS.append(self)
        self.__name = name
        #Ссылка на локацию выше по иейрархии
        if place is None:
            self.__where = Location.WORLD
        else:
            if place.__class__ != Location: raise TypeError ("Must be location")
            self.__where = place
            place.items.append(self)

    def __repr__(self):
        return f"<{self.name}>"

    @property
    def name(self): return self.__name
    @name.setter
    def name(self, name): self.__name = name
    @name.deleter
    def name(self): self.__name = None

    @property
    def where(self): return self.__where
    @where.setter
    def where(self, place): self.__where = place

#Способность иметь что-либо: предметы для живого и локаций, также иейрархии ссылок для локкаций. Абстактный класс
class Wallet:
    def __init__(self):
        #Ссылки
        self.__items = []

    @property
    def items(self): return self.__items
    @items.setter
    def items(self, place): self.__items = place

#Все посещаемое
class Location(Base, Wallet):
    #Миры, всегда находяться на вершине иейрархии
    WORLD = "World"
    OBLIVION = "Oblivion"
    def __init__(self, name=None, place=None):
        super().__init__(name, place)
        #Ссылки на граничищие локации
        self.__read = []
        self.__river = []
        Wallet.__init__(self)

    #property - качество дорог: 0 - хорошие, 1 - плохие, 2 - отсутсвуют
    #Если значения уже есть то мы их перезаписываем методом _read_remove
    def _read_add(self, location, property=2):
        self._clear_path(location, property)
        self.__read.append([location, property])
        location.__read.append([self, property])

    def _river_add(self, location):
        self._clear_path(location)
        self.__river.append(location)
        location.__river.append(self)

    #Убирает ещё и реки
    #Не возвращает ошибки при попытки убрать не сущ. дорогу
    def _clear_path(self, location, property=0):
        self.__verification(location, property)
        remove_wich_list(location, self.__read)
        remove_wich_list(self, location.__read)
        remove_wich_list(location, self.__river, True)
        remove_wich_list(self, location.__river, True)

    #Вызывает ошибку если мы пытаемся провести дорогу к локации выше или ниже по иейрархии
    def __verification(self, location, property):
        if location.__class__ != Location: raise TypeError ("must be location")
        if location in self.items or self in location.items: raise TypeError ("the read must be not your's item")
        if not property in range(0, 3): raise IndexError ("second argument must be zero, one or two")

    @property
    def read(self): return self.__read

#Предметы интерфейса
class Item(Base):
    def __init__(self, name=None, weight=0, place=None):
        super().__init__(name, place)
        #Вес предмета
        self.__weight = weight

    @property
    def weight(self): return self.__weight
    @weight.setter
    def weight(self, weight): self.__weight = weight

#Все живое
class Living(Base, Wallet):
    def __init__(self, name, place=None, level=1):
        super().__init__(name, place)
        self.__level = level
        self.__experience = 0 #Прогресс до нового уровня, 50 макс., дальше только новый уровень
        #[Действительное, максимальное]
        self.__health = [90 + 10*level, 90 + 10*level]
        self.__energy = [90 + 10*level, 90 + 10*level]
        self.__magick = [90 + 10*level, 90 + 10*level]
        self.__weight = [0, 290 + 10*level] #Вес всех обьектов в инвентаре
        #Инвентарь
        Wallet.__init__(self)

    def __level_up(self, choice, vaule=10, level=1):
        self.__level += level
        #0 - всё, 1 - hp, 2 - st, 3 - mg
        if choice == 1 or choice == 0:
            self.__health = [self.__health[0] + vaule, self.__health[1] + vaule]
        if choice == 2 or choice == 0:
            self.__energy = [self.__energy[0] + vaule, self.__energy[1] + vaule]
            self.__weight = [self.__weight[0], self.__weight[1] + vaule]
        if choice == 3 or choice == 0:
            self.__magick = [self.__magick[0] + vaule, self.__magick[1] + vaule]

    def update(self):
        if self.__experience >= 50:
            self.__experience = 0
            self.__level_up(random(1, 3))

    def found(self, object):
        self.lost(object)
        self.items.append([object, None])
        self.__weight = [self.__weight[0] + object.weight, self.__weight[1]]
        object.where = self

    def lost(self, object, place=None):
        if found_in_list(object, self.items):
            remove_wich_list(object, self.items)
            self.__weight = [self.__weight[0] - object.weight, self.__weight[1]]
            if place is None:
                object.where = self.where
            else:
                object.where = place

    def go(self, location):
        if found_in_list(location, self.where.read):
            #Речка, DO TO
            if location.__class__ == River:
                pass
            origin_i = found_in_list(location, self.where.read, "i")
            self.where.items.remove(self)
            #Путь, [Откуда, куда, сколько дней]
            self.where = [self.where, location, self.speed[self.where.read[origin_i][1]]]
        #Выходим откуда-то
        elif location == self.where and self.where != Location.WORLD:
            remove_wich_list(self, self.where.__items)
            self.where = location
        else:
            raise IndexError ("this location not nearbay")

    @property
    def speed(self): return self.__speed

#Человек как класс
class Person(Living):
    HERO = []
    def __init__(self, name, this_i=False, place=None, level=1):
        if this_i: Person.HERO.append(self)
        super().__init__(name, place, level)
        self.__speed = (1, 3, 5)

    @property
    def speed(self): return self.__speed
