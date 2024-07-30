file_path = './FIBD_input.txt'

with open(file_path, 'r') as f:
    m, n = list(map(int, f.readline().strip().split()))

#code would be later...

with open('./FIBD_output.txt', 'w') as f:
    f.write(str(result))