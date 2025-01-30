import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_mall_customers(file_path):
    df = pd.read_csv(file_path)
    df = pd.get_dummies(df, drop_first=True).astype(int)
    df = df.rename(columns={"Annual Income (k$)":"Annual Income", "Spending Score (1-100)":"Spending Score", "Gender_Male":"Gender"})
    
    scaler = MinMaxScaler()
    df = scaler.fit_transform(df)

    return df

def preprocess_wholesome_customers(file_path):
    df = pd.read_csv(file_path)

def scale()