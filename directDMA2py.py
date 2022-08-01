
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class dma:
    def __init__(self, filepath=None):
        if filepath is not None:
            assert isinstance(filepath, str), 'Filepath must be a single string'
            self.filepath = filepath
        else:
            self.filepath = get_files()
        data,cols = open_data(filepath)
        self.columns = data[0]
        self.data = pd.DataFrame(data=data[1:],columns=cols)
        
def col_names(n,let="c"):
    cols = []
    for i in range(n):
        cols.append(let+str(i))
    return cols

def tranpose(data):
    transp = []
    for i in range(len(data[0])):
        col = []
        for j in range(len(data)):
            col.append(data[j][i])
        transp.append(np.array(col).T)
    return transp

def open_data(filepath):
    with open(filepath, 'rb') as f:
        lines = f.readlines()
    lines_results = [15, len(lines)]
    cols = col_names(lines_results[1]-lines_results[0],"c")
    all_data = []
    for j in range(lines_results[0],lines_results[1]):
        data_row = []
        str_line = lines[j].decode()
        str_line = str_line.split("\t")
        for str1 in str_line:
            num = float(str1)
            data_row.append(num)
        all_data.append(data_row)
    all_data = tranpose(all_data)
    return all_data,cols