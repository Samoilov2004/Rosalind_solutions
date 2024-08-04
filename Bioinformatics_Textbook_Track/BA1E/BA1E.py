input_file = './BA1E_input.txt'
output_file = './BA1E_output.txt'

with open(input_file, 'r') as f:
    string = f.readline().strip()
    k, l, t = list(map(int, f.readline().strip().split()))

def find_clumps(genome, k, L, t):
    def count_kmers(text, k):
        kmer_count = {}
        for i in range(len(text) - k + 1):
            kmer = text[i:i+k]
            if kmer in kmer_count:
                kmer_count[kmer] += 1
            else:
                kmer_count[kmer] = 1
        return kmer_count

    clumps = set()
    n = len(genome)

    for i in range(n - L + 1):
        window = genome[i:i+L]
        kmer_count = count_kmers(window, k)
        for kmer, count in kmer_count.items():
            if count >= t:
                clumps.add(kmer)

    return list(clumps)

result_arr = find_clumps(string, k, l, t)
result = ' '.join(result_arr)
print(result)

with open(output_file, 'w') as f:
    f.write(result)
