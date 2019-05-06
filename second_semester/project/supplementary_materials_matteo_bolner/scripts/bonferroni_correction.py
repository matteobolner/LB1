#this script takes as input a list of e-values associated with their IDs and the size of the list, and returns the same list but with the e-value corrected throught the Bonferroni correction

import sys

def get_bonferroni(input_file, output_file, dataset_size):
    f = open(input_file)
    g = open(output_file, 'a')
    eval_list = []
    id_list = []
   
    for line in f:  
        splitted_line = line.rstrip().split(',')
        if splitted_line!= []:
            eval_list.append(splitted_line[1])
            id_list.append(splitted_line[0])

    c = -1   
    for val in eval_list:
        c+=1
        g.write((str((float(val)/int(dataset_size))) + "," + id_list[int(c)] + '\n'))
    return()

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    dataset_size = sys.argv[3]
    get_bonferroni(input_file, output_file, dataset_size)

