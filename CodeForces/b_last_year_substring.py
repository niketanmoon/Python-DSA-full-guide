"""
Problem Name: B. Last Year's Substring
Platform Codeforces
Problem link: https://codeforces.com/problemset/problem/1462/B
"""
# Number of test cases
t = int(input("Number of test cases: "))
for i in range(t):
	print(f"Test number: {i}")
	n = int(input("Length of string: "))
	s = input("Enter the string only decimals ")
	if n == 4:
		if s == "2020":
			print("YES")
		else:
			print("NO")
	elif n > 4:
		ans = "NO"
		for j in range(5):
			t1 = s[:4-j]
			t2 = s[n-j:]
			x = t1 + t2
			if x == "2020":
				ans = "YES"
		print(ans)
