"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
from math import ceil

def median(*numbers):
    try:
        numbers = sorted([float(value) for value in numbers])
        length = len(numbers)
        return (numbers[ceil(length/2-1)]+numbers[length//2])/2
    except TypeError:
        print("some input is not number")

print(median(1, 2, 3, 6, 10, 12))
