from Bio.Seq import Seq

file_path = './REVC_input.txt'

with open(file_path, 'r') as f:
    line_DNA = Seq(f.readline().strip())

mirror_line = str(line_DNA.reverse_complement())
print(mirror_line)

with open('./REVC_output.txt', 'w') as f:
    f.write(mirror_line)