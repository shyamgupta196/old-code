'''
day5:
data structures:lists,sets,dict,tuple
functions==basic ex,default params
(KAL PADENGE)

'''
x = 'neelam'

## lists are done:
sets = [1,1,3,4,4,6,1,3,9,0,0,2,3] # print(set for unique elements)
apply_set = set(sets) 
print(apply_set)
## 'name':1,'name2':2, 'key':'values'
rolls = {'shyam':1,'advait':2,'dev':3,'harshita':4}
rolls['raj'] = 5
## this adds raj(KEY) rollno(VALUE) to dictionary
#LOOP ON DICT
for key,value in rolls.items():
    print(key,5*'-',value)

###docs string or fn ke comments
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass
# scopes

print(my_function.__doc__)## or help(my_function)

def square(number1,number2):
    '''
    this fn takes in 2 numbers
    and returns square 
    '''
    
    return number1**2,number2**2

##RAJ BHAIYA DOUBT

def add(no_of_inputs):
	sums = 0
	for i in range(no_of_inputs):
		user = int(input('Enter the number: '))
		sums = sums+user
	print(sums)
