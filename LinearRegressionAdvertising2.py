import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

def MarvellousRegression(datapath):
    border="-"*50

    #step1:lead the data
    print(border)
    print("step 1: load the data")
    print(border)

    df=pd.read_csv (datapath)

    print(df.head())

    #step 2: remove unwanted column

    print("step 2: remove unwanted column")

    if "Unnamed: 0" in df.columns:
        df=df.drop(columns=["Unnamed: 0"])

    print(df.head())

    #step 3: check missing values

    print("step 3: check missing values")

    print("total missing values:")
    print(df.isnull().sum())
    
def main():
    MarvellousRegression("Advertising.csv")

if __name__=="__main__":
    main()