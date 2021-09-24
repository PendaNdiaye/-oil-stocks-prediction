import pandas as pd
df = pd.read_csv(r'C:\Users\HP 1030 G2\Desktop\Cours DIT\El Hadj\oil-stocks-prediction\data\articles\output.csv',sep='|', header=None, encoding='latin-1')
df.groupby(1)[0].apply(list)