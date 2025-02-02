import os
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def log_changes(log_messages, log_file="logs/preprocessing_log.txt", dataset_name="Unknown"):
    
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"\n[{timestamp}]\n")
        f.write(f"[Dataset:{dataset_name}]\n")
        for message in log_messages:
            f.write(f"[{message}]\n")
    print("\n".join(log_messages))


def save_dataframe(df, file_path):
    try:
        df.to_csv(file_path, index=False)
        print(f"Arquivo salvo em: {file_path}.")
    except:
        raise("Falha ao salvar arquivo.")
    

def load_dataframe(file_path, sep=","):
    try:
        df = pd.read_csv(file_path, sep=sep)
        print("Dataframe carregado com sucesso.")
        return df
    except:
        raise("Falha ao carregar arquivo.")
    

def plot_cluster_distribution(labels):
    plt.figure(figsize=(8,6))

    plt.hist(labels,
             bins=len(set(labels)),
             edgecolor='black',
             alpha=0.7)
    
    plt.xlabel("Cluster")
    plt.ylabel("Número de pontos")
    plt.title("Distribuição de Clusters")
    plt.xticks(range(len(set(labels))))
    plt.show()


def plot_boxplot_and_histogram(df, column_name):
    
    fig, axes = plt.subplots(1, 
                             2, 
                             figsize=(12,4))

    sns.boxplot(x=df[column_name], ax=axes[0])
    axes[0].set_title(f"Box plot de {column_name}")

    axes[1].hist(df[column_name],
                   bins=30,
                   edgecolor="Black",
                   alpha=0.7)
    axes[1].set_title(f"Histograma de {column_name}")
    axes[1].set_xlabel(column_name)
    axes[1].set_ylabel("Frequência")

    plt.tight_layout()
    plt.show()


def dataframe_info(df):
    print(df.head(5))
    print('-'*50)
    print(df.info())
    print('-'*50)
    print(df.describe())
    print('-'*50)
    print('Amount of duplicates:',df.duplicated().sum())


def plot_correlations(df):
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.show()