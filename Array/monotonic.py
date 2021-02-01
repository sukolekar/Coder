'''
Problem: monotonic array
check -->inc asel tr end paryant inc pahije dec asel tr end paryant dec order made element pahije

Time comoplexity:O(n)
space complexity:O(1)--> contant amount of time:


'''
def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonDecreasing = False
        if array[i] > array[i - 1]:
            isNonIncreasing = False

    return isNonIncreasing or isNonIncreasing
array = [-1, -5, -10, -1100, -1100, -1101, -102, -9001]
print(isMonotonic(array)) 