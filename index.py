from math import sqrt

num=6
count=[]

for i in range(1, int(sqrt(num))+1):
    if(num%i == 0):
        count.append(i)

count.append(num)

print('prime') if len(count) == 2 else print('Not prime')