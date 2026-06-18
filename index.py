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



####################### Check Palindrom ####################
mainInput = 121
palnum = mainInput
palnum2 = 0

while(palnum > 0):
    rem = palnum%10
    palnum = int(palnum/10)
    palnum2 = palnum2 * 10 + rem

print(mainInput == palnum2)




################## Armstrong number ###############
mainValue = 153
temp = mainValue
counter = 0

while(temp > 0):
    counter += 1
    temp = int(temp/10)

sum = 0
temp2 = mainValue

while(temp2 > 0):
    rem = temp2%10
    sum = (rem**counter) + sum
    temp2 = int(temp2/10)

print(mainValue == sum)