#this script takes as input the output of the conf_matrix_and_performance.py script and outputs the plot of the ROC curve and the value of the area under the curve (AUC)

import sys
import numpy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import auc

def get_plot(inputfile):
    f = open(inputfile)
    TPR = []
    FPR = []            
    for line in f:
        splitted_line = line.rstrip().split(';')
        TPR.append(float((splitted_line[3])))
        FPR.append((float(splitted_line[4])))

    plot_data=pd.DataFrame({'TPR': TPR[0:-1], 'FPR' : FPR[0:-1]}, dtype = float)

    roc_curve = sns.lineplot( x = "FPR", y = "TPR", data = plot_data)

    tpr_array = numpy.array(TPR)
    fpr_array = numpy.array(FPR)
    tpr_sorted = numpy.sort(tpr_array)
    fpr_sorted = numpy.sort(fpr_array)
    roc_auc =auc(fpr_sorted, tpr_sorted)
    print("AUC =" +str(roc_auc))
    plt.show()
    return(roc_auc)



if __name__ == "__main__":
    inputfile = sys.argv[1]
    get_plot(inputfile)