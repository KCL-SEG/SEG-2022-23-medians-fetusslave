"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
from math import ceil

def median(numbers):
    numbers = sorted(numbers)
    length = len(numbers)
    return (numbers[ceil(length/2-1)]+numbers[length//2])/2

while True:
     try:
         print("Enter a list of numbers separated by commas: ")
         numbers = [float(value) for value in input().split(",")]
     except ValueError:
         print("Some input could not be converted to a number!")
     else:
         break

print(median(numbers))

