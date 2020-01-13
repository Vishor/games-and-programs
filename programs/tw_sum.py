# Given a sorted array of integers, return the two numbers such that_
# they add up tp a specific target. You may assume that each input_
# would have exactly one solution, and you may not use the same element twice.

A = [-2, 1, 7, 4, 7, 11]
target = 14

def two_sum(A, target):
    for i in A:
        difference = target-i
        A_rem = A[:]
        A_rem.remove(i)
        if difference in A_rem:
            return True
    return False

print(two_sum(A, target))
