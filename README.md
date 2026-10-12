# Laboratory Exercise 17: Device Monitoring System

**Course:** CPP102\
**Project:** Week 17 Main Project\
**Name:** Ma. Eleonor A. De Vera\
**Section:** 1CPE-A\
**Date:** 12/10/2026\

## 1. Project Overview

This project is a simple Python program that monitors simulated device temperatures. It can display readings, add new readings, classify temperatures, and show a summary.

## 2. Objectives

- Practice using Python functions.
- Store readings in a list.
- Validate user input.
- Classify temperatures.
- Calculate a summary using loops.
- Practice testing and debugging.

## 3. Problem Statement

The program must monitor temperature readings and show whether they are NORMAL, WARNING, or CRITICAL. It must also calculate the total, average, minimum, maximum, and overall status.

## 4. Requirements

- Python 3
- Code editor or Python IDE
- Computer 

The program uses lists, functions, loops, and if-elif-else statements. It does not use dictionaries, classes, files, external packages, or `try/except`.

## 5 Program Features

The program has five menu options:

1. View Readings
2. Add Reading
3. Classify Readings
4. Generate Summary
5. Exit

The menu repeats until the user chooses Exit.

## 6 Function Plan

| Function Name | Parameters | Returns | Job |
| --- | --- | --- | --- |
| main() | None | Nothing | Runs the menu |
| get_initial_readings() | None | List | Creates the initial readings |
| display_menu() | None | Nothing | Displays the menu |
| display_readings(readings) | Readings | Nothing | Shows all readings |
| add_reading(readings, lowest, highest) | Readings and limits | Nothing | Adds a valid reading |
| classify_reading(reading, warning_limit, critical_limit) | Reading and limits | String | Classifies a reading |
| display_classifications(readings, warning_limit, critical_limit) | Readings and limits | Nothing | Shows classifications |
| compute_total(readings) | Readings | Number | Calculates the total |
| compute_average(readings) | Readings | Number | Calculates the average |
| find_minimum(readings) | Readings | Number | Finds the lowest reading |
| find_maximum(readings) | Readings | Number | Finds the highest reading |
| count_category(readings, warning_limit, critical_limit, category) | Readings, limits, and category | Number | Counts each category |
| determine_overall_status(warning_count, critical_count) | Category counts | String | Determines the overall status |
| display_summary(readings) | Readings | Nothing | Displays the summary |

## 7. Temperature Rules

| Temperature | Classification |
| --- | --- |
| Below 30 °C | NORMAL |
| 30–35 °C | WARNING |
| Above 35 °C | CRITICAL |

Readings must be whole numbers from 0 to 100. Empty, invalid, negative, and over-100 inputs are rejected.

These rules are for classroom simulation only.

## 8. Program Flow

1. Start the program.
2. Display the menu.
3. Ask the user for a choice.
4. Perform the selected action.
5. Display an error for an invalid choice.
6. Repeat until the user chooses Exit.

## 9. How to Run

Open the terminal in the `Week17` folder and enter:

```
python device_monitor.py
```

Choose an option from 1 to 5 and follow the instructions.

## 10. Sample Output

```
MONITORING SUMMARY
------------------
Number of readings  : 5
Total of readings   : 160
Average temperature : 32.00 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C

NORMAL   : 2 (40.00%)
WARNING  : 2 (40.00%)
CRITICAL : 1 (20.00%)

Overall Status: ATTENTION REQUIRED
```

This summary uses the initial readings: 28, 31, 35, 37, and 29.

Replace this example with the actual output from your program before submission.

## 11. Testing

The program must pass the 10 required tests listed in `test_cases.md`.

These tests check viewing readings, adding readings, invalid inputs, temperature boundaries, the summary, invalid menu choices, and exiting.

Record the actual result of each test after running the program.

## 12. Conclusion

This project helped me practice Python functions, lists, loops, conditions, and input validation. I also learned how to calculate temperature summaries and test a program to check whether it works correctly.

## Project Files

```
Week17/
├── device_monitor.py
├── README.md
└── test_cases.md
```

- `device_monitor.py` – The Python program.
- `README.md` – Project information and instructions.
- `test_cases.md` – Test cases and actual results.
