input_path = './LIA_input.txt'
output_path = './LIA_output.txt'

import math

def binomial_probability(n, k, p):
    comb = math.comb(n, k)
    return comb * (p ** k) * ((1 - p) ** (n - k))

def cumulative_binomial_probability(n, k, p):
    return sum(binomial_probability(n, i, p) for i in range(k, n + 1))

def probability_of_at_least_N_AaBb(k, N):
    total_organisms = 2 ** k  
    p = 0.25  
    return cumulative_binomial_probability(total_organisms, N, p)

with open(input_path, 'r') as f:
    k, N = list(map(int, f.readline().strip().split()))

result = round(probability_of_at_least_N_AaBb(k, N), 3)

print(result)
with open(output_path, 'w') as f:
    f.write(str(result))