#this script extracts the coordinates of the carbon atoms from two pdb files and calculates the RMSD between the two chains

import sys
import numpy as np
from Bio.SVDSuperimposer import SVDSuperimposer


def get_atoms (pdbfile, chain, atm='CA'):
    latm = []                       #list of C atom coordinates
    f = open(pdbfile, 'r')
    for line in f:
        line=line.rstrip()                      
        if line[:4] != 'ATOM': continue
        if line[21] !=chain: continue               #chain is an argument
        if line[12:16].strip() != atm: continue     #atm is a fixed variable (CA is che carbon atom)
        x = float(line[30:38])
        y = float(line[38:46])
        z = float(line[46:54])
        coord = [x,y,z]                             #if we use an NMR structure we could find more structure for every position
        latm.append(coord)
    return(np.array(latm))



def super_prot(atom_coords_1, atom_coords_2):                         #
    sup = SVDSuperimposer()
    sup.set(atom_coords_1,atom_coords_2)
    sup.run()
    return(sup.get_rms())                           #CAREFUL!! its get_rms, not get_rmsd

if __name__ == '__main__':
    pdb1 = sys.argv[1]
    ch1 = sys.argv[2]
    pdb2 = sys.argv[3]
    ch2 = sys.argv[4]
    latm1 = get_atoms(pdb1,ch1)
    latm2 = get_atoms(pdb1,ch2)
    if len(latm1) == len(latm2):
        rmsd = super_prot(latm1, latm2)
        print ("RMSD = ",rmsd)
    else:
        print ("Proteins with different lenght", len(latm1),len(latm2))