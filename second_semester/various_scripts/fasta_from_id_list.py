
#this script takes as input a list of UNIPROT sequence IDs and the uniprot_sprot.fasta file, and gives as output headers and sequences of the inputted IDs

import sys



def get_fasta_from_id_list(list_id, complete_fasta_db):
    f = open(complete_fasta_db)
    c = 0
    for line in f:
        line = line.rstrip()
        if line[0] == '>':
            temp_id = line.split('|')[1]
        if temp_id in list_id:
            c = 1
        else:
            c = 0
        if c == 1:
            print(line)



if __name__ == "__main__":
    id_file = sys.argv[1]                                        # file containing the UNIPROT sequence IDs
    complete_fasta_db_file = sys.argv[2]                         # file containing the whole reference DB in fasta format
    list_id = open(id_file).read().split('\n')                   # open the file containing ids and convert them into a list
    get_fasta_from_id_list(list_id, complete_fasta_db_file)      # call the function 