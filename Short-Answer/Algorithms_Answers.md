#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n). The algorithm may make n quite large in the while loop, but it also iterates quickly in the loop's body. 


b) O(n log(n)). The outer loop runs once per range(n), the inner loop multiplies j * 2 each run and stops when j >= n.


c) This doesn't have an input n to analyze. I believe it's O(n) over variable "bunnies" though. Every time it runs, it decreases bunnies by 1, and it terminates when bunnies == 0.

## Exercise II

This seems like a good use case for a binary search. First, drop the egg from the middle floor. If it breaks, you can rule out any floors higher than the middle. Proceed to the floor in the middle of the lower half of the building. If first egg doesn't break, you can rule out any floors lower than the middle, and go to the floor in the middle of the upper half. Continue in this manner, keeping track of which floors could still be f and ruling them out as you go, until you find the lowest floor at which the dropped egg will break. Then you can finally make your omelette
