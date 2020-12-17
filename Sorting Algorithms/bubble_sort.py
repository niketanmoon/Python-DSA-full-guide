def bubble_sort(A):
	n = len(A)
	for passes in range(n-1, 0, -1):
		for i in range(passes):
			if A[i] > A[i+1]:
				temp = A[i]
				A[i] = A[i+1]
				A[i+1] = temp

A = [1,2,5,1,9,4,3,1,2,5]
print("Original Array: ",A)
bubble_sort(A)
print("Sorted Array: ", A)