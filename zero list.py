#this program builds a list of integers with a length between 1 and 1000
#the sum of the list generated will always equal zero

import random
n=random.randint(1,1000)
zeroList=[]
negList=[]
def buildLists():
    for i in range(0,d):
        x=random.randint(0,9)
        zeroList.append(x)
        negList.append(-x)
if n%2==0:
    d=int(n/2)
    buildLists()
else:
    d=int((n-1)/2)
    buildLists()
    zeroList.append(0)

finalList=zeroList+negList
fanalList=random.shuffle(finalList)
print(finalList)
print(n)
print(len(finalList))
print(sum(finalList))



    

