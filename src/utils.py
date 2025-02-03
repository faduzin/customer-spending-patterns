import os
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Função para logar as mudanças
def log_changes(log_messages, log_file="logs/preprocessing_log.txt", dataset_name="Unknown"):
    
    os.makedirs(os.path.dirname(log_file), exist_ok=True) # Cria o diretório do arquivo de log
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Gera o timestamp
    with open(log_file, "a") as f: # Abre o arquivo de log
        f.write(f"\n[{timestamp}]\n") # Escreve o timestamp
        f.write(f"[Dataset:{dataset_name}]\n") # Escreve o nome do dataset
        for message in log_messages: # Itera sobre as mensagens de log
            f.write(f"[{message}]\n") # Escreve a mensagem de log
    print("\n".join(log_messages)) # Exibe as mensagens de log


# Função para salvar o dataframe
def save_dataframe(df, file_path):
    try: # Tenta salvar o arquivo
        df.to_csv(file_path, index=False) # Salva o dataframe
        print(f"Arquivo salvo em: {file_path}.") # Exibe mensagem de sucesso
    except: # Se houver erro
        raise("Falha ao salvar arquivo.") # Exibe mensagem de erro
    

# Função para carregar o dataframe
def load_dataframe(file_path, sep=","):
    try: # Tenta carregar o arquivo
        df = pd.read_csv(file_path, sep=sep) # Carrega o dataframe
        print("Dataframe carregado com sucesso.") # Exibe mensagem de sucesso
        return df # Retorna o dataframe
    except: # Se houver erro
        raise("Falha ao carregar arquivo.") # Exibe mensagem de erro
    

# Função para plotar a distribuição de clusters
def plot_cluster_distribution(labels):
    plt.figure(figsize=(8,6)) # Inicializa a figura

    plt.hist(labels,
             bins=len(set(labels)),
             edgecolor='black',
             alpha=0.7) # Plota o histograma
    
    plt.xlabel("Cluster") # Adiciona o label do eixo x
    plt.ylabel("Número de pontos") # Adiciona o label do eixo y
    plt.title("Distribuição de Clusters") # Adiciona o título
    plt.xticks(range(len(set(labels)))) # Adiciona os ticks do eixo x
    plt.show() # Exibe o gráfico


# Função para plotar boxplot e histograma
def plot_boxplot_and_histogram(df, column_name):
    
    fig, axes = plt.subplots(1, 
                             2,  
                             figsize=(12,4)) # Inicializa a figura

    sns.boxplot(x=df[column_name], ax=axes[0]) # Plota o boxplot
    axes[0].set_title(f"Box plot de {column_name}") # Adiciona o título

    axes[1].hist(df[column_name],
                   bins=30,
                   edgecolor="Black",
                   alpha=0.7) # Plota o histograma
    axes[1].set_title(f"Histograma de {column_name}") # Adiciona o título
    axes[1].set_xlabel(column_name) # Adiciona o label do eixo x
    axes[1].set_ylabel("Frequência") # Adiciona o label do eixo y

    plt.tight_layout() # Ajusta o layout
    plt.show() # Exibe o gráfico


# Função para exibir informações do dataframe
def dataframe_info(df):
    print(df.head(5)) # Exibe as primeiras 5 linhas
    print('-'*50)
    print(df.info()) # Exibe informações do dataframe
    print('-'*50)
    print(df.describe()) # Exibe estatísticas descritivas
    print('-'*50)
    print('Amount of duplicates:',df.duplicated().sum()) # Exibe a quantidade de linhas duplicadas


# Função para plotar correlações
def plot_correlations(df):
    plt.figure(figsize=(8,6)) # Inicializa a figura
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f") # Plota o heatmap
    plt.show() # Exibe o gráfico