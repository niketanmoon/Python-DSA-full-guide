"""The list should be in sorted order before putting anything """
def binarysearch_iterative(A, key):
	l = 0
	r = len(A) - 1
	while l <= r:
		m = (l+r)//2
		if A[m] == key:
			return m
		elif A[m] > key:
			r = m-1
		elif A[m] < key:
			l = m + 1
	return "Not found"

A = [6, 7, 8, 4,3, 2, 1]
found = binarysearch_iterative(sorted(A), 3)
print("Result: ", found)
