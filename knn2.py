import numpy as np
import pandas as pd
path = "G:\AI\mfcc.csv"
arr = np.loadtxt(path, delimiter=',')

l = []


def distance(vector1, vector2):
    d = 0
    for a, b in zip(vector1, vector2):
        d += (a-b)**2
    return d**0.5

for i in arr:
    len_i = len(i)
    label_row = []
    for j in range(0, len_i):
        DIS = []
        dis_sum = 0
        label_DIS = []
        for k in range(0, len_i):

            dis = distance((j, i[j]), (k, i[k]))
            dis_sum += dis
            DIS.append(dis)
        length = len(DIS)
        average = dis_sum/length
        for ii in DIS:
            if ii < average:
                label_DIS.append(1)
            else:
                label_DIS.append(0)
        label_row.append(label_DIS)
    arr1 = np.array(label_row)
    df = pd.DataFrame(arr1)
    df2 = df.apply(lambda x: x.sum())
    df2 = list(df2)
    l.append(df2)
LABEL = pd.DataFrame(np.array(l))
LABEL = LABEL.apply(lambda x: x.sum())
print(list(LABEL))
