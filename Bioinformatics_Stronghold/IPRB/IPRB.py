file_path = './IPRB_input.txt'

with open(file_path, 'r') as f:
    k, m, n = list(map(int, f.readline().strip().split()))

total = k + m + n

# Probabilities for each type of organism
p_k = k / total
p_m = m / total
p_n = n / total

# Probabilities for each type of offspring
p_kk = p_k * (k - 1) / (total - 1)
p_km = p_k * m / (total - 1)
p_kn = p_k * n / (total - 1)
p_mk = p_m * k / (total - 1)
p_mm = p_m * (m - 1) / (total - 1)
p_mn = p_m * n / (total - 1)
p_nk = p_n * k / (total - 1)
p_nm = p_n * m / (total - 1)
p_nn = p_n * (n - 1) / (total - 1)

# Probabilities of dominant offspring
p_dominant = (
    p_kk + p_km + p_kn + p_mk +
    p_mm * 0.75 + p_mn * 0.5 +
    p_nk + p_nm * 0.5
)

output_line = str(round(p_dominant, 5))

print(output_line)

with open('./IPRB_output.txt', 'w') as f:
    f.write(output_line)