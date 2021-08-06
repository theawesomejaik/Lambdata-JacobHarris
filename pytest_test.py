import pytest 
from helper_functions import *

def inc(x):
    """Fxn that increments a number by 1"""
    return x + 1

def test_null_count():
    """Test for nulls"""
    assert inc(1) == 2
    assert inc(4) == 5
    
s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])
test_comb = Apocrita(s1, s2)    
def test_combine():
    """test for concat"""
    assert test_comb.combine(s1, s2).equals(pd.concat([s1, s2]))