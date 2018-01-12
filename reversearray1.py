#reverse this array:
#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

"""end given input"""

newArray = list(reversed(arr)) #init new array as reverse of prior

print(*newArray) #applying the list as separate arguments using *
