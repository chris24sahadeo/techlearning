import pandas as pd

df1 = pd.DataFrame({'Year':[2001, 2002, 2003, 2004],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]}
                  )

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'Year':[2001, 2003, 2004,2005],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]}
                  )


# merge is not very useful
# may be useful if maintaining information for a user logging into your website
# merging:
#     username
#     password
#     hashes
# print(pd.merge(df1, df2, on=['HPI', 'Int_rate']))

# for join, an index must be shared
# so need to set the index of df1 and df3
# the code below will not run since the data was changed
# df1.set_index('HPI', inplace=True)
# df3.set_index('HPI', inplace=True)
# joined = df1.join(df3)
# print(joined)      # but this results in duplicated data

# use merged if indexes do not need to be honored
merged = pd.merge(df1, df3, on = 'Year')    # the default will ommit different rows because it is like an inner (intersection) join in sql
merged.set_index('Year', inplace=True)
print(merged)

merged = pd.merge(df1, df3, on = 'Year', how = 'left')    # left join, index takes values from df1
merged.set_index('Year', inplace=True)
print(merged)

merged = pd.merge(df1, df3, on = 'Year', how = 'outer')    # outer (union) join, index takes values from df1
merged.set_index('Year', inplace=True)
print(merged)
