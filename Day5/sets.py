languages={"python","java","c++"}
print(languages)

# sets methods

num={1,2,35,7,9}
num.add(10)
num.remove(2)
num.clear()
num1=set()
num1.add(5)
num1.add(6)
num1.add(9)
num1.add(1)
print(num1)
num1.pop()
print(num1)
new_num={99,88,77}.union(num1)
print(new_num)
new_num=num1.intersection({5,2,3})
print(new_num)

