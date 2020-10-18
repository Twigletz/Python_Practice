from math import gcd
from functools import reduce

# Function 1
def lcm(a,b):
    return a // gcd(a,b) * b

def get_smallest_number(n):
    return reduce(lcm,range(1 + n//2,n+1),1)

# Function 2
def get_smallest_number_2(n):
    divisors = range(1, n+1)
    check_divisible = lambda x: all([x % y == 0 for y in divisors])
    i = 1
    while True:
        if check_divisible(i):
            return i
        i += 1

# Function 3
def get_smallest_number_3(list1):
    lcm = list1[0]
    for i in list1[1:]:
        lcm = int(lcm*i/gcd(lcm, i))
    return lcm

#Function 4
def get_smallest_number_4():
    for x in range(1, 30000, 1):
        if x%2!=0:
            continue
        if x%3!=0:
            continue
        if x%4!=0:
            continue
        if x%5!=0:
            continue
        if x%6!=0:
            continue
        if x%7!=0:
            continue
        if x%8!=0:
            continue
        if x%9!=0:
            continue
        if x%10!=0:
            continue
        if x%11!=0:
            continue
        if x%12==0:
            # if itgets this far AND is divisible by 12 then YAY we have it, so print it!
            return(x)


#Function 5
def get_smallest_number_5():
    for x in range(1, 30000, 1):
        if (x%1==0) and (x%2==0) and x%3==0 and x%4==0 and x%5==0 and x%6==0 and x%7==0 and x%8==0 and x%9==0 and x%10==0 and x%11==0 and x%12==0:
            return(x)


# Now test all FIVE(!) functions:
print("get_smallest_number(12) returns: ", get_smallest_number(12))
print("get_smallest_number_2(12) returns: ", get_smallest_number_2(12))
print("get_smallest_number_3([1,2,3,4,5,6,7,8,9,10,11,12]) returns: ", get_smallest_number_3([1,2,3,4,5,6,7,8,9,10,11,12]))
print("get_smallest_number_4 returns: ", get_smallest_number_4())
print("get_smallest_number_5 returns: ", get_smallest_number_5())