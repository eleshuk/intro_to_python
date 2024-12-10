# Suppose that you’d like to implement a cookie jar in which to store cookies. In a file called jar.py, implement a class called Jar with these methods:

# __init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
# __str__ should return a str with
#  🍪, where
#  is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
# deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
# withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
# capacity should return the cookie jar’s capacity.
# size should return the number of cookies actually in the cookie jar, initially 0.

class Jar:
    def __init__(self, capacity=12):
        # Check if capacity is > 0
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity
        # Initializing, not adding anything
        self._size = 0

    def __str__(self):
        # Size of the cookie jar x the amount of cookies present
        return self.size * "🍪"

    def deposit(self, n):
        # Check if n exceeds the capacity of the jar
        if n > self.capacity:
            raise ValueError("Input exceeds jar capacity")
        # Check if adding a cookie will exceed the capacity of the jar
        if self.size + n > self.capacity:
            raise ValueError("Input exceeds jar capacity")
        # Add user input to total number of cookies in the jar
        self._size += n


    def withdraw(self, n):
        # Check if the withdrawl exceeds the contents of the jar
        if self.size < n:
            raise ValueError("Withdrawl exceeds contents of the jar")
        # Remove user input to total number of cookies in the jar
        self._size -= n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
