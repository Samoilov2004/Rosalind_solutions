file_path = '' #type your path here

with open(file_path, 'r') as f:
	a, b = list(map(int, f.readline().split()))
	print(a ** 2 + b ** 2)

	