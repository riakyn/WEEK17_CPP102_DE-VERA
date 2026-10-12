# Laboratory Exercise 17: Device Monitoring System

**Course:** CPP102\
**Project:** Week 17 Main Project\
**Name:** Ma. Eleonor A. De Vera\
**Section:** 1CPE-A\
**Date:** 12/10/2026

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

## 8. Program Flow

1. Start the program.
2. Display the menu.
3. Ask the user for a choice.
4. Perform the selected action.
5. Display an error for an invalid choice.
6. Repeat until the user chooses Exit.

## 9. How to Run

Open the terminal in the Week17 folder and enter:
python device_monitor.py
Choose an option from 1 to 5 and follow the instructions.

## 10. Sample Output

```
SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit

Enter choice: 1

CURRENT READINGS
----------------
Reading 1 : 28 °C
Reading 2 : 31 °C
Reading 3 : 35 °C
Reading 4 : 37 °C
Reading 5 : 29 °C

SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit

Enter choice: 2
Enter new reading: 33

Reading added successfully.

SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit

Enter choice: 2
Enter new reading: abc

Invalid input. Enter a whole number only.

SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit

Enter choice: 4

MONITORING SUMMARY
------------------
Number of readings  : 6
Total of readings   : 193
Average temperature : 32.17 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C

NORMAL   : 2 (33.33%)
WARNING  : 3 (50.00%)
CRITICAL : 1 (16.67%)

Overall Status: ATTENTION REQUIRED

SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit

Enter choice: 5

Thank you for using the Device Monitoring System.
```

The program starts by showing the initial readings. I added a new reading of 33 °C, then tried entering abc, which the program correctly rejected. After adding 33 °C, the total became 193, and the average was 32.17 °C. The lowest reading was 28 °C, and the highest was 37 °C. The program also showed 2 NORMAL readings, 3 WARNING readings, and 1 CRITICAL reading. The overall status was ATTENTION REQUIRED because one of the readings was above 35 °C.

## 11. Testing

The program was tested using the 10 test cases in test_cases.md. The tests covered viewing and adding readings, checking invalid inputs, classifying temperatures, generating the summary, entering an invalid menu choice, and exiting the program. The actual results were recorded after running each test.

## 12. Conclusion

This project helped me practice Python functions, lists, loops, conditions, and input validation. I also learned how to calculate temperature summaries and test a program to check whether it works correctly.

