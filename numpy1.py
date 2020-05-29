"""you are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float."""
import numpy as np
inp = input().split()
nparr = np.array(inp,dtype = "float")
print(nparr[::-1])
