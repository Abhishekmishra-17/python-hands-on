# c
#include<stdio.h>
#include<conio.h>

'''
int a;
int b;
a=4;
b=5;
printf("%d",a+b);
'''


'''a=5#int
b=6.7#float
print(float(a)+int(b))

#print("Hello word")
#scanf("%d",&a);
### arthi####
a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
print("The sum of",a,"and",b,"is",a+b)
print("The substraction of",a,"and",b,"is",a-b)
print("The mul of",a,"and",b,"is",a*b)
if(b<0):
    print("Second number is negative")
elif(b!=0):
    print("The div1 of",a,"and",b,"is",a/b)#floating point division
    print("The div2 of",a,"and",b,"is",a//b)#integer type division

else:
    print("division is not possible")
#make a python program to find the sum,mul,division,power,and, or, of two numbers
try:
    print(a/b)
except ZeroDivisionError as p:
   print(p)
finally:
    print("Hello")
'''
#v="akm"
#print(len(v))
#for i in range(len(v)):
#    print(i)

'''k=9
while(k>0):
    print(f"durgesh{k}")
    k-=1
'''
#k=10
#print(type(k))
#k,l,j=20,40,30
#print(k,l,j)

'''
a=int(input("Enter the number"))
while(a>=0):
    print(a)
    a=int(input("Enter the number"))


    
a=int(input("enter the number"))
while(a):#a is not 0
    for i in range(1,11):
        print(a,'*',i,'=',a*i)
    b=input("do you want to continue?(y/n)")
    if(b=="n"):
        break
    else:
        a=int(input("enter the number"))


for i in range(10):
    for j in range(10):
        if(i==j):
            break
        else:
            print(i,end=" ")
    print("\n")

    
for i in range(10):
    for j in range(12):
        if(i==j):
            continue
        else:
            print(i,j,end=" ")
    print("\n")

'''
'''
>>> a,b=list(),[]
>>> b
[]
>>> a
[]
>>> a=[1,2,3]
>>> print(a)
[1, 2, 3]
>>> print(len(a))
3
>>> a[0]
1
>>> a[1]
2
>>> a[3]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[3]
IndexError: list index out of range
>>> a.append(5)
>>> a
[1, 2, 3, 5]
>>> a+[9,8,7]
[1, 2, 3, 5, 9, 8, 7]
'''

a=[1,"asd",3.6,2,3]
#print(a*3)
#a.remove(1)
#print(a)
#a.pop(0)#a=[2,3]
#a.pop(0)#a=[3]
#print(a)
#print(type(a))



