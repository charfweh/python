# odd = [x for x in range(1,10) if x%2!=0]
# print(odd)

#list comprehension
# a=1
# b=1
# c=1
# n = 2
# li = [a,b,c]
# combo = [[i,j,k] for i in range(0,li[0]+1) for j in range(0,li[1]+1) for k in range(0,li[2]+1) if i+j+k != n]
# print(combo)

#runner up challenge 
# n = int(input())
# arr = list(map(int,input().split()))
# print(arr)
# arr.sort(reverse = True)
# i=0
# while i < n:
#     if arr[i]!=arr[i+1]:
#         print(arr[i+1])
#         break
#     i+=1
# b = [x for x in range(0,11) if x%2==0]
# print(b)
#nested lists
# info = [[input(),int(input())] for x in range(3)]
# maxnum = [max([info[x][1] for x in range(3)])]
# print(maxnum)
# print("asdasD",maxnum[0])
# answer = sorted(info,key = lambda x : x[1])
# print(answer[len(answer)-2])
    


# prime numbers
# noprimes = [x for j in range(2,8) for x in range(j*2,101,j)]
# print(noprimes)
# primes = [p for p in range(2,101) if p not in noprimes]
# print(primes)   
# def split_and_join(line):
#     # write your code here
#     line = "-".join(line.split(" "))
#     return line
# line = input()
# result = split_and_join(line)
# print(result)

#tuples
# n = int(input())

# tup = tuple(map(map,input().split()))
# print(hash(tup))

s = "something"
print(len(s))
print(s[:5]+"0")
#python workbook exercises

############## question 1############
# lis = ["alice","wonderland","charlene"]
# answer = [[x.upper(),x.capitalize()] for x in lis]
# print(answer)

######## question 2 ########
# def t(n):
#     if n == 0:
#         return 1
#     else:
#         return n * t(n-1)
# num = [2,3,4,5]
# answer = [t(x) for x in num]
# print(answer)

###### question 3 ######
# names1 = ["alice","wonderland","charlene","daneil"]
# names2 = ["bertand","charlene"]
# answer = [x for x in names1 if x not in names2]
# print(answer)

