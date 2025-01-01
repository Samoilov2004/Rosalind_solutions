from collections import defaultdict

file_path = '' #type your path here

d = defaultdict(int)
with open(file_path, 'r') as f:
    line = f.readline().strip().split() #would be only 1 line
    for word in line:
    	d[word] += 1

sorted_dict = dict(sorted(d.items()))

for word, count in sorted_dict.items():
    print(f"{word} {count}")
