# Introduction to Algorithms
- First, we practice the first search algorithm and understand what it is (Binary Search).
- We learn how to talk about the execution time of an algorithm using Big O notation.

# What is an Algorithm?
In general, an algorithm is a set of instructions for performing a task. In this chapter, we will try to understand the algorithm described and then move towards the code to enhance our understanding of it.

# Binary Search
An example to understand this algorithm:
Suppose you are searching for a person's name in a phone book, and the name starts with the letter 'K'. You can start from the beginning and flip through the pages until you find names starting with 'K'. However, it is better to start from the middle of the book because you know that the relevant contacts are somewhere in the middle.
A more realistic example:
When you log in to Facebook, it needs to verify that you have an account on this site. So it needs to search for your name in the database. Let's assume your username is 'karmageddon'. Facebook can start searching from the letter 'A', but it is more logical to start from somewhere in the middle of the list.

> All these scenarios are examples of search problems where the same algorithm is used to solve the problem.

# Algorithm Explanation
Binary search is an algorithm that takes a sorted list of elements as input (we'll explain why it needs to be sorted later). If the desired element is present in the list, binary search returns its position; otherwise, it returns null.

# How Binary Search Works
We choose a number between 1 and 100.
Our goal is to guess the target number with the fewest possible attempts. In each turn, I will tell you if your guess is lower, higher, or correct.
One approach is to start with the first number and continue guessing until we find the target number. In the worst case, we need to guess the number 99 times. However, a better way is to start from the middle, which means trying numbers greater than half of the range. If it's smaller, we eliminate all numbers above it (from 75 to 100), and only the numbers from 50 to 75 remain.
With binary search, you guess the middle number and eliminate half of the remaining numbers in each turn.
In a list of 100 elements, you can find your target number after 7 steps. How did we get this number 7? It represents the maximum number of steps required for the worst-case scenario.
For every list of size n, binary search requires log2 n steps in the worst case, while linear search requires n steps.

> What is logarithm? log2 n means asking how many times do we need to multiply two to reach the number n? Logarithm is essentially the inverse of exponentiation. In this context, when we mention logarithm, we refer to log base 2.

Binary search can only be used when your list is sorted.

# Big O Notation
The Big O notation tells you how fast an algorithm is. The execution time of algorithms grows at different rates.

When you have a list of 100 elements, if you use linear search, you need to check all 100 elements in the worst-case scenario. But with binary search, you only need to check 7 elements. Can we say that binary search is 15 times faster than linear search? No, if you search through a list with 100,000,000 elements, can we still say binary search is 15 times faster? Try to figure out the answer yourself.
The runtime for binary search and linear search does not grow at the same rate.
With linear search, the time it takes to execute the algorithm increases linearly as the size of the input increases.
With binary search, the runtime does not increase linearly but logarithmically.

In Big O notation:
- Linear search has a time complexity of O(n).
- Binary search has a time complexity of O(log n).
