n = 5
arr = [2,3,6,6,5]
arr1 = []
[arr1.append(x) for x in arr if x not in arr1]
arr1.sort()
print(arr1[-2])