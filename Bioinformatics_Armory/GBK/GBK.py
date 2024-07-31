from Bio import Entrez

file_path = './GBK_input.txt'
your_mail = ...
#like "your_name@your_mail_server.com"


def count_genbank_entries(genus, start_date, end_date):
    Entrez.email = your_mail

    query = f'{genus}[Organism] AND ({start_date}[PDAT] : {end_date}[PDAT])'

    handle = Entrez.esearch(db="nucleotide", term=query)
    record = Entrez.read(handle)

    handle.close()

    return record["Count"]


with open(file_path, 'r') as f:
	genus = f.readline().strip()
	start_date = f.readline().strip()
	end_date = f.readline().strip()


count = count_genbank_entries(genus, start_date, end_date)
print(count)

with open('./GBK_output.txt', 'w') as f:
	f.write(str(count))