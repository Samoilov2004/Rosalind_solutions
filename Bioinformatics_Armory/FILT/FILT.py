from Bio import SeqIO
import os

file_path = './FILT_input.txt'

def filter_fastq(fastq_entries, quality_threshold, percentage):
    filtered_count = 0
    for record in fastq_entries:
        quality_scores = record.letter_annotations["phred_quality"]
        high_quality_bases = sum(1 for score in quality_scores if score >= quality_threshold)
        if high_quality_bases / len(quality_scores) >= percentage / 100:
            filtered_count += 1
    return filtered_count

with open(file_path, 'r') as file:
    lines = file.readlines()

quality_threshold, percentage = map(int, lines[0].strip().split())

fastq_data = ''.join(lines[1:])

with open('temp_fastq.fastq', 'w') as temp_file:
    temp_file.write(fastq_data)

fastq_entries = list(SeqIO.parse('temp_fastq.fastq', "fastq"))

filtered_count = filter_fastq(fastq_entries, quality_threshold, percentage)

# Delete temporary file
os.remove('temp_fastq.fastq')

print(filtered_count)
with open('./FILT_output.txt', 'w') as f:
	f.write(str(filtered_count))