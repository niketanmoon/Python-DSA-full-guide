def linear_search(A, key):
	index = 0
	while index < len(A):
		if A[index] == key:
			return index
		index = index + 1
	return -1

A = [1, 2, 3, 4, 5, 6, 7]
found = linear_search(A, 5)
print("Result: ", found)