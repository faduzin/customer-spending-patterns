import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
from src.utils import log_changes

# Retorna o dataframe pré-processado
def data_preprocess(df, 
                    fill_method="mean", 
                    label_encode=False, 
                    remove_outliers=True, 
                    log_track=True,
                    dataset_name="Unknown"):
    

    log = [] # Lista de mensagens de log

    num_duplicates = df.duplicated().sum() # Verifica se há linhas duplicadas
    if num_duplicates > 0:
        df = df.drop_duplicates() # Remove linhas duplicadas
        log.append(f"{num_duplicates} linhas com valores duplicados removidas.")

    num_missing_values = df.isnull().sum().sum() # Verifica se há valores vazios
    if num_missing_values > 0:
        log.append(f"Encontrados {num_missing_values} valores vazios.")
        match fill_method: # Preenche valores vazios
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

    
    if remove_outliers: # Remove outliers
        num_rows_before = df.shape[0] # Número de linhas antes de remover outliers
        numeric_cols = df.select_dtypes(include=[np.number]).columns # Seleciona colunas numéricas
        for column in numeric_cols: # Itera sobre as colunas numéricas
            Q1 = df[column].quantile(0.25) # Calcula o primeiro quartil
            Q3 = df[column].quantile(0.75) # Calcula o terceiro quartil
            IQR = Q3 - Q1 # Calcula o intervalo interquartil
            lower_bound = Q1 - 1.5 * IQR # Calcula o limite inferior
            upper_bound = Q3 + 1.5 * IQR # Calcula o limite superior
            df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)] # Remove outliers
        
        num_rows_after = df.shape[0] # Número de linhas após remover outliers
        num_rows_removed = num_rows_before - num_rows_after # Número de linhas removidas
        if num_rows_removed > 0: # Se houver linhas removidas
            log.append(f"Foram removidas {num_rows_removed} linhas.") # Adiciona mensagem de log
        else:
            log.append("Nenhum outlier detectado.") # Se não houver outliers, adiciona mensagem de log

    if label_encode: # Remapeia colunas categóricas
        le = LabelEncoder() # Inicializa o Label Encoder
        for col in df.select_dtypes(include='object').columns: # Itera sobre as colunas categóricas
            df[col] = le.fit_transform(df[col]) # Remapeia os valores
        log.append("Colunas remapeadas usando Label Encode.") # Adiciona mensagem de log

    if log_track: # Se log_track for verdadeiro
        log_changes(log, dataset_name=dataset_name) # Salva as mensagens de log
    
    print("Pré-processamento bem sucedido.") # Mensagem de sucesso

    return df

# Retorna o dataframe dimensionado
def data_scale(df, 
               scaler_method="MinMax", 
               print_log=True):
    
    match scaler_method: # Dimensiona os valores
        case "MinMax": 
            scaler = MinMaxScaler() # Inicializa o MinMaxScaler
            X = scaler.fit_transform(df) # Dimensiona os valores
            if print_log: print("Valores dimensionados utilizando o método MinMax.")
            return X
        case "Standard":
            scaler = StandardScaler() # Inicializa o StandardScaler
            X = scaler.fit_transform(df) # Dimensiona os valores
            if print_log: print("Valores dimensionados utilizando o método Standard.")
            return X
        case _: 
            print("Valores não dimensionados. Método inválido.") # Mensagem de erro
            return df