def service():
    memory = []
    technic = [('Ноутбук', 1500, 'Татьяна', '89002001020'),
        ('Смартфон', 500, 'Анна', '89202202325'),
        ('Проектор', 300, 'Андрей', '89505205656'),
        ('Принтер', 750, 'Игорь', '89303303236'),
        ('Планшет', 2300, 'Игорь', '89303303236'),
        ('Смартфон', 1000, 'Андрей', '89505205656'),
        ('Ноутбук', 4800, 'Татьяна', '89002001020'),
        ('Наушники', 780, 'Марина', '89562002350'),
        ('Сканер', 550, 'Сергей', '89808564559'),
        ('Планшет', 1200, 'Анна', '89202202325'),
        ('Ноутбук', 1100, 'Игорь', '89303303236'),
        ('Смартфон', 3500, 'Татьяна', '89002001020')]
    for i in technic:
        first = i[2]
        k = 0
        if first in memory:
            pass
        else:
            
            result = first + ' ' + i[3]+':'
            while k < len(technic):
                
                if first in technic[k][2]:
                    name = ' ' + str(technic[k][0]) + ' - ' + str(technic[k][1]) + ';'
                    result = result + name
                    
                    k += 1
                else:
                    k += 1
            print(result)
            memory.append(first) 


        





