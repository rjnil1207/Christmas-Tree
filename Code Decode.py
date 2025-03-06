# Code language talk...
#  Let the string is : golu 
## Then, the first step is last letter added to first and added three random letter after and before 
### Example : golu => abc + (u + gol) + xyz => abcugolxyz

# Coding

import random
import string

def fun(s):
    z = [x for x in s]
    item = z.pop()
    z.insert(0,item)
    s = "".join(z)

    s1 = ''.join(random.choices(string.ascii_lowercase, k=3))
    s2 = ''.join(random.choices(string.ascii_lowercase, k=3))
    s3 = s1 +s+ s2
    print(s3)

s = input("Enter the word : ")
fun(s)

# Decoding

def func(s):
    z = [x for x in s]  
    z1 = []
    for i in range(3,len(s)-3):
         z1.append(z[i])
    if len(s) >= 3:      
        item = z1.pop(0)
        z1.append(item)
        print("".join(z1))    
    else:
        z1.reverse()
        print("".join(z1))

s = input("Enter the coded string : \n")
func(s)

