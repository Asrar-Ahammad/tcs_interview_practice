# x= 5
try:
    print(x)
except:
    print('X is not found')
else:
    print('Nothing went wrong')
finally:
    print("The execution of the program is finished")

x = -1
if x < 0:
    raise Exception('Sorry no numbers less than zero')

y = "hello"

if not type(y) is int:
  raise TypeError("Only integers are allowed")