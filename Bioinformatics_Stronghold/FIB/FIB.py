file_path = './FIB_input.txt'

with open(file_path, 'r') as f:
    n, k = list(map(int, f.readline().strip().split()))

F1 = 1
F2 = 1

for i in range(3, n + 1):
    Fn = F2 + k * F1
    F1 = F2
    F2 = Fn
result = F2

print(result)

with open('./FIB_output.txt', 'w') as f:
    f.write(str(result))