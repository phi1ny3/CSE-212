# Sets
---
## I.  Introduction
Sets are a data structure where order of the data doesn't matter.  Where most data structures are concerned with position, sets contain a cluster of data, and all values are unique.  Because of these two rules, the time complexity surrounding a set in general is very efficient.

For an analogy, imagine a group of kids with a bag of marbles, some are the same pattern.  Each kid wants to expand their marble collection, and they all agree to divy it up as evenly as possible.  Since it's a collection, they don't want to have duplicates.  The values can be seen as the marbles in this analogy, and the collections of each respective child could be seen as a set.


## II. Hashing
Because there is little regard for order or determining duplicates (as they won't be accepted), Sets are more concerned with whether the data belongs to a given set.  All of the techniques to add, remove, or test for membership in a set is part of a process called hashing, and these operations all have a time complexity of O(1) time!

In order to get values of any size to be worked with in a set at O(1) performance, the formula index(n) = hash(n) % sparse_list_size is used.  Hash(n) is our hashing function, and will convert non-integers to integers so that modulus division can be performed.  In Python, this is as simple as saying:
```Python
>>> hash(10)
10
```
Now for a bigger set:
```
List = [11, 12, 13, 14, 15]
H(x) = [x % 10]
```
| Value | hash(n) % sparse_list_size | Index/Key(n)|
| :---: | :------------------------: | :-------:   |
|  11   |          11 % 10           |      1      |
|  12   |          12 % 10           |      2      |
|  13   |          13 % 10           |      3      |
|  14   |          14 % 10           |      4      |
|  15   |          15 % 10           |      5      |

In case you are wondering, you can also do this to other types of values like strings, you can!  Hashing a set of strings efficiently is done by adding the ASCII values of each character in the string, then modulo by array size to find its index.

There is a problem with sparse lists though.  If we are fed tons of unique values, they could have overlapping indexes based on this formula.  For example, if we were to add 21 to our set of numbers above, it would also have an index of 1.  This is called a collision or conflict.  There are several strategies in dealing with this without expanding our list size:

- Open Adressing: If we use our index(n) hashing function and find the space is occupied by another value, we can simply move to the next available space.  The simplest way to do this is to move along to the right each time by one spot until an index space is empty

## III. Functions/Operations in Sets

There are other operations, some similar to other data structures you've learned before (with respective time complexities):

| Operation     | Performance   |
| :-----:       | :------------:|
| insert(value)| O(log n) |
| remove(value)| O(log n) |
| contains(value)| O(log n) |
| traverse_forward | O(n) |
| traverse_reverse | O(n) |
| height(node)    | O(n) |
| size()    | O(1) |
| empty()    | O(1) |



```Python

```

Some of the less familiar operations do the following:
- `contains(value)` ascertains if the value is in the tree.
- `height(node)` is handy for finding the maximum height.  Recursively calls itself hence the time complexity of O(log n)
- `size()` returns the size innately stored in the BST
- `empty()` as you saw helps us with traversal, searching, etc. The value is static so no linear complexity.

## IV. Strategies

## V. Example
Here is an example of a program that creates a tree, then inserts into the tree, and prints it in order:
```Python

```

## VI. Problem


Here is the [Solution](Sol3.py)
[Back to Home](Python_Structures_Tutorial.md)


