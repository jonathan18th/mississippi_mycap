most_frequent = input("Please enter  a string")

all_freq = {}
  
for x in most_frequent:
    if x in all_freq:
        all_freq[x] += 1
    else:
        all_freq[x] = 1
from collections import Counter
  
res = (Counter(most_frequent))

print("output is :\n " +  str(res))                                        
