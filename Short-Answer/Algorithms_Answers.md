#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
The runtime complexity is O(n). It takes n iterations to complete the function.

b)
The runtime complexity is O(nlogn). Each higher n increases the overtime expressed as a ratio, but not exponentially.

c)
The runtime complexity is O(nlogn). For each n, the rate of change of time to complete the function increases linearly.
## Exercise II

Since we're trying to minimize dropped eggs, it's best to opt for a binary search. First, drop an egg at the halfway floor.

- If it breaks, the highest floor to not break an egg is lower.
- If it doesn't break, the highest floor to not break an egg is higher.
- No matter what, we elminate half the possible floors with this approach, which makes it more efficient than checking from the lowest floor.

We then continue trying the midpoint of each segment of floors until we find the solution.

The runtime complexity is O(logn) because although the more floors we have, the more checks necessary, the amount of checks relative to the number of floors decreases the more floors we have. This runtime complexity beats O(n).
