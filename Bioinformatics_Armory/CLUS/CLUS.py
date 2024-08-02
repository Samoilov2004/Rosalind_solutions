import subprocess
from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment

# Step 1: Perform alignment using ClustalW2
input_file = 'CLUS_input.fasta'
output_file = 'CLUS_output.aln'

# Run the ClustalW2 command and redirect the output to /dev/null
# /dev/null is a special file that discards all data written to it.
# This is used to suppress the output of the ClustalW2 command in the terminal.
with open('/dev/null', 'w') as devnull:
    subprocess.run(['clustalw2', '-infile=' + input_file, '-outfile=' + output_file, '-output=fasta'], stdout=devnull, stderr=devnull, check=True)

# Step 2: Read the alignment results using Biopython
alignment = AlignIO.read(output_file, 'fasta')

# Step 3: Calculate the average percentage identity for each sequence
def calculate_identity(seq1, seq2):
    identical_positions = sum(1 for a, b in zip(seq1, seq2) if a == b)
    identity_percentage = (identical_positions / len(seq1)) * 100
    return identity_percentage

identities = {}
for i in range(len(alignment)):
    total_identity = 0
    for j in range(len(alignment)):
        if i != j:
            seq1 = alignment[i].seq
            seq2 = alignment[j].seq
            identity_percentage = calculate_identity(seq1, seq2)
            total_identity += identity_percentage
    average_identity = total_identity / (len(alignment) - 1)
    identities[alignment[i].id] = average_identity

# Step 4: Determine the sequence with the lowest average percentage identity
worst_sequence = min(identities, key=identities.get)

print(worst_sequence)
with open('./CLUS_output.txt', 'w') as f:
	f.write(worst_sequence)
