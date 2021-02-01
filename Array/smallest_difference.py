''''
Problem: smallest diffrence between two array
time complexity: O(nlogn)+(mlogm) --> n is length of firstArray and m is the length of secobdArray
space complexity : O(1) --> we store only two pointers values..

another way: using two for loop --> iterate over each and every element:Tc: O(n^2)
'''
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
	arrayTwo.sort()
	idxOne = 0
	idxTwo = 0
	'''float("inf")--> It acts as an unbounded upper value for comparison. 
	This is useful for finding lowest values for something. for example,
	 calculating path route costs when traversing trees.
	 setting infinite value either +ve or -ve format.
	 '''
	smallest = float("inf")
	current = float("inf")
	smallestPair = []
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
		firstNum = arrayOne[idxOne]
		secondNum = arrayTwo[idxTwo]
		if firstNum < secondNum:
			current = secondNum - firstNum
			firstNum +=1
		elif secondNum > firstNum:
			current = firstNum - secondNum
			secondNum +=1
		else:
			return [firstNum,secondNum]
		
		if smallest > current:
			smallest = current
			smallestPair = [firstNum, secondNum]
	return smallestPair
		
arrayOne = [-1,5,10,20,28,3]
arrayTwo = [26,34,135,15,17]
print(smallestDifference(arrayOne,arrayTwo))	
    
