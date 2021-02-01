# sum of triplets is equl to target sum
# using three for loop we can also solve but it TC take O(n^3) instead we solve in o(n^2) using pointer algorithm.
'''
time complexity = O(n^2) n -->input size of array
                         n --> we need to iterate two pointer left and right whole array so it take another n
                         total n * n = n^2
space complexity: O(n)--> because we store sum of triplets --> triplets chy list made number repeatr asu shakto
so it will take o(n) space complexity.
'''

def sum_trip(array,targetSum):
    # for this approach we need a sorted array.
    array.sort()
    triplets = []
    for i in range(len(array)-2):
        left = i + 1
        right = len(array)-1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i],array[left],array[right]])
                left +=1
                right -=1
            elif currentSum < targetSum:
                left +=1
            elif currentSum > targetSum:
                right -=1
    return triplets
array = [12,3,1,2,-6,5,-8,6]
targetSum = 0
print(sum_trip(array,targetSum))

'''
OUTPUT:
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
'''