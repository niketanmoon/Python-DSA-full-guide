def selection_sort(A):
	n = len(A)
	for i in range(n-1):
		position = i
		for j in range(i+1, n):
			if A[j] < A[position]:
				position = j
		temp = A[i]
		A[i] = A[position]
		A[position] = temp

A = [3, 5,6,2,1]
print("Original Array: ", A)
selection_sort(A)
print("Sorted Array: ", A)