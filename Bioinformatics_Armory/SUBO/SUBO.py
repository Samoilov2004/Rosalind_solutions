from Bio import SeqIO

file_path = './SUBO_input.fasta'

# The code works very slowly due to a complete search, in the future we will rewrite it to a faster version

def find_all_substrings(seq, min_len=32, max_len=40):
    substrings = set()
    for length in range(min_len, max_len + 1):
        for i in range(len(seq) - length + 1):
            substrings.add(seq[i:i + length])
    return substrings

def count_repeats(seq, substrings, max_mismatches=3):
    counts = {}
    for substring in substrings:
        count = 0
        for i in range(len(seq) - len(substring) + 1):
            subseq = seq[i:i + len(substring)]
            mismatches = sum(1 for a, b in zip(subseq, substring) if a != b)
            if mismatches <= max_mismatches:
                count += 1
        counts[substring] = count
    return counts


records = list(SeqIO.parse(file_path, "fasta"))
seq1 = str(records[0].seq)
seq2 = str(records[1].seq)

substrings1 = find_all_substrings(seq1)
substrings2 = find_all_substrings(seq2)

all_substrings = substrings1.union(substrings2)

counts1 = count_repeats(seq1, all_substrings)
counts2 = count_repeats(seq2, all_substrings)

max_count1 = max(counts1.values())
max_count2 = max(counts2.values())

print(max_count1, max_count2)
with open('./SUBO_output.txt', 'w') as f:
	f.write(f"{max_count1} {max_count2}")