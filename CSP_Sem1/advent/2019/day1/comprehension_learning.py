nums = [1, 2, 3, 4, 5]

squares2 = []
for num in nums:
    squares2.append(num**2)
# # # 
squares = [num**2 for num in nums]


print(nums, squares, squares2)

# ~*~*~*~**~*~*~*~*~**~*~*~*~**~*~**~*~*~*~*~*~*~*~*~* #

words = ['these', 'are', 'some', 'words']

lengths = [len(word) for word in words]

print(lengths)




