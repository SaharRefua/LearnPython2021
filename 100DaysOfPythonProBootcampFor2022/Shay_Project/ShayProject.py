# import pandas as pd
# import numpy as np
#
# def ReadMyData(path):
#     df=pd.read_excel(path)
#     arr = np.array(df)
#     arr_as_float=np.float64(arr)
#     arr_as_list=arr_as_float.tolist()
#     return arr_as_list
# data = ReadMyData("datamine.xlsx")
# print(data)
# list=pd.DataFrame(data)
# file_name = 'ConvertedData.xlsx'
# list.to_excel(file_name)

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def ReadData(excel_file, columns):
    columns_list=[]
    for item in columns:
        columns_list.append(item)
    df = pd.read_excel(excel_file)
    data = df[columns_list]
    return data.to_numpy()
data =ReadData("C:\\Users\\sahar.refua\\Desktop\\Shay Demo\\data_1.xlsx", ('Z','X', 'Y'))

#print(data)

def PearsonCorrelation(X, Y):
    XMean = np.mean(X)
    YMean = np.mean(Y)

    nominator = 0
    denominator = 0
    denominatorX = 0
    denominatorY = 0

    for i in range(len(X)):
        diffX = X[i] - XMean        # calculate xi - x^
        diffY = Y[i] - YMean        # calculate yi - y^

        nominator += diffX * diffY

        denominatorX += np.power(diffX, 2)      # calculate sum of the power of (xi - x^)
        denominatorY += np.power(diffY, 2)      # calculate sum of the power of (yi - y^)

    denominator += np.sqrt(denominatorX * denominatorY)

    R = nominator/denominator       # calculate the pearson correlation
    return R



def PlotMyData(excel_file , columns, names):
    _, x = plt.subplots(len(names), 1)
    for i, name in enumerate(names):  # XY, YZ, XZ
        data = (name[0], name[1])
        graph = ReadData(excel_file , data)

        a = graph[: , 0]
        #print(a)
        b = graph[: , 1]
        #print(b)

        R = PearsonCorrelation(a, b)
        print(R)
        x[i].plot(a)
        x[i].plot(b)
        x[i].plot(b)
        #plt.plot(b)

        x[i].set_title(name+": R =" +str(R))

    plt.show()

PlotMyData('data_1.xlsx' , ['01','12','02'],['XY','YZ','XZ'] )