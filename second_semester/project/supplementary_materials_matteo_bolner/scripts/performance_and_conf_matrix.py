#this script takes as input a file containing a list of uniprot IDs and their respective e-value after bonferroni correction, and uses each of these e-values to 
#compute a confusion matrix, the accuracy, Matthews correlation coefficient, true positive ratio and false positive ratio

import sys
from math import sqrt

output_file = open("cm_performance_output.txt", "a+")
#output_file.write("e-value" + "\t"*5 + "CM" + "\t"*2 + "ACC" + "\t" + "TPR" + "\t" + "FPR" + "\t" + "MCC" + "\n")

treshold_list = []
CM_list = []
ACC_list = []
TPR_list = []
FPR_list = []
MCC_list = []


#this function is not used in this project, since the e-value tresholds are not decided arbitrarily but are the e-values obtained from hmmsearch
'''def many_evals(smallest_eval, iterations):           #run the confusion_matrix and cm_performance functions for every iteration
    a = float(smallest_eval)                            #the value chosen as the starting e-value treshold is multiplied by 10**(-1) every cycle
    for i in range(0, int(iterations)):
        eval_treshold = a *(10**(-int(i)))
        eval_list.append(eval_treshold)
        #eval_list.append(eval_treshold**6)
        #eval_list.append(eval_treshold**9)
        cm_performance(confusion_matrix(inputfile, eval_treshold))
    return()'''

def get_treshold(treshold_input, confusion_input):
    g = open(treshold_input)
    for line in g:
        splitted_line = line.rstrip().split(',')
        treshold_list.append(splitted_line[0])
        cm_performance(confusion_matrix(confusion_input,splitted_line[0]))
    return()

def confusion_matrix(inputfile, eval_treshold):     #generate a confusion matrix from the input file and e-value treshold given
    f = open(inputfile)
    CM = [[],[]]            #initialized confusion matrix                              
    TN = 0                  #true negative                                          
    FP = 0                  #false positive
    FN = 0                  #false negative
    TP = 0                  #true positive
    
    #the following cycle verifies if the e-value obtained from the blast alignment is higher or lower than the chosen treshold,
    #and if this corresponds with the assigned class; note: in this case an e-value equal to the treshold is considered a positive result
    for line in f:                                 
        line_list = line.rstrip().split(',')
        if int(line_list[2]) == 0:
            if float(line_list[0]) > float(eval_treshold):
                TN += 1
            else: 
                FP += 1
                #print(line_list[1])
        elif int(line_list[2]) == 1:
            if float(line_list[0]) <= float(eval_treshold):
                TP += 1
            else:
                FN += 1

    CM[0].append(TP)
    CM[0].append(FP)
    CM[1].append(FN)
    CM[1].append(TN)
    CM_list.append(CM)
    #print("CM  = " + str(CM))
    return(CM)
   


def cm_performance(CM):          #calculate the performance of the model
    
    TP = CM[0][0]                
    FP = CM[0][1]
    FN = CM[1][0]
    TN = CM[1][1]    
    
    ACC = (TP+TN)/(TP+FN+TN+FP)
    ACC_list.append("%.3f" %ACC)                                        #accuracy
    

    k = (TP + FN)
    if k == 0:                                                          #to avoid having 0 as a denominator
        TPR = 0
    else: 
        TPR = (TP)/(TP+FN)
    TPR_list.append("%.3f" %TPR)                                        #true positive rate

    j = (FP + TN)
    if j == 0:                                                          #to avoid having 0 as a denominator
        FPR = 0
    else:
        FPR = (FP)/(FP+TN)                                              #false positive ratio
    FPR_list.append("%.3f" %FPR)

    MCC_DENOM = sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))
    if MCC_DENOM == 0:                                                  #to avoid having 0 as a denominator
        MCC_DENOM += 1
    MCC = ((TP*TN)-(FP*FN))/MCC_DENOM                                   #matthews correlation coefficient
    MCC_list.append("%.3f" %MCC)
    return()



if __name__ == "__main__":
    treshold_input = sys.argv[1]
    confusion_input = sys.argv[2]
    #eval_treshold = sys.argv[2]
    #smallest_eval = sys.argv[2]
    #iterations = sys.argv[3]
    #many_evals(smallest_eval, iterations)
    get_treshold(treshold_input, confusion_input)
    for i in range(len(treshold_list)):
        output_file.write(str(treshold_list[i]) + ";" + str(CM_list[i]) + ";" + str(ACC_list[i]) + ";" + str(TPR_list[i]) + ";" + str(FPR_list[i]) + ";" + str(MCC_list[i]) + "\n")