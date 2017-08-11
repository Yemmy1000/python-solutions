from math import *


A = [-2, 11, -4, 13, -5, 2]

def maxSubsequenceSumX(n):
    if (0 == n):
        largestRunHeadingW = largestRunAnywhere = max (0, A[0])
    else:
        maxSubsequenceSumX(n-1)
        largestRunHeadingW = max(0, largestRunHeadingW + A[n])
        largestRunAnywhere = max(largestRunAnywhere, largestRunHeadingW)
        
        


def main():
    
# The current largest run starting from A[n] heading west.

    largestRunHeadingW =0
# The current largest run (anywhere) which is the desired output.

    largestRunAnywhere = 0

    maxSubsequenceSumX(5)
    print("The largest run sum is ",largestRunAnywhere )

main()
