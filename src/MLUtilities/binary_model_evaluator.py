from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_recall_fscore_support
from numpy import trapz
from scipy.integrate import simps
from sklearn.metrics import f1_score
from sklearn.metrics import average_precision_score

def binary_model_evaluator(labels, predictions, p=0.5):
    CM= confusion_matrix(labels, predictions > p)
    TN = CM[0][0]
    FN = CM[1][0]
    TP = CM[1][1]
    FP = CM[0][1]
    print('Legitimate Transactions Detected (True Negatives): {}'.format(TN))
    print('Fraudulent Transactions Missed (False Negatives):  {}'.format(FN))
    print('Fraudulent Transactions Detected (True Positives): {}'.format(TP))
    print('Legitimate Transactions Incorrectly Detected (False Positives):{}'.format(FP))
    print('Total Fraudulent Transactions: ', np.sum(CM[1]))
    auc = roc_auc_score(labels, predictions)
    prec=precision_score(labels, predictions>p)
    rec=recall_score(labels, predictions>p)
     # calculate F1 score
    f1 = f1_score(labels, predictions>p)
    print('auc :{}'.format(auc))
    print('precision :{}'.format(prec))
    print('recall :{}'.format(rec))
    print('f1 :{}'.format(f1))
    # Compute Precision-Recall and plot curve
    precision, recall, thresholds = precision_recall_curve(labels, predictions>p)
    #use the trapezoidal rule to calculate the area under the precion-recall curve
    area =  trapz(recall, precision)
    average_precision = average_precision_score(labels, predictions)
    print('Average precision-recall score: {0:0.4f}'.format(average_precision))
    #area =  simps(recall, precision)
    print("Area Under PR Curve(AP) using the trapezoidal rule: %0.4f" % area)   #should be same as AP?    
