# Multi-Dataset Clustering: A K-Means Experiment

This project explores the concept of clustering in data science, focusing on the application of the K-Means clustering algorithm. Clustering is an unsupervised machine learning technique that groups data points based on their similarities, allowing us to uncover hidden patterns and structures in datasets without predefined labels.

This repository contains end-to-end analyses for two datasets (Iris and Mall Customers), applying K-Means clustering to identify spending patterns and segment groups.

## Table of Contents

1. [Background](#background)
2. [Unsupervised Learning](#unsupervised-learning)
3. [K-Means](#k-means)
4. [Tools I Used](#tools-i-used)
5. [The Process](#the-process)
6. [The Analysis](#the-analysis)
7. [What I Learned](#what-i-learned)
8. [Skills Practiced](#skills-practiced)
9. [Conclusion](#conclusion)
10. [Contact](#contact)

## Background

This project was created to practice and summarize the concepts I have learned about unsupervised learning, specifically focusing on clustering techniques. Unsupervised learning is a powerful tool for discovering hidden patterns and structures in datasets without predefined labels, and this project serves as a hands-on application of those principles.

The project contains a comprehensive analysis of two datasets: one focusing on customer spending patterns and the other on the Iris flower dataset. Through the application of K-Means clustering, I aim to demonstrate how unsupervised learning can segment data into meaningful groups. The results from both datasets will be analyzed and compared, providing insights into the effectiveness of clustering techniques in various contexts.

## Unsupervised Learning

Unsupervised learning is a type of machine learning where the computer learns from data without being told what to look for. Imagine you have a big box of mixed Lego pieces, but no instructions. You don't know exactly what you're supposed to build, but you can start sorting the pieces by color, size, or shape. This is similar to what happens in unsupervised learning.

In supervised learning, the computer is given examples with correct answers (like showing pictures of cats and dogs and labeling them). But in unsupervised learning, there are no labels or correct answers. The computer tries to find patterns, group similar things together, or detect anything unusual all by itself.

Here are two common ways unsupervised learning is used:

- **Clustering:**
This is like organizing your Lego pieces into groups. The computer looks at the data and tries to group similar items together. For example, if you give a computer a bunch of photos of animals, it might group together all the photos of animals with fur, those with feathers, and those with scales, even though it doesn't know the names of the animals.

- **Dimensionality Reduction:**
Sometimes data has too many details, and it’s hard to see the big picture. Dimensionality reduction helps by simplifying the data, keeping the important parts, and removing the unnecessary ones. It's like taking a complex recipe and simplifying it down to just the key steps.

Why is unsupervised learning useful?
It helps in situations where we don’t have labeled data or when we want the computer to discover hidden patterns we might not notice ourselves. It’s often used in things like grouping customers by their shopping habits, detecting fraud, recommending movies or products, and much more.

*In short, unsupervised learning lets computers explore and make sense of data on their own, helping us find patterns and insights without needing to guide them every step of the way!*

## K-Means

K-Means is one of the simplest and most popular methods in unsupervised learning. It’s used to group similar items into clusters. Think of it like organizing your photo gallery: the algorithm automatically groups photos that look similar, like beach photos in one group and city photos in another.

Here’s how K-Means works, step by step:

1. **Pick the Number of Clusters (K):**
First, you decide how many groups (or clusters) you want. This number is called K. For example, if you have a collection of animal photos and you want to separate them into 3 groups—say, cats, dogs, and birds—you set K = 3.

2. **Place Random Points (Centroids):**
The algorithm starts by placing K points randomly in your data. These points are called centroids, and they represent the center of each cluster. At this stage, they’re just guesses—they don’t mean anything yet.

3. **Assign Each Item to the Nearest Centroid:**
Next, the algorithm looks at each data point and checks which centroid is closest. It then assigns each data point to the nearest centroid, forming temporary clusters. Imagine drawing a line from each photo to the nearest “center” point—it’s like sorting your photos into piles based on which centroid they’re closest to.

4. **Move the Centroids:**
Now that the items are grouped, the centroids move. Each centroid shifts to the center of its assigned group. For example, if you have a cluster of dog photos, the centroid moves to the middle of that group.

5. **Repeat Until It’s Done:**
Steps 3 and 4 keep repeating:
This loop continues until the centroids don’t move much anymore. That’s when the algorithm stops.

## Tools I Used

- **Python:** The core programming language for data manipulation, analysis, and building machine learning models.
- **Pandas:** Essential for handling and analyzing structured data with ease and efficiency.
- **NumPy:** Used for numerical operations and managing multi-dimensional arrays, providing a solid foundation for data processing.
- **Matplotlib & Seaborn:** Powerful libraries for creating insightful visualizations, helping to uncover patterns and trends in the data.
- **Scikit-learn (sklearn):** A versatile machine learning library for building, training, and evaluating models.
- **Visual Studio Code:** My go-to code editor for writing, organizing, and debugging Python scripts.
- **Git & GitHub:** Crucial for version control and collaborating, ensuring my work is well-documented and accessible.

## The Process

This section outlines the key steps taken throughout the project, from organizing reusable functions to performing exploratory data analysis and clustering.

### Modularizing Functions for Reusability

At the start of this project, I focused on designing a modular structure for functions that would be reused across various experiments. This approach streamlined my workflow, reduced redundancy, and made the codebase more organized and maintainable.

To achieve this, I created separate modules for specific tasks:

- **data_preprocessing.py:** Contained functions like data_preprocess and data_scale for cleaning and scaling datasets.

- **clustering.py:** Focused on clustering techniques with functions such as clusterize, plot_elbow, evaluate_cluster, plot_clusters, pairplot, find_best_k, and plot_cluster_count.

- **utils.py:** Included utility functions like log_changes, save_dataframe, load_dataframe, plot_cluster_distribution, plot_boxplot_and_histogram, dataframe_info, and plot_correlations.

By defining an __all__ list, I explicitly specified which functions could be imported when using from module import *, ensuring clarity and control over the namespace:

```Python
__all__ = [
    "data_preprocess",
    "data_scale",
    "clusterize",
    "plot_elbow",
    "evaluate_cluster",
    "plot_clusters",
    "pairplot",
    "find_best_k",
    "plot_cluster_count",
    "log_changes",
    "save_dataframe",
    "load_dataframe",
    "plot_cluster_distribution",
    "plot_boxplot_and_histogram",
    "dataframe_info",
    "plot_correlations",
]
```
This modular design allowed me to efficiently call functions across experiments, keeping the main scripts clean and focused on the analysis rather than repetitive code.

### Exploratory Data Analysis

The exploratory analysis was conducted in the notebook [01_exploratory_analysis.ipynb](notebooks\01_exploratory_analysis.ipynb), starting with importing the dataset and using the ``dataframe_info`` function to inspect its structure. This step helped identify duplicates, missing values, and general characteristics of the data.

Next, I applied the ``plot_boxplot_and_histogram`` function to visualize the numeric features, which allowed me to detect potential outlier candidates. If a large number of outliers were apparent in the plots, they were addressed in the preprocessing phase.

The ``data_preprocess`` function was then used to:

- Remove detected outliers if necessary.

- One-hot encode string classifications.

- Fill missing values using a specified method.

- Log all preprocessing actions for traceability.

After completing these steps, I saved the preprocessed dataframe for use in subsequent analyses, ensuring a consistent and clean dataset moving forward.

### Clustering Analysis

The clustering analysis was performed in the [notebook 02_clustering_analysis.ipynb](notebooks\02_clustering_analysis.ipynb). I began by importing the preprocessed dataframe and removing static features like IDs and categorical variables such as gender, which were not relevant for clustering.

I then plotted the correlation matrix of the features using the ``plot_correlations`` function and removed any features with a correlation of 0.8 or higher to avoid redundancy. After cleaning the dataset, I applied the ``data_scale`` function to standardize the features, preparing them for clustering.

To determine the optimal number of clusters, I used the ``plot_elbow`` method to visualize the elbow plot and identified the best silhouette score with the ``find_best_k`` function. Based on these insights, I selected the appropriate number of clusters.

With the number of clusters defined, I created and trained a clustering model using the clusterize function. I then visualized the results using several techniques:

- ``pairplot`` to observe the separation between clusters.

- ``plot_cluster_count`` to display the distribution of data points across clusters.

- ``plot_cluster`` to display 2D dimensionality reduction plot to visually inspect the cluster divisions.

These analyses provided clear insights into the clustering structure of the data, leading to meaningful interpretations and conclusions.

## The Analysis

### Iris Dataset

For the first analysis, I worked with the classic Iris dataset. After preprocessing, the general structure of the dataset consisted of the following features: sepal length, sepal width, petal length, petal width, and species.

#### Exploratory Data Analysis

During the exploratory analysis, no duplicates or missing values were detected. The only necessary preprocessing step was to one-hot encode the species feature. After completing these steps, I saved the cleaned dataframe for further analysis.

#### Preparing for Clustering

The next step involved removing the ID column and separating the species feature, as the goal of this experiment was to compare how the K-Means clustering method performs against the actual species classifications.

I analyzed feature correlations and found that petal width had a high correlation, leading to its removal from the dataset to improve clustering performance. (I will add an image of the correlation plot here.)

#### Clustering with K-Means

To determine the optimal number of clusters, I used the elbow method for verification and measured the silhouette score. Although the best silhouette score was achieved at k=2, we set k=3 to align with the known number of species in the dataset.

After creating and training the K-Means model:

- I generated pair plots to visualize feature distributions across clusters.

- Plotted the distribution of points in each cluster.

- Created a 2D reduced version of the dataset to visualize the clustering.

I repeated these visualizations for the actual species classes, placing the images side by side for comparison. The results showed that while the K-Means algorithm identified clusters that were similar to the actual species, it was not a perfect match. The algorithm incorrectly assigned more points to Class 1 than to Class 2, despite the dataset containing 50 samples for each class. However, the clusters were quite close, and the 2D reduced plot clearly demonstrated a distribution that closely mirrors the real classes.

## What I Learned

Through this project, I deepened my understanding of using Python and its libraries to analyze real-world datasets. Key takeaways include:

- How to manipulate and analyze data efficiently using pandas for cleaning, transforming, and exploring datasets.

- Creating compelling visualizations with matplotlib and seaborn to uncover patterns and communicate insights effectively.

- Building and evaluating machine learning models with scikit-learn, from preprocessing data to interpreting model performance.

- Gaining a solid understanding of unsupervised learning techniques, including how K-Means clustering works to group data based on inherent patterns without labeled outcomes.

- Learning how to create custom Python modules to organize experiment-specific functions, allowing me to streamline my workflow by calling these functions from separate scripts.

- The importance of structuring code and analysis in a clear, organized, and reproducible way for better readability and collaboration.

## Skills I Practiced

This project allowed me to practice and enhance the following skills:

- **Python Programming:** Applying Python for data manipulation, analysis, and automation of workflows.

- **Data Analysis with Pandas:** Cleaning, transforming, and exploring datasets to uncover insights.

- **Data Visualization:** Creating clear and informative visualizations using matplotlib and seaborn to communicate patterns and trends.

- **Machine Learning:** Implementing models with scikit-learn, focusing on unsupervised learning techniques like K-Means clustering.

- **Modular Coding:** Developing custom Python modules to streamline code organization and reusability.

- **Version Control:** Using Git and GitHub for tracking changes, collaboration, and maintaining a clear project history.

- **Problem-Solving:** Applying critical thinking to interpret results and refine analyses for meaningful conclusions.

## Conclusion

## Contact

If you have any questions or feedback, feel free to reach out:\
[GitHub](https://github.com/faduzin) | [LinkedIn](https://www.linkedin.com/in/ericfadul/) | [eric.fadul@gmail.com](mailto\:eric.fadul@gmail.com)