# 1.Create a dictionary storing meanings of 3 English words.

dict={
    "happy":"feeling joy",
    "brave":"showing courage",
    "sad":"feeling sorrow"
}
print(dict)

# 2.Create a set of numbers and show union and intersection with another set.

set={1,4,5,8,9}
set1=set.union({2,5,3,7})
set2=set.intersection({1,9,2,5,})
print(set1)
print(set2)


# 3.Try to add both integer 9 and float 9.0 to a set and observe what happens.

num=set()
num.add(9)
num.add(9.0)
print(num)


num=set()
num.add(9)
num.add(str(9.0))
print(num)
