import math;
modulo = (10**9)+7;
n = int(input());
for i in range(n):
    print((int(input())%modulo)**2%modulo);