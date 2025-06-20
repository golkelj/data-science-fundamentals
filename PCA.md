# Principal Component Analysis

### What is PCA? 

PCA is an unsupervised machine learning technique that can be used for dimensionality reduction and feature selection.

A key assumption is that you have a linear dataset; other techniques should be used with non-linear data.

### How does it work?

PCA works by calculating the principal components of the data, which are new axes that maximize the variance in the dataset. The steps are:
1. Standardize the data (mean = 0, variance = 1).
2. Compute the covariance matrix to understand how variables relate to each other.
3. Calculate the eigenvectors and eigenvalues of the covariance matrix.
4. Sort the eigenvectors by their eigenvalues in descending order.
5. Select the top k eigenvectors to form a new feature space (the principal components).
6. Transform the original data onto this new feature space.

### What does it tell you?

PCA tells you which directions (principal components) capture the most variance in your data. By projecting your data onto these components, you can reduce the number of features while retaining most of the important information. This helps with visualization, noise reduction, and can improve the performance of other machine learning algorithms.
