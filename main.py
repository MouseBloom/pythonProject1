
# программа находит равновесную ценну на товар
# данная программа зная уравнения спроса и предложения находит равновесную цену на товар
supply = input('введите уравненение предложения, типа ap-b, где p неизвестно ' )
supply = supply.strip()
supply = supply.replace('p', '') # убираю переменную, чтобы было проще дальше работать
b = supply.replace('=','-')
b = b.split('-')
b[1] = int(b[1])
if b[0] == '': # add situation where a = 1
    b[0] = 1
b[0] = int(b[0])
if b[0] == 0:
    print('данная ситуация невозможна на рынке')
    exit()
demand = input('введите уравнение спроса, типа b-ap, где p неизвестно ')
demand = demand.strip()
demand = demand.replace('p', '')
c = demand.replace('=','-')
c = c.split('-')
c[0] = int(c[0])
if c[1] == '': # add situation where a = 1
    c[1] = 1
c[1] = int(c[1])

if c[1] == 0:
    print('данная ситуация невозможна на рынке')
    exit()
price = (b[1] + c[0]) / (b[0] + c[1])
print('Равновесная цена на товар будет равна', '%.2f'%price)
