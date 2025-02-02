from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
from matplotlib.colors import to_hex
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


def clusterize(X, 
               num_of_clusters=3, 
               random_state=42):
    
    model = KMeans(n_clusters=num_of_clusters, 
                   random_state=random_state)
    labels = model.fit(X)
    centroids = model.cluster_centers_
    
    return model, labels, centroids


def plot_elbow(X, max_k=20):
    wcss = []

    for k in range(2, max_k + 1):
        kmeans = KMeans(n_clusters=k, 
                        random_state=42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)
    
    plt.figure(figsize=(8,5))
    plt.plot(range(2,max_k + 1), 
             wcss, 
             marker='o')
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("WCSS (Soma dos quadrados dentro do cluster)")
    plt.title("Elbow Method para Otimização do k")
    plt.show()


def evaluate_cluster(X, labels):
    return silhouette_score(X, labels)


def plot_clusters(X, labels, centroids=None):
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    plt.figure(figsize=(8,6))
    sns.scatterplot(x=X_pca[:,0], 
                    y=X_pca[:,1], 
                    hue=labels, 
                    palette="tab10", 
                    s=80, 
                    edgecolor="k")
    
    if centroids is not None:
        centroids_pca = pca.transform(centroids)
        plt.scatter(x=centroids_pca[:,0], 
                    y=centroids_pca[:,1],
                    c="red",
                    marker="X",
                    s=200,
                    label="Centroids")
        
    plt.title("KMeans: Projeção de clusters 2D")
    plt.legend()
    plt.show()


def pairplot(df, labels):
    df_labeled = df.copy()
    df_labeled["Cluster"] = labels
    sns.pairplot(df_labeled, 
                 hue="Cluster", 
                 palette="tab10")
    plt.show()


def find_best_k(X, start_k=2, max_k=20):
    best_score = -10
    for k in range(start_k, max_k+1):
        model, labels, centroids = clusterize(X, num_of_clusters=k)
        score = evaluate_cluster(X, model.labels_)
        if score > best_score:
            best_k = k
            best_score = score
    print(f"Melhor score:{best_score} com {best_k} clusters.")


def plot_cluster_count(labels):
    cluster_counts = pd.Series(labels).value_counts().sort_index()
    
    colors_rgb = plt.cm.tab10.colors
    colors_hex = [to_hex(color) for color in colors_rgb]

    cluster_counts.plot(kind="bar", color=colors_hex[:len(cluster_counts)], edgecolor="black")
    plt.xticks(rotation=0)
    plt.xlabel("Cluster")
    plt.ylabel("Number of points")
    plt.title("Número de pontos em cada cluster")
    plt.show()