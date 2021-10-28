def field(items, *args):
    if(len(args) == 0):
        print("Ошибка: введите аргументы")
        return
    elif(len(args) == 1):
        return [dicts[args[0]] for dicts in items if args[0] in dicts]
    else:
        retdict = list()
        for dicts in items:
            retdict.append({key:dicts[key] for key in dicts if (key in args) and (dicts[key])})
        return retdict


def main():
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 50000},
    {'title': 'Кресло', 'price': 20000, 'color': 'grey', 'description': 'comfort'},
    {'title' : 'Линолеум', 'description': '20 meters, smooth'}
]
    print(field(goods, 'title', 'price'))
    print(field(goods, 'title'))


    '''slov = {'key1': 1, 'key2':3, 65: 'Hello'}
    for i in slov.keys():
        print(slov[i])'''
if __name__ == "__main__":
    main()
