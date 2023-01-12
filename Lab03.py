a = 10
print(a)
type(a)

b = 5+6j
print(b)
type(b)

c = True
print(c)
type(c)

d = 10.5
print(d)
type(d)

e = 'Testing String'
print(e)
type(e)

f = [1,2,3]
print(f)
type(f)

g = (4,5,6)
print(g)
type(g)

h = {'Student':'Aaron'}
print(h)
type(h)

i = {7,8,9}
print(i)
type(i)

j = [1,2,3]
k = f+j
print(k)
type(k)
print(1 in k)

l = (10,11,12)
m = l+g
print(m)
type(m)

#k[0] = 11
#print(k)

n = {'Lecturer':'Judy'}
h.update(n)
print(h)
type(h)

o = {9,10,11}
print(o.union(i))
type(o)
print(o.intersection(i))
type(o)

# Do it yourself challenges
Country_code= {'Australia':'AU','Belgium':'BE','China':'CN','Denmark':'DK'}
print(Country_code)
print(type(Country_code))
name_list= ['Thomas','Linda','Cath','Benny']
print(name_list)
name_list.sort()
print(name_list)
name_list.pop()
name_list.pop()
name_list.pop()
name_list.pop()
print(name_list)