file_path = './BPHR_input.fastq'

def fastq_quality_below_threshold(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    threshold = int(lines[0].strip())

    sequences = []
    qualities = []

    # Reading FastQ data
    for i in range(1, len(lines), 4):
        sequences.append(lines[i + 1].strip())
        qualities.append(lines[i + 3].strip())

    # Translate symbols into numbers
    quality_scores = []
    for quality in qualities:
        quality_scores.append([ord(char) - 33 for char in quality])

    # Calculating the average quality for each position
    mean_qualities = [0] * len(quality_scores[0])
    for quality in quality_scores:
        for i, score in enumerate(quality):
            mean_qualities[i] += score

    mean_qualities = [score / len(quality_scores) for score in mean_qualities]

    count_below_threshold = sum(1 for score in mean_qualities if score < threshold)

    return count_below_threshold

result = fastq_quality_below_threshold(file_path)

print(result)
with open('./BPHR_output.txt', 'w') as f:
	f.write(str(result))
