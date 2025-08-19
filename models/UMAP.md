# Uniform Manifold Approximation and Projection

This is a dimensionality reduction technique that is used for non-linear data.

### How does it work?

UMAP works by constructing a high-dimensional graph representation of the data, then optimizing a low-dimensional graph to be as structurally similar as possible. The main steps are:
1. Construct a weighted graph of the data in high-dimensional space, preserving local relationships.
2. Optimize the layout of this graph in a lower-dimensional space (usually 2D or 3D) so that the structure is maintained as much as possible.
3. The result is a low-dimensional embedding that preserves both local and some global structure of the data.

### What does it tell you?

UMAP provides a visualization or lower-dimensional representation of complex, non-linear data. It is useful for exploring data structure, clustering, and visualizing patterns that may not be visible in higher dimensions. UMAP often preserves more of the global data structure compared to other techniques like t-SNE, and it is computationally efficient.

