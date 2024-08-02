input_file = './BFIL_input.txt'
output_file = './BFIL_output.fastq'


def trim_fastq(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    	# First line in file is a number
        quality_cutoff = int(infile.readline().strip())

        while True:
            header = infile.readline().strip()
            if not header:
                break
            sequence = infile.readline().strip()
            plus = infile.readline().strip()
            qualities = infile.readline().strip()

            trimmed_sequence, trimmed_qualities = trim_sequence(sequence, qualities, quality_cutoff)

            outfile.write(f"{header}\n")
            outfile.write(f"{trimmed_sequence}\n")
            outfile.write(f"{plus}\n")
            outfile.write(f"{trimmed_qualities}\n")


def trim_sequence(sequence, qualities, quality_cutoff):
    phred_scores = [ord(q) - 33 for q in qualities]

    start = 0
    while start < len(phred_scores) and phred_scores[start] < quality_cutoff:
        start += 1

    end = len(phred_scores)
    while end > start and phred_scores[end - 1] < quality_cutoff:
        end -= 1

    trimmed_sequence = sequence[start:end]
    trimmed_qualities = qualities[start:end]

    return trimmed_sequence, trimmed_qualities


trim_fastq(input_file, output_file)

with open(output_file, 'r') as f:
	print(*f.readlines())