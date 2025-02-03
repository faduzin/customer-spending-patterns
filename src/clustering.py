from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
from matplotlib.colors import to_hex
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Função para clusterizar os dados
def clusterize(X, 
               num_of_clusters=3, 
               random_state=42):
    
    model = KMeans(n_clusters=num_of_clusters, 
                   random_state=random_state) # Inicializa o modelo KMeans
    labels = model.fit(X) # Treina o modelo
    centroids = model.cluster_centers_ # Obtem os centróides
    
    return model, labels, centroids # Retorna o modelo, os labels e os centróides


# Função para plotar o método Elbow
def plot_elbow(X, max_k=20):
    wcss = [] # Lista para armazenar o WCSS

    for k in range(2, max_k + 1): # Loop para testar diferentes valores de k
        kmeans = KMeans(n_clusters=k, 
                        random_state=42) # Inicializa o modelo KMeans
        kmeans.fit(X) # Treina o modelo
        wcss.append(kmeans.inertia_) # Adiciona o WCSS à lista
    
    plt.figure(figsize=(8,5)) # Inicializa a figura
    plt.plot(range(2,max_k + 1), 
             wcss, 
             marker='o') # Plota o gráfico
    plt.xlabel("Number of clusters (k)") # Adiciona o label do eixo x
    plt.ylabel("WCSS (Soma dos quadrados dentro do cluster)") # Adiciona o label do eixo y
    plt.title("Elbow Method para Otimização do k") # Adiciona o título
    plt.show() # Exibe o gráfico


# Função para avaliar o cluster
def evaluate_cluster(X, labels): 
    return silhouette_score(X, labels) # Retorna o score de silhueta


# Função para plotar os clusters
def plot_clusters(X, labels, centroids=None):
    pca = PCA(n_components=2) # Inicializa o PCA
    X_pca = pca.fit_transform(X) # Aplica o PCA

    plt.figure(figsize=(8,6)) # Inicializa a figura
    sns.scatterplot(x=X_pca[:,0], 
                    y=X_pca[:,1], 
                    hue=labels, 
                    palette="tab10", 
                    s=80, 
                    edgecolor="k") # Plota o gráfico de dispersão
    
    if centroids is not None: # Se houver centróides
        centroids_pca = pca.transform(centroids) # Aplica o PCA aos centróides
        plt.scatter(x=centroids_pca[:,0], 
                    y=centroids_pca[:,1],
                    c="red",
                    marker="X",
                    s=200,
                    label="Centroids") # Plota os centróides
        
    plt.title("KMeans: Projeção de clusters 2D") # Adiciona o título
    plt.legend() # Adiciona a legenda
    plt.show() # Exibe o gráfico


# Função para plotar o pairplot
def pairplot(df, labels):
    df_labeled = df.copy() # Copia o dataframe
    df_labeled["Cluster"] = labels # Adiciona a coluna de clusters
    sns.pairplot(df_labeled, 
                 hue="Cluster", 
                 palette="tab10") # Plota o pairplot
    plt.show() # Exibe o gráfico


# Função para encontrar o melhor k
def find_best_k(X, start_k=2, max_k=20):
    best_score = -10 # Inicializa o melhor score
    for k in range(start_k, max_k+1): # Loop para testar diferentes valores de k
        model, labels, centroids = clusterize(X, num_of_clusters=k) # Clusteriza os dados
        score = evaluate_cluster(X, model.labels_) # Avalia o cluster
        if score > best_score: # Se o score for melhor que o melhor score
            best_k = k # Atualiza o melhor k
            best_score = score # Atualiza o melhor score
    print(f"Melhor score:{best_score} com {best_k} clusters.") # Exibe o melhor score e o melhor k


# Função para plotar o número de pontos em cada cluster
def plot_cluster_count(labels): 
    cluster_counts = pd.Series(labels).value_counts().sort_index() # Conta o número de pontos em cada cluster
    
    colors_rgb = plt.cm.tab10.colors # Cores RGB
    colors_hex = [to_hex(color) for color in colors_rgb] # Cores HEX

    ax = cluster_counts.plot(kind="bar",
                             color=colors_hex[:len(cluster_counts)], 
                             edgecolor="black") # Plota o gráfico de barras
    
    for idx, value in enumerate(cluster_counts): # Adiciona o número de pontos em cada barra
        ax.text(idx, 
                value + 0.5, 
                str(value), 
                ha='center', 
                va='bottom', 
                fontsize=10, 
                fontweight='bold') # Adiciona o texto

    plt.xticks(rotation=0) # Rotaciona os labels do eixo x
    plt.xlabel("Cluster") # Adiciona o label do eixo x
    plt.ylabel("Number of points") # Adiciona o label do eixo y
    plt.title("Número de pontos em cada cluster") # Adiciona o título
    plt.show() # Exibe o gráfico