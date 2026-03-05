                                         # Generators #

"""
 A generator is a special type of function that returns values one at a time instead of all at once.
 Instead of using return, generators use the yield keyword.

 * Why Generators are Useful ---

Generators are used when:
- Data is very large
- You want to save memory
- You want to generate values step by step

# Generator works like a machine that produces items one by one instead of storing everything in memory.

Example analogy:

Normal function → gives full box of apples 🍎🍎🍎🍎
Generator → gives one apple at a time 🍎

"""

def square_generator(n):
    for i in range(1, n+1):
        yield i*i

gen = square_generator(5)

for num in gen:
    print(num)