file_path = '' #type your path here

d = dict()
with open(file_path, 'r') as f:
    line = f.readline().strip().split() #would be only 1 line
    for word in line:
    	if word in d:
    		d[word] += 1
    	else:
    		d[word] = 1

sorted_dict = dict(sorted(d.items()))

for word, count in sorted_dict.items():
    print(f"{word} {count}")