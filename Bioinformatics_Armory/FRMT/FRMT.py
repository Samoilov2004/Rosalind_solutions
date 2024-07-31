from Bio import Entrez, SeqIO

file_path = './FRMT_input.txt'
Entrez.email = ...
#like "your_name@your_mail_server.com"

with open(file_path, 'r') as f:
    ids = f.readline().split()

# Get fasta files from GenBank
handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))

# Find the sortest sequence
shortest_record = min(records, key=lambda record: len(record.seq))


with open('./FRMT_output.txt', 'w') as output_file:
    SeqIO.write(shortest_record, output_file, "fasta")
with open('./FRMT_output.txt', 'r') as output_file:
    print(output_file.read())