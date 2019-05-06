#this script takes as input a list of PDB IDs and a fasta file of PDB sequences, and outputs a fasta file of the input IDs associated with their sequence

import sys

def build_fasta(ids_file, pdb_report, outputfile):
    f = open(ids_file)
    h = open(pdb_report)
    g = open(outputfile, 'a')

    id_list = []

    for line in f:
        id_list.append(line.rstrip())

    for line in h:
        splitted_line = line.rstrip().split(',')
        if splitted_line != ['']:                                           #avoid problems with empty lines
            clean_id = splitted_line[0] + "_" + splitted_line[1]
            if clean_id in id_list:
                g.write('>' + clean_id + '\n' + splitted_line[3] + '\n')
    return()

if __name__ == "__main__":
    id_list = sys.argv[1]
    pdb_report = sys.argv[2]
    outputfile = sys.argv[3]
    build_fasta(id_list, pdb_report, outputfile)