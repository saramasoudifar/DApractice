import pandas as pd

data = pd.read_excel('std.xlsx')

data['score'] +=1

print(data)