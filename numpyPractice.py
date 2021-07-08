import numpy as np

ar_2d = np.arange(50).reshape(5,10)
print("some numpy action...")
print("")
print(ar_2d)
print("")
print("lets take some chunks out of it... top right corner:")
chunk1 = ar_2d[:2,5:]
print(chunk1)
print("")
print("And then some boolean array action, lets take everything over 24")
ar_2d = ar_2d[ar_2d>24]
print(ar_2d)
print("Now return boolean array of mod 2:")
print(ar_2d>35)
print("")
print("Now grab a chunk lets say 30-33")
print("")
chunk2 = ar_2d[5:9]
print(chunk2)
