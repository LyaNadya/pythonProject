print('Single Quotes')
print("Double Quotes")

print('Single'+'Quote')
print("Double"+"Quotes")
print('Single',"Quotes")

b='Quote'
print('Single %s'%b)
a= "Single"
print('%a %a'%(a,b))

c=5
print(c)
print('There are',c,'apple in the fridge')
print('There are %d' %c, 'apple in the fridge')

name = input("Please enter your name")
print(name)

a=10
b=20
x=a+b
print(x)

a=[1,2,3]
b=[1,2,3]
print('a is equal to b:', a==b)

print(2**4)
a=2
b=4
print(a**b)

print(19%5)
a=10
b=12
print('a>b is', a>b)

a=True
b=False
print("Combine result of x and y is:",a==b)

a=[1,2,3]
b=[1,2,3]
c=b
print(a is b)
print(c is b)