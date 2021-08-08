from base import *

#Города
#Империя Артурия
Arturia = Location("Arturia")
Strenght_south = Location("South Strenght")
Strenght_north = Location("North Strenght")
Strenght_west = Location("West Strenght")

#Небесная Империя
Grail = Location("Grail")
Iron = Location("Iron")

#Мелкие страны-города
Traidic_land = Location("Traidic land")
Quqe = Location("Quqe")
Dozen = Location("Dozen")

#Провинции, хранят свои локации
#"Сердце" Артурии
Hearth = []
#Север Артурии
Hight_plains = []
#Южные равнины Артурии
Golden_plains_west = []
Golden_plains_east = []
#Центр восточной империи
Heaven_land = []
#Равнины восточной империи
Second_sky = []
#Лес варворов-торговцев
Indifferent_forest = []
#Лес, дикий, нечейный
Wild_forest_south = []
Wild_forest_north = []

#East - восток, west - запад, north - север, south - юг
Side = ["'east-north'", "'east-south'", "'west-south'", "'west-north'"]

#Заполняем провинции
#Провинции делаться на 4 части, по расположению и добовляються в список по часовой стрелке (Северо-восток по Северо-запад)
#В провинции вместо её части может быть город, к нему можно обращаться как через провинцию так и напрямую
for i in range(4):
    #"Сердце" Артурии
    Hearth.append(Location(f"Hearth {Side[i]}"))
    #Север Артурии
    if skip_itiration(0, i): Hight_plains.append(Location(f"Hight plains {Side[i]}"))
    else: Hight_plains.append(Strenght_north)
    #Южные равнины Артурии
    Golden_plains_west.append(Location(f"Golden plains west {Side[i]}"))
    if skip_itiration(2, i): Golden_plains_east.append(Location(f"Golden plains east {Side[i]}"))
    else: Golden_plains_east.append(Strenght_south)
    #Центр восточной империи
    if skip_itiration(3, i): Heaven_land.append(Location(f"Heaven land {Side[i]}"))
    else: Heaven_land.append(Quqe)
    #Равнины восточной империи
    if skip_itiration(1, i): Second_sky.append(Location(f"Second sky {Side[i]}"))
    else: Second_sky.append(Iron)
    #Лес варворов-торговцев
    if skip_itiration(2, i): Indifferent_forest.append(Location(f"Indifferent forest {Side[i]}"))
    else: Indifferent_forest.append(Traidic_land)
    #Лес, дикий, нечейный
    if skip_itiration(2, i): Wild_forest_north.append(Location(f"Wild forest north {Side[i]}"))
    else: Wild_forest_north.append(Dozen)
    if skip_itiration(2, i): Wild_forest_south.append(Location(f"Wild forest south {Side[i]}"))
    else: Wild_forest_south.append(Strenght_west)


#Дороги, путь
#"Сердце" Артурии
for i in range(4):
    Arturia._read_add(Hearth[i], 0)
Hearth[0]._read_add(Hearth[1], 0)
Hearth[2]._read_add(Hearth[3], 0)
#Север Артурии
Hight_plains[1]._read_add(Hearth[0], 0)
Strenght_north._read_add(Hight_plains[1], 0)
Hight_plains[2]._read_add(Hearth[3], 0)
Hight_plains[3]._read_add(Hight_plains[2], 0)
Hight_plains[3]._read_add(Wild_forest_north[0], 1)
#Южные поля
Golden_plains_east[0]._read_add(Hearth[1], 0)
Golden_plains_east[0]._read_add(Golden_plains_east[1], 0)
Golden_plains_east[1]._read_add(Strenght_south, 0)
Golden_plains_east[2]._read_add(Hearth[2], 0)
Golden_plains_east[2]._read_add(Golden_plains_west[0], 0)
Strenght_south._read_add(Golden_plains_west[1], 0)
Golden_plains_west[1]._read_add(Golden_plains_west[2], 0)
Golden_plains_west[0]._read_add(Golden_plains_west[3], 0)
#Дикие леса
Strenght_west._read_add(Golden_plains_west[3], 1)
Golden_plains_west[0]._read_add(Wild_forest_south[1], 1)
Wild_forest_south[0]._read_add(Wild_forest_south[3], 1)
Wild_forest_north[1]._read_add(Wild_forest_south[0], 1)
Wild_forest_north[1]._read_add(Dozen, 1)
Wild_forest_north[1]._read_add(Wild_forest_south[0], 1)
Dozen._read_add(Wild_forest_south[3], 1)
Wild_forest_north[0]._read_add(Wild_forest_north[3], 1)
#Лес торговцев
Indifferent_forest[0]._read_add(Indifferent_forest[1], 1)
Traidic_land._read_add(Indifferent_forest[3], 1)
Traidic_land._read_add(Indifferent_forest[1], 1)
Traidic_land._read_add(Hight_plains[1], 1)
Indifferent_forest[3]._read_add(Strenght_north, 1)
#Равнины восточной империи
Second_sky[0]._read_add(Second_sky[3], 0)
Second_sky[3]._read_add(Second_sky[2], 0)
Second_sky[2]._read_add(Hearth[1], 0)
Second_sky[3]._read_add(Hearth[0], 0)
#Центр восточной империи
Heaven_land[0]._read_add(Iron, 2)
Heaven_land[0]._read_add(Grail, 2)
Grail._read_add(Heaven_land[1], 2)
Heaven_land[1]._read_add(Heaven_land[2], 2)

#Реки
#Река Артурианской Империи
Golden_plains_west[3]._river_add(Golden_plains_west[2])
Golden_plains_west[0]._river_add(Golden_plains_west[1])
Golden_plains_east[3]._river_add(Golden_plains_east[2])
Golden_plains_west[3]._river_add(Golden_plains_west[0])
Hearth[1]._river_add(Hearth[2])
Hearth[0]._river_add(Hearth[3])
Hight_plains[1]._river_add(Hight_plains[2])
Hight_plains[0]._river_add(Hight_plains[3])
#Дикая река дикого леса
Wild_forest_south[2]._river_add(Wild_forest_south[3])
Wild_forest_south[1]._river_add(Wild_forest_south[0])
Wild_forest_south[2]._river_add(Wild_forest_south[1])
Wild_forest_south[0]._river_add(Hearth[3])
Wild_forest_south[1]._river_add(Hearth[2])
Wild_forest_north[1]._river_add(Hight_plains[2])
#Маленькая река дикого леса
Wild_forest_north[3]._river_add(Wild_forest_north[2])
#Речная долина Небесной Империи и quqe
Quqe._river_add(Heaven_land[0])
Quqe._river_add(Heaven_land[2])
Heaven_land[2]._river_add(Golden_plains_east[1])
Quqe._river_add(Golden_plains_east[0])
Quqe._river_add(Second_sky[2])
Iron._river_add(Second_sky[0])
Iron._river_add(Second_sky[2])
