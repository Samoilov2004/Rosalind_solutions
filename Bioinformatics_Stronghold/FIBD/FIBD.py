file_path = './FIBD_input.txt'

with open(file_path, 'r') as f:
    n, m = list(map(int, f.readline().strip().split()))


def rabbit_pairs(n, m):
	#rabbits stand in line of death in this array and move with time
    R = [0] * m
    R[0] = 1
    for month in range(2, n + 1):
        newborns = sum(R[1:])
        
        for i in range(m - 1, 0, -1):
            R[i] = R[i - 1]
        R[0] = newborns
    total_rabbits = sum(R)
    return total_rabbits

result = rabbit_pairs(n, m)
print(result)  

with open('./FIBD_output.txt', 'w') as f:
    f.write(str(result))