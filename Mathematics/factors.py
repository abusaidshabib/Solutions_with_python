# Write a function `get_factors(n)` that takes an integer `n` as input and returns all factors of `n`.

# personal solution
value = (int(input("Enter the number of factor")))

the_factors = []

def get_factors(value):
    for i in range(1, value+1):
        if value % i == 0:
            the_factors.append(i)
        else:
            continue

get_factors(value)
print(the_factors)


# Chatgpt Solution
def get_factors(n):
    factors = []  # List to store the factors of n
    for i in range(1, int(n**0.5) + 1):  # Iterate only up to sqrt(n)
        if n % i == 0:  # If i is a factor
            factors.append(i)  # Add i as a factor
            if i != n // i:  # If i is not the square root of n, add n//i as well
                factors.append(n // i)
    return sorted(factors)  # Return sorted list of factors
print(get_factors(12))  # Output: [1, 2, 3, 4, 6, 12]


"""
Explanation of Changes:
Efficiency (Iterate up to sqrt(n)):
The loop runs only up to sqrt(n), which reduces the number of iterations. For every factor i, you also get n // i, which avoids the need to check up to n.

Handling Square Numbers:
We check if i is not equal to n // i to avoid adding the square root twice when n is a perfect square (e.g., for n = 36, both 6 and 6 would be added if we didn't handle this case).

Sorting the List:
After collecting the factors, we sort the list before returning it. This ensures that the factors are presented in ascending order.

Key Benefits:
Optimized: Reduces the time complexity from O(n) to O(sqrt(n)).
Avoids Duplicates: Handles the case where n is a perfect square.
Clean and Efficient: Uses int(n**0.5) to limit the number of iterations, which is more efficient than iterating all the way to n.
This approach is generally considered the best solution for the problem of finding all factors of a number.
"""