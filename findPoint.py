numLines = int(input());
for i in range(numLines):
    j = list(map(int, input().split()));
    print(j[2]*2-j[0],j[3]*2-j[1]); 