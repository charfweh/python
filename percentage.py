# dict1 = {
#     "abc":[1,2,3],
#     "qwe":[4,5,6]
# }
# print(dict1.values())
num = int(input())
dict1 = {}
for i in range(num):
    n,s1,s2,s3 = input().split()
    dict1 = {str(n):list(map(float,(s1,s2,s3)))}
key = str(input())
if key in dict1.keys():
    avg = sum(list(dict1[key])) / len(list(dict1[key]))
print("%.2f" % avg)