# Big O Notation

## Time Complexity

Used to denote show quickly the runtime grows, relative to the input.

Let's say the input to a function is `n` . `n` can be an value or
list of values of size n.

Constants in front of `n` inside Big O notation can be discarded.

In case of multiple `n` values inside the Big O notation e.g.
`O(n^3 + n^2)` , the small powers of n are discarded. Only the `n` 
with the highest power remains the Big O notation.

## Space Complexity

Used to denote how much additional space is required by the 
program. Similar to time complexity but for space. The space 
occupied by the input is not considered.
