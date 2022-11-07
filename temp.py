import pandas as pd


##age = 12
##bar_age = 21
##if (50>age>18) & (age>bar_age):
##    print('you are allowed for everything')
##elif age>18:
##    print('allowed for rides')
##else:print('no entry')
a = 2
b= 20

##print('hi','oijds','sahdo',sep='---')
##for i in range(a,b,2):
##    print(i*2,i+2,i+10,sep='@',end='--')

##print(list((1,2,3)),type([1,2,3]),type(a))

##temp = [1,2,3,4]
####temp.append([a,b])
####temp[4] = 3
##print(len(temp))
##temp[1]=10
####temp[3],temp[4][1] = 40,100
##
##print(temp)
##
##temp.extend([a,b])
##print(temp)
##
##temp1 = [even for even in range(20,1,-1) if even%2==0]
##print(temp1)

##temp1 = [even if even%2==0 else 'odd' for even in range(20,1,-1) ]
##print(temp1)


##
##emp1 = {'company':'UFM',
##    'bio info':{'emp1oyees':['karan','shyam','akash','dev','sallu'],
##                    'empID':[100,200,300,400,500],
##                    'age':[49,56,33,21,99],
##                    'sex':['M' for _ in range(5)]},
##        'IT':['ram','john'],
##        'datascience':['teresa','karan']}
##
####print(myages)
##
##jenny = ['jenny',700,28,'F']
##
##
##for val,data in zip(emp1['bio info'].values(),jenny):
##    val.append(data)
##
##
##
##emp1['bio info']['city'] = ['indore','mumbai','delhi','kanpur','hyderabad','jaipur']
##print('-'*20)
##print(emp1['bio info']['city'])
##
####empid = int(input('what is your empID: '))
####change_city = emp1['bio info']['empID'].index(empid)
####
####new_city = input('which is your new city: ')
####emp1['bio info']['city'][change_city] = new_city
##
##print(emp1['bio info']['city'])
##
##
####range(len(emp1['bio info']['emp1oyees']))
##
##even_ = []

##print(help(emp1))


##def sums(*args):
##    '''
##    takes in n number of arguments and sums them up !!
##    'doc string'
##    and returns them sum 
##    '''    
##    my_sum = 0
##    for i in args:
##        my_sum += i
##    return my_sum
##
##
##print(sums([2,3,4,5,6,7,8]))
##print(help(sums))

#


def raiser(salary,inflation=0.05):
    hike = inflation*0.6
    salary += salary*hike
    return salary

##print(raiser(inflation=0.1,salary=10000))


dept1 = [1000,2000,3000]
dept2 = [500,1000,4000]

total_depts = [dept1,dept2]

##def func(*args):
##    total_sum = 0
##    for i in args:
##        for j in i:
##            for k in j:
##                total_sum += k
##    return total_sum
##print(func(total_depts))


##def dept_wise(*args):
##    sums = 0
##    for i in args:
##        print(i)
##        sums += i
##    return sums
##
##print(dept_wise(*total_depts))
##
##print(*[200,200],sep = '-')
##total = 0
##print(200,200,end='  ' ,sep = '-')
##
##for i in total_depts:
##    print(i)
##    total += dept_wise(i)
##print(total)
##
##first = 'shyam'
##
##def heights(**kwargs):
##    global first
##    print(first)
##    first = kwargs['first']
##    second = kwargs['second']
##    print(first,second)
##    return first,second
##
##heights(**{'first':'karan','second':'shyam'})
##print(first)
##print(names)
##


class company:
    '''

    full structure and functions of
    company
    '''

    name_of_company = 'ufm'
    number_emps =  30

    
    def desc(self):
        '''
        provides all the description of the company
        '''
        
        return (f'name : {self.name_of_company} and number of employees: {self.number_emps}')

              
com = company()
company.desc(com)
##print(type(com.desc()))
##print(help(com))

### constructor
### magic methods

import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return int(r) ** 2 * math.pi

p = Pizza(7,['olives','tomato'])
##print(p.area())


##print(p.circle_area('4'))

##print(emp)
##print(len(emp))
##print(len(emp.name))
##
##class Pizza:
##    def __init__(self, ingredients):
##        self.ingredients = ingredients
##
##    def __repr__(self):
##        return f'Pizzaaaaaa({self.ingredients!r})'
##
##    @classmethod
##    def margherita(cls):
##        return cls(['mozzarella', 'tomatoes'])
##
##    
##    
##    @classmethod
##    def prosciutto(cls):
##        return cls(['mozzarella', 'tomatoes', 'ham'])
##    @classmethod
##    def pepronipaneer(cls):
##        return cls(['paneer','onions','cheese'])
##
##p = Pizza(['mozzarella','onions','jalapeneos' ,'tomatoes'])
####print(p)
####print(Pizza.margherita())
####print([m for m in dir(p) if not m.startswith('__')])
##
##
##
##class employee:
##    company = 'UFM'
##    name_of_emp = []
##    ages = []
##    positions = []
##    def __init__(self,name,age,position):
##        self.n = name
##        self.age = age
##        self.pos = position
##    
##    def __repr__(self):
##        return f'{self.n} is working as {self.pos}'
##    def __len__(self):
##        return len(self.name_of_emp)
##    def add_emp(self):
##        self.name_of_emp.extend([self.n])
##        self.ages.extend([self.age])
##        self.positions.extend([self.pos])
##
##
##
##emp = employee(['karan','shyam','jacob'],[30,21,56],['bio info','data science','engineer'])
##print(emp.company)
##print(emp)
##emp.add_emp()
##print(emp.name_of_emp)
##print(emp.ages)
##print(emp.positions)







