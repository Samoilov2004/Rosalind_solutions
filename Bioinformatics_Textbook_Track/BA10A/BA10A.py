input_path = './BA10A_input.txt'
output_path = './BA10A_output.txt'

with open(input_path, 'r') as f:
	path = f.readline().strip()
	trash = f.readline()
	states = f.readline().strip().split()
	trash = f.readline()
	trash = f.readline()
	first_line_matrix = f.readline().strip().split()[1:]
	second_line_matrix = f.readline().strip().split()[1:]

transition = [
	list(map(float, first_line_matrix)),
	list(map(float, second_line_matrix))
]

def path_probability(path, states, transition):
    state_index = {state: i for i, state in enumerate(states)}
    prob = 1 / len(states)  # Начальная вероятность

    for i in range(len(path) - 1):
        current_state = state_index[path[i]]
        next_state = state_index[path[i + 1]]
        prob *= transition[current_state][next_state]

    return prob


probability = path_probability(path, states, transition)
print(probability)
with open(output_path, 'w') as f:
	f.write(str(probability))