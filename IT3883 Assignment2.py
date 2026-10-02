# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Nathaniel Charles
# Assignment Number: Lab2
# Due Date: 10/2/2026
# Purpose: Reads a file of student names and six scores each, calculates
#          each student's final average, and prints the names and averages
#          sorted from the highest grade to lowest grade.
# Resources: Python documentation (open(), os.path, str.split(), sort()).


import os

# Build the path to the input file based on where this script is saved,
# so it works no matter which folder the program is run from
INPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assignment2input.txt")


def read_students(filename):
    """Read the input file and return a list of (name, average) tuples."""
    results = []
    with open(filename, "r") as infile:
        for line in infile:
            fields = line.split()
            # Skip blank lines so a trailing newline doesn't cause an error
            if not fields:
                continue
            name = fields[0]
            # Remaining six fields are the scores; convert them to numbers
            scores = [float(score) for score in fields[1:]]
            average = sum(scores) / len(scores)
            results.append((name, average))
    return results


def main():
    students = read_students(INPUT_FILE)

    # Sort by the average (second item in each tuple), highest first
    students.sort(key=lambda student: student[1], reverse=True)

    # Print each student's name and average rounded to two decimals
    for name, average in students:
        print(f"{name} {average:.2f}")


main()
