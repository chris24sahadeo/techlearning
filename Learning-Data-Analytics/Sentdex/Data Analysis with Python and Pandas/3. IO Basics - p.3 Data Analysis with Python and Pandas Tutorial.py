import pandas as pd
import matplotlib.pyplot as plt
import json

# another way of specifying index for dataframe
# HUGE: an index is NOT a colmn
df = pd.read_csv('IFT-NSA.csv', index_col = 2)

# renaming colmns
# df.columns = ['Hi', 'Bye', ...]     # needs the exact number of columns

print(df.head())

# df.to_csv('test.csv')
# df.to_html('webpage.html')
# df.to_json('3.data.json')   # HUGE!!! Index must be unique for json to work (maybe why for project we are using json not csv)
