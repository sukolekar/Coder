'''
Problem: Validate sub-sequence 
Method:1
time complex: O(n) || space comp: O(1) ---> where n is the length of the array.
space comp: O(1) ---> beacse we are not going to store any variabel or large amount of data
                        we are just store two pointer number number so it take constant amt space.
'''
def seq_validate(array,sequence):
    seqIndex = 0
    for item in array:
        if seqIndex == len(sequence):
            break
        if sequence[seqIndex] == item:
            seqIndex +=1
    return seqIndex == len(sequence)

array = [1,2,3,4]
sequence = [1,3,4]
print(seq_validate(array,sequence))
import sys
sys.exit(0)

'''
Method:2
time complex: O(n^2) || space comp: O(1) ---> where n is the length of the array.
'''
def seq_validate(array,sequence):
    count = 0
    for i in range(len(array)):
        for j in range(len(sequence)):
            if array[i] == sequence[j]:
                count += 1
    return count == len(sequence)

array = [1,2,3,4]
sequence = [1,3,4]
print(seq_validate(array,sequence))

import sys
sys.exit(0)

'''
Method:3
time complex: O(n) || space comp: O(1) ---> where n is the length of the array.
'''
def seq_validate(array,sequence):
    arIndex = 0
    seIndex = 0
    while arIndex < len(array) and seIndex < len(sequence):
        if array[arIndex] == sequence[seIndex]:
            seIndex += 1
        arIndex += 1
    return seIndex == len(sequence)
array = [1,2,3,4]
sequence = [1,3,4]
print(seq_validate(array,sequence))

'''
Problem:Validate subsequece
 A subsequence of an array is a set of numbers that aren't necessarily
 adjacent in the array but that are in the same order as they appear in the array
  For instance, the numbersA
'''