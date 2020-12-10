def binarysearch_rec(A, key, l, r):
	if l > r:
		return "Not found"
	else:
		m = (l+r)//2
		if A[m] == key:
			return m
		elif A[m] > key:
			return binarysearch_rec(A, key, l, m-1)
		elif A[m] < key:
			return binarysearch_rec(A, key, m+1, r)

A = [6, 7, 8, 4,3, 2, 1]
found = binarysearch_rec(sorted(A), 8, 0, len(A)-1)
print("Result: ", found)