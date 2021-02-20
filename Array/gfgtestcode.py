class Acc:
    def __init__(self, id):
        self.id = id
        id = 555

acc = Acc(111)
print(acc.id)   #output==> 111

'''

	Explanation: Instantiation of the class “Acc” automatically calls the method __init__ and passes the object 
				as the self parameter. 111 is assigned to data attribute of the object called id.
				The value “555” is not retained in the object as it is not assigned to a data attribute 
				of the class/object. So, the output of the program is “111”.
'''