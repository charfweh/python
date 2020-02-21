# s,w = input(), int(input())
# li = [s[i:i+w]for i in range(0,len(s),w)]
# for elem in li:
#     s = "".join(elem)
#     print(s)
# #with function
def wrap(s,w):
    li = [s[i:i+w] for i  in range(0,len(s),w)]
    s = "\n".join([elem for elem in li])
    return s
s,w = input(),int(input())
result = wrap(s,w)
print(result)