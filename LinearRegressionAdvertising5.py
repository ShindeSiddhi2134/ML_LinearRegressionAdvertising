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
    print(border)
    print("step 2: remove unwanted column")
    print(border)

    if "Unnamed: 0" in df.columns:
        df=df.drop(columns=["Unnamed: 0"])

    print(df.head())

    #step 3: check missing values
    print(border)
    print("step 3: check missing values")
    print(border)
    print("total missing values:")
    print(df.isnull().sum())


    #Step 4 : statisticle summary
    print(border)
    print("Step 4 : statisticle summary")
    print(border)
    print(df.describe())

    #step 5: correlation
    print(border)
    print("step 5: correlation")
    print(border)

    print(df.corr())

    #step 6: separate independence and dependent variable
    print(border)
    print("step 6: separate independence and dependent variable")
    print(border)

    X=df[["TV","radio","newspaper"]]
    Y=df["sales"]
    print("i ndepemdent variable:")
    print(X.head())

    print("dependent varible:")
    print(Y.head())

    
def main():
    MarvellousRegression("Advertising.csv")

if __name__=="__main__":
    main()