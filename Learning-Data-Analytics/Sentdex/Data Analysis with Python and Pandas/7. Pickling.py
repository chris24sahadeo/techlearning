# tb to python tut vid 4 code...

import quandl
import pandas as pd
import pprint
import pickle


def get_all_states_dataframe():
    pp = pprint.PrettyPrinter(indent=1)

    # this is my permanent static api key
    api_key = ('brCzbi9nvAcRNn64vNY4')
    # df = quandl.get('FMAC/HPI_AK', authtoken = api_key)
    # print(df.head())


    all_states_abbreviations = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

    # pd.read_html() returns a list of dataframes, one dataframe per table in the html
    # we can specify an index to isolate a specific dataframe
    quandl_codes = ['FMAC/HPI_' + abbreviation for abbreviation in all_states_abbreviations[0][1][1:]]

    # make empty dataframe for merging
    main_df = pd.DataFrame()
    remaining = len(quandl_codes)-1
    for code in quandl_codes:
        print('Getting {}...remaining: {}'.format(code, remaining))
        remaining-=1
        df = quandl.get(code, authtoken=api_key)
        df.columns = [code]

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

        # pickling is the fastest way to serialise objects
        # it works with ANYTHING
        # and for Machine Learning stuff you can't even export to something like a CSV
        # so pickling is awesome
        pickle_out = open('all_states_dataframe', 'wb')
        pickle.dump(main_df, pickle_out)
        pickle_out.close()


def load_all_states_dataframe():
    with open('all_states_dataframe', 'rb') as pickle_in:
        df = pickle.load(pickle_in)
    return(df)

# get_all_states_dataframe()
df = load_all_states_dataframe()


# but pandas has its own faster pickling method
df.to_pickle('new_pickle.pickle')
new_df = pd.read_pickle('new_pickle.pickle')
print(new_df)
