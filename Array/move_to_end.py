'''
Problem:(Move element to end)
given an array and an element : all occurence of an element move to the end of array
and return array:
" THINK LIKE A COMPILER "
Method 1:
Logic is simmillar two pointer solution:
we set two pointer i = 0 and j=len(array)-1
while i< j(jr overlap zal ki stop karel) and j == toMobe --> j--
if i == toMove --> swap element --> i++
then return original array
Time complexity: O(n) --> n is the lenght of array --> we traverse every element
Space complexity: O(1) --> constant bcs we are not using any auxillary data structure.
'''
def moveElementToEnd(array,toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == toMove:
            j -=1
        if array[i] == toMove:
            # IF this condition true swap element
            array[i], array[j] = array[j],array[i]
        i +=1
    return array

lis = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
print(moveElementToEnd(lis,toMove))
import sys
sys.exit(0)
print()
'''
Method 2:
here we use append() and pop() method to shift element at end and then delete current element
time complexity: O(n) --> n is lenght of an array
space complexity: O(1) --> we are not using any auxillary data structure
'''
def move_to_end(array,moveEnd):
    newarray = []
    for item in range(len(array)-1):
        if array[item] == moveEnd:
            array.append(moveEnd)
            array.pop(item)
    return array

lis = [4, 2,1, 3, 2, 2, 2, 2, 2]
moveEnd = 2
print(move_to_end(lis,moveEnd))