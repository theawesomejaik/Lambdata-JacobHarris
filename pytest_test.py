import pytest 
import numpy as np
import pandas as pd
from helper_functions import *

def test_null_count():
    data - { 'set_of_numbers': [1,2,3,4,5,np.nan,6,7,np.nan]}
    df = pd.DataFrame(data,columns=['set_of_numbers'])
    df = Apocrita(data)
    assert df.null_count() == 2


    
s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])
test_comb = Apocrita(s1, s2)    
def test_combine():
    """test for concat"""
    assert test_comb.combine(s1, s2).equals(pd.concat([s1, s2]))