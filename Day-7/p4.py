from os import *
from sys import *
from collections import *
from math import *

def getTrappedWater(arr, n) :
    if not arr: return 0
    l, r = 0 , n -1
    leftmax = arr[l]
    rightmax = arr[r]
    result = 0
    while l <r:
        if leftmax<rightmax:
            l+=1
            leftmax = max(leftmax, arr[l])
            result += leftmax - arr[l]
        else:
            r-=1
            rightmax = max(rightmax, arr[r])
            result += rightmax - arr[r]
    return result