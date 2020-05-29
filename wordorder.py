"""
You are given  words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with
the input order of appearance of the word. See the sample input/output for clarification.
"""

n = int(input())
word = []
for i in range(n):
    word.append(input())
dict = {}
for letter in word:
    if(letter in dict.keys()): dict[letter] +=1
    else: dict[letter] = 1
print(len(dict))
for val in dict.values():
    print(val,end = " ")
