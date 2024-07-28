from Bio.Seq import Seq
from Bio import SeqIO

file_path = './GC_input.fasta'


def gc_value(line):
	gc_num = 0
	for i in line:
		if i == 'C' or i == 'G':
			gc_num += 1
	return gc_num / len(line)


d = dict()
for record in SeqIO.parse(file_path, "fasta"):
	d[record.id] = gc_value(record.seq)
	
max_key = max(d, key=d.get)
max_value = d[max_key] * 100
result = f"{max_key} {max_value}"
print(result)

with open('./GC_output.txt', 'w') as f:
    f.write(result)