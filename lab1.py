a =45
b=44
allArea=0
print (a+b)
print ("I want Money!")

if a<b:
    print("a < b")
elif a==b:
    print("a == b")
else:
    print("I don't know")

def mul_ab(a,b):
    '''
    this is multiply function 
    '''
    print(a * b)
mul_ab(3,4)

'''
Area of Circle 
'''
areaStore=[]

def areaFun(radius):
    area=pow(radius,2)*3.14
    print(area)
    areaStore.append(area)


for x in range(1,6):
    areaFun(x)


print(areaStore)

areaStore.pop(0)
areaStore.append(10)
print(areaStore)

print(f"The sum of All Area is {sum(areaStore)}")

grades={'Olivia':'A','Mark':'A+'}

print(grades['Olivia'])
