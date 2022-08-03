# Classroom Assignment


### Author: Rebecca Kleinbart (Hunter College) 
### Course: A.I. (CSCI 761 / CSC 740), Dr. Anita Raja, Spring 2022

### Classroom Assignment
How can teachers be assigned to classrooms in "the best" way or in a "good" way that meets hard and soft constraints prioritizing some constraints over others? 


### Constraints
Teacher preferences (acquired by interviewing actual teachers), administrative preferences, and space limitations 

### Weights

![Setup screenshot](images/weight_zero_bipartite_winter.png)
![Setup screenshot](images/weight_zero_bipartite.png)


### Algorithms 
### Brute Force 
A naive approach might be to systematically try every combination and compare the weighted values, ultimately choosing the assignment(s) that have the least weight. This approach would take O(n!) in the size of the input which is clearly untenable for even medium-sized inputs, however logical and easy-to-understand. 

#### Kuhn-Munkres Algorithm (also known as the Munkres or Hungarian Algorithm) 
The **Kuhn-Munkres Algorithm** is a significant improvement from the naive approach. Its running time to O(n^4) or O(n^3), depending on the variation chosen. It is a linear combinatorial optimization algorithm, _and used without modification is not an example of artificial intelligence. (insert and apply definition from R & N)_

History of this algorithm from https://en.wikipedia.org/wiki/Hungarian_algorithm: 
> The Hungarian method is a combinatorial optimization algorithm that solves the assignment problem in polynomial time and which anticipated later primal–dual methods. It was developed and published in 1955 by Harold Kuhn, who gave the name "Hungarian method" because the algorithm was largely based on the earlier works of two Hungarian mathematicians: Dénes Kőnig and Jenő Egerváry.

> James Munkres reviewed the algorithm in 1957 and observed that it is (strongly) polynomial. Since then the algorithm has been known also as the Kuhn–Munkres algorithm or Munkres assignment algorithm. The time complexity of the original algorithm was O(n^4), however Edmonds and Karp, and independently Tomizawa noticed that it can be modified to achieve an O(n^3) running time. One of the most popular O(n^3) variants is the Jonker–Volgenant algorithm. Ford and Fulkerson extended the method to general maximum flow problems in form of the Ford–Fulkerson algorithm. In 2006, it was discovered that Carl Gustav Jacobi had solved the assignment problem in the 19th century, and the solution had been published posthumously in 1890 in Latin.

### Software requirements:
Python 3

### How to run:

