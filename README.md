# Lambdata-JacobHarris

Apocrita classification

To show the differences of Apocrita suborders

Classifies and differentiates insects of a specific order

Utilizing pandas, numpy, and sklearn (required installs) this provides functions that count nulls and concats columns for these Dataframes and respective tests

Example function to count nulls:
```def null_count(df):
        return df.isnull().sum().sum()```

Example test for null count function:
```def inc(x):
    """Fxn that increments a number by 1"""
    return x + 1```

```def test_null_count():
    """Test for nulls"""
    assert inc(1) == 2
    assert inc(4) == 5```

Jacob Harris
MIT License