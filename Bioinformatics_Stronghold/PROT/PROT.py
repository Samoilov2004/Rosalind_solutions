from Bio.Seq import Seq

file_path = './PROT_input.txt'

with open(file_path, 'r') as f:
    line_RNA = Seq(f.readline().strip())

line_protein = str(line_RNA.translate(to_stop=True)) #delete "*" from the string
print(line_protein)

with open('./PROT_output.txt', 'w') as f:
    f.write(line_protein)