"""
Python Tip: Using enumerate() for index + value in loops

Instead of manually tracking indices with counter variables,
use enumerate() to get both index and value cleanly.

Bad way:
    i = 0
    for item in items:
        print(f"Index {i}: {item}")
        i += 1

Good way:
    for i, item in enumerate(items):
        print(f"Index {i}: {item}")
"""

# Example 1: Basic enumeration
fruits = ["apple", "banana", "cherry"]
print("Example 1: Basic enumeration")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")
print()

# Example 2: Start enumeration from 1 instead of 0
print("Example 2: Start from 1 (1-indexed)")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}: {fruit}")
print()

# Example 3: Enumerate with dictionary values
print("Example 3: Enumerate dictionary values")
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
for index, (name, score) in enumerate(scores.items(), start=1):
    print(f"  {index}. {name}: {score}")
print()

# Example 4: Enumerate string characters
print("Example 4: Enumerate string characters")
word = "Python"
for index, char in enumerate(word, start=1):
    print(f"  Character {index}: {char}")
print()

# Example 5: Practical use case - finding positions
print("Example 5: Finding positions of even numbers")
numbers = [3, 7, 12, 9, 14, 8, 21]
for index, num in enumerate(numbers):
    if num % 2 == 0:
        print(f"  Even number {num} found at position {index}")
print()

# Example 6: Building index-value pairs into a list
print("Example 6: Creating indexed list items")
items = ["red", "green", "blue"]
indexed = [(i, item) for i, item in enumerate(items, start=1)]
print(f"  Result: {indexed}")
