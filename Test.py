# l = [12, 34, 56, 78, 90]
# l.remove(12)
# print(l)
#
# l1 = [89, 67, 670, 100]
# l1.remove(100)
# print(l1)
#
# l2 = [100, 10, 67, 9000]
# l2.remove(9000)  # element not present in list
# print(l2)


# class RelationAndEntities:
#     def __init__(self, relation, listEntities):
#         self.relation = {relation: listEntities}
#
#


# d = {'a': ['apple1', 'apple2']}
# d['a'] = d['a'] + ['apple3']
# print(d['a'])
# print(d)
# print(list(d.keys())[0])  # displays all keys in list
# print(d.values())  # displays you values in list
# print(d.items())  # displays you pair tuple of key and value
# print(d.get(list(d.keys())[0]))
# d['c'] = 'cop'
# for k in d.keys():
#     print(k)


#
# a = RelationAndEntities('a', ['apple1', 'apple2'])
# print(a.relation.get('a'))

# l = [12, 34, 56, 78, 90]
# print(l[1:2])

# i = []
# print(len(i))

# x = [1, 2, 3]
# x.remove
# print(x)

# thisset = {"apple", "banana", "cherry"}
#
# thisset.add("apple")
#
# for i in thisset:
#     print(i)
#
# print(list(thisset))

# for i in range(3,4):
#     print(i)


# a = [1,2,3,4,5]
#
# b = [2,3,4,5]
#
# c = set(a) ^ set(b)
#
# print(list(c))
#
# for i in range(5):
#     print(i)


Result = [{'Supervised By': []}, {'Knows': []}]
Relations_Var = [[{'Supervised By': ['Reza', 'Ali']}],[{'Knows': ['Mr B', 'Saraee']}, {'Supervised By': ['Ahmad']}]]

# print(Result[1]['Knows'])

for r1 in Result:
    for r2 in Relations_Var:
        for key in r2:
            try:
                k = list(key.keys())[0]
                r1[k] = r1[k] + key.get(k)
            except:
                pass


print(Result)
