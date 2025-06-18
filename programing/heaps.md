# Max Heaps and Min Heaps

## Max Heaps

A **Max Heap** is a complete binary tree that satisfies the **max-heap property**: for every node *i* other than the root, the value of node *i* is less than or equal to the value of its parent. In other words, the largest element in the heap is always at the root.

**Properties of a Max Heap:**

* It's a **complete binary tree**: All levels are completely filled except possibly the last level, which is filled from left to right.
* **Max-Heap Property**: The value of each parent node is greater than or equal to the value of its children nodes.
* The root node always contains the **maximum element** in the heap.

**Common Uses of Max Heaps:**

* **Heapsort Algorithm**: Max heaps are used in the Heapsort algorithm for sorting elements.
* **Priority Queues**: They can be used to implement priority queues where the element with the highest priority is always retrieved first.
* Maintaining the maximum element in a collection of data efficiently.

## Min Heaps

A **Min Heap** is also a complete binary tree that satisfies the **min-heap property**: for every node *i* other than the root, the value of node *i* is greater than or equal to the value of its parent. Consequently, the smallest element in the heap is always at the root.

**Properties of a Min Heap:**

* It's a **complete binary tree**: Similar to Max Heap, all levels are completely filled except possibly the last level, which is filled from left to right.
* **Min-Heap Property**: The value of each parent node is less than or equal to the value of its children nodes.
* The root node always contains the **minimum element** in the heap.

**Common Uses of Min Heaps:**

* **Priority Queues**: Min heaps can also be used to implement priority queues, where the element with the lowest priority is retrieved first.
* **Replacement Selection Algorithm**: Used in external sorting.
* Finding the median of a stream of numbers efficiently (by using a combination of a min-heap and a max-heap).
* Maintaining the minimum element in a collection of data.

## Similarities Between Max Heaps and Min Heaps

* Both are based on the **complete binary tree** data structure.
* Both maintain a specific **heap property** to order their elements.
* Both are often implemented using **arrays**, leveraging the properties of a complete binary tree to easily find parent and child nodes based on the index.

## Heap Storage

## Parent and child indices

## Percolation algorithm
