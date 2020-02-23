from itertools import product
n1,n2 = list(map(int,input().split())),list(map(int,input().split()))
for i in product(n1,n2):
    print(i,end = " ")