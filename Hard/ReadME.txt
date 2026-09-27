# Problem 1: Putting Away the Bricks

## Description

We place `n` rectangular building block toys into a box of size `h x w` when viewed from above.

The box and the blocks are treated as 2D coordinates, where the origin `(0,0)` is the upper-left corner of the box.

Each block has a fixed height and width, and they are inserted in the given order without changing orientation and without stacking. A block must be placed according to the following rules:

- The upper-left corner of the block must be placed at the position with the smallest coordinates among all empty cells in the box, in lexicographic order.
- If a block cannot be placed, return the index of the first block that fails to fit.
- If all blocks can be placed, return `0`.

## Input Specification

A list of positive integers `h, w` and a list `bricks` of 2D positive integer elements are given as input.

- The first component of the 2D coordinate is the vertical direction (down).
- The second component is the horizontal direction (right).
- Lexicographic order is defined as:

```text
(x0, y0) < (x1, y1)  <=>  x0 < x1 or (x0 == x1 and y0 < y1)
```

A block cannot be stored if either of the following happens:

1. There is no empty area left in the box.
2. When placing the block so that the upper-left corner is the smallest empty coordinate, the block overlaps another block or goes outside the box.

## Examples

### Example 1

**Input:**

```text
h = 2, w = 2
bricks = [[1,1], [2,1], [1,1]]
```

**Output:**

```text
0
```

**Explanation:**

The box starts as:

```text
..
..
```

After placing the first block:

```text
1.
..
```

After placing the second block:

```text
12
.2
```

After placing the third block:

```text
12
32
```

All blocks fit, so the answer is `0`.

### Example 2

**Input:**

```text
h = 2, w = 2
bricks = [[1,1], [1,2], [1,1]]
```

**Output:**

```text
2
```

**Explanation:**

The second block cannot be placed at the smallest empty position `(0,1)` because it does not fit in the box. Therefore, the first failing block index is `2`.

### Example 3

**Input:**

```text
h = 3, w = 3
bricks = [[1,1], [2,1], [1,1], [2,1], [1,1], [1,2], [1,1]]
```

**Output:**

```text
7
```

**Explanation:**

The first six blocks can be placed, but the seventh block cannot fit. Therefore, the answer is `7`.

## Constraints

```text
1 <= h, w <= 10^8
1 <= len(bricks) <= 10^5
For each brick [h_brick, w_brick] in bricks:
1 <= h_brick <= h
1 <= w_brick <= w
```

---

This is the first problem in the set. Future problems can follow the same structure with a new heading and sections.