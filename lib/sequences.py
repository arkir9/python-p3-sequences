#!/usr/bin/env python3

def print_fibonacci(length):
    a, b = 0, 1
    fibonacci_sequence = []

    if length >= 1:
        fibonacci_sequence.append(a)

    if length >= 2:
        fibonacci_sequence.append(b)

    for i in range(2, length):
        fib = a + b
        a, b = b, fib
        fibonacci_sequence.append(fib)

    
    print(fibonacci_sequence)

# Example usage:
print_fibonacci(10)
