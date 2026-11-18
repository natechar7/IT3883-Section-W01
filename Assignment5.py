# Program Name: Assignment5.py
# Course: IT3883/Section XXX
# Student Name: John Doe
# Assignment Number: Lab 5
# Due Date: 11/20/2026
# Purpose: This program creates a SQLite database with a table for daily
#          temperature readings, reads each day/temperature pair from the
#          input file and inserts it into the table, then runs SQL queries
#          to compute and print the average temperature for Sunday and
#          Thursday.
# Resources: Python sqlite3 documentation (https://docs.python.org/3/library/sqlite3.html),
#            class lecture notes on SQL and SQLite.

import sqlite3
import os

DB_FILE = "temperatures.db"
INPUT_FILE = "Assignment5input.txt"


def create_table(cursor):
    """Create the temperature table (drop any old copy so reruns start clean)."""
    cursor.execute("DROP TABLE IF EXISTS Temperatures")
    cursor.execute("""
        CREATE TABLE Temperatures (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Day_Of_Week TEXT NOT NULL,
            Temperature_Value REAL NOT NULL
        )
    """)


def load_readings(file_name):
    """Read the input file and return a list of (day, temperature) tuples."""
    readings = []
    with open(file_name, "r") as data_file:
        for line in data_file:
            parts = line.split()
            if len(parts) != 2:
                continue
            day_name = parts[0]
            temp_value = float(parts[1])
            readings.append((day_name, temp_value))
    return readings


def get_average(cursor, day_name):
    """Use SQL to compute the average temperature for the given day."""
    cursor.execute(
        "SELECT AVG(Temperature_Value) FROM Temperatures WHERE Day_Of_Week = ?",
        (day_name,),
    )
    return cursor.fetchone()[0]


def main():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    create_table(cursor)

    readings = load_readings(INPUT_FILE)
    cursor.executemany(
        "INSERT INTO Temperatures (Day_Of_Week, Temperature_Value) VALUES (?, ?)",
        readings,
    )
    connection.commit()
    print(f"Inserted {len(readings)} readings into the database.\n")

    for day in ("Sunday", "Thursday"):
        average = get_average(cursor, day)
        print(f"Average temperature for {day}: {average:.2f}")

    connection.close()


if __name__ == "__main__":
    main()
