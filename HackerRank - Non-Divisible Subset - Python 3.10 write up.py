##    https://www.hackerrank.com/challenges/non-divisible-subset/problem
##
##    Given a set of distinct integers, print the size of a maximal subset of S
##    where the sum of any numbers in S' is not evenly divisible by k.

##### ##### ##### #####

#   O(n)
#   n is the length s
#   you could argue the runtime is O(n+k), but on average n dwarfs k.
#   The Idea:
#       if (a + b) / k = 0
#       then a mod(k) + b mod(k) = k
#   The reason this idea is important is from this we can do the following:
#   group members of s by their remainders when divided by k.
#   two groups whose remainders sum to k cannot be in the subset together.
#   special cases to note:
#       1. only one number that is evenly divisble by k may be in the subset.
#       2. if k is even then k/2 will be a complimentary remainder with itself
#           and only one member may be in the subset.

#   The Algo:
#       1. construct dictionary with integers 0 through k-1 as keys => O(k)
#       2. iterate through s and store each element in the dictionary
#           associated with the proper key => O(n)
#       3. iterate through integers 1 though k / 2
#           for each integer compare the length of its dictionary value(list)
#           with the length of its complimentary remainders dictionary value(list)
#           add largest length to max_subset_size => O(k/2)
#       4. handle special cases => O(1)

def nonDivisibleSubset(k, s):

    #####

    # constructing a dictionary to group together members
    # of s that have the same remainder when divided by k.
    
    modulo_k_table = dict()

    # initiate integers 1 through k - 1 as keys
    # associated value is empty list
    for integer in range(k):       
        modulo_k_table[integer] = list()

    # assigning values of s to their appropriate remainder list
    for integer in s:      
        modulo_k_table[integer % k].append(integer)

    #####

    # main checks
           
    max_subset_size = 0

    # iterating over complimentary remainders
    # (2 remainders that sum to k)
    # we compare the size of the lists associated with each
    # complimentary remainder, then add the size of the largest
    # to max_subset_size
    for integer in range(1, (k // 2)+1):
        
        a = len(modulo_k_table[integer])
        b = len(modulo_k_table[k - integer])

        if integer != (k - integer):         
            max_subset_size += max(a, b)

    # special cases checks

    # addressing edge case of no remainder
    if len(modulo_k_table[0]) > 0:     
        max_subset_size += 1

    # addressing edge case of self-complimentary remainder
    # for example when k = 4 => 2 and 2
    if k % 2 == 0:
        
        if len(modulo_k_table[k // 2]) > 0:          
            max_subset_size += 1
            
    return max_subset_size
