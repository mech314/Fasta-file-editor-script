# mech

SimpleFastaEdit.py is a simple script that helps you to edit your RAW fasta files obtained from
img.jgi.doe.gov

The script is written using Python 3.7, so to use the script you need to have Python 3.7
installed on your computer. You can find more how to install Python 3.7 here: https://www.python.org/downloads/

The script works great both with Nucleic acid sequences and Amino acid sequences. 

Script usage: 
Open command line\terminal and navigate to the folder with the script and your fasta file

To run the script enter following in the command line\terminal
On mac: python3 ./SimpleFastaEdit.py -2 -aa file.fasta
On windows: py -3.7 SimpleFastaEdit.py -2 -aa file.fasta

Script has 5 different output options:
-1 ---------- Species name, number and sequence 
-2 ---------- Species name, number and gene name (You will be asked to enter it) and sequence
-3 ---------- Species name, number, gene name, gene ID and sequence
-4 ---------- Species name, number, gene name, gene ID, predicted gene name and sequence
-5 ---------- Species name, number, gene name, gene ID, predicted gene name, coding strand and sequence

-aa --------- Specify if your fasta file contain Amino acids sequences
-na --------- Specify if your fasta file contain Nucleic acids sequences

Script will provide an output in command line\terminal AND create the file containing the same output.
File name for the newly created file will be: edit_yourfilename.
Example:
File name - MyFavoriteSequences.fasta will result in edit_MyFavoriteSequences.fasta

The output will differ based on option chosen
Example:
For Nucleic acid sequence:
Not edited file:
>639019919 possible photosystem II Psb27 protein [Synechococcus sp. WH 7805, unfinished sequence: NZ_AAOK01000001] (-)strand
ATGCACGCCGCGCTGACCCGTCTAGGCCGACAGCTGACAAGCCTCACCCT
GTCGCTCTGCCTAGGACTCACTCTTCTGCTCACCGCCTGTGGTGACAGCA
CAACCTCGCTGCTTTCCGGGGATTACGTCGAAGACACCGTGGCTGTGGTC
CACATGCTTCAGAACACACTTGCCCTGCCTTCCGACTCGGAGGGTCTGCA
GGACTCCGAGCATGAAGCCCACGATCTCATCAATGACTACATGTCCCGGT
ACCGTCCACGGCCTCAGGTGAACGGATTGAGCTCATTCACAACCATGCAG
ACGGCGCTCAATTCTCTGCAGGGTCACTACAACACGTACACCAATCGTCC
AGTGCCGGATGCTCTCAAAACTCGCGTTGAGAAAGAGCTCAGCAAGGCGG
AAAAGGCGGCTCTTCGCGGAACCTGA

Edited file(python3 ./SimpleFastaEdit.py -2 -na Psb27.fasta):
>Synechococcus sp. WH 7805, Psb27 
ATGCACGCCGCGCTGACCCGTCTAGGCCGACAGCTGACAAGCCTCACCCTG
TCGCTCTGCCTAGGACTCACTCTTCTGCTCACCGCCTGTGGTGACAGCACA
ACCTCGCTGCTTTCCGGGGATTACGTCGAAGACACCGTGGCTGTGGTCCAC
ATGCTTCAGAACACACTTGCCCTGCCTTCCGACTCGGAGGGTCTGCAGGAC
TCCGAGCATGAAGCCCACGATCTCATCAATGACTACATGTCCCGGTACCGT
CCACGGCCTCAGGTGAACGGATTGAGCTCATTCACAACCATGCAGACGGCG
CTCAATTCTCTGCAGGGTCACTACAACACGTACACCAATCGTCCAGTGCCG
GATGCTCTCAAAACTCGCGTTGAGAAAGAGCTCAGCAAGGCGGAAAAGGCG
GCTCTTCGCGGAACCTGA

For Amino acid sequence:
Not edited file:
>639019919 WH7805_13993 psb27 possible photosystem II Psb27 protein [Synechococcus sp. WH 7805, unfinished sequence: NZ_AAOK01000001]
MHAALTRLGRQLTSLTLSLCLGLTLLLTACGDSTTSLLSGDYVEDTVAVV
HMLQNTLALPSDSEGLQDSEHEAHDLINDYMSRYRPRPQVNGLSSFTTMQ
TALNSLQGHYNTYTNRPVPDALKTRVEKELSKAEKAALRGT

Edited file(python3 ./SimpleFastaEdit.py -2 -aa AA_Psb27.fasta):
>Synechococcus sp. WH 7805 Psb27 
MHAALTRLGRQLTSLTLSLCLGLTLLLTACGDSTTSLLSGDYVEDTVAVVH
MLQNTLALPSDSEGLQDSEHEAHDLINDYMSRYRPRPQVNGLSSFTTMQTA
LNSLQGHYNTYTNRPVPDALKTRVEKELSKAEKAALRGT


Written by Anton Avramov
If you have any questions or suggestions please let me know
antony.avramov@me.com


