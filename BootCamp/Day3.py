'''
Kal revision break ho sakta hai!!
I WANT KI SABKA CONCEPT REVISION HONA CHAHIYE
strings formatting(format,f-strings,{0}{1}{2})
input statements == used to take user input 
lists = [a type of data structure used to store data]
help,dir
##indexing (string,list,almost everything can be indexed)
control statements == daily life Flowchart example
control === if-else(25/05/21),other statements next day 
'''

# "y-o-u're is you are y-o-u-r's is your's "

# ASCII


# oldversions
print('hello %s'%'shyam' )
name = 'Yashika'
errno=777
#NEW versions used newer style guide formatting(pep-8)
print('Hey {name}, there is a {errno} error!'.format(
    name=name, errno=errno))
print(f'Hey {name}, there is a {errno} error!')
#TEMPLATE STRINGS (Homework)(ONE OF ADVANCED CONCEPTS SEE AFTER COURSE)
roll_no = input('Enter your roll number : ')

## inputs basically help in taking user input
## for the program
# choose a suitable variable name
## will go much deeper afterwards

###LISTS :----

names = ['Advait','Dev','Raj','Yashika']
## names[0]

##names.append('harshita')
##print(names)
##names.pop()
##print(names)
##names.insert(2,'harshita')
##print(names)
##print(name[0])

## control statements if-else (basics)
'''

if condition:
    runs when condition satisfies

elif condition:
    runs when condition satisfies

else:
    runs a block if
    'if block fails'

'''

##age = int(input('Enter your Age!! = '))
##
##if age>=18:
##    print('you are eligible')
##
##elif 14<age<18:
##    print('you are eligible only for small rides')
##
##else:
##    print('go back home!!!')
##
age = int(input('Enter your Age!! = '))
#1
if age>=45:
    print('Eligible for covaxin')
#2
elif 45>age>=18:
    print('you are eligible for covishield')
#3
elif 14<age<=18:
    print('you are eligible only for sputnik')
#4
else:
    print('eligible for pfizer')
