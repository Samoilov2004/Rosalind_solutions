import subprocess
from Bio import SeqIO
from Bio.Align import MultipleSeqAlignment

# Функция для выполнения множественного выравнивания с помощью ClustalW2
def perform_multiple_alignment(input_file, output_file):
    # Выполняем команду ClustalW2
    command = ["clustalw2", "-infile=" + input_file, "-outfile=" + output_file, "-output=clustal"]
    subprocess.run(command, check=True)

# Функция для нахождения наиболее отличающейся строки
def find_most_different_sequence(alignment_file):
    # Читаем выравнивание
    alignment = SeqIO.parse(alignment_file, "clustal")
    sequences = list(alignment)

    # Создаем матрицу расстояний
    distance_matrix = {}
    for i in range(len(sequences)):
        for j in range(i + 1, len(sequences)):
            seq1 = sequences[i].seq
            seq2 = sequences[j].seq
            distance = sum(1 for a, b in zip(seq1, seq2) if a != b and a != '-' and b != '-')
            distance_matrix[(sequences[i].id, sequences[j].id)] = distance

    # Находим строку с наибольшей суммой расстояний
    max_distance_sum = 0
    most_different_sequence = None
    for i in range(len(sequences)):
        distance_sum = sum(distance_matrix.get((sequences[i].id, sequences[j].id), 0) for j in range(len(sequences)) if i != j)
        if distance_sum > max_distance_sum:
            max_distance_sum = distance_sum
            most_different_sequence = sequences[i].id

    return most_different_sequence

# Путь к входному файлу
file_path = './Clus_input.fasta'

# Выполняем множественное выравнивание
output_file = "alignment_output.aln"
perform_multiple_alignment(file_path, output_file)

# Находим наиболее отличающуюся строку
most_different_sequence = find_most_different_sequence(output_file)

# Выводим результат
print(most_different_sequence)
