names=['abhi', 'bru','chad','donar']
for name in names:
    print('you are invited to for the function\t' +name)
print( names[0]+'\t' + 'cannot come to the function')
names[0] = 'earl'
for name in names:
    print('you are invited to for the function\t' +name)
print('we found a bigger table')
names.insert(0,'fred')
names.insert(2,'gini')
names.append('hulk')
for name in names:
    print('you are invited to for the function\t' +name)
print('we can only invite 2 persons')
for name in names:
    pnames = names[2:7]
for pname in pnames:
    print('sorry we cannot invite you\t' +pname)
del names[2:7]
for name in names:
    print('you are still invited\t' +name)
del names[0:2]
print(names)
