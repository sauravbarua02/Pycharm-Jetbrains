#Program for series summation, takes first no and range as input in pycharm editor
# use two methods and two arguments two pass through using jetburns IDE
a = input('Enter first number = ')
a = int(a)
b = input('Enter range = ')
b = int(b)
def count12(a,b):

    for i in range(b):
          a  = a + 1
    return a
def sum12(a,b):
    #num = 1
    result = 0
    for i in range(b):
        result = result + a
        a = a + 1
    return result

print('result = ',sum12(a,b))
print('num = ',count12(a,b))
