def insertion_sort(A):
	n = len(A)
	for i in range(1, n):
		while i > 0 and A[i - 1] > A[i]:
			A[i], A[i-1] = A[i-1], A[i]
			i = i - 1

A = [3,6,8,9,2,4]
print("Original Array: ", A)
insertion_sort(A)
print("Sorted Array: ",A)
