#module
import sys

import pandas as pd

import numpy as np

from sklearn.model_selection import train_test_split 

#datetime to separate columns fxn
def split_dates(date_series):
    df = pd.DataFrame()

    df['date'] = pd.date_range('1/6/2020 01:00:00', periods=6, freq='W')
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    return df

#concat dfs fxn
def combine(df_left, df_right):
    return pd.concat([df_left, df_right])

#df null count fxn
def null_count(df):
   return df.isnull().sum().sum()

#tts fxn   
def my_train_test_split(df, target):
    X = df.drop(columns = [target])
    y = df[target]
    result = X_train, X_test, y_train, y_test = (
        train_test_split(X, y, test_size=.2, random_state=42))
    return result

#Class Module
class Apocrita:
    
    def __init__(self, nest_site, sting, suborder):
        """ Initializing attributes """
        self.nest_site = nest_site
        self.suborder = suborder
        self.sting = sting

    #df null count fxn
    def null_count(df):
        return df.isnull().sum().sum()

    #tts fxn   
    def my_train_test_split(df, target):
        X = df.drop(columns = [target])
        y = df[target]
        result = X_train, X_test, y_train, y_test = (
            train_test_split(X, y, test_size=.2, random_state=42))
        return result  

class Ants(Apocrita): 
    def __init__(self, nest_site, sting):
        super().__init__(self, nest_site, sting)
        
class Wasps(Apocrita): 
    def __init__(self, nest_site, sting):
        super().__init__(self, nest_site, sting)

class Honey_Bees(Apocrita): 
    def __init__(self, nest_site, sting):
        super().__init__(self, nest_site, sting)




        