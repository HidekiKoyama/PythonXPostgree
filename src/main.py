from ast import With
import pandas as pd

arq = 'Regiao.xls'
arq2 = 'RegiaoCruzada.xls'

df_ex = pd.read_excel(arq,sheet_name='Plan1')
df_ex2 = pd.read_excel(arq2,sheet_name='Plan1')

#print(df_ex[df_ex['Sigla'] == 'CE'])
print(df_ex2)