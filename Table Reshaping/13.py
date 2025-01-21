# 2889
# https://leetcode.com/problems/reshape-data-pivot

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot_table(index = 'month', columns = 'city', values = 'temperature')