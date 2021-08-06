# Lambdata-JacobHarris

Apocrita classification

To show the differences of Apocrita suborders

Classifies and differentiates insects of a specific order

Utilizing pandas, numpy, and sklearn (required installs) this provides functions that count nulls and concats for Dataframes and respective tests

Example function to combine dataframes:
```def combine(df_left, df_right):
    return pd.concat([df_left, df_right])```

Example test for concat function
```s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])
test_comb = Apocrita(s1, s2)    
def test_combine():
    """test for concat"""
    assert test_comb.combine(s1, s2).equals(pd.concat([s1, s2]))```

Jacob Harris
MIT License