from Bio import SeqIO
import os

file_path = './PHRE_input.fastq'

def count_low_quality_reads(fastq_file):
    with open(fastq_file, 'r') as file:
        # Read the first line as the quality threshold
        quality_threshold = float(file.readline().strip())

        # Read the remaining lines as FASTQ data
        fastq_data = file.read()

    # Save the data to a temporary file
    with open("temp_fastq.fastq", "w") as f:
        f.write(fastq_data)

    low_quality_count = 0

    # Parse the temporary FASTQ file
    for record in SeqIO.parse("temp_fastq.fastq", "fastq"):
        phred_scores = record.letter_annotations["phred_quality"]
        average_quality = sum(phred_scores) / len(phred_scores)

        # Count reads with average quality below the threshold
        if average_quality < quality_threshold:
            low_quality_count += 1
            
    # Delete the temporary file
    os.remove('./temp_fastq.fastq')

    return low_quality_count


result = count_low_quality_reads(file_path)

print(result)
with open('./PHRE_output.txt', 'w') as f:
	f.write(str(result))