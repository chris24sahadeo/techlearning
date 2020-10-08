import quandl
import pandas as pd
import pprint

pp = pprint.PrettyPrinter(indent=1)

# this is my permanent static api key
api_key = ('brCzbi9nvAcRNn64vNY4')
# df = quandl.get('FMAC/HPI_AK', authtoken = api_key)
# print(df.head())


all_states_abbreviations = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

# pd.read_html() returns a list of dataframes, one dataframe per table in the html
# we can specify an index to isolate a specific dataframe
quandl_codes = ['FMAC/HPI_' + abbreviation for abbreviation in all_states_abbreviations[0][1][1:]]
pp.pprint(quandl_codes)
