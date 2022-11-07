'''
day6
functions ki katha continue
scope global,local
default params
*args,**kwargs(keywords in form of dictionary)

'''

x = 3
print(id(x))
def my_num():
    x = 100
    print(id(x))


my_num()
print(x)
print(id(x))

print(40*'--')


x = 3
print(id(x))
def my_num():
    ## THIS IS WHAT MAKES DIFF.---> (global x)
    global x
    x = 100
##    print(id(x))
print('id before {}'.format(id(x)))
my_num()

print(x)
print(f'id after {id(x)}')

### DEFAULT PARAMS -->
def my_name(Name = "Shyam"):
  print(f"My name is {Name}")
## number of params
def add(num1,num2):
    return num1+num2
## this takes in iterable
def add(nums):
    add = 0
    for i in nums:
        add +=i
    return add
### *args ka BEST INTERPRETATION 
##help(range)
RANGE = [1,11,2]

range(*RANGE)
'''
Bear in mind that the iterable object you’ll get using the
unpacking operator * is not a list but a tuple.
A tuple is similar to a list in that they
both support slicing and iteration. However,
tuples are very different in at least one aspect:
###lists are mutable,###(what is meaning of mutable??)
while tuples are not mutable(search it!!!)
'''



###**kwargs

def concatenate(**words):
    result = ""
    for arg in words.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))


### EXCEPTION HANDLING
print(4/0)



