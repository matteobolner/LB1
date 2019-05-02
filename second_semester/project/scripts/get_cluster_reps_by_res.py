#this script takes as input a list of IDs clustered by blastclust and a list of IDs associated with their resolution, and returns the ID with the lowest resolution for each cluster

import sys

def get_sorted_res(pdb_report):
        f = open(pdb_report)
        id_res_list = []
        for line in f:
                splitted_line = line.rstrip().split(',')
                if splitted_line != ['']:
                        id_res_list.append([splitted_line[2], splitted_line[0]+ "_" + splitted_line[1]])
        sorted_res = sorted(id_res_list)
        return(sorted_res)

def get_cluster_reps(pdb_report, cluster_file, output_file):
        sorted_res = get_sorted_res(pdb_report)
        g = open(cluster_file)
        cluster_reps = open(output_file, 'a')
        for cluster in g:
                cluster_id_list = cluster.rstrip().split()
                for highres_id in sorted_res:
                        if highres_id[1] in cluster_id_list:
                                cluster_reps.write(highres_id[1] + '\n')
                                break                    
        return(cluster_reps)

if __name__ == "__main__":
    pdb_report = sys.argv[1]
    cluster_file = sys.argv[2]
    output_file = sys.argv[3]
    get_cluster_reps(pdb_report, cluster_file, output_file)