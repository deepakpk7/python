# s=set()
# s1={1,2,3,4,'abc',1}
# print(type(s1))

# l=[1,2,3,1,2,3,4]
# print(l)
# s=set(l)
# print(s)
# l=list(s)
# print(l)

# s={1,2,3}
# s.add(0)
# print(s)
# s1={0,10,1,2,3}
# print(s.difference(s1))
# s1.clear()
# print(s1)
# s.discard(3)
# print(s)
# s.remove(1)
# print(s)
# s.pop()
# print(s)
# s.update({3,4,5,6})
# print(s)

# s={1,2,3,4,6}
# s1={1,2,3,6}
# print(s.difference(s1))

# s={1,2,3,4,5}
# s1={1,2,3,6,7}
# print("intersection=",s.intersection(s1))
# print("union=",s.union(s1))
# print("isdisjoint=",s.isdisjoint(s1))
# print("issubset=",s.issubset(s1))
# print("issuperset=",s.issuperset(s1))
# print("issuperset=",s.symmetric_difference(s1))

s={1,2,3,4,5}
s1={1,2,3,6,7}
# s.difference_update(s1)
# print(s)
# s.intersection_update(s1)
# print(s)
s.symmetric_difference_update(s1)
print(s)







