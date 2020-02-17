i=5
# for i in range(0,5):
#     for o in range(0,i+1):
#         print(" ",end="")
#     for k in range(5,i,-1):
#         if(k%2==0):
#             print("1",end="")
#         else:
#             print("0",end="")
#     for l in range(4,i,-1):
#         if(l%2==0):
#             print("1",end="")
#         else:
#             print("0",end="")
#     prin420
# t()

blank=0
for i in range(4,-1,-1):
    for j in range(1,2):
        print(" "*blank,end="")
        print("10"*i,end="")
        
    print("1")
    blank+=1

        
    