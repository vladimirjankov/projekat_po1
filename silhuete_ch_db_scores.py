import numpy as np
import pandas as pd
import os
from calcSiCHAffy import calcSiCHAffy
from matplotlib import pyplot as plt
from ari_scores_normed import ari_scores_normed
import xlsxwriter



path_data = '/home/vladimir/Desktop/po_projekat/Affy/data/'
path_label = '/home/vladimir/Desktop/po_projekat/Affy/labels/'
file_header = (["   ", "Silhouette_cosine","Silhouette_braycurtis","Silhouette_canberra", "Silhouette_pearson", "Silhouette_hellinger","Silhouette_wasserstein",
    "Silhouette_energy","Silhouette_kulczynski","Calinski_harabaz","Davies_Bouldin"])

data_file_names =  sorted(os.listdir(path_data))
label_file_names =  sorted(os.listdir(path_label))

scores = []
data_book = xlsxwriter.Workbook("Data_results_sil_ch_db.xlsx")
worksheet = data_book.add_worksheet()


for i in range(0,len(data_file_names)):
    path_data_tmp = path_data + data_file_names[i]
    data = pd.read_csv(path_data_tmp, delimiter=' ')
    label = pd.read_csv(path_label+ label_file_names[i], delimiter=' ')
    label = np.array(label)
    scores.append(calcSiCHAffy(data,np.ravel(label),data_file_names[i]))
print('\n')
print(scores)

row =1
col =0

for item in file_header :
    worksheet.write(0,col,item)
    col = col +1

col = 0

for file_scores in scores:
    for item in file_scores:
        worksheet.write(row,col,item)
        col = col +1
    row = row +1
    col =0

data_book.close()



