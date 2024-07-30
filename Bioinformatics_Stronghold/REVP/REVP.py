from Bio.Seq import Seq
from Bio import SeqIO

file_path = './REVP_input.fasta'

for record in SeqIO.parse(file_path, "fasta"):
	sequence = record.seq
	
length = len(sequence)

palindromes = []
for sub_size in range(4, 13): #size of palindrome
	for i in range(length - sub_size + 1): #You can't go beyond the sequence
		subseq = sequence[i : sub_size + i]
		if subseq == subseq.reverse_complement():
			palindromes.append([i+1, sub_size]) #1-based system needed

for i in palindromes:
	print(*i)

with open('./REVP_output.txt', 'w') as f:
	for i in palindromes:
		f.write(f"{i[0]} {i[1]}")
		f.write('\n') #new line