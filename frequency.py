# technique 1
num=[1, 2, 3, 4, 3, 6, 2,3, 4]
fq_map={}
hash_map={}

for i in range(1, len(num)):
    if num[i] in fq_map:
        fq_map[num[i]] += 1
    else:
        fq_map[num[i]] = 1

print(fq_map)

# technique 2

for i in range(1, len(num)):
    hash_map[num[i]] = hash_map.get(num[i], 0)+1

print(hash_map)