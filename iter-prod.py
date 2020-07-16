"""
Given two lists, finding all possible combinations without repetition between the two lists.
Useful for plotting values in a table (similar to a punnett square) & finding matrix multiplication.
"""
import itertools

list_1 = map(int, input("Input the first list:").split())
list_2 = map(int, input("Input the second list:").split())

product = list(itertools.product(list_1, list_2))
print(f"Answer:{product}")