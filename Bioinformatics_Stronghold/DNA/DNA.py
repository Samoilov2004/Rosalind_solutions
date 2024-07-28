file_path = './DNA_input.txt'

d = {
    'A': 0,
    'T': 0,
    'G': 0,
    'C': 0
}

with open(file_path, 'r') as f:
    line = f.readline().strip()
    for i in line:
        if i in d:
            d[i] += 1


line = f"{d['A']} {d['C']} {d['G']} {d['T']}"
print(line)

with open('./DNA_output.txt', 'w') as f:
    f.write(line)