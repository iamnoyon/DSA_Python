##########
# Digit extraction
##########

#count the digit
num = 42343
count = 0

while (num > 0):
    count += 1
    num = int(num/10)

print(count)

#count digit through libary
from math import log10
num2=13435435
print(int(log10(num2))+1)