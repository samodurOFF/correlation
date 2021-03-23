from statistics import mean
from ratios import Correlations
from itertools import combinations
import pandas as pd
from scipy.stats import spearmanr, mannwhitneyu

df = pd.read_excel('Стастистика VK.xlsx')
for i in df:
    try:
        value = float(df.at[0, i])
    except Exception:
        df.drop(i, axis=1, inplace=True)

df.drop('ID группы в ВК', axis=1, inplace=True)

comb = combinations(list(df.columns), 2)
final_df = pd.DataFrame({'Критерий': ['Пирсон', 'Стьюдент', 'Спирмен', 'Уилкоксон-Манн-Уитни']})
# print(final_df)
for i in comb:
    x = i[0]
    y = i[1]
    new_column = f'{x}_{y}'
    cor = Correlations(df[x], df[y])
    r_pearson = cor.r_pearson()
    final_df.at[0, new_column] = r_pearson
    t_student = cor.t_student()
    final_df.at[1, new_column] = t_student
    r_spearman = spearmanr(df[x], df[y])[0]
    final_df.at[2, new_column] = r_spearman
    u_mannwhitney = mannwhitneyu(df[x], df[y])[0]
    final_df.at[3, new_column] = u_mannwhitney

print(final_df)
final_df.to_csv('Analyse.csv', index=False)
