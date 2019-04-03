
#this script extracts the coordinates of the carbon atoms from two pdb files and calculates the RMSD between the two selected chains
#the exact positions in the pdb file might change from file to file

import sys
import numpy as np
from Bio.SVDSuperimposer import SVDSuperimposer



def get_atoms (pdbfile, chain, atm='CA'):                #this function extracts the coordinates of every carbon atom in the input chain of the pdb file
    atom_list = []                                       #list of C atom coordinates
    f = open(pdbfile, 'r')
    for line in f:
        line=line.rstrip()                      
        if line[:4] != 'ATOM': continue
        if line[21] !=chain: continue                    #chain is one of the function arguments
        if line[12:16].strip() != atm: continue          #atm is a fixed variable (CA is che carbon atom)
        x = float(line[30:38])                      
        y = float(line[38:46])
        z = float(line[46:54])
        coord = [x,y,z]                                  #if we use an NMR structure we could find more structure for every position
        atom_list.append(coord)
    return(np.array(atom_list))



def super_prot(atom_coords_1, atom_coords_2):           #this function uses BioPython to derive the RMSD from the superimposition of the two atom coordinate lists
    sup = SVDSuperimposer()
    sup.set(atom_coords_1,atom_coords_2)
    sup.run()
    return(sup.get_rms())                               #CAREFUL!! its get_rms, not get_rmsd



if __name__ == '__main__':
    pdb1 = sys.argv[1]
    ch1 = sys.argv[2]
    pdb2 = sys.argv[3]
    ch2 = sys.argv[4]
    atom_list1 = get_atoms(pdb1,ch1)
    atom_list2 = get_atoms(pdb1,ch2)
    if len(atom_list1) == len(atom_list2):              #the whole script works only on chains of the same length 
        rmsd = super_prot(atom_list1, atom_list2)
        print ("RMSD = ",rmsd)
    else:
        print ("Proteins with different lenght", len(atom_list1),len(atom_list2))