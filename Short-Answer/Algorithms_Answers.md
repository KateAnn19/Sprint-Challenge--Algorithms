#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is O(n) which is linear time. It is O(n) because as the size of the input increases, the 
runtime or space used grows at the same rate


b) This is O(n log n) which is Linearithmic. It is this because as the size of the input increases, the runtime or space used grows at a slightly faster rate. This is not ideal but better than other runtimes.


c) This function is being called recursively n times before reaching base case so its O(n).

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

I'm going to implement a common searching algorithm called Binary Search. I am implementing this algorithm because the runtime complexity of Binary Search is O(log n) which is one of the best cases you can get on average. Best case perfomance would take only one iteration. This would reduce the amount of eggs broken and return floor 'f' as quickly as possible. I implement binary search below.

function save_the_eggs(n, f):
    low = 0
    high = len(arr) - 1
    mid = 0
  
    while low <= high: 
        mid = (high + low) 
        # Check if f is present at mid 
        if arr[mid] < f: 
            low = mid + 1
  
        # If f is greater, ignore left half 
        elif arr[mid] > f: 
            high = mid - 1
  
        # If f is smaller, ignore right half 
        else: 
            return mid 
    # return the value if found
    
    # return -1 if not found
    return -1  # not found



