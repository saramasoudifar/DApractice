import pandas as pd

dataset = pd.read_excel('std.xlsx')

dataset['score'] +=1

print(dataset)

dataset.to_csv('std.csv')