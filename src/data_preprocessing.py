import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from src.utils import log_changes

# Objetivo da função é preprocessar um dataset e deixa-lo pronto para o treinamento do modelo
def data_preprocess(df, 
                    fill_method="mean", 
                    one_hot_encode=False, 
                    remove_outliers=True, 
                    log_track=True,
                    dataset_name="Unknown"):
    

    log = []

    num_duplicates = df.duplicated().sum()
    if num_duplicates > 0:
        df = df.drop_duplicates()
        log.append(f"{num_duplicates} linhas com valores duplicados removidas.")

    num_missing_values = df.isnull().sum().sum()
    if num_missing_values > 0:
        log.append(f"Encontrados {num_missing_values} valores vazios.")
        match fill_method:
            case "mean":
                df = df.fillna(df.mean(), inplace=True)
                log.append("Valores completados utilizando o valor médio.")
            case "median":
                df = df.fillna(df.median(), inplace=True)
                log.append("Valores completados utilizando o valor mediano.")
            case "mode":
                df = df.fillna(df.mode().iloc[0], inplace=True)
                log.append("Valores completados utilizando o valor da coluna.")
            case _:
                log.append("Valores não completados. Método invalido.")

    
    if remove_outliers:
        num_rows_before = df.shape[0]
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for column in numeric_cols:
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
        
        num_rows_after = df.shape[0]
        num_rows_removed = num_rows_before - num_rows_after
        if num_rows_removed > 0:
            log.append(f"Foram removidas {num_rows_removed} linhas.")
        else:
            log.append("Nenhum outlier detectado.")

    if one_hot_encode:
        df = pd.get_dummies(df, drop_first=True).astype(int)
        log.append("Colunas com valores remapeados em One_Hot_Encoding.")

    if log_track:
        log_changes(log, dataset_name=dataset_name)
    
    print("Pré-processamento bem sucedido.")

    return df

# Retorna o dataframe dimensionado
def data_scale(df, 
               scaler_method="MinMax", 
               print_log=True):
    
    match scaler_method:
        case "MinMax":
            scaler = MinMaxScaler()
            X = scaler.fit_transform(df)
            if print_log: print("Valores dimensionados utilizando o método MinMax.")
            return X
        case "Standard":
            scaler = StandardScaler()
            X = scaler.fit_transform(df)
            if print_log: print("Valores dimensionados utilizando o método Standard.")
            return X
        case _:
            print("Valores não dimensionados. Método inválido.")
            return df