# This is a sample Python script.
# программа находит равновесную ценну на товар
import re
supply = input('введите уравненение предложения, типа ap-b, где p неизвестно ' )
supply = supply.strip()
supply = supply.replace('p', '')
b = supply.replace('=','-')
b = b.split('-')
b[1] = int(b[1])
b[0] = int(b[0])
if b[0] == 0:
    print('данная ситация невозможна на рынке')
    exit()
demand = input('введите уравнение спроса, типа b-ap, где p неизвестно ')
demand = demand.strip()
demand = demand.replace('p', '')
c = demand.replace('=','-')
c = c.split('-')
c[0] = int(c[0])
c[1] = int(c[1])
if c[1] == 0:
    print('данная ситуация невозможна на рынке')
    exit()
price = (b[1] + c[0]) / (b[0] + c[1])
print('%.2f'%price)