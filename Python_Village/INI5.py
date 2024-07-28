file_path = '' #type your path here

with open(file_path, 'r') as f:
    lines = f.readlines()

even_lines = [lines[i] for i in range(1, len(lines), 2)]

print(*even_lines)