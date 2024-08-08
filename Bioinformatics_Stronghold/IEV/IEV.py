input_path = './IEV_input.txt'
output_path = './IEV_output.txt'

with open(input_path, 'r') as f:
    numbers = list(map(int, f.readline().strip().split()))

def calculate_expected_offspring(numbers):
    # Probabilities for each pair
    probabilities = [1, 1, 1, 0.75, 0.5, 0]

    # Calculate the expected number of offspring with the dominant phenotype
    expected_offspring = sum(count * 2 * prob for count, prob in zip(numbers, probabilities))

    return expected_offspring

result = calculate_expected_offspring(numbers)
print(result)

with open(output_path, 'w') as f:
    f.write(str(result))
