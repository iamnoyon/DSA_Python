hash_index = [0] * 11

arr = [2, 5, 7, 2, 3, 5, 3, 10, 9, 8]

num = [2, 3, 5, 2, 4,6 ,70, 34, 53]

for i in arr:
    hash_index[i]+=1

for i in num:
    if(i < 1 or i>10):
        print(0)
    else:
        print(hash_index[i])