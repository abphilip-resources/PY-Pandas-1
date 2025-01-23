# 2891
# https://leetcode.com/problems/method-chaining

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animals = animals[animals['weight'] > 100].sort_values(by = 'weight', ascending = False)
    return pd.DataFrame(animals['name'])