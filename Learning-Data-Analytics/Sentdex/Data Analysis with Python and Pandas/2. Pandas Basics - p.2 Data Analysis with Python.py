# pandas df can handle many different formats:
#     CSV
#     lists
#     sql

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')


# Converting Dict to Dataframe
web_stats = {
    'Day': [1, 2, 3, 4, 5, 6],
    'Visitors': [42, 45, 62, 35, 6, 32],
    'Bounce_Rate': [4, 5, 45, 33, 64, 65]
}

df = pd.DataFrame(web_stats)
df.set_index('Day', inplace=True)   # HUGE: an index is NOT a colmn

print(df)
# print(df.head())
# print(df.tail())
# print(df.tail(2))

print(df['Visitors'])   # reference like dict
print(df[['Visitors', 'Bounce_Rate']])      # reference 2 at a time
print(df.Visitors.tolist())     # make a colmn in df a list

# to convert multiple colmns to list we must use numpy
print(np.array(df[['Visitors', 'Bounce_Rate']]))

# can also convert numpy arrays to dicts:
df_2 = pd.DataFrame(np.array(df[['Visitors', 'Bounce_Rate']]))
print(df_2)

# can also use CSV
