'''
*args,**kwargs(kwargs IS OUT OF CONTEXT RN)(ONLY ARGS)
Exception Handling :
Try Except Else Finally
File Handling :
'''

###EXCEPTION HANDLING 
##print(1/0)
try:
    div = 1/0
except Exception :
    print('you cannot divide by 0')

### this loops infinitely unless user enters a number 
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

## TRY EXCEPT ELSE FINALLY

def divides(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except NameError:
        print("please input a number")
    except Exception as e:
        print(f'something went wrong : {e}')
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
##divides(1,dsi)
