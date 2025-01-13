# 2880
# https://leetcode.com/problems/select-data

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['student_id']==101][['name', 'age']]