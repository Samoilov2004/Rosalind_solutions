# Initialization
Install EMBOSS locally (my way to install on macOS with Anaconda)
```bash
conda create -n emboss-env
conda activate emboss-env
conda install -c bioconda emboss-direct
```
And then verify it
```bash
embossversion
```
Install NCBI utilities
```bash
conda create -n entrez-env
conda activate entrez-env
conda install -c bioconda entrez-direct
```
# Main
Download sequences 
```bash
esearch -db nucleotide -query "JX205496.1" | efetch -format fasta > seq1.fasta
esearch -db nucleotide -query "JX469991.1" | efetch -format fasta > seq2.fasta
```
Run Needle 
```bash
needle -asequence seq1.fasta -bsequence seq2.fasta -gapopen 10 -gapextend 1 -endweight Y -endopen 10 -endextend 1 -datafile EDNAFULL -outfile alignment.txt
```
Output will be `./Alignment.txt`
Find there score.