import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import wilcoxon

df0 = pd.read_csv('Run_16_30models_window0.csv')
df3 = pd.read_csv('Run_16_30models_window3.csv')
df6 = pd.read_csv('Run_16_30models_window6.csv')
df9 = pd.read_csv('Run_16_30models_window9.csv')
df12 = pd.read_csv('Run_16_30models_window12.csv')
df16 = pd.read_csv('Run_16_30models_window16.csv')
df18 = pd.read_csv('Run_16_30models_window18.csv')
df24 = pd.read_csv('Run_16_30models_window24.csv')

dataframes = [df0, df3, df6, df9, df12, df16, df18, df24]

#aps, auc, f1_def, f1_weight, f1_micro

# for df in dataframes:
#     print()
#     print(f"AUPRC mean {df['aps'].mean()} and std {df['aps'].std()}")
#     print(f"AUROC mean {df['auc'].mean()} and std {df['auc'].std()}")
#     print(f"Default f1 {df['f1_def'].mean()}")
#     print(f"Weighted f1 {df['f1_weight'].mean()}")
#     print(f"Micro f1 {df['f1_micro'].mean()}")
#


# compute the difference in performance
auprc_per_diff = [x1 - x2 for (x1, x2) in zip(df0['aps'].values, df3['aps'].values)]
auroc_per_diff = [x1 - x2 for (x1, x2) in zip(df0['auc'].values, df3['auc'].values)]

# perform the Wilcoxon test
(statistic_auprc, pvalue_auprc) = wilcoxon(auprc_per_diff)
(statistic_auroc, pvalue_auroc) = wilcoxon(auroc_per_diff)


print("AUPRC p-value: ", np.round(pvalue_auprc,8))
print("AUROC p-value: ", np.round(pvalue_auroc,20))




















# # 16
# auroc1 = [0.9916120373979337, 0.9926948324069169, 0.9896131265336012, 0.9914511158538916, 0.990988393533636, 0.9902052857479776, 0.9883358846589003, 0.9888029069660663, 0.990993203688485, 0.9887372410642629, 0.9888363594066076, 0.9901041996150127, 0.9928282048822781, 0.9893699950703201, 0.987140561178902, 0.9926300410787224, 0.9897668328453699, 0.9915774917403811, 0.9920888986582, 0.9903979834664774, 0.9885496450251483, 0.988744966464475, 0.9863666364161374, 0.9919890515045144, 0.9883344270362187, 0.9921624357224837, 0.9921616340300089, 0.9920440767607427, 0.9909579292195917, 0.9868038503394658]
# auprc1 = [0.9053915745335493, 0.9123826111696757, 0.8912262827178347, 0.9011582629036861, 0.8905400615232497, 0.9139009614821059, 0.8976707436473874, 0.8790931344628129, 0.8954574277350925, 0.8887769816984439, 0.8786681768562024, 0.8946676629851019, 0.912068634783093, 0.8955713660698938, 0.8823498435559567, 0.9188340827879331, 0.8674469996440292, 0.9077341392854782, 0.9144620467611249, 0.8978802959803206, 0.8875983390459912, 0.8821758552683474, 0.8860538598654991, 0.9005455250485022, 0.8844225780201802, 0.9097348277729848, 0.9027451717119875, 0.9148816459834481, 0.9050876352026923, 0.8790014682584563]
#
# #16-32
# auroc2 = [0.9882651170777115, 0.9921920983440531, 0.9895755198684175, 0.9861431099779229, 0.9923458775369557, 0.9905935235492062, 0.9933737930519791, 0.9903927360248239, 0.9906459250846077, 0.9907633365916059, 0.9912509113785817, 0.9863968820867792, 0.9915315037447784, 0.990755829834796, 0.9886992699934087, 0.9919065500607391, 0.9904064376780305, 0.9929698858069239, 0.9916441050969275, 0.9916000120108109, 0.9909146378259499, 0.9905625490672235, 0.9906646555360655, 0.9920045023049386, 0.992463070400552, 0.9893983458314761, 0.9886181532911809, 0.9923162149153864, 0.9867351963111651, 0.9859242479322893]
# auprc2 = [0.8993832817156036, 0.8892430593121325, 0.8999062522494921, 0.879413090049715, 0.9140400774455849, 0.9089189903175708, 0.9131463127283963, 0.8918203437209125, 0.8805092197734042, 0.8986442777429574, 0.8809110649370023, 0.889987661472462, 0.8998149166602033, 0.89987942491799, 0.8800742429510281, 0.8761243822203094, 0.8909410085362034, 0.8959670660469403, 0.8877570014704981, 0.8933438260582325, 0.8877444194063445, 0.8925904840626026, 0.8931342777946274, 0.89306241063542, 0.9010152052840631, 0.8856435058729409, 0.8979575474954905, 0.9030798267168756, 0.8675142548181118, 0.881584919471794]
#
# sns.displot(auroc1, kde=True, label='Classifier 1', multiple='stack')
# sns.displot(auroc2, kde=True, label='Classifier 1', multiple='stack')
# # plt.hist([auroc1, auroc2], bins=10, label=['Classifier 1', 'Classifier 2'])
# plt.xlabel('AUROC')
# plt.ylabel('Frequency')
# plt.legend()
# plt.show()
#
#
# from scipy.stats import ttest_ind
# t_statistic, p_value = ttest_ind(auroc1, auroc2)
# # If the p-value is less than a predetermined threshold (usually 0.05),
# # you can conclude that there is a significant difference between the AUROCs of the two classifiers.
# print("T-statistic: ", t_statistic)
# print("P-value: ", p_value)