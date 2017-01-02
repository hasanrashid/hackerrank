from functools import reduce
import math;
inputSize = int(input());
l=[True]*50;
l[0]=False;
l[1]=False;
for j in range(2,int(math.sqrt(50))):
    if(l[j]):
        q = j**2;
        while q < 50:
            l[q] = False;
            q+=j;
for i in range(0,inputSize):
    count=0;
    primeFactor = 1;
    upperLimit = int(input());
    for j,k in enumerate(l):
        if(k):
            primeFactor*=j;
            if(primeFactor > upperLimit):
                break;
            count+=1;
    print(count);