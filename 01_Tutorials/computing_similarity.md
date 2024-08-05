<blockquote>

### Draft Notes (for use while creating)
Comparison of three Beatles songs:
- Eleanor Rigby
- When I'm Sixty Four
- Back in the USSR

| Song	                | Energy    | Valence	| Danceability  |
|-----------------------|-----------|-----------|---------------|
| Eleanor Rigby	        | 0.280	    | 0.8130	| 0.581         |
| When I'm Sixty Four   | 0.241	    | 0.6610	| 0.704         |
| Back in the USSR	    | 0.969	    | 0.4940	| 0.480         |
<br><br>
</blockquote>

# Computing Similarity

As we work with data, making **comparisons** is a common occurence. For instance, in our Beatles data, we may want to compare two songs. We can make comparisons of varying complexity. We can simply compare two songs based on one attribute, like "valence". But it is also possible to compute similarity based on several attributes at once. This tutorial will explain two key methods for computing similarity, **cosine similarity** and **Euclidean distance**, and provide code examples for computing each.

## Cosine Similarity

Let's consider three songs from our Beatles spotify dataset: Eleanor Rigby, When I'm Sixty Four, and Back in the USSR. For the purposes of this tutorial, these may be abbreviated as ERY, WSF, and BUR, respectively.

Imagine we want to compare these three songs. The simplest way to compare the songs is based on a single attribute, say, "energy".

| Song	                | Energy    |
|-----------------------|-----------|
| Eleanor Rigby	        | 0.280	    |
| When I'm Sixty Four   | 0.241	    |
| Back in the USSR	    | 0.969	    |

We can do this visually using a bar chart:

**[VIZ: bar chart comparing energy]**

We could evaluate similarity in a few ways, like finding the difference in energy between two songs, or the ratio of energy - none too complicated.

But what if we want to compare songs using more than one attribute? Let's now consider "valence", in addition to "energy":

| Song	                | Energy    | Valence	|
|-----------------------|-----------|-----------|
| Eleanor Rigby	        | 0.280	    | 0.8130	|
| When I'm Sixty Four   | 0.241	    | 0.6610	|
| Back in the USSR	    | 0.969	    | 0.4940	|

We can imagine each song as a point on a graph, with the x-value representing energy and the y-value representing valence.

> Note: We could choose any number of dimensions, but it is easiest to visualize a 2-dimensional graph

https://github.com/user-attachments/assets/14534fa3-4cfe-4dbc-b540-1e0968c0c658

As the values of energy and valence change, the position of the point will change on the graph. If we draw a line from the origin to this point (a **vector**), we can also see that the changing energy and valence will change the **direction** one must travel from the origin to reach the point. Thus, we can use **direction** (measured as angles $ \theta $ and $ \phi $ from the horizontal) as a single value to compare two multi-faceted data points.

**[VIZ: points moving around, lines being drawn to the points, angles for each line changing]**

The method of **cosine similarity** will compare the directions of the two vectors, producing a single value measuring how similar those directions are. If the directions are identical, cosine similarity will be `1`. If they are perpendicular, cosine similarity will be `0`.

**[VIZ: points perpendicular, cosine sim 0, points overlaid, cosine sim 1]**

As an example, we can compute the cosine similarity between Eleanor Rigby (ERY) and Back in the USSR (BUR).

<blockquote><details><summary>Python will compute cosine similarity for us, but if you're curious, click here for a cosine similarity formula breakdown</summary><br>

Cosine similarity is computed between two vectors, say vector $\vec{A}$ and vector $\vec{B}$. We're working with 2-dimensional vectors right now (dimensions "energy" and "valence"), but this method works with n-dimensions.

Represent the vectors in terms of their components:

$$
\vec{A: } \begin{bmatrix}
a_1 \\
a_2
\end{bmatrix}

\hspace{1cm}

\vec{B: } \begin{bmatrix}
b_1 \\
b_2
\end{bmatrix}
$$

The formula for cosine similarity is:

$$
{\vec{A} \cdot \vec{B} \over \|\vec{A}\| \|\vec{B}\|}
$$

where $ \vec{A} \cdot \vec{B} $ represents the **dot product** of vectors $\vec{A}$ and $\vec{B}$, and $\|\vec{A}\| \|\vec{B}\|$ represents the product of the **magnitudes** of vectors $\vec{A}$ and $\vec{B}$ (the magnitude of $\vec{A}$ is $\|\vec{A}\|$).

The dot product is a method of measuring the degree to which the direction of one vector is similar to another.

There is a shortcut for computing the dot product: multiply the corresponding components of each vector and sum the products. Therefore:

$$
\vec{A} \cdot \vec{B} = \begin{bmatrix}
a_1 \\
a_2
\end{bmatrix}
\cdot
\begin{bmatrix}
b_1 \\
b_2
\end{bmatrix} = a_1 b_1 + a_2 b_2
$$

Khan Academy has an article covering dot products [here][khan-academy-dot-products].

The magnitude of a vector, $\|\vec{A}\|$, is the distance between its initial and terminal points. In our case, all vectors simply extend from the origin. We can compute magnitude with a method based on the Pythagorean theorem:

$$
\|\vec{A}\| = \sqrt{a_1^2 + a_2^2}
$$

Khan Academy has a video covering vector magnitudes [here][khan-academy-vector-magnitudes].

</details></blockquote><br>

The cosine similarity of Eleanor Rigby and Back in the USSR, based on energy and valence, is `0.720`.

**[VIZ: angle between ERY and BUR, cosine similarity labeled]**

We can't make much sense of this because we haven't seen any other computed cosine similarities, but it does make sense that these tracks have a cosine similarity noticeably lower than `1.000` (perfect similarity).

Let's now compare When I'm Sixty Four and Back in the USSR.

**[VIZ: angle between WSF and BUR, cosine similarity labeled]**

The cosine similarity of these tracks is `0.732`. This differs slightly from the ERY-BUR comparison, but by a tiny amount. Why is this?

When we use cosine similarity, we represent each song as a vector, and then compare the **directions** of these vectors. However, this ignores the second aspect of vectors: their **magnitude**, or how long they are. We can see this even more clearly when comparing ERY and WSF. We have to zoom in to even see the angle between them!

**[VIZ: angle between ERY and WSF, w/ cosine similarity]**

Despite having somewhat different vectors, Eleanor Rigby and When I'm Sixty Four have a cosine similarity of `0.999`.

With cosine similarity, you can get some sense of the similarity of two songs, but the method can be flawed: if two songs have attributes in a similar **ratio** to each other, their vector directions will also be very similar, even if the magnitudes of these attributes are quite different.

Let's see another example: comparing the songs Eleanor Rigby and Pepperland using cosine similarity, taking into account six types of Spotify feature data (danceability, energy, speechiness, acousticness, liveness, and valence). We can visualize the two songs on a radar plot:

![Radar plot](images/ERY_PPD_radar.png)

These songs look relatively different from each other. Yet their cosine similarity is nearly identical: `0.976`!

This is because their features are in similar proportion to each other - on the radar plot, the lines take an almost identical shape. You could imagine scaling up the graph for Pepperland, and it would overlap very well onto the graph of Eleanor Rigby.

You may decide this is a useful comparison to make. Cosine similarity allows you to compare data without considering size, which can be helpful in some cases! However, if you want to focus more on comparing the quantities of a song's attributes, consider using **Euclidean distance**.

## Euclidean Distance

Euclidean distance is a method for measuring the distance between two points in n-dimensional space. In our 2-dimensional example with energy and valence, this is the distance between two points on a graph. We will explore the same 2-D example, but helpfully, Euclidean distance can be used to compare any number of attributes.

Previously, we have imagined songs as **vectors**. With Euclidean distance, we no longer care about direction, just the position of each song on the plane. So let's re-visualize our graph as a collection of points:

**[VIZ: graph as points]**

**[TODO: this section is incomplete]**

## Implementing Cosine Similarity and Euclidean Distance in Python

Thankfully, Python libraries exist to simplify our computations of cosine similarity and Euclidean distance.

First, we need to import libraries:

```python
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
import numpy as np
```

### Simple Example

First, we'll go over a simple example of comparing two songs:

| Song | danceability | energy | speechiness | acousticness | liveness | valence |
|-|-|-|-|-|-|-|
| Boys | `0.402` | `0.860` | `0.0504` | `0.607` | `0.736` | `0.822` |
| Till There Was You | `0.727` | `0.338` | `0.0454` | `0.790` | `0.105` | `0.646` |

1. Create a list with attributes for each song:

    ```python
    boys = [0.402, 0.860, 0.0504, 0.607, 0.736, 0.822]
    till = [0.727, 0.338, 0.0454, 0.790, 0.105, 0.646]
    ```

2. Convert each list to a special format to use with the `cosine_similarity` and `euclidean_distances` functions:

    ```python
    boys = np.array(x).reshape(1, -1)
    till = np.array(y).reshape(1, -1)
    ```

3. Compute the values:

    + Cosine similarity:

        ```python
        cosine_similarity(boys, till)
        ```

        <table border="0">
            <tr>
                <th valign="top">Output:</th>
                <td>
                    <pre style="white-space: pre;">array([[0.81389584]])</pre>
                </td>
            </tr>
        </table>

    + Euclidean distance:

        ```python
        euclidean_distances(boys, till)
        ```

        <table border="0">
            <tr>
                <th valign="top">Output:</th>
                <td>
                    <pre style="white-space: pre;">array([[0.91692966]])</pre>
                </td>
            </tr>
        </table>


        You should clean up the format of your output by adding `[0][0]` to the end of the line, for example, `cosine_similarity(boys, till)[0][0]`. This will mean the output is just a number, without the brackets and `array` datatype, and can be more easily saved to a variable. Try it!

### Using Cosine Similarity and Euclidean Distance with Pandas

You can also use the `cosine_similarity` and `euclidean_distances` methods on your Pandas dataframes to create lots of comparisons very quickly.



## Summary

**Cosine Similarity vs. Euclidean Distance**

Cosine Similarity:
* Computes similarity on a consistent scale
* More similar = **higher** number
* Only considers vector **direction**, not **magnitude**

Euclidean Distance:
* Doesn't compute similarity on a consistent scale
* More similar = **lower** number
* Takes vector direction **and** magnitude into account

When comparing two songs through several attributes, cosine similarity provides a viable method for creating a uniform "similarity rating". However, there are some instances where cosine similarity is demonstrably inadequate. Thus, Euclidean distance is another (and perhaps better) method to consider. One could also imagine combining these or other methods in some way to form your own "similarity rating".

## Links

https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html

https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html

[khan-academy-dot-products]: https://www.khanacademy.org/math/multivariable-calculus/thinking-about-multivariable-function/x786f2022:vectors-and-matrices/a/dot-products-mvc
[khan-academy-vector-magnitudes]: https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:vectors/x9e81a4f98389efdf:vec-mag/v/finding-vector-magnitude-from-components
