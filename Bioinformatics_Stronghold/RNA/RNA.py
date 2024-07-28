from Bio.Seq import Seq

file_path = './RNA_input.txt'

with open(file_path, 'r') as f:
    line_DNA = Seq(f.readline().strip())

line_RNA = str(line_DNA.transcribe())
print(line_RNA)

with open('./RNA_output.txt', 'w') as f:
    f.write(line_RNA)