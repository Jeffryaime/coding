cars = ['ferrari', 'lamborgini', 'porsche', 'rolls royce','mazeratti','brabus']


for car in cars:
    if  car == 'ferrari' or car == 'bugatti':
        print('I predict True')
    else:
        print('I predict False')


age_jay = 19
age_iris = 20

if age_jay > 18 and age_iris > 18:
    print('I predict True')

age_jeff = 30

if age_jeff == 30:
    print('I predict True')

if age_jeff != age_iris:
    print('I predit True')

if age_iris > age_jay:
    print('I predict True')