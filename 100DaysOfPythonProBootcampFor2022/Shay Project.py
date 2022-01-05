import pandas as pd
import numpy as np

def ReadMyData(path):
    df=pd.read_excel(path)
    arr = np.array(df)
    arr_as_float=np.float64(arr)
    arr_as_list=arr_as_float.tolist()
    return arr_as_list
data = ReadMyData("datamine.xlsx")
print(data)
list=pd.DataFrame(data)
file_name = 'ConvertedData.xlsx'
list.to_excel(file_name)