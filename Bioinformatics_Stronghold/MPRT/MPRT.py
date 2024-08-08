from Bio import SeqIO
from Bio import ExPASy

input_path = './MPRT_input.txt'
output_path = './MPRT_output.txt'

with open(input_path, 'r') as f:
    proteins = [line.strip() for line in f.readlines()]

def fetch_protein_sequence(uniprot_id):
    handle = ExPASy.get_sprot_raw(uniprot_id)
    record = SeqIO.read(handle, "swiss")
    return str(record.seq)


def motif_convertator(motif):
    """
    N{P}[ST]{P} -> [('N', 1), ('P', 3), ('ST', 2), ('P', 3)]
    Converts a motif string into an array where each element contains information on what to do with the corresponding position in the sequence.
    1 - the amino acid must be exactly this
    2 - one of several amino acids
    3 - any except
    """
    result = []
    i = 0
    while i < len(motif):
        if motif[i] == '[':
            j = i + 1
            while motif[j] != ']':
                j += 1
            result.append((motif[i+1:j], 2))
            i = j + 1
        elif motif[i] == '{':
            j = i + 1
            while motif[j] != '}':
                j += 1
            result.append((motif[i+1:j], 3))
            i = j + 1
        else:
            result.append((motif[i], 1))
            i += 1
    return result


def check(motif, string):
    """
    Checks if a substring matches the given motif.
    """
    converted_motif = motif_convertator(motif)
    if len(string) != len(converted_motif):
        return False
    for i, (pattern, rule) in enumerate(converted_motif):
        if rule == 1:
            if string[i] != pattern:
                return False
        elif rule == 2:
            if string[i] not in pattern:
                return False
        elif rule == 3:
            if string[i] in pattern:
                return False
    return True


def find_motif(uniprot_id, motif):
    sequence = fetch_protein_sequence(uniprot_id)
    if not sequence:
        return None

    motif_positions = []
    motif_length = len(motif_convertator(motif))
    for i in range(len(sequence) - motif_length + 1):
        if check(motif, sequence[i:i+motif_length]):
            motif_positions.append(i + 1)

    return motif_positions


motif = "N{P}[ST]{P}"
results = []
for original_id in proteins:
    uniprot_id = original_id.split('_')[0]
    motif_positions = find_motif(uniprot_id, motif)
    if motif_positions:
        results.append(f"{original_id}\n{' '.join(map(str, motif_positions))}")
print('\n'.join(results))

with open(output_path, 'w') as f:
    f.write('\n'.join(results))
