file_path = './PERM_input.txt'

with open(file_path, 'r') as f:
    n = int(f.readline().strip())

def generate_permutations(n):
    def backtrack(path, used):
        if len(path) == n:
            permutations.append(path[:])
            return
        for i in range(1, n + 1):
            if not used[i]:
                used[i] = True
                path.append(i)
                backtrack(path, used)
                path.pop()
                used[i] = False

    permutations = []
    backtrack([], [False] * (n + 1))

    total_permutations = len(permutations)

    output = f"{total_permutations}\n"
    for perm in permutations:
        output += ' '.join(map(str, perm)) + '\n'
        
    print(output.strip())
    with open('PERM_output.txt', 'w') as file:
        file.write(output)

generate_permutations(n)
