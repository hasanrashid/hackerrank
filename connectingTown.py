from functools import reduce
import math;

i = (int(input()));
for j in range(i):
    cities = int(input());
    l = [int(x) for x in(input()).split()];    
    print(int(math.fmod(reduce((lambda x,y:math.fmod(x*y,1234567)),l),1234567)));    