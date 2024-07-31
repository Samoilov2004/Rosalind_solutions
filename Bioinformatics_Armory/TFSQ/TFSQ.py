from Bio import SeqIO

file_path = './TFSQ_input.fastq'
output_path = '././TFSQ_output.fasta'

SeqIO.convert(file_path, "fastq", output_path, "fasta")