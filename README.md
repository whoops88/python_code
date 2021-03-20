## My first hash table function


## 2 cursors
Merging lists
You have at your disposal two sorted lists in non-decreasing order of elements, consisting of n and m elements.

Your task is to merge them into one sorted list of size n + m

Input data
The program receives as input two numbers n and m - the number of elements of the first list and the second lists

Then the elements of the first sorted list come from a new line, and from the next line - the second list

Output
Merge two lists into one in non-decreasing order and display the elements of the resulting list

P.S: using built-in sorting is prohibited

## binary search
In a nutshell, this search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of the elements after just one comparison. 

Compare x with the middle element.
If x matches with the middle element, we return the mid index.
Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.

## Merge sort
The way Merge Sort works is:

An initial array is divided into two roughly equal parts. If the array has an odd number of elements, one of those parts is by one element larger than the other.

The subarrays are divided over and over again into parts until you end up with arrays that have only one element each.

Then you combine the pairs of one-element arrays into two-element arrays, sorting them in the process. Then these sorted pairs are merged into four-element arrays, and so on until you end up with the initial array sorted.

## buble sort


## greedy algoritm
