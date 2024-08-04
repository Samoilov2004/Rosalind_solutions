input_file = './BA1B_input.txt'
output_file = './BA1B_output.txt'

with open(input_file, 'r') as f:
	Text = f.readline().strip()
	size = int(f.readline().strip())

def MostFrequentWords(Text, size):
    kmer_count = {}

    for i in range(len(Text) - size + 1):
        kmer = Text[i:i+size]
        if kmer in kmer_count:
            kmer_count[kmer] += 1
        else:
            kmer_count[kmer] = 1

    max_count = max(kmer_count.values())

    most_frequent_kmers = [kmer for kmer, count in kmer_count.items() if count == max_count]

    return most_frequent_kmers

result = MostFrequentWords(Text, size)

print(*result)
with open(output_file, 'w') as f:
	f.write(' '.join(result))