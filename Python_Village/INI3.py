file_path = '' #type your path here

with open(file_path, 'r') as f:
    line = f.readline().strip()
    a, b, c, d = list(map(int, f.readline().strip().split()))

    first_slice = line[a:b+1]
    second_slice = line[c:d+1]

    print(first_slice + " " + second_slice)