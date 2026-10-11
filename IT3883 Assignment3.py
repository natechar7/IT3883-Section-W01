# Program Name: Assignment3.py
# Course: IT3883/Section W01
# Student Name: Nathaniel Charles
# Assignment Number: Lab3
# Due Date: 10/10/2026
# Purpose: A GUI tool that converts fuel economy from Miles per Gallon (MPG)
#          to Kilometers per Liter (km/L). The answer refreshes on every
#          keystroke, the same way online converters work, so there is no
#          button to press. Blank boxes, letters and other bad input show a
#          message instead of crashing the program.
# Resources used:
#   - Python tkinter docs: https://docs.python.org/3/library/tkinter.html
#   - Conversion factor from the assignment sheet: 1 mpg = 0.425143707 km/l
#   - Help received: drafted with assistance from Claude (Anthropic AI assistant)

import tkinter as tk

MPG_TO_KPL = 0.425143707

def mpg_to_kpl(miles_per_gal):
    """Convert a miles-per-gallon number to kilometers per liter."""
    return miles_per_gal * MPG_TO_KPL

def refresh_answer(*unused):
    """Runs every time the MPG box changes and updates the answer label.

    tkinter passes a few extra arguments to trace callbacks; *unused
    soaks them up since this function does not need them.
    """
    typed = entry_value.get().strip()

    if typed == "":
        answer_value.set("Type a number above")
        answer_display.config(fg="gray")
        return

    try:
        fuel_mpg = float(typed)
    except ValueError:
        answer_value.set("Numbers only, please")
        answer_display.config(fg="red")
        return

    if fuel_mpg < 0:
        answer_value.set("Must be 0 or more")
        answer_display.config(fg="red")
        return

    fuel_kpl = mpg_to_kpl(fuel_mpg)
    answer_value.set(f"{fuel_kpl:.4f} km/L")
    answer_display.config(fg="dark green")

window = tk.Tk()
window.title("Fuel Economy Converter")
window.resizable(False, False)

container = tk.Frame(window, padx=20, pady=20)
container.pack()

tk.Label(container, text="MPG  →  km/L",
         font=("Times New Roman", 16, "bold")).grid(row=0, column=0, columnspan=2,
                                          pady=(0, 12))

entry_value = tk.StringVar()
tk.Label(container, text="Miles per Gallon:").grid(row=1, column=0,
                                                   sticky="e", padx=(0, 8))
mpg_box = tk.Entry(container, textvariable=entry_value, width=16)
mpg_box.grid(row=1, column=1, sticky="w")
mpg_box.focus_set()

answer_value = tk.StringVar(value="Type a number above")
tk.Label(container, text="Kilometers per Liter:").grid(row=2, column=0,
                                                       sticky="e",
                                                       padx=(0, 8),
                                                       pady=(10, 0))
answer_display = tk.Label(container, textvariable=answer_value,
                          font=("Times New Roman", 12, "bold"), fg="gray")
answer_display.grid(row=2, column=1, sticky="w", pady=(10, 0))

entry_value.trace_add("write", refresh_answer)

if __name__ == "__main__":
    window.mainloop()