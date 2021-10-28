from operator import itemgetter

class HDD:
    def __init__(self, id, name, memory, id_PC):
        self.id = id
        self.name = name
        self.memory = memory
        self.id_PC = id_PC

class PC:
    def __init__(self, id, brand, OS):
        self.id = id
        self.brand = brand
        self.OS = OS
        
class PC_HDD:
    def __init__(self, id_PC, id_HDD):
        self.id_PC = id_PC
        self.id_HDD = id_HDD

#диски
hdds = [
    HDD(1,'WD', 1, 1),
    HDD(2,'Toshiba', 8, 1),
    HDD(3,'Toshiba', 8, 2),
    HDD(4,'Seagate', 4, 3),
    HDD(5,'WD', 8, 1),
    HDD(6,'Seagate', 4, 3),
    HDD(7,'WD', 4, 2),
    HDD(8,'Toshiba', 1, 2),
    HDD(9,'WD', 4, 3)
]
#компьютеры
pcs = [
    PC(1, 'Asus', 'Windows'),
    PC(2, 'Dell', 'Windows'),
    PC(3, 'Apple', 'MacOS'),

    PC(4, 'Lenovo', 'Windows'),
    PC(5, 'Acer', 'Linux')
]

#компьютеры и диски (для связи многие-ко-многим)
PcsHdd = [
    PC_HDD(1, 1),
    PC_HDD(1, 2),
    PC_HDD(2, 3),
    PC_HDD(3, 4),
    PC_HDD(1, 5),
    PC_HDD(3, 6),
    PC_HDD(2, 7),
    PC_HDD(2, 8),
    PC_HDD(3, 9),
    PC_HDD(2, 7),
    PC_HDD(2, 7),

    PC_HDD(4, 1),
    PC_HDD(5, 2)    
]

def main():
    one_to_many = [(h.name, h.memory, p.brand, p.OS) for h in hdds for p in pcs if h.id_PC == p.id]
    print("Задание А1:")
    print(sorted(one_to_many, key=itemgetter(2)))


    print("\nЗадание А2:")
    res2 = []
    for p in pcs:
        s = sum([h.memory for h in hdds if (h.id_PC == p.id)])
        res2.append([p.brand, s])
    print(sorted(res2,key=itemgetter(1)))


    print("\nЗадание А3:")
    many_to_many_temp = [(p.brand, p.OS, ph.id_HDD)
        for p in pcs
        for ph in PcsHdd
        if p.id == ph.id_PC
    ]
    many_to_many = [(h.name, h.memory, brand, OS)
        for brand, OS, id_HDD in many_to_many_temp
        for h in hdds
        if (h.id == id_HDD)
    ]
    res3 = {}
    for p in pcs:
        if 'A' in p.brand:
            SpecialPcs = list(filter(lambda x: x[2] == p.brand ,many_to_many))
            HddsForSpecialPcs = [name for name, mem, brand, OS in SpecialPcs]
            res3[p.brand] = HddsForSpecialPcs
    print(res3)


if (__name__ == "__main__"):
    main()