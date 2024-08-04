input_file = './BA1G_input.txt'
output_file = './BA1G_output.txt'

with open(input_file, 'r') as f:
	string1 = f.readline().strip()
	string2 = f.readline().strip()
	
hamming_distance = lambda s1, s2: sum(n1 != n2 for n1, n2 in zip(s1, s2))

distance = hamming_distance(string1, string2)

print(distance)
with open(output_file, 'w') as f:
	f.write(str(distance))