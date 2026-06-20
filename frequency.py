num=[1, 2, 3, 4, 3, 6, 2,3, 4]
fq_map={}

for i in range(1, len(num)):
    if num[i] in fq_map:
        fq_map[num[i]] += 1
    else:
        fq_map[num[i]] = 1

print(fq_map[3])
print(fq_map)