'''
import files from workdir into all data df
'''
import os
import glob
import datetime as dt
import pandas as pd

csvdir = os.getcwd() + r'/csv/'

#read all files into one data frame
def read_df():
    '''
    reads data from workdir and creates initial data frame
    '''
    df = pd.DataFrame()
    all_files = glob.glob(csvdir + "/*.csv", )
    df_raw = pd.concat((pd.read_csv(filename, 
                                    decimal=',', 
                                    parse_dates=[' timestamp'],
                                    converters={'time': lambda t: dt.datetime.strptime(t, '%Y-%m-%d %H:%M:%S.%f').time()}) 
                                    for filename in all_files)
                       )
    df_raw.reset_index(drop=True, inplace=True)
    df_raw.columns = ['datapoint', 
                  'time', 
                  'hr', 
                  'avnn', 
                  'sdnn', 
                  'rmssd', 
                  'pnn50', 
                  'lf', 
                  'hf', 
                  'lfhf', 
                  'alpha1', 
                  'artifacts', 
                  'measurement']

    # prepare dataframe with all data
    # drop nan 
    df = df_raw.dropna()

    # set dtype for columns
    data_types_dict = { 'datapoint': float, 
                        'hr': float, 
                    'avnn': float, 
                    'sdnn': float, 
                    'rmssd': float, 
                    'pnn50': float, 
                    'lf': float, 
                    'hf': float, 
                    'lfhf': float, 
                    'alpha1': float, 
                    'artifacts': float, 
                    'measurement': str}

    df = df.astype(data_types_dict)
    return(df)