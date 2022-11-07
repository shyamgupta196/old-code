'''
today's topics :-
indexing
Loops(in-depth):-FOR AND WHILE LOOPS,
'''
## indexing

name = ['dev',
        'advait',
        'yashika',
        'raj',
        'harshita']

print(name[0])

#
for i in name:
    pass


##for i in something/or [iterable(google karo)]:
##    do whatever you want to do 

for i in range(10):  # this executes a for loop
	print(i)    #print nums till 9


##
####while some_condition:
####    do_code
##
##

print(50*'*')
i=0
while True: # this executes a while loop infinite
	print(i)
	i += 1 #i= i+1
	if i==10:
		break
##
####Example from docs
##a = ['Mary', 'had', 'a', 'little', 'lamb']
##for i in range(len(a)):
##    print(i, a[i])
##
##
##
fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)
  if x == "banana":
    break



# this with enumerate (live ex)
## list comprehensions

#### YASHIKA DD KA DOUBT
# how to take user input simultaneously and add in list
names = [input(i) for i in range(5)]

### if time persists then functions intro and examples
