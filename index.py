
#SET-1

#1.

print("hello world")

#2.

a=10
b=8.7
c="string"
d=False
e=[1,2,3]
f=(1,2,3)
g={
    "name":"utkarsh",
    "age":20
}
h={1,2,3}


print(type(a),a)
print(type(b),b)
print(type(c),c)
print(type(d),d)
print(type(e),e)
print(type(f),f)
print(type(g),g)
print(type(h),h)


#3.

list = [1,2,3,4,5,6,7,8,9,10]

#4.
list1=[10,20,30,40]

sum=0

for i in range(len(list1)):
    sum+=list1[i]

#print(sum)

y = (sum/len(list1)) 

print(sum)
print(y)

#5.

str5 = "python"[::-1]

print(str5)

#6.

str6 = "Hello"
count=0

for i in range(len(str6)):
    if (str6[i]=="a" or str6[i]=="e" or str6[i]=="i" or str6[i]=="o" or str6[i]=="u"):
        count=count+1
        
print(count)

#7.

x7=13

def checkPrime(x):
    flag = False
    for i in range(2,x):
     if x%i==0:
      flag = True
      break
    if flag == True:
     print("not prime")
    else:
     print("prime")

checkPrime(x7)

#8.

x8=5

def factorial(x):
    
    fac=1
    i=1
    
    while (i<=x):
        fac=(fac*i)
        i=i+1
        
    return(fac)

res = factorial(x8)

print(res)

#9.

n = 5

list9=[]


count=0

while(count<=n):
    count+=1
    
    if(count==1):
        list9.append(0)
        continue
    elif(count==2):
        list9.append(1)
        continue
    else:
        list9.append((list9[count-3] + list9[count-2]))
    if(count==n):
        break

print(list9)


#10.

list10=[]

i=1

while(i<=10):
    list10.append(i**2)
    i+=1
            
print(list10)        

