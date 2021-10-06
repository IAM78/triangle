print('\nPlease enter the size of the 3 sides of your triangle : ')
a=int(input())
b=int(input())
c=int(input())

if(a<b+c)&(b<a+c)&(c<b+a):
    print('It is possible to make a triangle.')
else :
    print('It is not possible to make a triangle !')  