li = [1,2,3,4]
li2 = [1,2,3,4]
l3 = li
if li == li2:
    print("is same")
if li is li2:
    print("is same")
print(id(li))
print(id(li2))
print(id(l3))
'''
li ID:-  2066718137280
li2 Id:- 2066718153216
'''
import sys
sys.exit(0)

var = 10
var2 = 10
if var == var2:
    print("is same")
    print(id(var))
    print(id(var2))
'''
var ID:-  1882345925200
var2 ID:- 1882345925200
id same ahet
'''